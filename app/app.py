from flask import Flask
import requests

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/price")
def price():
    data = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    ).json()

    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
