
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        count = [0] * (n + 1)
        min_price = float('inf')

        for factor, price in items:
            count[factor] += 1
            min_price = min(min_price, price)

        # Calculate free-copy opportunities
        gain = [0] * (n + 1)

        for i in range(1, n + 1):
            total = 0

            for j in range(i, n + 1, i):
                total += count[j]

            gain[i] = total - 1

        # Keep useful deals only
        deals = []

        for factor, price in items:
            if price < 2 * min_price and gain[factor] > 0:
                deals.append((price, gain[factor]))

        deals.sort()

        result = 0

        # Buy the cheapest value-2 copies first
        for price, available in deals:
            buy = min(available, budget // price)

            result += buy * 2
            budget -= buy * price

        # Use remaining budget for cheapest value-1 copies
        result += budget // min_price

        return result
