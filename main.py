def calculate_price(order):
    # Validate input
    if type(order) != dict:
        raise TypeError("Invalid input type. Expected dict, but got {}.".format(type(order)))
    
    toppings = order.get("toppings")
    if not toppings:
        raise ValueError("Missing required input 'toppings'.")
    
    if not isinstance(toppings, list):
        raise TypeError("Invalid input type for 'toppings'. Expected list, but got {}.".format(type(toppings)))
    
    if len(toppings) > 2:
        raise ValueError("Too many toppings selected. Maximum of 2 allowed.")
    
    # Calculate price
    price = 0
    for topping in toppings:
        if topping == "ชานมแก้ว":
            price += 25
        elif topping == "ท๊อปปิ้ง":
            price += 5
        elif topping == "เฉาก๊วย":
            price += 10
        elif topping == "ถั่วแดง":
            price += 15
        elif topping == "วิปครีม":
            price += 15
    
    return price

def test_calculate_price():
    # Test valid inputs
    assert calculate_price({"toppings": ["ชานมแก้ว"]}) == 25
    assert calculate_price({"toppings": ["ท๊อปปิ้ง", "เฉาก๊วย"]}) == 15
    assert calculate_price({"toppings": ["วิปครีม", "ถั่วแดง"]}) == 30
    
    # Test invalid inputs
    try:
        calculate_price(None)
    except TypeError as e:
        assert str(e) == "Invalid input type. Expected dict, but got <class 'NoneType'>."
    
    try:
        calculate_price("not a dict")
    except TypeError as e:
        assert str(e) == "Invalid input type. Expected dict, but got <class 'str'>."
    
    try:
        calculate_price({})
    except ValueError as e:
        assert str(e) == "Missing required input 'toppings'."
    
    try:
        calculate_price({"toppings": "not a list"})
    except TypeError as e:
        assert str(e) == "Invalid input type for 'toppings'. Expected list, but got <class 'str'>."
    
    try:
        calculate_price({"toppings": ["too", "many", "toppings"]})
    except ValueError as e:
        assert str(e) == "Too many toppings selected. Maximum of 2 allowed."
