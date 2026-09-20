# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

# Display available stocks
print("===== Stock Portfolio Tracker =====")
print("Available Stocks:", ", ".join(stock_prices.keys()))

# Ask user how many different stocks they want
number_of_stocks = int(input("How many stocks do you want to add? "))

total_investment = 0

# Store portfolio details
portfolio = []

# Get stock details from user
for i in range(number_of_stocks):

    stock_name = input("\nEnter stock symbol: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock_name]

        investment = price * quantity

        total_investment += investment

        portfolio.append(
            (stock_name, quantity, price, investment)
        )

        print("Investment added:", investment)

    else:
        print("Stock not available in our price list.")

# Display portfolio
print("\n===== Portfolio Summary =====")

for stock, quantity, price, investment in portfolio:
    print(
        f"{stock} | Quantity: {quantity} | "
        f"Price: ${price} | Investment: ${investment}"
    )

print("--------------------------------")
print(f"Total Investment: ${total_investment}")

# Save result to a text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":

    with open("portfolio.txt", "w") as file:

        file.write("===== Stock Portfolio =====\n")

        for stock, quantity, price, investment in portfolio:
            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${price} | Investment: ${investment}\n"
            )

        file.write("--------------------------------\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("Portfolio saved successfully!")