import os
import ctypes
import logging

_HAND_TRACKING_GRAPH = "mediapipe/graphs/hand_tracking/hand_tracking_desktop_live.pbtxt".encode("utf-8")
_OBJECT_DETECTION_GRAPH = "mediapipe/graphs/hand_tracking/multi_hand_tracking_desktop.pbtxt".encode("utf-8")
_MULTI_HAND_TRACKING_GRAPH = "mediapipe/graphs/object_detection/object_detection_desktop_tflite_graph.pbtxt".encode("utf-8")


class Mediapipe:
    """
    Responsible for handling API calls for Media Pipe libraries.
    """
    def __init__(self):
        self._func = ctypes.cdll.LoadLibrary(os.path.abspath("src/lib/mediapipe_api_binary.so"))
        self._func.RunMPPGraph.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
        

    def hand_tracking(self, input_video, output_folder):
        if not os.path.exists(input_video):
            raise FileNotFoundError
        
        if not os.path.exists("mediapipe"):
            logging.info("Mediapipe main directory at root not found.")
            raise SystemError
        
        logging.info("Searching for binary file.")
        try:
            logging.info("Found it.")
            self._func.RunMPPGraph("".encode("utf-8"),
                                   input_video.encode("utf-8"),
                                   output_folder.encode("utf-8"),
                                   _HAND_TRACKING_GRAPH)
            logging.info("Done.")
        except FileNotFoundError as e:
            print(e)


    def multi_hand_tracking(self, input_video, output_folder):
        if not os.path.exists(input_video):
            raise FileNotFoundError
        
        if not os.path.exists("mediapipe"):
            logging.info("Mediapipe main directory at root not found.")
            raise SystemError
        
        logging.info("Searching for binary file.")
        try:
            logging.info("Found it.")
            self._func.RunMPPGraph("".encode("utf-8"),
                                   input_video.encode("utf-8"),
                                   output_folder.encode("utf-8"),
                                   _MULTI_HAND_TRACKING_GRAPH)
            logging.info("Done.")
        except FileNotFoundError as e:
            print(e)


    def object_detection(self, input_video, output_folder):
        if not os.path.exists(input_video):
            raise FileNotFoundError
        
        if not os.path.exists("mediapipe"):
            logging.info("Mediapipe main directory at root not found.")
            raise SystemError
        
        logging.info("Searching for binary file.")
        try:
            logging.info("Found it.")
            self._func.RunMPPGraph("".encode("utf-8"),
                                   input_video.encode("utf-8"),
                                   output_folder.encode("utf-8"),
                                   _OBJECT_DETECTION_GRAPH)
            logging.info("Done.")
        except FileNotFoundError as e:
            print(e)
