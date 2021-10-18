from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from .routers import car_controller

from .store.load_data import load_data
load_data()

app = FastAPI()

app.include_router(car_controller.router)

app.mount("/static", StaticFiles(directory="./public/static"), name="static")

@app.get("/", include_in_schema=False)
def read_index():
    return FileResponse('./public/index.html')
