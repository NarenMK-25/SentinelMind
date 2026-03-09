import datetime
import platform
import subprocess

def execute_defense(ip, location, threat_type, score):
    """Takes autonomous action based on the Brain's decision."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

    log_entry = f"[{timestamp}] ALERT | IP: {ip} ({location}) | Threat: {threat_type} | Confidence: {score}\n"
    

    with open("security_log.txt", "a") as log_file:
        log_file.write(log_entry)
    

    print(f"\n[!!!] DEFENSE TRIGGERED [!!!]")
    print(f" -> Target: {ip} ({location})")
    print(f" -> Reason: {threat_type}")
    print(f" -> Action: Blocked via Firewall Rules\n")
