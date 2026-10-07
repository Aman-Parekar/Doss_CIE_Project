# CampusFix CIE-01 Requirements Checklist

Source basis: the provided TY B.Tech IT DevOps for Scalable System Group CIE-01 Assessment Method & Rubrics.

## Required tools

1. Git
2. Jenkins CI/CD OR GitHub Actions
3. Docker
4. Kubernetes
5. Prometheus
6. Grafana
7. Group integration and troubleshooting

## Four-person primary allocation

- Student 1: Git
- Student 2: Jenkins/GitHub Actions
- Student 3: Docker
- Student 4: Kubernetes
- Prometheus + Grafana: group/rotating responsibility

## Evidence to prepare

### Git
- add/commit/push/pull/clone
- branch
- merge or pull request
- verify result
- explain why version control is required

### GitHub Actions
- workflow configuration
- trigger
- automated build
- deployment stage or explain deployment stage

### Docker
- Dockerfile: FROM, COPY, RUN, CMD/ENTRYPOINT
- build/tag/verify image
- run container
- inspect/access using port

### Kubernetes
- Deployment YAML
- Pods verification
- Service
- replica scaling
- troubleshoot with get/describe/logs/events

### Prometheus
- architecture: Prometheus, targets, exporters where applicable
- prometheus.yml
- target status
- metric/query

### Grafana
- dashboard
- PromQL
- visualization
- identify an anomaly

### Integration
Demonstrate:

Git
  ↓
CI/CD
  ↓
Docker image
  ↓
Kubernetes deployment
  ↓
Prometheus metrics
  ↓
Grafana dashboard

## Troubleshooting scenarios to practice

1. Git push does not trigger CI/CD.
2. CI/CD build fails.
3. Docker container runs but app is inaccessible.
4. Kubernetes Pod is CrashLoopBackOff.
5. Prometheus target is DOWN.
6. Grafana panel shows no data.

## Assessment timing

0–1 min: introduction
1–5 min: primary demonstrations
5–7 min: integration
7–9 min: troubleshooting
9–10 min: viva

## Mark target

Individual primary tool: 9 marks each × 4 students = 36
Group integration/troubleshooting = 14
Total = 50

Goal: demonstrate actual configuration/execution, verify results, explain commands/configuration, integrate all stages, and troubleshoot.
