import csv
import os
from datetime import datetime

STOCK_PRICES = {
    "AAPL":  180.00,   
    "TSLA":  250.00,   
    "GOOGL": 140.00,   
    "AMZN":  185.00,   
    "MSFT":  420.00,
    "META":  500.00,   
    "NFLX":  650.00,
}

def show_available_stocks():
    print("\n  📈 Available Stocks:")
    print("  " + "-" * 30)
    print(f"  {'Symbol':<10} {'Price (USD)':>12}")
    print("  " + "-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<10} ${price:>11.2f}")
    print("  " + "-" * 30)


def get_stock_symbol():
    while True:
        symbol = input("\n  Enter stock symbol (or 'done' to finish): ").upper().strip()
        if symbol == "DONE":
            return None
        elif symbol in STOCK_PRICES:
            return symbol
        else:
            print(f"  ⚠  '{symbol}' not found. Choose from the list above.")


def get_quantity(symbol):
    while True:
        try:
            qty = int(input(f"  Enter quantity for {symbol}: ").strip())
            if qty <= 0:
                print("  ⚠  Quantity must be greater than 0.")
            else:
                return qty
        except ValueError:
            print("  ⚠  Please enter a whole number.")


def display_portfolio(portfolio):
    if not portfolio:
        print("\n  ⚠  Your portfolio is empty.")
        return

    print("\n  " + "=" * 50)
    print("         📊 YOUR STOCK PORTFOLIO SUMMARY")
    print("  " + "=" * 50)
    print(f"  {'Stock':<8} {'Qty':>6} {'Price':>12} {'Total Value':>14}")
    print("  " + "-" * 50)

    grand_total = 0
    for symbol, qty in portfolio.items():
        price       = STOCK_PRICES[symbol]
        total       = price * qty
        grand_total += total
        print(f"  {symbol:<8} {qty:>6} ${price:>11.2f} ${total:>13.2f}")

    print("  " + "-" * 50)
    print(f"  {'TOTAL INVESTMENT':>38} ${grand_total:>13.2f}")
    print("  " + "=" * 50 + "\n")


def save_to_csv(portfolio):
    if not portfolio:
        print("  ⚠  Nothing to save — portfolio is empty.")
        return

    filename  = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    rows      = []
    grand_total = 0

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        total = price * qty
        grand_total += total
        rows.append([symbol, qty, f"{price:.2f}", f"{total:.2f}"])

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock Symbol", "Quantity", "Price (USD)", "Total Value (USD)"])
        writer.writerows(rows)
        writer.writerow([])
        writer.writerow(["", "", "GRAND TOTAL", f"{grand_total:.2f}"])

    print(f"\n  ✅ Portfolio saved to '{filename}'")
    print(f"  📂 Location: {os.path.abspath(filename)}\n")


def main():
    print("\n" + "=" * 50)
    print("    💼 Welcome to Stock Portfolio Tracker!")
    print("=" * 50)

    portfolio = {}

    while True:
        print("\n  MENU:")
        print("  1. Add stock to portfolio")
        print("  2. View portfolio summary")
        print("  3. Save portfolio to CSV")
        print("  4. Exit")

        choice = input("\n  Choose an option (1-4): ").strip()

        if choice == "1":
            show_available_stocks()
            symbol = get_stock_symbol()
            if symbol:
                qty = get_quantity(symbol)
                if symbol in portfolio:
                    portfolio[symbol] += qty
                    print(f"  ✅ Updated {symbol}: now {portfolio[symbol]} shares.")
                else:
                    portfolio[symbol] = qty
                    print(f"  ✅ Added {qty} share(s) of {symbol}.")

        elif choice == "2":
            display_portfolio(portfolio)

        elif choice == "3":
            display_portfolio(portfolio)
            save_to_csv(portfolio)

        elif choice == "4":
            print("\n  👋 Goodbye! Happy investing!\n")
            break

        else:
            print("  ⚠  Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()