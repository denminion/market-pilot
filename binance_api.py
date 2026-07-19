import requests

BASE_URL = "https://api.binance.com/api/v3"


def get_usdt_symbols():
    """Повертає список усіх активних USDT-пар."""

    url = f"{BASE_URL}/exchangeInfo"

    data = requests.get(url, timeout=10).json()

    symbols = []

    for s in data["symbols"]:
        if s["quoteAsset"] == "USDT" and s["status"] == "TRADING":
            symbols.append(s["symbol"])

    return symbols


def get_24h_candles(symbol):
    """Повертає 24 останні годинні свічки."""

    url = (
        f"{BASE_URL}/klines"
        f"?symbol={symbol}"
        f"&interval=1h"
        f"&limit=24"
    )

    return requests.get(url, timeout=10).json()