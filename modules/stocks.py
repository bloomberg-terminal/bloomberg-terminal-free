import yfinance as yf
import plotext as plt
from rich.table import Table

def get_stock_quote(ticker):
    """
    Fetches fundamental data for a given ticker using yfinance.
    Returns a Rich Table object.
    """
    try:
        # Fetch data
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # Check if data exists (yfinance returns empty dicts sometimes)
        if 'regularMarketPrice' not in info:
            return f"[red]Error:[/red] Ticker '{ticker}' not found or data unavailable."

        # Create a table formatted for the terminal
        table = Table(title=f"{info.get('shortName', ticker)} ({ticker})", expand=True)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="bold green")

        # Populate rows
        table.add_row("Price", f"${info.get('currentPrice', 'N/A')}")
        table.add_row("Market Cap", f"${info.get('marketCap', 0):,}")
        table.add_row("PE Ratio", str(info.get('trailingPE', 'N/A')))
        table.add_row("52 Week High", str(info.get('fiftyTwoWeekHigh', 'N/A')))
        table.add_row("Sector", info.get('sector', 'N/A'))
        
        return table
    except Exception as e:
        return f"[red]System Error:[/red] {str(e)}"

def get_stock_chart(ticker):
    """
    Generates an ASCII candle/line chart string using plotext.
    """
    try:
        # Download historical data (last 3 months)
        data = yf.download(ticker, period="3mo", interval="1d", progress=False)
        if data.empty:
            return "No data available for chart generation."

        prices = data['Close'].tolist()
        
        # Configure plotext for terminal rendering
        plt.clear_figure()
        plt.theme('dark')
        plt.plot(prices, label="Close Price")
        plt.title(f"{ticker} - 3 Months Trend")
        plt.xlabel("Trading Days")
        plt.ylabel("Price ($)")
        plt.grid(True, True)
        plt.frame(True)
        
        # Return the string representation of the chart
        return plt.build()
    except Exception as e:
        return f"[red]Chart Error:[/red] {str(e)}"
