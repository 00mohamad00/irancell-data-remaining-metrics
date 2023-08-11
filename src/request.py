import logging
from typing import Dict
import requests


logger = logging.getLogger()


def request_endpoint(url: str, headers: Dict = None) -> Dict:
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as err:
        logger.error("Request failed", exc_info=err)
        raise err
