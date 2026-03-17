#!/usr/bin/env python3
"""
Network Port Scanner
A beginner-friendly tool to scan open ports on a target host.

Usage:
    python scanner.py --host <IP or hostname> [--start PORT] [--end PORT] [--timeout SECS] [--output FILE]

Example:
    python scanner.py --host 127.0.0.1 --start 1 --end 1024
"""

import socket
import argparse
import sys
from datetime import datetime
from utils.banner import grab_banner
from utils.reporter import print_result, save_report, print_header


# --- Default Settings -------------------------------------------
DEFAULT_START_PORT = 1
DEFAULT_END_PORT   = 1024
DEFAULT_TIMEOUT    = 1.0  # seconds


def scan_port(host: str, port: int, timeout: float) -> dict:
    """
    Attempt a TCP connection to host:port.
    Returns a dict with 'port', 'status', and optional 'banner'.
    """
    result = {"port": port, "status": "closed", "banner": ""}
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        conn = sock.connect_ex((host, port))  # 0 = success
        if conn == 0:
            result["status"] = "open"
            result["banner"] = grab_banner(sock)
        sock.close()
    except socket.gaierror:
        print(f"[!] Cannot resolve hostname: {host}")
        sys.exit(1)
    except socket.error as e:
        print(f"[!] Socket error on port {port}: {e}")
    return result


def run_scan(host: str, start: int, end: int, timeout: float, output: str | None):
    """Main scanning loop."""
    print_header(host, start, end)

    open_ports = []
    start_time = datetime.now()

    for port in range(start, end + 1):
        result = scan_port(host, port, timeout)
        if result["status"] == "open":
            open_ports.append(result)
            print_result(result)

    duration = datetime.now() - start_time

    print(f"\n[✓] Scan complete in {duration.total_seconds():.2f}s")
    print(f"[✓] Found {len(open_ports)} open port(s) on {host}")

    if output:
        save_report(host, open_ports, output)
        print(f"[✓] Report saved to: {output}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="🔍 Network Port Scanner — Learn network security hands-on"
    )
    parser.add_argument("--host",    required=True,                        help="Target IP address or hostname")
    parser.add_argument("--start",   type=int, default=DEFAULT_START_PORT, help=f"Start port (default: {DEFAULT_START_PORT})")
    parser.add_argument("--end",     type=int, default=DEFAULT_END_PORT,   help=f"End port   (default: {DEFAULT_END_PORT})")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT,  help=f"Timeout in seconds (default: {DEFAULT_TIMEOUT})")
    parser.add_argument("--output",  type=str, default=None,               help="Save results to a text file")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_scan(
        host=args.host,
        start=args.start,
        end=args.end,
        timeout=args.timeout,
        output=args.output
    )
