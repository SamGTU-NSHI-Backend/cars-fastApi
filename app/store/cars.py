from ..models.car import Car
from typing import List, Optional

cars: List[Car] = []

def find_car_by_id(id: int) -> Optional[Car] :
    values = list(filter(lambda v: v.id == id, cars))
    return values[0] if values else None

def add_car(car: Car):
    last_id = cars[-1].id if cars else 0
    car.id = last_id + 1
    cars.append(car)

def remove_car_by_id(id: int):
    indexes = []
    for index in range(len(cars)):
        car = cars[index]
        if car.id == id:
            indexes.append(index)
    indexes.reverse()
    for index in indexes:
        cars.pop(index)

def update_car(car: Car, id: int) -> Optional[Car] :
    old_car = find_car_by_id(id)
    if old_car:
        old_car.maker = car.maker
        old_car.model = car.model
        old_car.model_year = car.model_year
    return old_car

def find_cars_by_maker(maker: str) -> List[Car] :
    return list(filter(lambda car: car.maker.lower().startswith(maker.lower()), cars))

def find_cars_by_model(model: str) -> List[Car] :
    return list(filter(lambda car: car.model.lower().startswith(model.lower()), cars))

def get_cars_sorted_by_year() -> List[Car] :
    return list(sorted(cars, key=lambda car: car.model_year))
