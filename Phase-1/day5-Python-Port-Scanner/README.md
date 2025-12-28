# Day 5 – Python Port Scanner 

## Objective
To build a basic port scanning tool using Python and understand how attackers and defenders identify open network services.

---

## Tool Description
This project is a **custom Python-based TCP port scanner** that scans ports **1–1000** on a given target IP address and reports open ports.

The script uses Python’s `socket` module to attempt connections and identify open ports.

---

## How to Run
```bash
python3 port_scanner.py <target_ip>
```

---

## ⚙️ How It Works
1. Takes the target IP address as a command-line argument
2. Validates the IP format (IPv4)
3. Iterates through ports 1–1000
4. Attempts a TCP connection using `socket.connect_ex()`
5. Displays only open ports

---

## 🧠 Security Relevance

### 🔴 Attacker Perspective
- Identify running services
- Discover potential vulnerabilities
- Plan exploitation strategies

### 🔵 Defender Perspective
- Audit exposed services
- Reduce attack surface
- Detect unnecessary open ports

> Port scanning is one of the first steps in real-world cyber attacks and security assessments.

## 🧪 Concepts Learned
- Python basics for security scripting
- Socket programming
- Network ports and services
- Input validation
- Writing CLI-based tools
- Understanding attacker methodology

---

## Future Improvements
- Add multi-threading for faster scans
- Implement banner grabbing
- Allow custom port ranges
- Save scan results to a file

---

## ⚠️ Disclaimer
This tool is created for educational purposes only.
Do not scan systems you do not own or have permission to test.
