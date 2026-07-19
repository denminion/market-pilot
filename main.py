import requests

print("=" * 50)
print("Market Pilot")
print("Аналіз BTCUSDT")
print("=" * 50)

symbol = "BTCUSDT"

url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1h&limit=24"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    candles = response.json()

    print(f"\nОтримано {len(candles)} свічок.\n")

    first_open = float(candles[0][1])
    last_close = float(candles[-1][4])

    change = (last_close - first_open) / first_open * 100

    print(f"Монета: {symbol}")
    print(f"Ціна 24 години тому: {first_open:.2f}")
    print(f"Поточна ціна: {last_close:.2f}")
    print(f"Зміна: {change:.2f}%")

except Exception as e:
    print("Помилка:")
    print(e)
    
bullish = 0
bearish = 0

for candle in candles:
    open_price = float(candle[1])
    close_price = float(candle[4])

    if close_price > open_price:
        bullish += 1
    else:
        bearish += 1

first_open = float(candles[0][1])
last_close = float(candles[-1][4])

change = (last_close - first_open) / first_open * 100

trend_score = bullish / len(candles) * 100

print(f"\nМонета: {symbol}")
print(f"Зміна за 24 години: {change:.2f}%")
print(f"Зелених свічок: {bullish}")
print(f"Червоних свічок: {bearish}")
print(f"Trend Score: {trend_score:.1f}/100")