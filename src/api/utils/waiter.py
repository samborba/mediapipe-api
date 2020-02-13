import os
import logging

class Waiter:
    """Responsible for taking care of basic functions (such as removing IO files, for example).
    """
    @staticmethod
    def cleanIO(input_path, output_path):
        """[summary]
        
        Arguments:
            input_path {string} -- video-input.mp4 path
            output_path {string} -- video-output.mp4 path
        Raises:
            FileNotFoundError: requested files do not exist
        """
        if not os.path.exists(input_path) and not os.path.exists(output_path):
            raise FileNotFoundError
        
        logging.info("Removing files.")

        os.remove(input_path)
        os.remove(output_path)

        logging.info("Done.")
