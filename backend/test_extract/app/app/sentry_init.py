import os
import logging
import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

logger = logging.getLogger(__name__)

SENTRY_DSN = os.environ.get("SENTRY_DSN", None)
SENTRY_ENV = os.environ.get("SENTRY_ENV", "development")


def init_sentry():
    """
    Initialize Sentry SDK if SENTRY_DSN is present.
    Returns an ASGI middleware wrapper when needed.
    """
    if not SENTRY_DSN:
        logger.info("SENTRY_DSN not set. Skipping Sentry initialization.")
        return None

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        environment=SENTRY_ENV,
        traces_sample_rate=0.1,
    )
    logger.info("Sentry initialized (env=%s).", SENTRY_ENV)
    return True
