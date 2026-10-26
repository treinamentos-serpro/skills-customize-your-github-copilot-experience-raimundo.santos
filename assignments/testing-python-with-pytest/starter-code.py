def is_even(number):
    return number % 2 == 0


def average(numbers):
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return sum(numbers) / len(numbers)


def discounted_price(price, discount_percent):
    if price < 0:
        raise ValueError("price must be non-negative")
    if discount_percent < 0 or discount_percent >= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    return round(price * (1 - discount_percent / 100), 2)
