#!/usr/bin/env python3
"""
banner.py — Attempt to grab a service banner from an open socket.

A "banner" is the greeting message a service sends when you connect.
For example, SSH sends: 'SSH-2.0-OpenSSH_8.9'
This tells us the service name and version — useful info in security audits.
"""

import socket

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
    except Exception:
        return ""
