from flask import Flask, render_template, request, redirect, url_for, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import sqlite3
from pathlib import Path
from datetime import datetime

app = Flask(__name__)
metrics = PrometheusMetrics(app)
DB_PATH = Path("campusfix.db")

def init_db():
    with sqlite3.connect(DB_PATH) as con:
        con.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Reported',
            created_at TEXT NOT NULL
        )
        """)
        con.commit()

@app.route("/")
def index():
    with sqlite3.connect(DB_PATH) as con:
        complaints = con.execute(
            "SELECT id,title,category,location,description,status,created_at "
            "FROM complaints ORDER BY id DESC"
        ).fetchall()
    return render_template("index.html", complaints=complaints)

@app.post("/complaints")
def create_complaint():
    title = request.form.get("title", "").strip()
    category = request.form.get("category", "").strip()
    location = request.form.get("location", "").strip()
    description = request.form.get("description", "").strip()

    if not all([title, category, location, description]):
        return "All fields are required", 400

    with sqlite3.connect(DB_PATH) as con:
        con.execute(
            "INSERT INTO complaints(title,category,location,description,created_at) "
            "VALUES (?,?,?,?,?)",
            (title, category, location, description,
             datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        con.commit()
    return redirect(url_for("index"))

@app.post("/complaints/<int:complaint_id>/status")
def update_status(complaint_id):
    status = request.form.get("status", "")
    allowed = {"Reported", "Assigned", "In Progress", "Resolved"}
    if status not in allowed:
        return "Invalid status", 400

    with sqlite3.connect(DB_PATH) as con:
        con.execute("UPDATE complaints SET status=? WHERE id=?", (status, complaint_id))
        con.commit()
    return redirect(url_for("index"))

@app.get("/health")
def health():
    return jsonify(status="healthy", service="CampusFix")

@app.get("/api/complaints")
def api_complaints():
    with sqlite3.connect(DB_PATH) as con:
        rows = con.execute(
            "SELECT id,title,category,location,description,status,created_at "
            "FROM complaints ORDER BY id DESC"
        ).fetchall()
    keys = ["id","title","category","location","description","status","created_at"]
    return jsonify([dict(zip(keys, row)) for row in rows])

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
