from scapy.all import sniff, IP, TCP
from collections import defaultdict
import time

# ---------- Settings ----------
PORT_THRESHOLD = 10      # number of ports = "scan"
TIME_WINDOW = 5          # within this many seconds

# Track activity: { ip: {"ports": set(), "time": first_seen} }
activity = defaultdict(lambda: {"ports": set(), "time": time.time()})

def print_banner():
    print("=" * 50)
    print("        🛡️  Port Scan Detector")
    print("=" * 50)
    print(f"Watching for scans... (>{PORT_THRESHOLD} ports in {TIME_WINDOW}s)")
    print("Press Ctrl+C to stop.\n")

def detect_scan(packet):
    """Analyze each packet and detect possible port scans."""
    if packet.haslayer(TCP) and packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport

        record = activity[src_ip]
        now = time.time()

        # Reset record if time window has passed
        if now - record["time"] > TIME_WINDOW:
            record["ports"] = set()
            record["time"] = now

        # Add the targeted port
        record["ports"].add(dst_port)

        # Trigger alert if threshold crossed
        if len(record["ports"]) >= PORT_THRESHOLD:
            print(f"🚨 [ALERT] Possible port scan from {src_ip} "
                  f"→ {len(record['ports'])} ports in {TIME_WINDOW}s")
            # Reset to avoid duplicate alerts
            record["ports"] = set()
            record["time"] = now

def main():
    print_banner()
    # Start sniffing TCP packets
    sniff(filter="tcp", prn=detect_scan, store=0)

if __name__ == "__main__":
    main()
