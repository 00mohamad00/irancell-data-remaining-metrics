from typing import Dict, Tuple
from request import request_endpoint
from src.metrics import DATA_GAUGE

ENDPOINT_URL = "https://my.irancell.ir/api/sim/v2/account"


def get_header(irancell_authorization_token: str) -> Dict:
    return {
        "accept": "application/json",
        "authorization": irancell_authorization_token,
    }


def parse_response(response: Dict) -> Tuple[int, int]:
    total = 0
    remained = 0
    for offer in response.get('active_offers'):
        if offer.get('type') != 'data':
            continue
        total += int(offer.get('total_amount'))
        remained += int(offer.get('remained_amount'))
    return total, remained


def update_data_stats(irancell_authorization_token: str):
    response = request_endpoint(ENDPOINT_URL, headers=get_header(irancell_authorization_token))
    total, remained = parse_response(response)
    DATA_GAUGE.labels(type="remained").set(remained)
    DATA_GAUGE.labels(type="total").set(total)
