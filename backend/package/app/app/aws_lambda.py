from mangum import Mangum
from .main import app as fastapi_app

# Create the handler used by AWS Lambda
handler = Mangum(fastapi_app)
