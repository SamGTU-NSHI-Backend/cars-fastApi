import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

def get_file_handler():
    file_handler = logging.FileHandler("logs/x.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler

def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(get_file_handler())
logger.addHandler(get_stream_handler())

app = FastAPI()

app.mount("/static", StaticFiles(directory="./public/static"), name="static")

@app.get("/")
def read_index():
    logger.info("Input path /")
    return FileResponse('./public/index.html')

@app.get("/hello")
def hello():
    logger.info("Input path /hello")
    return {"value": "Hello World"}
