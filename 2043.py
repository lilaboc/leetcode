# https://leetcode.com/problems/simple-bank-system/

from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance
        
    def _valid_account(self, account):
        if account > len(self.accounts):
            return False
        return True

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._valid_account(account1) or not self._valid_account(account2):
            return False
        if self.accounts[account1 - 1] < money:
            return False
        self.accounts[account1 - 1] -= money
        self.accounts[account2 - 1] += money
        return True
        

    def deposit(self, account: int, money: int) -> bool:
        if not self._valid_account(account):
            return False
        self.accounts[account - 1] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid_account(account):
            return False
        if self.accounts[account - 1] < money:
            return False
        self.accounts[account - 1] -= money
        return True
        

bank = Bank([10, 100, 20, 50, 30])
print(bank.withdraw(3, 10))
print(bank.accounts)
print(bank.transfer(5, 1, 20))
print(bank.accounts)
print(bank.deposit(5, 20))
print(bank.accounts)
print(bank.transfer(3, 4, 15))
print(bank.accounts)
print(bank.withdraw(10, 50))
print(bank.accounts)

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)