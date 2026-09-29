def calculate_items_subtotal(items):
    subtotal = 0

    for item in items:
        price = item["price"]
        quantity = item["qty"]

        if price > 0:
            if quantity > 0:
                subtotal = subtotal + price * quantity

    return subtotal


def calculate_member_discount(subtotal, is_member):
    if is_member == True:
        if subtotal > 100:
            discount = subtotal * 0.2
        else:
            if subtotal > 50:
                discount = subtotal * 0.1
            else:
                discount = 0
    else:
        discount = 0

    return discount


def calculate_shipping_cost(country):
    if country == "PK":
        shipping_cost = 5
    else:
        if country == "US":
            shipping_cost = 15
        else:
            shipping_cost = 25

    return shipping_cost


def calculate_order_total(order):
    subtotal = calculate_items_subtotal(order["items"])
    discount = calculate_member_discount(subtotal, order["member"])
    shipping_cost = calculate_shipping_cost(order["country"])

    return subtotal - discount + shipping_cost