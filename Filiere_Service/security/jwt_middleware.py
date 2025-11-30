from flask import request, jsonify
from functools import wraps
import jwt
from config import Config

# load public key
with open(Config.RSA_PUBLIC_KEY_PATH, "rb") as f:
    PUBLIC_KEY = f.read()

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # Allow GET requests without token
        if request.method == "GET":
            return f(*args, **kwargs)

        auth = request.headers.get("Authorization", None)
        if not auth:
            return jsonify({"error": "Missing Authorization header"}), 401

        # Accept "Bearer <token>" format only
        parts = auth.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return jsonify({"error": "Invalid Authorization header format"}), 401

        token = parts[1]
        try:
            jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"], options={"verify_aud": False}, leeway=30)
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError as e:
            return jsonify({"error": "Invalid token", "message": str(e)}), 401

        return f(*args, **kwargs)
    return wrapper
