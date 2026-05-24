Wisecow DevOps Project
Project Overview

This project is built to demonstrate basic DevOps practices using containerization, Kubernetes, and CI/CD automation.
It includes a simple application deployed using Docker and Kubernetes along with automated pipeline using GitHub Actions.
Along with that, basic system monitoring and application health checking scripts are also added using Python.

Tech Stack
Docker
Kubernetes (Kind)
GitHub Actions
Python
Linux (Bash basics)
Project Structure
wisecow/
│
├── .github/workflows/        # CI/CD pipeline
├── k8s/                      # Kubernetes YAML files
├── Dockerfile               # Docker configuration
├── index.html               # Sample application page
├── system_health.py        # System monitoring script
├── app_health.py           # Application health checker
├── requirements.txt       # Python dependencies
└── README.md
Features
Docker
Application is containerized using Docker
Easy to build and run in any environment
Kubernetes
Deployment done using Kind cluster
Service exposed using NodePort
Handles scaling and container management
CI/CD Pipeline
GitHub Actions used for automation
Builds Docker image on every push
Pushes image to DockerHub automatically
Monitoring Scripts
Checks CPU, memory, and disk usage
Monitors application status using HTTP response codes
How to Run
1. Clone Repository
git clone https://github.com/1Pranav12/wisecow.git
cd wisecow
2. Build and Run Docker
docker build -t wisecow .
docker run -p 4499:4499 wisecow
3. Run Kubernetes
kubectl apply -f k8s/
4. Run Python Scripts
pip install -r requirements.txt

python system_health.py
python app_health.py
CI/CD Flow

Whenever code is pushed to GitHub:

GitHub → GitHub Actions → Docker Build → DockerHub → Ready for Deployment

Requirements
psutil
requests

Install using:

pip install -r requirements.txt
Status
Docker image builds successfully
Kubernetes deployment working
CI/CD pipeline running (GitHub Actions green tick)
Monitoring scripts working
Author

Pranav Garg