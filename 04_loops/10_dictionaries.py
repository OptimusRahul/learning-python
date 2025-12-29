users = [
    {"id": 1, "total": 100, "coupon": "p20"},
    {"id": 2, "total": 200, "coupon": "p30"},
    {"id": 3, "total": 300, "coupon": "p40"},
]

discounts = {
    "p20": (0.2, 0),
    "p30": (0.3, 0),
    "p40": (0, 10),
}

for user in users:
    coupon: str = user["coupon"]  # type: ignore
    percent_discount, fixed = discounts.get(coupon, (0, 0))
    total: float = user["total"]  # type: ignore
    discount = total * percent_discount + fixed
    user["total"] = total - discount
    print(f"User {user['id']} has a discount of {discount} and total is {user['total']}")
