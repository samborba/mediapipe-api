import base64
import os
import flask
import logging
from flask import Blueprint, Response, abort, jsonify, request, send_file

from api.utils import Mediapipe, Waiter, model_handler

blueprint = Blueprint("gesture_recognition", __name__)

@blueprint.route("/", methods=["POST"])
def init_service():
    request_file_path = "resources/video-input.mp4"
    response_file_path = "resources/video-input.csv"
    mediapipe = Mediapipe()
    
    logging.info("Writting .mp4 to Bytes.")
    with open(request_file_path, "wb") as video:
        video.write(request.data)
    logging.info("Video file was successfully received.")

    try:
        logging.info("Hand Gesture Recognition on video-input.")
        mediapipe.gesture_recognition(request_file_path, "./resources/")

        classification_type = model_handler.start_predict(response_file_path)
        Waiter.cleanIO(request_file_path, response_file_path)
        
        return jsonify(classification=classification_type)
    except ProcessLookupError as e:
        print(e)
        abort(500)
    pass
