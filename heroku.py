import os
from create_bot import token
from urllib.parse import urljoin

PROJECT_NAME = os.getenv('heroku_tgmb_project')  # Set it as you've set TOKEN env var

WEBHOOK_HOST = f'https://{PROJECT_NAME}.herokuapp.com/'  # Enter here your link from Heroku project settings
WEBHOOK_URL_PATH = '/webhook/'
WEBHOOK_URL = urljoin(WEBHOOK_HOST, WEBHOOK_URL_PATH)

# webserver settings
WEBAPP_HOST = '0.0.0.0'  # or ip
WEBAPP_PORT = os.environ.get('PORT')