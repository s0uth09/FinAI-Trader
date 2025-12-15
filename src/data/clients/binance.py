import ccxt

exchange = ccxt.binance()

def get_market_data(symbol: str):
    return exchange.fetch_ticker(symbol)
