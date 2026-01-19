import sys
import requests
import json

def main():
    amt = get_amt()
    price = get_price()
    cost = amt * price
    print(f"${cost:,.4f}")

# command-line argument the number of Bitcoins, 𝑛,
def get_amt():
    if len(sys.argv) == 2:
        try:
            amt = float(sys.argv[1])
            return amt
        except ValueError:
            sys.exit("Command-line argument is not a number")
    elif len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

#API
def get_price():
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=6967df3a6a609e4a9c50e502cbae195121119f65a2c4fb71282275a7c86738ba"
        ) 
        content = response.json()
        price = float(content["data"]['priceUsd'])
        return price
    except requests.RequestException:
        sys.exit()

if __name__ == "__main__":
    main()
