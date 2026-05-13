import socket

# Common ports and their default services
common_services = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NETBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-ALT"
}

target = input("Enter Target IP: ")

# Ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 8080]

print(f"\nScanning Target: {target}")
print("-" * 50)

for port in ports:

    try:
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Timeout
        s.settimeout(1)

        # Attempt connection
        result = s.connect_ex((target, port))

        if result == 0:

            print(f"[+] Port {port} OPEN")

            # Show common service name
            service = common_services.get(port, "Unknown Service")
            print(f"    Service: {service}")

            # Try banner grabbing
            try:

                # Send basic request for web ports
                if port == 80 or port == 8080:
                    s.send(b"GET / HTTP/1.1\r\nHost: test\r\n\r\n")

                elif port == 443:
                    print("    HTTPS detected (SSL/TLS encrypted)")
                    s.close()
                    continue

                # Receive banner
                banner = s.recv(1024).decode().strip()

                if banner:
                    print(f"    Banner: {banner}")

            except:
                print("    Banner: Not Available")

        s.close()

    except KeyboardInterrupt:
        print("\nExiting...")
        break

    except socket.gaierror:
        print("Hostname could not be resolved.")
        break

    except socket.error:
        print("Could not connect to server.")
        break

print("\nScan Completed.")
