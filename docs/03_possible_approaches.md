# Possible Approaches

Before building the Feedback Collector Microservice, several architectural options were evaluated.  
Each approach offers different benefits depending on scale, cost, and operational complexity.

This section outlines the main alternatives considered and why serverless microservices were ultimately chosen.

## 1. Monolithic Application (Single Backend + Database)

### Description
All logic (feedback API + UI + database operations) bundled into one backend service, typically deployed on a single server or VM.

### Pros
- Simple to start with
- Easy local development
- Minimal deployment steps

### Cons
- Difficult to scale individual parts
- Updating one feature requires redeploying the entire application
- Not suitable for distributed, event-driven, or modular systems


## 2. Traditional Backend on EC2

### Description
Deploy a Python/Node backend on an EC2 instance, using DynamoDB or RDS for storage.

### Pros
- Full control over OS, runtime, and environment
- Easy to add background jobs or custom libraries

### Cons
- Requires server maintenance, patching, scaling configuration
- Costs more (server runs 24/7 even if no requests)
- Not optimized for bursty workloads like feedback submission

## 3. Containerized Microservice (ECS / EKS / Docker)

### Description
Package the backend as a Docker container and deploy via ECS (Fargate) or Kubernetes (EKS).

### Pros
- Highly portable and scalable
- Clear microservice boundaries
- Works well for larger systems or multi-service platforms

### Cons
- Requires containerization + orchestration knowledge
- ECS/EKS add cost and operational complexity
- Overkill for a simple CRUD-style microservice

## 4. Serverless Microservice (API Gateway + Lambda + DynamoDB) — *Chosen Approach*

### Description
A fully serverless backend where API Gateway routes requests, Lambda runs backend logic, and DynamoDB stores feedback records.

### Pros
- No servers to manage  
- Auto-scaling  
- Extremely low cost (often free)  
- Highly modular microservice  
- Perfect for low-latency API workloads  
- Easy IAM security integration  

### Cons
- Cold starts (minor for low-traffic systems)
- Limited execution time compared to full servers

### Fit for This Project
The best combination of:
- Scalability  
- Low cost  
- Modern cloud architecture  
- Clean microservice separation  
- Easy integration with frontend  
- Perfect for long-term portfolio hosting  

---

## Summary Table

| Approach | Complexity | Cost | Scalability | Maintenance | Fit |
|---------|------------|------|-------------|-------------|------|
| Monolithic | Low | Low | Low | Medium | Not ideal |
| EC2 Backend | Medium | Medium–High | Medium | High | Too heavy |
| Containerized | Medium–High | Medium | High | Medium | Overkill |
| Serverless Microservice | Low | Very Low | Very High | Very Low | Excellent |

---

Serverless microservices provided the highest value with the lowest operational burden, making it the ideal architecture for this project.

---