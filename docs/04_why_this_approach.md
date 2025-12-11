# Why This Approach?

The chosen architecture — **API Gateway + AWS Lambda + DynamoDB (Serverless Microservice)** — is designed to maximize scalability, minimize cost, and provide a clean separation of responsibilities while keeping the operational overhead close to zero.

This section explains *why* this architecture was selected by evaluating both engineering and product perspectives.

## 1. Business Motivation

### a. Zero-Maintenance Infrastructure
Because this microservice powers a feedback form used by public visitors, traffic is unpredictable.  
A serverless backend eliminates the need for:
- Monitoring server uptime  
- Managing patches or updates  
- Scaling EC2 instances  

This reduces operational effort and lowers long-term maintenance costs.

### b. Extremely Low Cost (Ideal for Portfolios and Side Projects)
AWS Lambda and DynamoDB operate on a pay-per-use model.  
For typical portfolio traffic, this often results in:
- Near-zero monthly cost  
- No cost when idle  
- Fully free under AWS Free Tier  

This makes the solution financially sustainable even after the project is deployed on Vercel for long-term hosting.

### c. Fast Iteration Cycle
New features (like public feedback listing / admin panel) can be added independently without touching the rest of the architecture.  
This modularity accelerates development and future enhancements.

## 2. Technical Motivation

### a. High Scalability with Zero Effort
Lambda automatically scales based on incoming requests.  
Whether 10 or 10,000 people submit feedback at once, the backend handles it without provisioning resources.

### b. Event-Driven Execution
The backend is triggered only when needed:
- POST /feedback → Lambda computes + stores in DynamoDB  
- GET /feedbacks → Lambda reads from DynamoDB  

This is a perfect match for lightweight CRUD microservices.

### c. DynamoDB for Flexible, Fast Storage
DynamoDB is the ideal data store for this project because:
- It has millisecond latency  
- It requires no schema migrations  
- It can scale to millions of records without re-architecture  
- It works seamlessly with Lambda  

The table structure supports:
- feedback_id (PK)  
- name, email, rating, message  
- created_at  
- tag (in future versions)

### d. Clean Microservice Boundary
By placing all backend logic inside `/app` and exposing only API endpoints, the architecture achieves:
- Clear responsibility separation  
- Easy integration with any frontend (HTML/JS, React, Next.js, Vercel, etc.)  
- Future expansion into an API suite (auth, analytics, admin dashboard)  

## 3. Security & Resilience Considerations

### a. IAM-Based Access Control
Lambda has strict permissions:
- Allow only PutItem and Query on the DynamoDB feedbacks table  
Nothing else is accessible.

### b. CORS-controlled API Gateway
The backend accepts input only from trusted frontend origins (Vercel domain, local dev).

### c. Graceful Fallback Mode (Demo Mode)
If AWS is not reachable (after resource cleanup or failure):
- Frontend switches to demo mode  
- Sample feedback is displayed  
- Application still works in portfolio showcase mode  

This ensures **zero downtime** for your personal website and portfolio demonstrations.

## 4. Developer Experience Benefits

### a. Simple Local Development
FastAPI + Mangum allows local testing:
- Run on Uvicorn locally  
- Deploy via Lambda without rewriting the code  

### b. Easy Deployment
A single zipped folder upload updates the entire backend.  
No container registry, no servers, no load balancer.

## 5. Why This Approach Is Ideal for This Project

| Requirement | Chosen Architecture Benefit |
|------------|------------------------------|
| Low cost | Lambda + DynamoDB pay-per-request |
| Super simple deployment | Upload one zip file |
| Highly scalable | Automatic concurrency scaling |
| Minimal maintenance | No servers, no patching |
| Easy portfolio hosting | Works even after AWS resource cleanup |
| Future extensibility | Can add tags, analytics, public feed, admin UI |

The architecture delivers exactly what this project needs:  
**a lightweight, scalable, cost-effective microservice that remains reliable even when AWS resources are temporarily unavailable.**

## Summary

The serverless microservice approach was chosen because it delivers the best blend of:
- Engineering reliability  
- Low operational overhead    
- Modern cloud-native best practices  
- High scalability and minimal cost  

---