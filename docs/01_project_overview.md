# Project Overview – Feedback Collector Microservice

The Feedback Collector Microservice is a fully serverless, event-driven backend system designed to securely capture user feedback and store it in a scalable, cloud-native database. The service exposes lightweight REST APIs that allow client applications to submit structured feedback data and retrieve service health status.

This microservice demonstrates the core principles of modern backend architecture:

- **Stateless compute** using AWS Lambda  
- **API-driven communication** using Amazon API Gateway  
- **NoSQL persistence** via DynamoDB  
- **Decoupled frontend–backend integration**  
- **Automatic fallback mode** for when cloud resources are unavailable

The system is built as a standalone microservice so it can be independently deployed, monitored, scaled, and replaced without affecting other components of a larger application. This aligns strongly with microservice best practices where each service owns a single responsibility—in this case, the lifecycle of user feedback.

The backend is implemented using **FastAPI**, chosen for its speed, simplicity, and native support for async operations. To ensure clean isolation and maintainability, the codebase is organized into modular components for database operations, validation, business logic, and (optional) third-party integrations.

Although the production workflow relies on AWS resources, the service is intentionally designed with a **demo mode**, enabling the frontend to continue functioning even when AWS resources are shut down. This ensures the project remains fully demonstrable.

Overall, the Feedback Collector Microservice serves as a practical demonstration of building real-world serverless backends, covering architectural decision-making, cloud integration, operational considerations, and software engineering discipline.

---