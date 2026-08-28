from flask import Blueprint, request, jsonify
from logger import logger

incident_bp = Blueprint("incident", __name__)

incidents = []

@incident_bp.route("/api/incidents", methods=["POST"])
def create_incident():

    logger.info("Creating incident")

    data = request.get_json()

    incident = {
        "id": len(incidents) + 1,
        "title": data.get("title"),
        "description": data.get("description"),
        "priority": data.get("priority"),
        "status": "open"
    }

    incidents.append(incident)

    logger.info(f"Incident {incident['id']} created")

    return jsonify(incident), 201
