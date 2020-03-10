import base64
import os
import flask
import logging
from flask import Blueprint, Response, abort, jsonify, request, send_file

from api.utils import Mediapipe, Waiter

blueprint = Blueprint("gesture_recognition", __name__)

@blueprint.route("/", methods=["POST"])
def init_service():
    """Run model
    """
    pass
