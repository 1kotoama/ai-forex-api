from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    rsi = data.get("rsi")
    macd = data.get("macd")
    signal = "📉 Strong SELL signal" if rsi > 70 and macd < 0 else \
             "📈 Strong BUY signal" if rsi < 30 and macd > 0 else \
             "🔵 Neutral"
    return jsonify({"signal": signal})

if __name__ == '__main__':
    app.run(debug=True)
