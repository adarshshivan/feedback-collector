# Feedback Collector – Project Summary

This project is a lightweight feedback collection system designed with a cloud-native architecture and deployed on a modern static hosting workflow. The solution includes a FastAPI backend originally powered by `AWS Lambda`, `API Gateway`, and `DynamoDB`, with a graceful fallback mode that keeps the application fully functional even after cloud resources are decommissioned.

The frontend is built using `HTML`, `CSS`, and `vanilla JavaScript`, communicating with the backend through `REST APIs`. When the production API is reachable, the frontend submits and stores user feedback in the cloud. If AWS is unavailable, the application automatically switches to `Demo Mode`, allowing seamless portfolio demonstrations without any live infrastructure.

The project showcases key concepts including API integration, serverless backend design, fault-tolerant UX, and modern deployment practices using Vercel. It is structured for scalability, maintainability, and future enhancements such as Sentry monitoring, reCAPTCHA validation, and public feedback display.

---

**Detailed documentation is available inside the `docs/` folder.**

---