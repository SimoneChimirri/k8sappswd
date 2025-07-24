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