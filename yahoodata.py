import argparse
import yfinance as yf
import pandas as pd

def fetch_stock_data(stock_symbol, start_date, end_date):
    stock = yf.Ticker(stock_symbol)
    data = stock.history(start=start_date, end=end_date)
    return data

def save_to_csv(data, filename):
    data.to_csv(filename)
    print(f"Data saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description='Trading Strategy Execution')
    parser.add_argument("-strategy", default='TDQN', type=str, help="Name of the trading strategy")
    parser.add_argument("-stock", default='AAPL', type=str, help="Ticker symbol of the stock (e.g., 'AAPL' for Apple)")
    parser.add_argument("-start_date", default='2020-1-1', type=str, help="Start date for the data (format: YYYY-MM-DD)")
    parser.add_argument("-end_date", default='2021-1-1', type=str, help="End date for the data (format: YYYY-MM-DD)")
    
    args = parser.parse_args()

    # Fetching stock data
    stock_data = fetch_stock_data(args.stock, args.start_date, args.end_date)

    # Save data to CSV
    csv_filename = f"Data/{args.stock}_{args.start_date}_{args.end_date}.csv"
    save_to_csv(stock_data, csv_filename)

    # Displaying some basic info
    print(f"Strategy: {args.strategy}")
    print(f"Stock Data for {args.stock} from {args.start_date} to {args.end_date}:")
    print(stock_data.head())  # Display first few rows of the DataFrame

if __name__ == "__main__":
    main()

