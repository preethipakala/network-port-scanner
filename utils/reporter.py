#!/usr/bin/env python3
"""
reporter.py — Terminal output and file report generation.
"""

import json
from datetime import datetime

# ANSI color codes for colorized terminal output
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

# Map of common port numbers to their service names
SERVICE_NAMES = {
    21: "FTP",    22: "SSH",    23: "Telnet", 25: "SMTP",
    53: "DNS",    80: "HTTP",   110: "POP3",  143: "IMAP",
    443: "HTTPS", 445: "SMB",   3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 6379: "Redis", 8080: "HTTP-Alt",
    27017: "MongoDB"
}


def get_service(port: int) -> str:
    """Return a human-readable service name for a well-known port."""
    return SERVICE_NAMES.get(port, "unknown")


def print_header(host: str, start: int, end: int):
    """Print a formatted scan header."""
    print(f"\n{BOLD}{CYAN}{'─' * 50}")
    print(f"  🔍 Network Port Scanner")
    print(f"{'─' * 50}{RESET}")
    print(f"  Target  : {YELLOW}{host}{RESET}")
    print(f"  Ports   : {start} → {end}")
    print(f"  Started : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{CYAN}{'─' * 50}{RESET}\n")


def print_result(result: dict):
    """Print a single open-port result to the terminal."""
    port    = result["port"]
    service = get_service(port)
    banner  = result.get("banner", "")
    banner_str = f"  ↳ {banner}" if banner else ""
    print(f"  {GREEN}[OPEN]{RESET}  Port {BOLD}{port:5d}{RESET}  ({YELLOW}{service}{RESET}){banner_str}")


def save_report(host: str, open_ports: list, filename: str, fmt: str = "txt"):
    """Write a report of open ports to a file in the specified format."""
    # Auto-append extension if filename has none
    if "." not in filename.split("/")[-1].split("\\")[-1]:
        filename += ".json" if fmt == "json" else ".txt"

    if fmt == "json":
        report = {
            "target": host,
            "scanned_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "open_ports": [
                {
                    "port": r["port"],
                    "service": get_service(r["port"]),
                    "banner": r.get("banner", "")
                }
                for r in open_ports
            ]
        }
        with open(filename, "w") as f:
            json.dump(report, f, indent=2)
    else:
        with open(filename, "w") as f:
            f.write("Network Port Scan Report\n")
            f.write("========================\n")
            f.write(f"Target  : {host}\n")
            f.write(f"Date    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Open Ports: {len(open_ports)}\n\n")
            for r in open_ports:
                service = get_service(r["port"])
                banner  = r.get("banner", "")
                line = f"  Port {r['port']:5d}  [{service}]"
                if banner:
                    line += f"  — {banner}"
                f.write(line + "\n")
