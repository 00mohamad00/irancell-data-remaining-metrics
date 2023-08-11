from prometheus_client import Gauge


DATA_GAUGE = Gauge('irancell_data_remaining', 'Status of Irancell data remaining and total', ["type"])
