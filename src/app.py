import logging
import os

from api import create_app

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

if not os.path.isdir(os.path.abspath("/resources")):
    os.mkdir("/resources")

app = create_app("development")
app.run()
