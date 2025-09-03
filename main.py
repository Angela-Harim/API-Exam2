from numbers import Number

from click.types import StringParamType
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"pong"}

class Car(BaseModel):
    id: str
    brand: str
    model: str
class Characteristic(BaseModel):
        max_speed: float
        max_fuel_capacity: float

@app.post("/cars")
def created_list_of_object_JSON(cars_payload: List[Cars]):
    cars_store.extend(cars_payload)
cars_as_json = []
for c in cars_store:
    cars_as_json.append(c.model_dump())
return JSONResponse(content=cars_as_json, status_code=201, media_type="application/json")
