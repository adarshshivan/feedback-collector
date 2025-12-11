# Step-by-Step Tutorial

This section explains how the entire system was designed, built, deployed, and made portfolio-ready.

## 1. Project Setup

1. Create a GitHub repository  
2. Initialize frontend folder  
3. Initialize backend folder (`/src/app`)  
4. Add FastAPI, Pydantic, Mangum  
5. Add feedback models, routes, and DB helper functions  
6. Create requirements.txt for Lambda deployment

## 2. AWS Setup

### A. Create DynamoDB Table
- Name: `feedbacks`
- Partition key: `feedback_id` (String)

### B. Create Lambda Function
- Runtime: Python 3.9  
- Handler: `app.aws_lambda.handler`  
- Upload backend zip package  
- Increase timeout (5 sec recommended)

### C. IAM Role Setup
Attach least-privilege permissions:
- `dynamodb:PutItem`
- `dynamodb:Query`
- Resource: your `feedbacks` table ARN

### D. Create API Gateway REST API
- Add `/feedback` POST route  
- Add `/status` GET route  
- Connect both to the Lambda function  
- Enable CORS  

## 3. Frontend Setup

### A. Create basic HTML/CSS/JS UI
- Input fields (email, rating, message)
- Dummy recaptcha token
- Submit handler using Fetch API

### B. Add API Base URL

const API_BASE = "https://your-api-id.execute-api.ap-south-1.amazonaws.com/prod
";

### C. Add Demo Mode Fallback
If AWS fails:
- Show local sample feedback
- Display message “Backend temporarily unavailable (demo mode)”

## 4. Deployment

### A. Frontend → Vercel
- Push repo to GitHub  
- Import in Vercel  
- Auto-deployment enabled  

### B. Backend → AWS Lambda
- Package backend files  
- Upload zip manually  
- Test using Lambda console + API Gateway console  

## 5. Verify End-to-End Flow

1. Open Vercel URL  
2. Submit feedback  
3. Confirm response  
4. Check DynamoDB for inserted items  
5. Test fallback mode by disabling API endpoint  

---
