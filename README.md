# CampusFix – Smart Campus Complaint & Maintenance System

A simple DevOps-ready college project for the TY B.Tech IT CIE-01 assessment.

## 1. Project idea

CampusFix lets students report campus maintenance issues and lets staff update their status:

Reported → Assigned → In Progress → Resolved

Examples:
- Wi-Fi issue
- Broken classroom projector
- Electrical problem
- Water leakage
- Laboratory computer fault
- Cleaning issue

## 2. Architecture

Browser
  ↓
CampusFix Flask application
  ↓
SQLite

DevOps flow:
Git → GitHub Actions → Docker → Kubernetes → Prometheus → Grafana

## 3. CIE tool ownership

Student 1: Git
Student 2: GitHub Actions
Student 3: Docker
Student 4: Kubernetes
Group integration: Prometheus + Grafana

The official CIE rubric requires the group to demonstrate the end-to-end flow and troubleshooting. See `docs/CIE_REQUIREMENTS.md`.

## 4. Run locally

Create a virtual environment if desired:

python -m venv .venv

Activate it and install:

pip install -r requirements.txt

Run:

python app.py

Open:

http://localhost:5000

Health check:

http://localhost:5000/health

Metrics:

http://localhost:5000/metrics

## 5. Run with Docker

docker build -t campusfix:latest .
docker run --rm -p 5000:5000 campusfix:latest

Open:

http://localhost:5000

## 6. Docker Compose

docker compose up --build

## 7. Kubernetes / Minikube

See `k8s/README.md`.

## 8. Monitoring

For an easy local monitoring demo:

cd monitoring
docker compose -f docker-compose.monitoring.yml up --build

Open:
- CampusFix: http://localhost:5000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

The Grafana dashboard is provisioned automatically.

## 9. Important CIE demonstration sequence

1. Show Git repository and branch/commit.
2. Push a small change.
3. Show GitHub Actions workflow running.
4. Show successful build.
5. Show Dockerfile and image.
6. Run/access the Docker container.
7. Show Kubernetes Deployment and Pods.
8. Scale the deployment.
9. Show Prometheus target and metric.
10. Show Grafana dashboard.
11. Demonstrate one controlled troubleshooting case.

## 10. Troubleshooting practice

Practice these before the viva:
- Push does not trigger CI: check workflow, branch and Actions logs.
- Container inaccessible: check port mapping, application binding and logs.
- Pod CrashLoopBackOff: use kubectl get/describe/logs/events.
- Prometheus target DOWN: check endpoint and scrape configuration.
- Grafana no data: check data source, time range and PromQL.

## 11. Important limitation

This is intentionally a simple CIE implementation. SQLite is used to avoid database setup complexity. If you later need a more production-grade architecture, replace SQLite with PostgreSQL/MySQL and use persistent storage for Kubernetes.
