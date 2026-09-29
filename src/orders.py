def calculate_items_subtotal(items):
    subtotal = 0

    for item in items:
        price = item["price"]
        quantity = item["qty"]

        if price <= 0:
            continue
        if quantity <= 0:
            continue

        subtotal = subtotal + price * quantity

    return subtotal


def calculate_member_discount(subtotal, is_member):
    if is_member != True:
        return 0
    if subtotal > 100:
        return subtotal * 0.2
    if subtotal > 50:
        return subtotal * 0.1

    return 0


def calculate_shipping_cost(country):
    if country == "PK":
        return 5
    if country == "US":
        return 15

    return 25


def calculate_order_total(order):
    subtotal = calculate_items_subtotal(order["items"])
    discount = calculate_member_discount(subtotal, order["member"])
    shipping_cost = calculate_shipping_cost(order["country"])

    return subtotal - discount + shipping_cost