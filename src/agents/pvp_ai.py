# pvp_ai.py

from hacking_ai import HackingAI

class PvPAI(HackingAI):
    def __init__(self, name, hacking_power, defense, stealth, strategy):
        super().__init__(name, hacking_power, defense, stealth)
        self.strategy = strategy

    def execute_strategy(self, opponent):
        if self.strategy == "aggressive":
            return self.battle(opponent)
        elif self.strategy == "defensive":
            return f"{self.name} defends against {opponent.name}'s attack!"
        else:
            return f"{self.name} tries to outsmart {opponent.name} with clever tactics."

    def get_status(self):
        status = super().get_status()
        status["strategy"] = self.strategy
        return status
