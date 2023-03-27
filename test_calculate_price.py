def calculate_price(order):
    # Input validation
    if not isinstance(order, dict):
        raise TypeError("order must be a dictionary")
    
    toppings = order.get('toppings')
    if not isinstance(toppings, list) or len(toppings) > 2:
        raise ValueError("toppings must be a list of at most 2 items")
    
    # Process order
    price = 0
    for topping in toppings:
        if topping == 'ไข่มุก':
            price += 5
        elif topping == 'เฉาก๊วย':
            price += 10
        elif topping == 'ถั่วแดง':
            price += 15
        elif topping == 'วิปครีม':
            price += 15
    
    # Validate output
    if not isinstance(price, int):
        raise ValueError("price must be an integer")
    
    return 25 + price
