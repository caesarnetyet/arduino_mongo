from typing import TypedDict


class TemperatureHumidity(TypedDict):
    _id: str
    temperature: float
    humidity: float