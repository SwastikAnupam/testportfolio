from scapy.all import ARP, Ether, srp

def scan_devices(ip_range):
    # Create an ARP request packet to send to the network
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)

    # Send and receive ARP requests using srp (send and receive packets)
    result = srp(arp_request, timeout=3, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def main():
    ip_range = "192.168.1.0/24"  # Replace with your network's IP range
    devices = scan_devices(ip_range)

    print("Detected devices:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")

if __name__ == "__main__":
    main()
