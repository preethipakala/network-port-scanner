#!/usr/bin/env python3
"""
banner.py — Attempt to grab a service banner from an open socket.

A "banner" is the greeting message a service sends when you connect.
For example, SSH sends: 'SSH-2.0-OpenSSH_8.9'
This tells us the service name and version — useful info in security audits.
"""

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

# Well-known ports that respond to an HTTP-style request
HTTP_PORTS = {80, 8080, 8000, 8443, 443}


def grab_banner(sock: socket.socket) -> str:
    """
    Try to read a banner from an already-connected socket.
    Returns the banner string, or empty string if none received.
    """
    try:
        peer = sock.getpeername()
        port = peer[1] if peer else None

        # HTTP ports need a request before they respond
        if port in HTTP_PORTS:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")

        sock.settimeout(2)
        banner = sock.recv(1024).decode("utf-8", errors="ignore").strip()
        return banner[:80]  # truncate long banners
    except Exception as e:
        print(f"Error grabbing banner: {e}")
        return ""


def scan_port(host: str, port: int, timeout: int) -> str:
    """
    Scan a single port on the given host.
    Returns the banner string, or empty string if none received.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            return grab_banner(sock)
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
            return ""


def main():
    parser = argparse.ArgumentParser(description="Grab service banners")
    parser.add_argument("--host", required=True, help="Host to scan")
    parser.add_argument(
        "--port-range", required=True, help="Port range to scan (e.g. 1-100)"
    )
    parser.add_argument(
        "--timeout", type=int, default=2, help="Socket timeout in seconds"
    )
    parser.add_argument(
        "--threads", type=int, default=100, help="Number of threads to use"
    )
    args = parser.parse_args()

    host, port_range = args.host, args.port_range
    start, end = map(int, port_range.split("-"))
    timeout = args.timeout
    threads = args.threads

    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = list(
            executor.map(lambda p: scan_port(host, p, timeout), range(start, end + 1))
        )

    for port, banner in enumerate(results, start=start):
        if banner:
            print(f"Port {port} banner: {banner}")


if __name__ == "__main__":
    main()
