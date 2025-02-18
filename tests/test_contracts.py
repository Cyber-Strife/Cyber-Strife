# test_contracts.py

import unittest
from web3 import Web3
from src.contracts.Token import Token

class TestTokenContract(unittest.TestCase):

    def setUp(self):
        self.web3 = Web3(Web3.EthereumTesterProvider())
        self.account = self.web3.eth.accounts[0]
        self.token = Token.deploy(1000000, {'from': self.account})

    def test_initial_supply(self):
        self.assertEqual(self.token.totalSupply(), 1000000)

    def test_transfer(self):
        initial_balance = self.token.balanceOf(self.account)
        self.token.transfer(self.web3.eth.accounts[1], 100, {'from': self.account})
        new_balance = self.token.balanceOf(self.account)
        self.assertEqual(new_balance, initial_balance - 100)

if __name__ == '__main__':
    unittest.main()
