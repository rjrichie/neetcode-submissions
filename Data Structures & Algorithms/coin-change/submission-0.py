class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        tar = [amount + 1] * (amount + 1)
        tar[0] = 0

        for i in range(1, len(tar)):
            for coin in coins:
                if i - coin >= 0:
                    tar[i] = min(tar[i], 1 + tar[i - coin])

        if tar[amount] == amount + 1:
            return -1

        return tar[amount]