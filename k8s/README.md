# Kubernetes deployment

For a local Minikube setup:

1. `minikube start`
2. `eval $(minikube docker-env)`
3. `docker build -t campusfix:latest .`
4. `kubectl apply -f namespace.yaml`
5. `kubectl apply -f deployment.yaml`
6. `kubectl apply -f service.yaml`
7. `kubectl -n campusfix get pods`
8. `kubectl -n campusfix get svc`
9. `minikube service campusfix -n campusfix`

Useful CIE commands:
- `kubectl -n campusfix get pods`
- `kubectl -n campusfix describe pod <pod-name>`
- `kubectl -n campusfix logs <pod-name>`
- `kubectl -n campusfix get events --sort-by=.lastTimestamp`
- `kubectl -n campusfix scale deployment campusfix --replicas=3`

Note: this starter setup uses SQLite inside the container for simplicity. For a more durable multi-replica production deployment, use a persistent external database. For CIE demonstration, the simple setup keeps implementation easy.
