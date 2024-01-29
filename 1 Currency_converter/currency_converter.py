import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f" https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    if response.status_code==200:
        data = response.json()
        return data["conversion_rate"]
    else:
        raise Exception(f"Failed to fetch exchange rate. Error code{response.status_code}")




def main():
    api_key = "ea132fcba71a92f4cdb498f5"
    base_currency = input("Enter the base currency(e.g, INR, USD, EUR, GBP):").upper()
    target_currency = input("Enter the target currency(e.g, INR, USD, EUR, GBP):").upper()
    try:
        exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
        print("Exchange Rate=",exchange_rate)
        amount = float(input("Enter the amount to convert: "))
        converted_amount = amount*exchange_rate
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    except:
        print("An error occurred")


if __name__ == "__main__":
    main()