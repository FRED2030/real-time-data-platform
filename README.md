# 🚀 Real-Time Event-Driven Platform on AWS EKS
A production-style cloud-native DevOps project demonstrating the complete lifecycle of modern infrastructure engineering using Docker, Kubernetes, Terraform, Ansible, CI/CD, Monitoring, and AWS.

## 📌Project Overview
This project simulates a real-world enterprise event-driven platform inspired by modern cloud engineering practices used in large-scale environments.
The platform processes streaming events using microservices architecture and demonstrates how to:

Containerize applications
Automate infrastructure
Configure servers
Deploy to Kubernetes
Monitor system health
Implement autoscaling
Operate in AWS cloud infrastructure

## 🏗️ Architecture
Producer Service       ↓Apache Kafka       ↓Consumer Service       ↓Prometheus Metrics       ↓Grafana Dashboards       ↓AWS EKS Kubernetes Cluster

## ⚡ Technologies Used
☁️ Cloud & Infrastructure
AWS EC2
AWS EKS
Terraform
Ansible

# 🐳 Containers & Orchestration
Docker
Kubernetes
Minikube

## 🔄 CI/CD
GitHub Actions
Docker Hub

# 📊 Monitoring & Observability
Prometheus
Grafana

# 🧩 Streaming & Backend
Apache Kafka
Python

# 🧠 Key Features
✅ Event-driven architecture
✅ Microservices deployment
✅ Dockerized services
✅ Kubernetes orchestration
✅ Infrastructure as Code (IaC)
✅ Automated server configuration
✅ CI/CD automation
✅ Monitoring & observability
✅ Horizontal autoscaling
✅ Cloud-native deployment

## 📁 Project Structure

real-time-data-platform/
│
├── producer/
│   ├── producer.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── consumer/
│   ├── consumer.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── terraform/
│   └── main.tf
│
├── ansible/
│   ├── inventory.ini
│   └── setup.yml
│
├── monitoring/
│   └── prometheus.yml
│
├── k8s/
│   ├── producer-deployment.yml
│   ├── consumer-deployment.yml
│   ├── kafka-deployment.yml
│   ├── services.yml
│   └── grafana-service.yml
│
├── .github/
│   └── workflows/
│       ├── docker-ci.yml
│       └── cd.yml
│
└── docker-compose.yml

## 🐳 Step 1 — Dockerized Microservices
The producer and consumer applications were containerized using Docker.

### Purpose
Standardized runtime environments
Service isolation
Portable deployments
Build Containers

docker build -t producer ./producerdocker build -t consumer ./consumer

# 🔄 Step 2 — CI/CD Pipeline
Implemented CI/CD using GitHub Actions.

## CI Pipeline
Builds Docker images
Validates configurations
Ensures deployment consistency

## CD Pipeline
Pushes images to Docker Hub
Automates deployment workflows

## ☁️ Step 3 — Infrastructure as Code
Provisioned AWS infrastructure using Terraform.

### Terraform Responsibilities
Create EC2 resources
Configure security groups
Provision cloud infrastructure
Deploy Infrastructure

terraform init
terraform apply

## ⚙️ Step 4 — Configuration Management
Configured infrastructure using Ansible.

### Ansible Responsibilities
Install Docker
Configure server environment
Prepare deployment runtime
Run Playbook

ansible-playbook -i inventory.ini setup.yml

## ☸️ Step 5 — Kubernetes Deployment
Migrated services from Docker Compose to Kubernetes.

### Kubernetes Features
Self-healing pods
Declarative deployments
Service discovery
Horizontal scaling
Deploy Workloads

kubectl apply -f k8s/

## 📊 Step 6 — Monitoring & Observability
Implemented observability using Prometheus and Grafana.

Metrics Collected
Messages processed
Alerts triggered
Service activity
Monitoring Stack

Prometheus → metric collection
Grafana → dashboard visualization

## ☁️ Step 7 — AWS EKS Deployment
Deployed Kubernetes workloads to AWS EKS.

### Benefits
Managed Kubernetes control plane
Cloud-native scalability
Production-grade orchestration
Create EKS Cluster

eksctl create cluster \--name devops-platform \--region ap-northeast-1 \--nodegroup-name workers \--node-type t3.medium \--nodes 2

## 📈 Step 8 — Autoscaling
Implemented Kubernetes Horizontal Pod Autoscaler (HPA).

### Features
Dynamic scaling
Load-based resource allocation
Improved reliability
Create Autoscaler

kubectl autoscale deployment consumer \--cpu-percent=50 \--min=2 \--max=10

## 🔍 Monitoring Dashboard

### Prometheus
http://localhost:9090

### Grafana
http://localhost:3000
Default login:
admin / admin

## 🎯 Project Outcomes
This project demonstrates practical experience with:

DevOps engineering
Cloud-native infrastructure
Kubernetes orchestration
Infrastructure automation
Monitoring & observability
Event-driven systems
CI/CD workflows
AWS cloud deployment


# 🧠 Professional Summary
I Designed and deployed this cloud-native event-driven microservices platform using Docker, Kubernetes, Terraform, Ansible, GitHub Actions, Prometheus, Grafana, and AWS EKS.

### Implemented:
CI/CD automation
Infrastructure as Code
Monitoring & observability
Kubernetes autoscaling
Cloud-native deployment workflows


### This project simulates a production-grade DevOps and cloud engineering environment.

# Author:
### Fred King Mensah
