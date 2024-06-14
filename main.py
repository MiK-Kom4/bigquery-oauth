import uvicorn

import config

import os
import logging
import google_auth_oauthlib.flow

from starlette.responses import RedirectResponse
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}

client_secrets_file = config.GOOGLE_CLIENT_SECRET_FILE
scopes = config.GOOGLE_SCOPES
redirect_uri = config.GOOGLE_REDIRECT_URI

flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(client_secrets_file, scopes)

flow.redirect_uri = redirect_uri


@app.get("/login")
async def login():

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_grant_scopes='true',
        prompt='consent'
    )
    print("Authorization URL:", authorization_url)
    return RedirectResponse(authorization_url)


@app.get("/callback")
async def callback(request: Request):
    try:
        print("Callback URL:", request.url)
        flow.fetch_token(authorization_response=str(request.url))
        credentials = flow.credentials
        return {"login success": True, "token": credentials.token}
    except Exception as e:
        logging.error(f"Error during callback: {e}")
        return JSONResponse({"error": str(e)}, status_code=500)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)