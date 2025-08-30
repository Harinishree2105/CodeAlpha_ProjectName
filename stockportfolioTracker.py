
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 300
}

def stock_portfolio_tracker():
    total_investment = 0
    print("📈 Welcome to Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not found. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("⚠️ Please enter a valid number for quantity.")
            continue

        investment = stock_prices[stock] * quantity
        total_investment += investment
        print(f"Added {quantity} shares of {stock} worth ${investment}")

    print("\n💰 Total Investment Value:", total_investment)

# Run the tracker
stock_portfolio_tracker()
