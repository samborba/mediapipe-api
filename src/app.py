import logging
import os

from api import create_app

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

app = create_app("development")
app.run()
