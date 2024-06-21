from flask import Flask
from flask_cors import CORS
from flask_session import Session
from config import SECRET_KEY
from routes import routes

app = Flask(__name__)
CORS(app)

app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = SECRET_KEY
Session(app)

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
