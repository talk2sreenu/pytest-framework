import json 
from pydantic import BaseModel
from typing import Type, Optional

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[str] = None
    friends: list[int] = []

user_data = User(id=123, name="Srinivasu", signup_ts="Python", friends=[1, 2, 3])

json_string = user_data.model_dump_json()

print(json_string)
print(type(json_string))

dict_data = user_data.model_dump()
print(dict_data)
print(type(dict_data))
