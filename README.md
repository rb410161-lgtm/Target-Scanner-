# Python Port Scanner

A beginner-friendly TCP Port Scanner built using Python and Socket Programming.

This project scans common ports on a target machine, identifies open ports, detects common services, and performs basic banner grabbing for educational and cybersecurity learning purposes.

---

# Features

- TCP Port Scanning
- Service Detection
- Banner Grabbing
- Timeout Handling
- Error Handling
- Beginner-Friendly Code Structure

---

# Technologies Used

- Python 3
- Socket Programming

---

# Ports Scanned

| Port | Service |
|------|----------|
| 21 | FTP |
| 22 | SSH |
| 23 | TELNET |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 139 | NETBIOS |
| 143 | IMAP |
| 443 | HTTPS |
| 445 | SMB |
| 3306 | MySQL |
| 3389 | RDP |
| 8080 | HTTP-ALT |

---

# How It Works

The scanner:

1. Takes a target IP address from the user
2. Loops through predefined ports
3. Attempts TCP connection using Python sockets
4. Checks whether the port is open or closed
5. Identifies common services running on open ports
6. Attempts basic banner grabbing for service information

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-port-scanner.git
```

Go to the project folder:

```bash
cd python-port-scanner
```

---

# Usage

Run the scanner:

```bash
python3 scanner.py
```

Enter target IP:

```text
Enter Target IP: 192.168.0.105
```

---

# Example Output

```text
Scanning Target: 192.168.0.105
--------------------------------------------------

[+] Port 22 OPEN
    Service: SSH
    Banner: SSH-2.0-OpenSSH_8.2p1 Ubuntu

[+] Port 80 OPEN
    Service: HTTP
    Banner: Apache/2.4.41 (Ubuntu)

Scan Completed.
```

---

# Learning Objectives

This project helps beginners understand:

- Python basics
- Socket programming
- TCP networking
- Port scanning concepts
- Banner grabbing
- Cybersecurity automation
- Service enumeration
- Error handling

---

# Disclaimer

This tool is created for:

- Educational purposes
- Personal labs
- Authorized security testing only

Do NOT scan systems without permission.

---

# Future Improvements

- Multi-threaded scanning
- Full port range scanning
- OS detection
- UDP scanning
- Service version detection
- GUI interface
- Export scan reports

---

# Author

Created as a cybersecurity learning project using Python.
