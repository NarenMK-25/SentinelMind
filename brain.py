class SentinelBrain:
    def __init__(self):
        
        self.threat_keywords = ["admin", "drop table", "exec", "password", "login_retry", "cmd"]

    def analyze(self, data):
        """The AI reasoning logic to determine threat levels."""
        if not data:
            return 0.0, "None"

        payload = data.get('payload', '').lower()
        score = 0.0
        reason = "Normal Traffic"

        
        for word in self.threat_keywords:
            if word in payload:
                score += 0.8
                reason = f"Malicious Payload Keyword: '{word}'"
                break 

        
        if data.get('size', 0) > 2000:
            score += 0.3
            if score < 0.8:
                reason = "Anomalous Packet Size"

    
        return min(score, 1.0), reason
