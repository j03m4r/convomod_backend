from endpoints import api_bp
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET")
app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
