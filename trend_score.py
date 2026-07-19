def normalize(value, minimum, maximum):

    if value <= minimum:
        return 0

    if value >= maximum:
        return 100

    return (value - minimum) / (maximum - minimum) * 100


def calculate(candles):

    bullish = 0
    bearish = 0
    total_body = 0

    first_open = float(candles[0][1])
    last_close = float(candles[-1][4])

    for candle in candles:

        open_price = float(candle[1])
        close_price = float(candle[4])

        body = abs(close_price - open_price) / open_price * 100

        total_body += body

        if close_price > open_price:
            bullish += 1
        else:
            bearish += 1

    change = (last_close - first_open) / first_open * 100

    average_body = total_body / len(candles)

    bull_score = normalize(bullish, 0, 24)
    change_score = normalize(change, -10, 20)
    body_score = normalize(average_body, 0, 2)

    market_pilot_score = (
        bull_score +
        change_score +
        body_score
    ) / 3

    return {
        "bull_score": bull_score,
        "change_score": change_score,
        "body_score": body_score,
        "market_pilot_score": market_pilot_score,
        "change": change,
        "average_body": average_body
    }