# CampusFix Command Cheat Sheet

## Git

git clone <repo>
git status
git checkout -b feature/demo
git add .
git commit -m "Add CampusFix feature"
git push origin feature/demo
git pull

## Docker

docker build -t campusfix:latest .
docker images
docker run --rm -p 5000:5000 campusfix:latest
docker ps
docker logs <container>
docker stop <container>

## Kubernetes

kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl -n campusfix get pods
kubectl -n campusfix get svc
kubectl -n campusfix describe pod <pod>
kubectl -n campusfix logs <pod>
kubectl -n campusfix get events --sort-by=.lastTimestamp
kubectl -n campusfix scale deployment campusfix --replicas=3

## Prometheus

Open /targets and verify CampusFix is UP.
Try:
flask_http_request_total
rate(flask_http_request_total[1m])

## Grafana

Open dashboard:
CampusFix Monitoring

If there is no data:
1. Check Prometheus is running.
2. Check target is UP.
3. Check Grafana Prometheus data source.
4. Check time range.
5. Check PromQL query.
