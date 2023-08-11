# Irancell Data Remaining Metrics

This Python code is designed to request data remaining statistics from your Irancell phone network provider and collect the information using Prometheus metrics.


## Configuration
The code requires an environment variable `IRANCELL_AUTHORIZATION_TOKEN` to be set. This token is required for authentication with the Irancell API. Make sure to set the environment variable with your Irancell authorization token before running the code.

## Docker

You can run the code using Docker. Follow these steps:

1. Build the Docker image using the provided `Dockerfile`:

```bash
docker build -t irancell-data-metrics .
```

2. Set the `IRANCELL_AUTHORIZATION_TOKEN` environment variable:

```bash
export IRANCELL_AUTHORIZATION_TOKEN=<your-authorization-token>
```

3. Run the Docker container:

```bash
docker run -d -p 9000:9000 --env IRANCELL_AUTHORIZATION_TOKEN=$IRANCELL_AUTHORIZATION_TOKEN irancell-data-metrics
```

4. Verify that the code is running and metrics are being exposed by accessing `http://localhost:9000` in your web browser.


## Prometheus Integration

To integrate the Prometheus metrics collected by this code into your Prometheus setup, follow these steps:

1. Ensure that the Prometheus Python client library (`prometheus_client`) is installed.

1. Configure Prometheus to scrape the metrics exposed by this code. Add the following job configuration to your Prometheus configuration file:

```yaml
scrape_configs:
  - job_name: 'irancell_data'
    static_configs:
      - targets: ['localhost:9000']  # Replace with the actual host and port where this code is running
```

3. Start the Prometheus server and verify that it successfully scrapes the metrics from this code.

1. Access the Prometheus web interface and explore the Irancell data remaining metrics under the `irancell_data_remaining` metric.

## Troubleshooting

- If you encounter any errors while running the code, ensure that you have provided a valid Irancell authorization token and that your network connectivity is functioning correctly.

## Contributing

If you find any issues with this code or have suggestions for improvement, please feel free to contribute by opening an issue or submitting a pull request on the GitHub repository.

## License

This code is licensed under the [MIT License ↗](https://opensource.org/licenses/MIT).
