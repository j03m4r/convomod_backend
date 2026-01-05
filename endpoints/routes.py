from flask import Blueprint, jsonify
import os
import firebase_admin
from firebase_admin import credentials, firestore

private_key = os.getenv("FIREBASE_PRIVATE_KEY").replace('\\n', '\n')
cred_dict = {
    "type": os.getenv("FIREBASE_TYPE"),
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": private_key,
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN")
}

cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred)
db = firestore.client()

api_bp = Blueprint("api", __name__)


@api_bp.get("/api/verify/<code>")
def verify(code):
    user_id = code
    doc = db.collection("users").document(user_id).get()
    
    if doc.exists:
        return {"verified": True}, 200
    return {"verified": False}, 404

