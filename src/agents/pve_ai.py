# pve_ai.py

from hacking_ai import HackingAI

class PvEAi(HackingAI):
    def __init__(self, name, hacking_power, defense, stealth, mission_type):
        super().__init__(name, hacking_power, defense, stealth)
        self.mission_type = mission_type

    def complete_mission(self, target_system):
        if self.mission_type == "stealth":
            return self.hack(target_system)
        else:
            return f"{self.name} battles against {target_system.name} in a direct confrontation."

    def get_status(self):
        status = super().get_status()
        status["mission_type"] = self.mission_type
        return status
