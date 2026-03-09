from sensor import start_sniffing, extract_features
from brain import SentinelBrain
from actuator import execute_defense

# Initialize the AI Brain
brain = SentinelBrain()

def agent_loop(packet):
    # 1. Observe (Sensor)
    data = extract_features(packet)
    
    if data:
        # 2. Think (Brain)
        risk_score, threat_type = brain.analyze(data)
        
        # 3. Act (Actuator)
        if risk_score > 0.4:
            execute_defense(data['src_ip'], threat_type, risk_score)

if __name__ == "__main__":
    # Start the autonomous loop
    start_sniffing(agent_loop)
