from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    # Ambil data dari request
    price = data.get("price")
    rsi = data.get("rsi")
    macd = data.get("macd")

    # Logika AI sederhana (simulasi)
    if rsi < 30 and macd > 0:
        signal = "🔥 Strong BUY signal"
    elif rsi > 70 and macd < 0:
        signal = "🔻 Strong SELL signal"
    else:
        signal = "⏸️ Neutral / Wait"

    return jsonify({
        "signal": signal,
        "price": price,
        "rsi": rsi,
        "macd": macd
    })

if __name__ == '__main__':
    app.run(port=5000)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    # Ambil data dari request
    price = data.get("price")
    rsi = data.get("rsi")
    macd = data.get("macd")

    # Logika AI sederhana (simulasi)
    if rsi < 30 and macd > 0:
        signal = "🔥 Strong BUY signal"
    elif rsi > 70 and macd < 0:
        signal = "🔻 Strong SELL signal"
    else:
        signal = "⏸️ Neutral / Wait"

    return jsonify({
        "signal": signal,
        "price": price,
        "rsi": rsi,
        "macd": macd
    })

if __name__ == '__main__':
    app.run(port=5000)
