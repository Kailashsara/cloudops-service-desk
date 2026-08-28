from flask import Blueprint, jsonify
from config import Config

info_bp = Blueprint("info", __name__)

@info_bp.route("/api/info")
def info():
    return jsonify({
        "application": Config.APP_NAME,
        "version": Config.APP_VERSION,
        "environment": Config.APP_ENV
    })
