def generate_html(coins):

    html = """
<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<title>Market Pilot</title>

<style>

body{
    font-family: Arial;
    background:#101010;
    color:white;
    padding:20px;
}

h1{
    color:#00d084;
}

table{
    width:100%;
    border-collapse:collapse;
}

th,td{
    padding:10px;
    border-bottom:1px solid #333;
}

th{
    background:#222;
}

tr:hover{
    background:#1a1a1a;
}

</style>

</head>

<body>

<h1>🚀 Market Pilot MVP</h1>

<table>

<tr>
<th>#</th>
<th>Монета</th>
<th>Score</th>
<th>24h</th>
</tr>
"""

    for i, coin in enumerate(coins, start=1):

        html += f"""
<tr>
<td>{i}</td>
<td>{coin['symbol']}</td>
<td>{coin['market_pilot_score']:.1f}</td>
<td>{coin['change']:.2f}%</td>
</tr>
"""

    html += """
</table>

</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Файл index.html створено.")