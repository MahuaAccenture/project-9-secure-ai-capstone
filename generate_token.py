
import os
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()

secret = os.getenv("JWT_SECRET")
algorithm = os.getenv("JWT_ALGORITHM", "HS256")
expiry = int(os.getenv("JWT_EXPIRY_MINUTES", "30"))

if not secret:
    raise RuntimeError("JWT_SECRET is not configured")

payload = {
    "sub": "project9-user",
    "iat": datetime.now(timezone.utc),
    "exp": datetime.now(timezone.utc) + timedelta(minutes=expiry)
}

token = jwt.encode(payload, secret, algorithm=algorithm)

print("\nGenerated JWT Token:\n")
print(token)
