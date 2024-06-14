import os

from dotenv import load_dotenv
load_dotenv()

GOOGLE_CLIENT_SECRET_FILE = os.getenv('GOOGLE_CLIENT_SECRET_FILE')
GOOGLE_SCOPES = os.getenv('GOOGLE_SCOPES')
GOOGLE_REDIRECT_URI = os.getenv('GOOGLE_REDIRECT_URI')
