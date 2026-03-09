import scapy.all as scapy
import requests

def get_location(ip):
    """Fetches location data for an IP address."""
    if ip.startswith("192.168.") or ip.startswith("10.") or ip == "127.0.0.1":
        return "Local Network"
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=2).json()
        if res.get('status') == 'success':
            return f"{res.get('city')}, {res.get('country')}"
    except Exception:
        pass
    return "Unknown Location"

def extract_features(packet):
    """Extracts relevant data from the raw network packet."""
    features = {}
    if packet.haslayer(scapy.IP):
        features['src_ip'] = packet[scapy.IP].src
        features['dst_ip'] = packet[scapy.IP].dst
        features['size'] = len(packet)
        features['location'] = get_location(packet[scapy.IP].src)
        
        if packet.haslayer(scapy.Raw):
            try:
                features['payload'] = packet[scapy.Raw].load.decode('utf-8', errors='ignore')
            except:
                features['payload'] = ""
        else:
            features['payload'] = ""
    return features

def start_sniffing(callback_function):
    """Starts the continuous sniffing loop."""
    print("[*] Sensor Initialized: Listening to network interfaces...")
    scapy.sniff(store=False, prn=callback_function)
