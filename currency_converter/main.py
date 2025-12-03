exchange_rates = {
    "USD": {
        "INR": 83.12,
        "GBP": 0.79,
        "EUR": 0.92,
        "AUD": 1.51
    },
    "INR": {
        "USD": 0.012,
        "GBP": 0.0095,
        "EUR": 0.011,
        "AUD": 0.018
    },
    "GBP": {
        "USD": 1.27,
        "INR": 105.4,
        "EUR": 1.16,
        "AUD": 1.92
    },
    "EUR": {
        "USD": 1.09,
        "INR": 90.8,
        "GBP": 0.86,
        "AUD": 1.66
    },
    "AUD": {
        "USD": 0.66,
        "INR": 54.8,
        "GBP": 0.52,
        "EUR": 0.60
    }
}


amount = int(input("Enter amount : "))

from_currency = input("Enter from currency : ")
to_currency = input("Enter to currency : ")


exchange_rate = exchange_rates[from_currency][to_currency]
converted_amount = amount * exchange_rate
print(f"Converted amount is {converted_amount} {to_currency} with exchange rate of {exchange_rate}")
