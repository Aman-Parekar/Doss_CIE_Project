# CampusFix Viva – Short Answers

Q1. What is CampusFix?
A. A campus complaint and maintenance management system.

Q2. Why Git?
A. To track code changes and collaborate safely.

Q3. What is CI/CD?
A. CI automatically validates/builds changes; CD automates delivery/deployment.

Q4. Why Docker?
A. It packages the application and its dependencies into a portable container.

Q5. What is a Docker image?
A. A packaged template used to create containers.

Q6. What is a container?
A. A running instance of an image.

Q7. What is Kubernetes?
A. A platform for deploying and managing containers.

Q8. What is a Pod?
A. The smallest deployable unit in Kubernetes; it runs one or more containers.

Q9. What is a Deployment?
A. It manages Pods and keeps the desired number of replicas running.

Q10. What is a Service?
A. It provides stable network access to Kubernetes Pods.

Q11. Why replicas?
A. For availability and to handle more requests.

Q12. What is Prometheus?
A. A monitoring system that collects time-series metrics.

Q13. What is a target?
A. An endpoint that Prometheus scrapes for metrics.

Q14. What is PromQL?
A. Prometheus Query Language used to query metrics.

Q15. What is Grafana?
A. A visualization/dashboard tool that can use Prometheus as a data source.

Q16. Why use Prometheus and Grafana together?
A. Prometheus collects metrics; Grafana visualizes them.

Q17. Why /health?
A. Kubernetes can use it to check whether the application is healthy.

Q18. How do you troubleshoot CrashLoopBackOff?
A. Use kubectl get, describe, logs and events to find the cause.

Q19. How do you troubleshoot a Prometheus target DOWN?
A. Check endpoint, connectivity, service/exporter and scrape configuration.

Q20. How do you troubleshoot Grafana no data?
A. Check data source, time range, PromQL and metric availability.
