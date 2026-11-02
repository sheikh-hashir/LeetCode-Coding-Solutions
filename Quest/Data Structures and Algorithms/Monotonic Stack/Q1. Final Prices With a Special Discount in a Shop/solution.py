class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        length = len(prices)

        for idx in range(length):
            for jdx in range(idx + 1, length):
                if prices[idx] >= prices[jdx]:
                    prices[idx] -= prices[jdx]
                    break
        return prices
