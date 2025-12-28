import socket
import sys

def main():
    target = get_ip()
    scanner(target)

def get_ip():
    if len(sys.argv) != 2:
        print("Usage: python3 port_scanner.py <target_ip>")
        sys.exit(1)

    ip_add = sys.argv[1]
    ip_parts = ip_add.split(".")

    if len(ip_parts) != 4:
        print("Invalid IP address format")
        sys.exit(1)

    for part in ip_parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            print("Invalid IP address")
            sys.exit(1)

    return ip_add

def scanner(target_ip):
    print(f"\nScanning target: {target_ip}")
    print("-" * 40)

    for port in range(1, 1001):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")

        s.close()

if __name__ == "__main__":
    main()
