# 🔍 Network Port Scanner

A beginner-friendly Python tool for scanning open ports on a target host. Built to help you learn core **network security** concepts hands-on.

> ⚠️ **Ethical Use Only**: Only scan systems you own or have explicit written permission to test.

---

## 📚 What You'll Learn

- How TCP/IP connections work
- What ports are and why they matter
- How attackers use port scanning for reconnaissance
- Basic Python socket programming

---

## 🛠️ Features

- ✅ Scan a single port or a range of ports
- ✅ Detect open/closed ports
- ✅ Grab service banners (e.g., SSH, HTTP)
- ✅ Export results to `.txt` or `.json` reports
- ✅ Colorized terminal output
- ✅ Adjustable timeout for slow networks

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/preethipakala/network-port-scanner.git
cd network-port-scanner
```

### 2. Run the scanner
```bash
# Scan common ports on localhost
python scanner.py --host 127.0.0.1

# Scan a custom port range
python scanner.py --host 192.168.1.1 --start 20 --end 100

# Save results to a file
python scanner.py --host 127.0.0.1 --output results.txt

# Save results as JSON
python scanner.py --host 127.0.0.1 --output results.json --format json

# Set a custom timeout (seconds)
python scanner.py --host 127.0.0.1 --timeout 0.5
```

---

## 📁 Project Structure

```
network-port-scanner/
├── scanner.py          # Main scanner script
├── utils/
│   ├── __init__.py
│   ├── banner.py       # Banner grabbing
│   └── reporter.py     # Output & report generation
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 Common Ports Reference

| Port | Service |
|------|---------|
| 21   | FTP     |
| 22   | SSH     |
| 23   | Telnet  |
| 25   | SMTP    |
| 53   | DNS     |
| 80   | HTTP    |
| 443  | HTTPS   |
| 3306 | MySQL   |
| 8080 | HTTP Alt|

---

## 🔭 Next Steps / Ideas

- [ ] Add UDP scanning support
- [ ] Add multithreading for faster scans
- [x] Add JSON export format
- [ ] Add OS fingerprinting
- [ ] Build a simple web UI

---

## 📜 License

MIT License — free to use, modify, and learn from.
