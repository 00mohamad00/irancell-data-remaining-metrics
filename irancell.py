from typing import Dict
import requests
from prometheus_client import Gauge

DATA_GAUGE = Gauge('irancell_data_remaining', 'Status of Irancell data remaining and total',
                   ["type"])
ENDPOINT_URL = "https://my.irancell.ir/api/sim/v2/account"


def request_endpoint(url, params=None, headers=None) -> Dict:
    try:
        res = requests.get(url, params=params, headers=headers)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        print("Error occurred: ", e)


def get_data_stats(irancell_authorization_token: str):
    headers = {
        "accept": "application/json",
        "authorization": irancell_authorization_token,
    }
    response = request_endpoint(ENDPOINT_URL, headers=headers)

    total = 0
    remained = 0
    for offer in response.get('active_offers'):
        if offer.get('type') != 'data':
            continue
        total += int(offer.get('total_amount'))
        remained += int(offer.get('remained_amount'))

    DATA_GAUGE.labels(type="remained").set(remained)
    DATA_GAUGE.labels(type="total").set(total)