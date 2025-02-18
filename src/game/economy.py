# economy.py

class Economy:
    def __init__(self):
        self.cyber_tokens = 1000000

    def earn_tokens(self, amount):
        self.cyber_tokens += amount

    def spend_tokens(self, amount):
        if self.cyber_tokens >= amount:
            self.cyber_tokens -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.cyber_tokens
