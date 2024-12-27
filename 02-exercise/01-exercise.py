# exercise: Review the following code and provide feedback to improve it.

def apply_discount(prices, discount_rate):
    discounted_prices = []
    for price in prices:
        discounted_prices.append(price - (price * discount_rate))
    return discounted_prices

prices = [100, 200, 300]
discount_rate = 0.1
print(apply_discount(prices, discount_rate))