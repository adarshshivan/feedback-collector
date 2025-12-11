# Challenges and Solutions

This section highlights the major challenges encountered during development and how they were solved.

## 1. Lambda Import Errors
**Issue:** Lambda failed to import modules (Pydantic, email-validator).  
**Cause:** Dependencies were not packaged correctly inside the zip.  
**Solution:**  
- Installed dependencies inside project folder  
- Rebuilt package using `pip install -t`  
- Verified directory structure before zipping  

## 2. "rating" and "tag" Attribute Errors
**Issue:** Backend crashed because the model didn’t include fields.  
**Cause:** Mismatch between request payload and Pydantic model.  
**Solution:**  
- Updated `FeedbackInput` model  
- Synced frontend fields with backend  

## 3. DynamoDB AccessDeniedException
**Issue:** Lambda couldn't write to DynamoDB.  
**Cause:** IAM role missing `PutItem` policy.  
**Solution:**  
- Added least-privilege IAM policy  
- Attached ARN-scoped access  

## 4. CORS Failures
**Issue:** Requests from frontend were blocked.  
**Cause:** API Gateway didn't allow browser-origin requests.  
**Solution:**  
- Enabled CORS at API Gateway  
- Allowed necessary headers & methods  

## 5. Frontend 502 Errors
**Issue:** Bad Gateway after deployment.  
**Cause:** Incorrect API URL or missing `/prod`.  
**Solution:**  
- Updated API_BASE constant  
- Confirmed invoke URL from API Gateway  

---

