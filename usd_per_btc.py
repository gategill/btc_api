from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from call_api import get_usd_per_btc


if __name__ == '__main__':
    try:
        usd_per_btc = get_usd_per_btc()
        print(usd_per_btc)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("Go play outside")