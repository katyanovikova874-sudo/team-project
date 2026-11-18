def calc_discount(price, percent):
    new_price = price - (price * percent / 100)
    return new_price