import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_user_token(user):
    payload = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(minutes=10)  # expires in 10 minutes
    }
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token
