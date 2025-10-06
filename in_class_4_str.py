import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import seaborn as sb
import yfinance as yf
sb.set_theme()

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()


    def get_data(self):
        """method that downloads data and stores in a DataFrame
           uncomment the code below wich should be the final two lines 
           of your method"""
        df = yf.download(self.symbol, start=self.start, end=self.end, progress=False)

        df.index = pd.to_datetime(df.index)

        self.calc_returns(df)
        self.data = df
        return df

    
    def calc_returns(self, df):
        """method that adds change and return columns to data"""
        close = df["Close"]
        df["change"] = (close / close.shift(1) - 1).round(4)
        df["instant_return"] = np.log(close).diff().round(4)

    
    def plot_return_dist(self):
        """method that plots instantaneous returns as histogram"""
        if self.data is None or self.data.empty:
            raise ValueError("No data to plot. Fetch data first.")
        vals = self.data["instant_return"].dropna()
        plt.figure(figsize=(8, 5))
        plt.hist(vals, bins=50, edgecolor="white")
        plt.title(f"{self.symbol} – Instantaneous Return Distribution")
        plt.xlabel("Daily log return")
        plt.ylabel("Frequency")
        plt.grid(axis="y", alpha=0.3)
        plt.show()


    def plot_performance(self):
        """method that plots stock object performance as percent """
        if self.data is None or self.data.empty:
            raise ValueError("No data to plot. Fetch data first.")
        close = self.data["Close"].dropna()
        perf = (close / close.iloc[0]) - 1.0  # percent gain/loss from start
        plt.figure(figsize=(9, 5))
        plt.plot(perf.index, perf.values)
        plt.title(f"{self.symbol} – Performance (from start)")
        plt.xlabel("Date")
        plt.ylabel("Return")
        plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.show()


def main():
    # uncomment (remove pass) code below to test
    test = Stock(symbol="AAPL")  # or "MSFT", "GOOG", etc.
    print(test.data.head())
    test.plot_performance()
    test.plot_return_dist()

if __name__ == '__main__':
    main() 