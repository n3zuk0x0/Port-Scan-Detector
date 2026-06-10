#  Port Scan Detector

A lightweight **port scan detection tool** built in Python using **Scapy**. It monitors live network traffic and raises an alert when a single IP attempts to connect to too many ports in a short time — a common sign of port scanning.

>  **For educational and authorized use only.** Run only on systems/networks you own or have permission to monitor.

---

##  Features

-  **Live packet sniffing** using Scapy
-  **Real-time alerts** when a port scan is detected
-  **Configurable thresholds** (ports count + time window)
-  **Tracks activity per source IP**
-  **Lightweight** — minimal dependencies

---

##  Tech Stack

- **Python 3**
- **Scapy** (packet capture & analysis)

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/nezuk0x0/Port-Scan-Detector.git
cd Port-Scan-Detector
```

Install dependencies:



>  **Scapy needs admin/root privileges to sniff packets.**
> - **Linux/Mac:** run with `sudo`
> - **Windows:** run as Administrator + install [Npcap](https://npcap.com/)

---

##  Usage

Run the detector:

```bash
sudo python detector.py
```

(On Windows, run your terminal as Administrator, then `python detector.py`)

Leave it running — it will alert you when a scan is detected.

---

##  How to Test It

Use it together with a port scanner (like my [Python Port Scanner](https://github.com/n3zuk0x0/Python-Port-Scanner)):

**Terminal 1 — start the detector:**
```bash
sudo python detector.py
```

**Terminal 2 — run a scan against your machine:**
```bash
python port_scanner.py
# Target: 127.0.0.1, Ports: 1-100
```

**Result in Terminal 1:**
```
 [ALERT] Possible port scan from 127.0.0.1 → 100 ports in 5s
```

---

##  Configuration

Edit these values at the top of `detector.py`:

```python
PORT_THRESHOLD = 10   # ports needed to trigger an alert
TIME_WINDOW = 5       # time window in seconds
```

---

##  What I Learned

- How port scans look at the network level
- Packet sniffing and analysis with Scapy
- Detecting attack patterns based on behavior
- Blue team (defensive security) fundamentals

---

##  Legal Disclaimer

This tool is intended for **educational purposes** and **authorized monitoring only**. Monitoring networks without permission may be illegal. The author is not responsible for any misuse.

---

##  Future Improvements

- [ ] Log alerts to a file with timestamps
- [ ] Whitelist trusted IPs
- [ ] Detect different scan types (SYN, FIN, etc.)
- [ ] Email/Telegram notifications on alert

---

##  Author

**Your Name**
- GitHub: [@n3zuk0x0](https://github.com/n3zuk0x0)
