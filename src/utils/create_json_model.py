from pydantic import create_model
from typing import Type

dynamic_fields = {
    "name": (str, ...),
    "age": (int, ...),
}

Dynamic_Model = create_model("DynamicModel", **dynamic_fields)

data_schema = {
        "product_id": int,
        "quantity": int,
        "price": float,
}
    
# Convert schema to Pydantic-compatible format
pydantic_fields = {
    field_name: (field_type, ...) for field_name, field_type in data_schema.items()
}
DynamicProductPayload = create_model("DynamicProductPayload", **pydantic_fields)

payload1 = Dynamic_Model("Alice", 30)
print(payload1.model_dump())

# Using DynamicProductPayload
product_data = {"product_id": 123, "quantity": 5, "price": 19.99}
product_payload = DynamicProductPayload(**product_data)
print(product_payload.model_dump())