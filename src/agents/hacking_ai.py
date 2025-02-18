# hacking_ai.py

from ai_agent import AIAgent

class HackingAI(AIAgent):
    def __init__(self, name, hacking_power, defense, stealth):
        super().__init__(name, hacking_power, defense)
        self.stealth = stealth

    def hack(self, target_system):
        if self.stealth > target_system.security_level:
            return f"{self.name} successfully hacked the system!"
        else:
            return f"{self.name} failed to hack the system."

    def get_status(self):
        status = super().get_status()
        status["stealth"] = self.stealth
        return status
