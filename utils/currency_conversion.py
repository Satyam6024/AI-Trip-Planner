import requests

class CurrencyConverter:
    def __init__(self, api_key: str):
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    
    def convert(self, amount:float, from_currency:str, to_currency:str):
        """Convert the amount from one currency to another"""
        url = f"{self.base_url}/{from_currency}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("API call failed:", response.json())
        rates = response.json()["conversion_rates"]
        if to_currency not in rates:
            raise ValueError(f"{to_currency} not found in exchange rates.")
        return amount * rates[to_currency]
    


# import requests

# class CurrencyConverter:
#     def __init__(self, api_key: str):
#         self.api_key = api_key
#         self.base_url = "https://api.exchangeratesapi.io/v1/latest"

#     def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
#         """
#         Convert the amount from one currency to another using exchangeratesapi.io.
#         """
#         # Request latest rates with specified base currency
#         url = f"{self.base_url}?access_key={self.api_key}&base={from_currency}&symbols={to_currency}"
#         response = requests.get(url)

#         if response.status_code != 200:
#             raise Exception("API call failed:", response.json())

#         data = response.json()

#         # Ensure success flag
#         if not data.get("success", False):
#             raise Exception("API error:", data)

#         rates = data.get("rates", {})
#         if to_currency not in rates:
#             raise ValueError(f"{to_currency} not found in exchange rates.")

#         return amount * rates[to_currency]
