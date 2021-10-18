import json
from typing import Set
from ..store.cars import *

def load_data():
    with open("data/cars.json") as json_file:
        data = json.load(json_file)

        for value in data:
            car = Car(
                maker=value['car_make'],
                model=value['car_model'],
                model_year=value['car_model_year']
                )
            add_car(car)
