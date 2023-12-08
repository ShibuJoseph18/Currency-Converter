import requests

API_KEY = "Your API key"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

def convert_currency(base, outcome):
    url = f"{BASE_URL}"
    try:
        response = requests.get(url)
        data = response.json()
        output = data["data"][f"{outcome}"]
        return output
    except:
        print("Invalid Currency")


while True:
    base_currency = input("Enter the base currency (q for quit):").upper()
    if base_currency == "Q":
        break
    outcome_currency = input("Enter the outcome currency (q for quit):").upper()
    if outcome_currency == "Q":
        break
    final_output = convert_currency(base_currency, outcome_currency)
    if final_output is not None:
        print(final_output)
    else:
        continue
