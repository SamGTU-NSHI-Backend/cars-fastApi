from typing import List
from fastapi import APIRouter
from ..store import cars

router = APIRouter(
    prefix="/cars",
    tags=["cars"]
)

@router.get("/",
response_model=List[cars.Car],
description="Get all cars.")
async def get_cars():
    return cars.cars

@router.get("/sorted",
response_model=List[cars.Car],
description="Get all cars sorted by model year.")
async def get_sorted_by_year_cars():
    return cars.get_cars_sorted_by_year()

@router.get("/maker",
response_model=List[cars.Car],
description="Find cars by maker (full name or first charachters).")
async def cars_by_maker(maker: str):
    return cars.find_cars_by_maker(maker)

@router.get("/model",
response_model=List[cars.Car],
description="Find cars by model (full name or first charachters).")
async def cars_by_model(model: str):
    return cars.find_cars_by_model(model)

@router.get("/{id}",
response_model=cars.Car,
description="Find car by id.")
async def find_car(id: int):
    return cars.find_car_by_id(id)

@router.post("/",
response_model=cars.Car,
description="Create new car (id in object is not used).")
async def create_car(car: cars.Car):
    cars.add_car(car)
    return car

@router.delete("/{id}",
description="Delete car by id.")
async def delete_car(id: int):
    cars.remove_car_by_id(id)

@router.post("/{id}",
response_model=cars.Car,
description="Update car with id in path param (id in object is not used)")
async def update_car(id: int, car: cars.Car):
    return cars.update_car(car, id)
