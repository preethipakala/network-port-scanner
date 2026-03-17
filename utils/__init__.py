# Utils package for network-port-scanner
import argparse
import concurrent.futures
import logging


def scan_port(host, port, timeout):
    """
    Scan a single port on a host.

    Args:
        host (str): Host IP address.
        port (int): Port number.
        timeout (int): Scan timeout in seconds.

    Returns:
        bool: Whether the port is open.
    """
    # TO DO: implement port scanning logic
    return True  # placeholder for actual implementation


def concurrent_scan(host, port_range, threads, timeout):
    """
    Scan multiple ports concurrently.

    Args:
        host (str): Host IP address.
        port_range (list): List of port numbers to scan.
        threads (int): Number of threads to use for scanning.
        timeout (int): Scan timeout in seconds.

    Returns:
        list: List of tuples containing host, port, and whether the port is open.
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        results = list(executor.map(lambda p: scan_port(host, p, timeout), port_range))
    return [(host, p, r) for p, r in zip(port_range, results)]


def main():
    parser = argparse.ArgumentParser(description="Network Port Scanner")
    parser.add_argument("--host", required=True, help="Host IP address")
    parser.add_argument(
        "--port-range", required=True, help="List of port numbers to scan (e.g., 1-100)"
    )
    parser.add_argument(
        "--threads", type=int, default=100, help="Number of threads to use for scanning"
    )
    parser.add_argument(
        "--timeout", type=int, default=5, help="Scan timeout in seconds"
    )
    args = parser.parse_args()

    host, port_range = args.host, [int(p) for p in args.port_range.split("-")]
    threads, timeout = args.threads, args.timeout

    logging.info(
        f"Scanning {host} ports {port_range[0]}-{port_range[-1]} concurrently with {threads} threads..."
    )
    results = concurrent_scan(host, port_range, threads, timeout)
    for host, port, open in results:
        logging.info(f'Port {port} on {host} is {"open" if open else "closed"}')


if __name__ == "__main__":
    import logging.config

    logging.config.dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "handlers": {
                "wsgi": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://flask.logging.wsgi_errors_stream",
                    "formatter": "default",
                }
            },
            "root": {"level": "INFO", "handlers": ["wsgi"]},
        }
    )
    main()
