from tradingview_ta import TA_Handler

def get_ta_analysis(symbol: str):
    handler = TA_Handler(symbol=symbol, exchange="BINANCE", screener="crypto", interval="1h")
    return handler.get_analysis()
