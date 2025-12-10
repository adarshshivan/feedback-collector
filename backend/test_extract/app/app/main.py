from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import FeedbackInput
from .db import save_feedback, list_feedbacks
from .recaptcha import verify_recaptcha
from .sentry_init import init_sentry

app = FastAPI()

# Initialize Sentry
init_sentry()

# Allow frontend calls (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict later for Vercel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "ok", "service": "feedback-backend"}


# --------------------------------------------------------
# POST /feedback
# --------------------------------------------------------
@app.post("/feedback")
async def submit_feedback(payload: FeedbackInput):
    # Validate reCAPTCHA (bypass locally if secret not set)
    if not verify_recaptcha(payload.recaptcha_token):
        raise HTTPException(status_code=400, detail="Invalid reCAPTCHA")

    # Write to DynamoDB
    feedback_id = save_feedback(payload)

    return {
        "message": "Feedback stored successfully",
        "feedback_id": feedback_id,
    }


# --------------------------------------------------------
# GET /feedbacks
# --------------------------------------------------------
@app.get("/feedbacks")
async def get_feedbacks(limit: int = 20):
    items = list_feedbacks(limit)
    return {"count": len(items), "items": items}
