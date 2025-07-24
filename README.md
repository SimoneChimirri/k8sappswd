# Flask App for Kubernetes Demo

This project is a simple Flask web application designed to run inside a Docker container and be deployed on Kubernetes.

## How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## How to Build and Run with Docker

```bash
docker build -t flask-k8s-demo .
docker run -p 5000:5000 flask-k8s-demo
```

## Endpoint

- `GET /` — Returns a JSON greeting message

## Kubernetes: Deploy and Expose Locally

To deploy your app and expose it on localhost using Kubernetes (e.g., with Minikube or Docker Desktop):

### 1. Dry-Run and Validation (Preview and validate your YAML files before applying)

You can use the `--dry-run=client` flag to check your YAML files, and `--validate=true` to validate them:

```bash
kubectl apply -f deploy.yaml --dry-run=client --validate=true
kubectl apply -f service.yaml --dry-run=client --validate=true
```

### 2. Apply Deployment and Service

```bash
kubectl apply -f deploy.yaml
kubectl apply -f service.yaml
```

### 3. Check Pod and Service Status

```bash
kubectl get pods
kubectl get services
```

### 4. Access the Service on Localhost

If using Minikube, run:

```bash
minikube service <service-name>
```

If using Docker Desktop, find the NodePort and access via:

```
http://localhost:<node-port>
```

Replace `<service-name>` and `<node-port>` with your actual service name and port.