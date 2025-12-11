# Tech Stack

This microservice uses a lean, cloud-native stack designed for low cost, high reliability, and minimal operational overhead.

## 1. Frontend

### **HTML, CSS, JavaScript (Vanilla)**
- Lightweight, dependency-free UI
- Hosted on **Vercel** for fast global edge delivery
- Clean separation from backend (API-based communication)


## 2. Backend

### **FastAPI**
- High-performance Python web framework  
- Type-safe request validation using Pydantic  
- Clean routing structure (`/feedback`, `/status`, etc.)

## 3. AWS Services

### **AWS Lambda**
- Fully serverless execution environment  
- No servers, no patching, auto-scaling  
- Ideal for short-lived API requests

### **API Gateway**
- Provides REST API interface  
- Handles routing, throttling, and CORS  
- Connects frontend to Lambda securely

### **DynamoDB**
- NoSQL database with millisecond latency  
- Schema-flexible design for evolving feedback structure  
- Pay-per-request, nearly free for small projects

### **IAM**
- Strict least-privilege access for:
  - `dynamodb:PutItem`
  - `dynamodb:Query`

## 4. Developer Tools

### **GitHub**
- Repo hosting  
- Version control  
- CI-ready for future automation

### **Vercel**
- Frontend hosting  
- Automatic deployments  
- Ideal for static frontends with APIs

### **Postman**
- GET & POST test

---

## 5. Why This Tech Stack Works

| Requirement | Solution |
|------------|----------|
| Zero-cost backend | Lambda + DynamoDB |
| Quick deployments | FastAPI + Mangum |
| Public showcase | Vercel hosting |
| Easy scalability | API Gateway + Lambda |
| Future enhancement ready | Microservice architecture |

This stack is optimized for learning cloud-native development while remaining production-quality.
