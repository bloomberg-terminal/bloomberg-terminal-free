import requests
from rich.table import Table

def get_top_crypto():
    """
    Fetches the top 10 cryptocurrencies by market cap via CoinGecko API.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code != 200:
             return f"[red]API Error:[/red] Status Code {response.status_code}"

        data = response.json()
        
        # Initialize table
        table = Table(title="TOP 10 CRYPTO ASSETS (Real-Time)", expand=True)
        table.add_column("Rank", justify="right", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_column("Price ($)", justify="right", style="green")
        table.add_column("24h Change %", justify="right")

        # Parse data
        for coin in data:
            change = coin['price_change_percentage_24h']
            # Color coding: Green for profit, Red for loss
            color = "green" if change is not None and change > 0 else "red"
            change_str = f"{change:.2f}%" if change else "N/A"
            
            table.add_row(
                str(coin['market_cap_rank']),
                coin['name'],
                f"${coin['current_price']:,}",
                f"[{color}]{change_str}[/{color}]"
            )
        return table
    except Exception as e:
        return f"[red]Connection Error:[/red] {str(e)}"
