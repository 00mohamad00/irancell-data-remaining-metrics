import os
import time
from prometheus_client import start_http_server
from irancell import get_data_stats

if __name__ == '__main__':
    start_http_server(9000)

    irancell_authorization_token = os.environ.get('IRANCELL_AUTHORIZATION_TOKEN')

    while True:
        get_data_stats(irancell_authorization_token)
        time.sleep(60)
