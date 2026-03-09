import re
class SentinelBrain:
    def __init__(self):
        self.threat_keywords = ["admin", "drop table", "exec", "password", "login_retry"]

    def analyze(self, data):
        """The 'Thought' process of the agent."""
        if not data:
            return 0.0, "Normal"

        score = 0.0
        reason = "Normal Traffic"

        # Logic 1: Payload analysis (Heuristic AI)
        for word in self.threat_keywords:
            if word in data.get('payload', '').lower():
                score += 0.7
                reason = f"Suspicious Keyword Detected: {word}"

        # Logic 2: Size-based anomaly
        if data.get('size', 0) > 1500:
            score += 0.3
            reason = "Unusually large packet size (Potential Buffer Overflow)"

        return min(score, 1.0), reason
