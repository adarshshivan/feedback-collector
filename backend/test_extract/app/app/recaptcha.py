import os
import requests
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

RECAPTCHA_SECRET = os.environ.get("RECAPTCHA_SECRET", None)
RECAPTCHA_VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"


def verify_recaptcha(token: str, min_score: float = 0.3) -> bool:
    """
    Verify reCAPTCHA token with Google.
    If no RECAPTCHA_SECRET is configured, return True (useful for local dev).
    For reCAPTCHA v3 you may want to inspect 'score' in response.
    """
    if not token:
        logger.warning("No reCAPTCHA token provided")
        return False

    if not RECAPTCHA_SECRET:
        logger.warning("RECAPTCHA_SECRET not set — bypassing verification (local/dev).")
        return True

    try:
        resp = requests.post(RECAPTCHA_VERIFY_URL, data={
            "secret": RECAPTCHA_SECRET,
            "response": token
        }, timeout=5)
        data = resp.json()
        success = data.get("success", False)

        # If using reCAPTCHA v3, you can also enforce a score threshold:
        if "score" in data:
            score = float(data.get("score", 0.0))
            logger.info("reCAPTCHA score: %s", score)
            return success and (score >= min_score)

        return success
    except Exception as e:
        logger.exception("Error verifying reCAPTCHA: %s", e)
        # Fail-safe: treat verification as failed
        return False
