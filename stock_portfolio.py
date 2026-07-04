# task 2 - stock portfolio tracker
print("=====================================")
print("     STOCK PORTFOLIO TRACKER     ")
print("=====================================")

# dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 200,
    "MSFT": 300,
    "AMZN": 150
}

total_value = 0

# number of different stocks
num_stocks = int(input("Enter the number of different stocks you own:"))

print()

# loop through each stock
for i in range(num_stocks):
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        stock_value = stock_prices[stock_name] * quantity
        total_value += stock_value

        print(f"value of {stock_name}: ₹{stock_value}\n")
    else:
        print("Stock not found in our database.\n")

print("-----------------------------------")
print(f"Total Portfolio value = ₹{total_value}")
print("-----------------------------------")
