# Why This Project?

The Feedback Collector Microservice was designed with a dual purpose:  
1. **To build a practical, real-world product capability**, and  
2. **To serve as a strong engineering project that demonstrates modern cloud and backend skills.**

This hybrid motivation shaped the design decisions, the architecture, and the scope of the solution.


## 1. Product Motivation – Why Build a Feedback System?

Every application—whether consumer-facing or internal—needs a structured mechanism to capture user insights. A scalable feedback pipeline enables:

- **Continuous improvement** based on real user sentiment  
- **Early detection of issues or dissatisfaction**  
- **Better decision-making** using actual usage feedback  
- **Increased user engagement** by showing that feedback is valued  

Most products start with manual forms or spreadsheets. As usage grows, this approach becomes error-prone, slow, and difficult to maintain.  
A dedicated feedback service solves these limitations by providing:

- A standardized data structure  
- A permanent and queryable storage mechanism  
- Secure submission endpoints  
- An independently deployable module that can be plugged into any frontend

This project captures these real-world requirements in a simple but production-ready microservice.

## 2. Technical Motivation – Why Build It as a Serverless Microservice?

This project was intentionally designed to demonstrate core cloud competencies. Specifically, it showcases how to build:

### **a. Serverless compute using AWS Lambda**  
No servers to manage, automatic scaling, and pay-per-use execution.  
Ideal for bursty workloads like feedback submission.

### **b. API-first architecture using API Gateway**  
This introduces routing, integration responses, CORS configuration, and versioned stages—similar to production REST APIs.

### **c. NoSQL data modeling through DynamoDB**  
A simple yet highly scalable way to store feedback records without managing schemas or migrations.

### **d. Modular backend implementation using FastAPI**  
Clear separation of concerns:
- Input models  
- Database layer  
- Validation logic  
- Optional integrations (reCAPTCHA, Sentry)

### **e. Real-world engineering constraints**  
Features like:
- Fallback/demo mode  
- CORS configuration  
- Error handling  

## 3. Why This Project Is Valuable 

This microservice represents the exact type of workload companies commonly migrate to serverless. It demonstrates:

- API design  
- Cloud integration  
- IAM permissions  
- Logging and monitoring  
- Packaging and deploying Lambda functions  
- Documentation discipline  
- Frontend–backend collaboration  

Additionally, a **demo mode** ensures the project remains interactive even after cloud resources are shut down—making it practical and cost-effective for long-term use.

## 4. Summary

This project provides both **real product value** and **strong engineering depth**.  
It solves a relatable problem—capturing structured user feedback—while simultaneously showcasing modern serverless backend development, microservice design, and cloud-native thinking.

---

