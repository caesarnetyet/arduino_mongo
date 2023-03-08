from typing import TypedDict


class Arduino(TypedDict):
    model: str
    client_id: int
    sensors: list
    _id: str
