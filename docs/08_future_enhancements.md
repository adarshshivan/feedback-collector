# Future Enhancements

This microservice is intentionally minimal but designed for easy extension.  
Below are enhancement ideas that can turn this into a full production-grade system.

## 1. Public Feedback Display Page
- Fetches stored feedbacks  
- Shows message, rating, tags (optional)  
- Pagination / infinite scroll  
- Sorting and filtering (latest, highest rating)

## 2. Admin Dashboard
- Authentication layer  
- View/search feedback  
- Export CSV  
- Delete or archive entries  

## 3. Client-Side reCAPTCHA
- Replace dummy token with real Google reCAPTCHA v3  
- Add server-side validation  
- Reduce bot submissions  

## 4. Analytics Pipeline
- Integrate with Amazon Kinesis Firehose  
- Store analytics in S3  
- Build visual dashboards using QuickSight  

## 5. E-mail Notifications
- SES integration  
- Notify admin when new feedback arrives  
- Optional confirmation email to user  

## 6. Sentry Integration
- Real-time exception tracking  
- Frontend + backend monitoring  
- Performance metrics for API latency  

## 7. Multi-Environment Setup
- dev / staging / prod APIs  
- CloudFormation/Terraform IaC templates  

## 8. Container Option (Future Migration)
- Migrate Lambda-based API to ECS Fargate if traffic grows  
- Add load balancer, autoscaling, CI/CD pipelines  

Each enhancement builds on the existing architecture without requiring major redesign.

---
