import logging
import os
import time
from prometheus_client import start_http_server
from irancell import update_data_stats


logger = logging.getLogger()


if __name__ == '__main__':
    start_http_server(9000)

    irancell_authorization_token = os.environ.get('IRANCELL_AUTHORIZATION_TOKEN')

    while True:
        try:
            update_data_stats(irancell_authorization_token)
        except Exception as err:
            logger.error(err)
        time.sleep(60)
