# 🛡️ SentinelMind: Autonomous AI Security Agent

SentinelMind is an advanced, modular AI agent designed to monitor network traffic, reason about potential threats using a heuristic-AI brain, and execute autonomous defense actions in real-time.



---

## 🚀 Overview
Unlike traditional firewalls that simply block predefined ports, **SentinelMind** operates as an intelligent agent. It observes the environment (Network Packets), processes information through a reasoning engine (The Brain), and changes its environment (Firewall Actuator) without human intervention.

### Core Features:
* **Autonomous Reasoning:** Uses keyword heuristics and AI scoring to identify malicious intent.
* **Geographic Intelligence:** Automatically identifies the location (City/Country) of suspicious source IPs.
* **Proactive Defense:** Can execute OS-level commands to block malicious actors instantly.
* **Web Dashboard:** A Streamlit-based interface for real-time threat visualization.

---

## 👥 Team & Contribution Matrix
Our instructor's requirement for equal contribution was met by dividing the agent into four distinct functional modules:

| Member | Role | Module | Responsibility |
| :--- | :--- | :--- | :--- |
| **Naren M K** | Team Lead / DevOps | `main.py` / `dashboard.py` | Integration, Streamlit UI, & Git management. |
| **Nandha Kishore M** | AI Logic Lead | `brain.py` | Heuristic threat engine & risk scoring logic. |
| **Rishi J** | Network Specialist | `sensor.py` | Packet sniffing using Scapy & feature extraction. |
| **Sharu Khan F K** | Security Actuator | `actuator.py` | Logging system & firewall response execution. |

---

## 🛠️ Project Architecture
The agent follows the classic **MAPE-K** (Monitor, Analyze, Plan, Execute) loop:
1. **Monitor (`sensor.py`):** Captures raw packets and extracts IP, Size, and Payload.
2. **Analyze (`brain.py`):** Scores the risk based on payload content and anomalies.
3. **Execute (`actuator.py`):** Logs the alert and triggers system-level defense.
4. **Visualize (`dashboard.py`):** Provides a human-readable interface for the logs.

---

## 🏁 Getting Started

### Prerequisites
* Python 3.x
* Npcap (Windows) or Libpcap (Linux)
* Administrator/Root privileges (Required for packet sniffing)



### Installation
```bash
pip install -r requirements.txt


1. Running the Agent
Start the Engine:

python main.py

2. Start the Dashboard:

python -m streamlit run dashboard.py


📊 Execution Example
When a threat is detected (e.g., a packet containing cmd or admin), the system generates the following output:

Plaintext
[!!!] DEFENSE TRIGGERED [!!!]
 -> Target: 10.158.101.1 (Local Network)
 -> Reason: Malicious Payload Keyword: 'cmd'
 -> Action: Blocked via Firewall Rules.

---

### **How to add this to your GitHub:**
1. Go to your repository `NarenMK-25/SentinelMind`.
2. Click on the **README** file (or the pencil icon to edit).
3. Delete anything there and paste the text above.
4. Click **"Commit changes..."** and make sure your commit message says: `docs: update R
