from flask import Flask, jsonify

from config import config as Config


def handle_bad_request(e):
    return jsonify(response=e.description), e.code


def create_app(config_name):
    """Creates Flask Application.

    Arguments:
        config_name {str} -- file containing application settings

    Returns:
        flask.app -- flask app
    """
    app = Flask(__name__)
    app.config.from_object(Config[config_name])

    # Register Error Handler
    app.register_error_handler(400, handle_bad_request)
    app.register_error_handler(404, handle_bad_request)
    app.register_error_handler(413, handle_bad_request)
    app.register_error_handler(422, handle_bad_request)

    # Register Blueprint
    from .controller import default_page as home
    app.register_blueprint(home.blueprint, url_prefix="/")

    from .controller import hand_tracking
    app.register_blueprint(hand_tracking.blueprint, url_prefix="/mediapipe/handtracking")

    from .controller import object_detection
    app.register_blueprint(object_detection.blueprint, url_prefix="/mediapipe/objectdetection")

    from .controller import multi_hand_tracking
    app.register_blueprint(multi_hand_tracking.blueprint, url_prefix="/mediapipe/multihandtracking")

    from .controller import gesture_recognition
    app.register_blueprint(gesture_recognition.blueprint, url_prefix="/recognition/gesture")

    return app
