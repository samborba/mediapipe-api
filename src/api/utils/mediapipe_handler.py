import os
from ctypes import cdll
import logging


class Mediapipe:
    """Responsible for handling API calls for Media Pipe libraries"""

    def hand_tracking(self):
        """Calls for Hand Tracking feature.
        
        Raises:
            FileNotFoundError: multimedia file was not found.
        Returns:
            function -- main function from C++ code.
        """
        if not os.path.exists("resources/video-input.mp4"):
            raise FileNotFoundError
        
        if not os.path.exists("mediapipe"):
            logging.info("Mediapipe not found in this project.")
            raise SystemError
        
        logging.info("Searching for hand_tracking.so (lib) file.")
        try:
            hand_tracking = cdll.LoadLibrary(os.path.abspath("src/lib/hand_tracking.so"))
            logging.info("Found it.")
            return hand_tracking.main()

        except FileNotFoundError as e:
            logging.info(e)


    def multi_hand_tracking(self):
        """Calls for Multi Hand Tracking feature.
        
        Raises:
            FileNotFoundError: multimedia file was not found.
        Returns:
            function -- main function from C++ code.
        """
        if not os.path.exists("resources/video-input.mp4"):
            raise FileNotFoundError

        if not os.path.exists("mediapipe"):
            logging.info("Mediapipe not found in this project.")
            raise SystemError
        
        logging.info("Searching for multi_hand_tracking.so(lib) file.")
        try:
            multi_hand_tracking = cdll.LoadLibrary(os.path.abspath("src/lib/multi_hand_tracking.so"))
            logging.info("Found it.")
            return multi_hand_tracking.main()

        except FileNotFoundError as e:
            logging.info(e)


    def face_detection(self):
        """Calls for Face Detection feature.
        
        Raises:
            FileNotFoundError: multimedia file was not found.
        Returns:
            function -- main function from C++ code.
        """
        if not os.path.exists("resources/video-input.mp4"):
            raise FileNotFoundError

        if not os.path.exists("mediapipe"):
            logging.info("Mediapipe not found in this project.")
            raise SystemError
        
        logging.info("Searching for face_detection.so (lib) file.")
        try:
            face_detection = cdll.LoadLibrary(os.path.abspath("src/lib/face_detection.so"))
            logging.info("Found it.")
            return face_detection.main()

        except FileNotFoundError as e:
            logging.info(e)


    def object_detection(self):
        """Calls for Multi Hand Tracking feature.
        
        Raises:
            FileNotFoundError: multimedia file was not found.
        Returns:
            function -- main function from C++ code.
        """
        if not os.path.exists("resources/video-input.mp4"):
            raise FileNotFoundError

        if not os.path.exists("mediapipe"):
            logging.info("Mediapipe not found in this project.")
            raise SystemError

        logging.info("Searching for object_detection.so (lib) file.")
        try:
            object_detection = cdll.LoadLibrary(os.path.abspath("src/lib/object_detection.so"))
            logging.info("Found it.")
            return object_detection.main()

        except FileNotFoundError as e:
            logging.info(e)
