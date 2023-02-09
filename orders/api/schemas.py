"""
Implementation of the validation models using pydantic
"""
from enum import Enum
from typing import List, Optional
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field, conlist, conint


class Size(Enum):
    small = "small"
    medium = "medium"
    big = "big"


class Status(Enum):
    created = "created"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"


class OrderItemSchema(BaseModel):
    product: str
    # constraint the values of a property by setting type to
    # enumeration
    size: Size
    # strict=True value passed should be > 1
    quantity: Optional[conint(ge=1, strict=True)] = 1


class CreateOrderSchema(BaseModel):
    order: conlist(OrderItemSchema, min_items=1)


class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: Status


class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]