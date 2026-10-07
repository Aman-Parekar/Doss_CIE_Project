# 8–10 Minute CampusFix CIE Demo Script

## 0:00–1:00 Introduction

Student 1:
"CampusFix is a smart campus complaint and maintenance system. Students report issues and maintenance staff update them from Reported to Assigned, In Progress and Resolved."

Then each student states their primary tool.

## 1:00–5:00 Primary demonstrations

### Student 1 – Git
Show:
- repository
- branch
- `git status`
- `git add`
- `git commit`
- `git push`
- branch/merge

Say:
"Git provides version control and allows our team to safely manage changes."

### Student 2 – GitHub Actions
Open Actions tab.
Show workflow file.
Make a small commit if necessary.
Show workflow running and successful.

Say:
"GitHub Actions automatically runs our CI workflow after a push or pull request."

### Student 3 – Docker
Show Dockerfile.
Point to:
FROM → COPY → RUN → CMD.
Run:
docker build -t campusfix:latest .
docker images
docker run --rm -p 5000:5000 campusfix:latest

Open the app.

### Student 4 – Kubernetes
Show:
kubectl -n campusfix get pods
kubectl -n campusfix get svc
kubectl -n campusfix scale deployment campusfix --replicas=3
kubectl -n campusfix get pods

Explain Deployment, Pods, Service and scaling.

## 5:00–7:00 Integration

Show the flow:

Git → GitHub Actions → Docker → Kubernetes → Prometheus → Grafana

Explain:
"A code change starts in Git. CI validates/builds it. Docker packages the application. Kubernetes runs the containers. Prometheus collects metrics and Grafana visualizes them."

## 7:00–9:00 Troubleshooting

Practice one safe controlled issue.

Example: Kubernetes troubleshooting.

Show:
kubectl -n campusfix get pods
kubectl -n campusfix describe pod <pod-name>
kubectl -n campusfix logs <pod-name>
kubectl -n campusfix get events --sort-by=.lastTimestamp

Explain what was wrong and how it was fixed.

## 9:00–10:00 Viva

Likely questions:
1. Why Git?
2. Why Docker?
3. What is a container?
4. Difference between Pod and Deployment?
5. What does a Kubernetes Service do?
6. Why scale replicas?
7. What does Prometheus do?
8. What is PromQL?
9. Why Grafana?
10. What happens after a Git push?

Keep answers short and demonstrate rather than memorizing definitions.
