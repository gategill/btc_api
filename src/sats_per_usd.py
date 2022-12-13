from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from call_api import get_sats_per_usd


if __name__ == "__main__":
    try:
        sats_per_usd = get_sats_per_usd()
        print(sats_per_usd)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("Go play outside")
