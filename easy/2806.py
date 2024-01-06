"""2806. Account Balance After Rounded Purchase"""


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 == 5:
            actual_amount = purchaseAmount + 5
        elif purchaseAmount % 10 < 5:
            actual_amount = purchaseAmount // 10 * 10
        else:
            actual_amount = (purchaseAmount // 10 + 1) * 10

        return 100 - actual_amount
