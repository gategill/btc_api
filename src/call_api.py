from requests import Request, Session
import json
import os
from dotenv import load_dotenv
from icecream import ic

load_dotenv()


def get_usd_per_btc():
    api_response = _get_api_response()
    usd_per_btc = _extract_usd_per_btc_from_api_response(api_response)

    return usd_per_btc


def get_sats_per_usd():
    sats_per_btc = _get_sats_per_btc()
    usd_per_btc = get_usd_per_btc()
    sats_per_usd = sats_per_btc / usd_per_btc

    rounded_sats_per_usd = _round_price(sats_per_usd, 0)
    int_sats_per_usd = int(rounded_sats_per_usd)

    return int_sats_per_usd


##########################################################################


def _get_api_response():
    uri = _get_api_uri()
    request_parameters = _get_request_parameters()
    request_headers = _get_request_headers()
    session = _get_session(request_headers)

    api_response = session.get(uri, params=request_parameters)

    return api_response


def _extract_usd_per_btc_from_api_response(api_response):
    data = json.loads(api_response.text)
    usd_per_btc = data["data"][0]["quote"]["USD"]["price"]

    rounded_usd_per_btc = _round_price(usd_per_btc, 0)
    int_usd_per_btc = int(rounded_usd_per_btc)

    return int_usd_per_btc


def _get_sats_per_btc():
    # hundred million sats per btc
    SATS_PER_BTC = 100_000_000

    return SATS_PER_BTC


def _round_price(price, decimal_places=2):
    rounded_price = round(price, decimal_places)

    return rounded_price


def _get_session(request_headers):
    session = Session()
    session.headers.update(request_headers)

    return session


def _get_api_uri():
    uri = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    return uri


def _get_request_parameters():
    request_parameters = {"start": "1", "limit": "1", "convert": "USD"}

    return request_parameters


def _get_api_key():
    api_key = os.environ.get("API_KEY")
    if api_key:
        return api_key
    else:
        raise KeyError("Unable to find the environment variable: API_KEY")


def _get_request_headers():
    api_key = _get_api_key()
    request_headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": api_key,
    }

    return request_headers
