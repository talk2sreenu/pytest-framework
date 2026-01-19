from pydantic import BaseModel
from typing import Optional, List

class BarModel(BaseModel):
    whatever: str

class FooBarModel(BaseModel):
    foo: str
    bar: BarModel
    baz: Optional[List[str]] = None

class booBarModel(BaseModel):
    boo: str
    bar: BarModel

m = FooBarModel(foo="Test", bar=BarModel(whatever="BarModel Testing"), baz=["baz1", "baz2"])
b = booBarModel(boo="Boo", bar=BarModel(whatever="BooBarModel Testing"))

final_json = m.model_dump_json(indent=2)
print(final_json)

another_json = b.model_dump_json(indent=2)
print(another_json)