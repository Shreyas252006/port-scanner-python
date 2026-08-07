# 🔎 Python TCP Port Scanner

> A beginner-friendly TCP port scanner built with Python sockets on Kali Linux to explore networking and cybersecurity fundamentals.

**Python 3** · **TCP** · **Sockets** · **Kali Linux** · **Git/GitHub**



---

## 🚀 Features

- 🔌 TCP Connect Scanning
- ⏱️ Connection Timeout Handling
- 🔢 Port Range Scanning
- 🟢 Open / 🔴 Closed Detection
- 💻 Lightweight CLI Output

---

## ⚙️ How It Works

```text
Target → Port → TCP Connection → Result
                         ↓
                  OPEN / CLOSED
```

For each port, the scanner:

1. Creates a TCP socket
2. Attempts a connection
3. Reports the result
4. Closes the socket
5. Moves to the next port

---

## 🧪 Quick Start

```bash
git clone https://github.com/Shreyas252006/port-scanner-python.git
cd port-scanner-python

python3 -m venv venv
source venv/bin/activate

python scanner_basic.py
```

For safe local testing:

```text
127.0.0.1
```

Create a test service:

```bash
python3 -m http.server 8000
```

Expected:

```text
[CLOSED] Port 7999
[OPEN] Port 8000
[CLOSED] Port 8001
```

---

## 🧠 What I Learned

- TCP vs UDP
- IPv4 & ports
- Python socket programming
- Connection timeouts
- Basic network reconnaissance
- Linux networking
- Git/GitHub workflow

---

## 🛠️ Tech Stack

| Tool       | Purpose                 |
| ---------- | ----------------------- |
| Python 3   | Scanner                 |
| `socket`   | TCP connections         |
| Kali Linux | Development             |
| Git        | Version control         |
| GitHub     | Documentation & hosting |

---

## 🗺️ Roadmap

- [x] Basic TCP scanner
- [x] Timeout handling
- [x] Git/GitHub documentation
- [ ] Multithreading
- [ ] Better error classification
- [ ] Service detection
- [ ] `argparse` CLI
- [ ] Desktop GUI
- [ ] Web dashboard

---

## 🔐 Responsible Use

Built for **education and authorized security testing only**.

Only scan systems you own or have explicit permission to test.

---

## 👨‍💻 Author

**Shreyas Chavhan**

Learning → Building → Testing → Documenting → Improving

🔗 GitHub:\
[https://github.com/Shreyas252006](https://github.com/Shreyas252006)

Python TCP Port Scanner: A beginner-friendly cybersecurity project built on Kali Linux using Python sockets. The tool performs TCP connect scanning to identify open ports on a target host.

Features - TCP port scanning using Python's built-in "socket" module - Configurable connection timeout - Scans a range of ports - Clear terminal output for open and closed ports - Works on Linux (tested on Kali Linux)

Technologies Used: - Python 3 - socket - Git & GitHub - Kali Linux

Project Structure:

port-scanner/

├── Screenshots/

├── scanner\_basic.py

├── README.md

└── .gitignore

How It Works:-

For each port, the scanner:

Creates a TCP socket.\
Attempts a connection to the target IP and port.\
Reports the port as OPEN if the connection succeeds.\
Reports the port as CLOSED if the connection fails.\
Closes the socket before moving to the next port.\
This approach is called a TCP connect scan.\
Setup:-

python3 -m venv venv\
source venv/bin/activate\
Run the Scanner- python scanner\_basic.py

Example target : 127.0.0.1

Create a Test Service:- In another terminal: -> python3 -m http.server 8000 -> The scanner should detect port 8000 as OPEN.

Example Output: Scanning 127.0.0.1... [CLOSED] Port 7999 [OPEN] Port 8000 [CLOSED] Port 8001

What I Learned - TCP vs UDP fundamentals - How sockets work in Python - Connection timeouts - Basic network reconnaissance concepts - Git version control workflow on Linux

Security & Ethics: This project is for educational and authorized testing only. Scan only systems you own or have explicit permission to test.

Future Improvements: - Multithreaded scanning - Asynchronous scanning with "asyncio" - Service banner detection - Port range arguments - CLI interface with "argparse" - Desktop GUI - Web dashboard

Author Shreyas Chavhan GitHub: [https://github.com/Shreyas252006](https://github.com/Shreyas252006)
