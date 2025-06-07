from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates

app = Flask(__name__)
c = CurrencyRates()

# List of currencies as (code, full name)
CURRENCIES = [
    ("USD", "United States Dollar"),
    ("EUR", "Euro"),
    ("GBP", "British Pound Sterling"),
    ("INR", "Indian Rupee"),
    ("JPY", "Japanese Yen"),
    ("AUD", "Australian Dollar"),
    ("CAD", "Canadian Dollar"),
    ("CHF", "Swiss Franc"),
    ("CNY", "Chinese Yuan"),
    ("NZD", "New Zealand Dollar"),
    ("SGD", "Singapore Dollar"),
    ("HKD", "Hong Kong Dollar"),
    ("ZAR", "South African Rand"),
    ("SEK", "Swedish Krona"),
    ("NOK", "Norwegian Krone"),
    ("MXN", "Mexican Peso"),
    ("BRL", "Brazilian Real"),
    ("RUB", "Russian Ruble"),
    ("KRW", "South Korean Won"),
    ("TRY", "Turkish Lira")
]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            amount = float(request.form.get("amount"))
            from_currency = request.form.get("from_currency")
            to_currency = request.form.get("to_currency")

            result_value = c.convert(from_currency, to_currency, amount)
            result = f"{amount:.2f} {from_currency} = {result_value:.2f} {to_currency}"
        except ValueError:
            error = "Invalid amount entered. Please enter a numeric value."
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template("index.html", result=result, error=error, currencies=CURRENCIES)

if __name__ == "__main__":
    app.run(debug=True)
