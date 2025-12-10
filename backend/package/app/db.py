import os
import uuid
from datetime import datetime
import logging
import boto3
from botocore.exceptions import ClientError
from typing import List, Dict, Any

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Read settings from environment
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE", "feedbacks")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

# boto3 DynamoDB client / resource
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(DYNAMODB_TABLE)


def save_feedback(payload) -> str:
    """
    Save the FeedbackInput-like payload to DynamoDB.
    Returns the generated feedback_id.
    """
    feedback_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat() + "Z"

    item = {
        "feedback_id": feedback_id,
        "created_at": now,
        "rating": int(payload.rating),
        "message": payload.message,
        "tag": payload.tag or "general",
    }

    if getattr(payload, "name", None):
        item["name"] = payload.name
    if getattr(payload, "email", None):
        item["email"] = payload.email

    try:
        table.put_item(Item=item)
        logger.info("Saved feedback %s", feedback_id)
        return feedback_id
    except ClientError as e:
        logger.exception("Failed to write item to DynamoDB: %s", e)
        raise


def list_feedbacks(limit: int = 20) -> List[Dict[str, Any]]:
    """
    Simple listing of feedbacks. Uses Scan and returns latest `limit` results
    sorted by created_at descending. For production, create a GSI on created_at.
    """
    try:
        resp = table.scan()
        items = resp.get("Items", [])
        # sort by created_at (ISO format)
        items_sorted = sorted(items, key=lambda x: x.get("created_at", ""), reverse=True)
        return items_sorted[:limit]
    except ClientError as e:
        logger.exception("Failed to scan DynamoDB table: %s", e)
        return []
