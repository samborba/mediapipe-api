from api import create_app
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

app = create_app("development")
app.run()
