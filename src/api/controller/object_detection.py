import os
import logging
from flask import Blueprint, abort, request, send_file

from api.utils import Mediapipe, Waiter

blueprint = Blueprint("object_detection", __name__)


@blueprint.route("/", methods=["POST"])
def init_service():
    """Receives the video file sent by the client and applies
       the Mediapipe framework.

    Returns:
        multimedia file -- Returns a video file (.mp4) processed by Mediapipe.
        function -- Removes the input video file (provided by the customer) and
        the output file (generated by Mediapipe).
    """
    request_file_path = "resources/video-input.mp4"
    response_file_path = "resources/video-output.mp4"
    mediapipe = Mediapipe()

    logging.info("Writting .mp4 to Bytes.")
    with open(request_file_path, "wb") as video:
        video.write(request.data)
    logging.info("Video file was successfully received.")

    try:
        logging.info("Applying Object Detection on video-input.mp4.")
        mediapipe.object_detection(request_file_path, response_file_path)

        logging.info("Response video successfully generated.")
        logging.info("Returning file to response.")

        return send_file(os.path.abspath("resources/video-output.mp4"),
                         mimetype="video/mp4"), Waiter.cleanIO(request_file_path,
                                                               response_file_path)
    except ProcessLookupError as e:
        print(e)
        abort(500)
