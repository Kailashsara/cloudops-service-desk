from flask import Flask
from flask import jsonify
from routes.health import health_bp
from routes.info import info_bp
from routes.incidents import incident_bp

app = Flask(__name__)

app.register_blueprint(health_bp)
app.register_blueprint(info_bp)
app.register_blueprint(incident_bp)

@app.route("/")
def home():
    return "CloudOps Service Desk Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
