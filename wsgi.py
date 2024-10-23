from uvicorn import run
from main import app

def application(environ, start_response):
    run(app, host="0.0.0.0", port=8000)
