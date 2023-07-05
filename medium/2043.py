"""2043. Simple Bank System"""

from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self._accounts = balance
        self._count = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self._count or account2 > self._count:
            return False

        if self._accounts[account1 - 1] < money:
            return False

        self._accounts[account1 - 1] -= money
        self._accounts[account2 - 1] += money

        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self._count:
            return False

        self._accounts[account - 1] += money

        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self._count or self._accounts[account - 1] < money:
            return False

        self._accounts[account - 1] -= money

        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
