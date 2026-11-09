'''
Example 11 — Custom JSON Serialization
'''
import json
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from decimal import Decimal


@dataclass
class Order:
    order_id: int
    amount: Decimal
    created_at: datetime


def custom_encoder(obj):
    if isinstance(obj, Decimal):
        return str(obj)

    if isinstance(obj, datetime):
        return obj.isoformat()

    raise TypeError(
        f"Object of type {type(obj).__name__} "
        "is not JSON serializable"
    )


order = Order(
    101,
    Decimal("2499.99"),
    datetime.now(UTC)
)

json_data = json.dumps(
    asdict(order),
    default=custom_encoder,
    indent=4
)

print(json_data)

restored = json.loads(json_data)

restored["amount"] = Decimal(restored["amount"])
restored["created_at"] = datetime.fromisoformat(
    restored["created_at"]
)

print(restored)