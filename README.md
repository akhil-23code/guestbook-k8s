# guestbook-k8s
Tutorial for building docker image and deploying under k8s svc


# 📖 Guestbook on Kubernetes

A multi-tier **Guestbook application** deployed on **Kubernetes** using **Docker Desktop**.  
This project demonstrates Kubernetes concepts including **Deployments, Services, and Load Balancing**.

---

# 🚀 Tech Stack
Kubernetes
Docker
Flask
Redis (Leader/Follower replication)

---

## 🏗️ Architecture

- **Frontend:** Flask + HTML, containerized with Docker  
- **Database:** Redis Leader (write) + Redis Followers (read replicas)  
- **Kubernetes Services:** Expose frontend and Redis components  
- **Deployment:** Kubernetes manifests (`k8s/` folder)  

[ User ] → [ Frontend Service ] → [ Guestbook Frontend Pods ]
↕
[ Redis Leader Service ]
↕
[ Redis Follower Pods ]



---

## ⚙️ Setup Instructions

### 1. Clone the Repo
git clone https://github.com/<your-username>/guestbook-k8s.git
cd guestbook-k8s

### 2. Build & Push Frontend Docker Image
cd frontend
docker build -t <your-dockerhub-username>/guestbook-frontend:latest .
docker push <your-dockerhub-username>/guestbook-frontend:latest

### 3. Deploy on Kubernetes
kubectl apply -f k8s/

### 4. Access the page
kubectl port-forward svc/frontend 8080:80

### 5. Open 
https://localhost:8080
