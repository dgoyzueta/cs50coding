import sys
import requests

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def get_bitcoin_value(coins):
    try:
        url="https://rest.coincap.io/v3/assets/bitcoin?apiKey=0b4e420c52371b4c8c8830259909887d2f2ffff904a6b6e9b1e4ba42d6aec8cd"
        response = requests.get(url)
    except requests.RequestException:
        sys.exit("Error in trying to obtain bitcoin value from the remote server")
    except requests.ConnectTimeout:
        sys.exit("The request timed out while trying to connect to the remote server")
    except requests.JSONDecodeError:
        sys.exit("Couldn’t decode the text into json")
    else:
        obj = response.json()
        bitcoin_price = None
        bitcoin_price = float(obj["data"]["priceUsd"])

        return f"${bitcoin_price * float(coins):,.4f}"

def main():
    match len(sys.argv):
        case 1:
            sys.exit("Missing command-line argument")
        case 2:
            if isfloat(sys.argv[1].strip()):
                print(get_bitcoin_value(sys.argv[1].strip()))
            else:
                sys.exit("Command-line argument is not a number")
        case _:
            sys.exit("Invalid number of command-line arguments")

if __name__ == "__main__":
    main()
