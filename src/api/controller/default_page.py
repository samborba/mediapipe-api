import flask
from flask import Blueprint, jsonify


blueprint = Blueprint("home_page", __name__)


@blueprint.route("/")
def home_page():
    """Access the default API endpoint.
    
    Returns:
        json -- returns information on how to make a request.
    """
    return jsonify(response="Use the POST method at "
                            "/mediapipe/<service-name>/ to apply the mediapipe service.")
