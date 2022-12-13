from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

if __name__ == "__main__":
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    parameters = {"start": "1", "limit": "1", "convert": "USD"}

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "API_KEY",
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        p = data["data"][0]["quote"]["USD"]["price"]
        print(round(p, 2))
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("Go play outside")
