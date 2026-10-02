# Best Time to Buy and Sell Stock

https://neetcode.io/problems/buy-and-sell-crypto/history?list=neetcode150&submissionIndex=1

## Question

You are given an integer array `prices` where `prices[i]` is the price of NeetCoin on the `i`th day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be `0`.

### Example 1

```
Input: prices = [10,1,5,6,7,1]

Output: 6
```

Explanation: Buy `prices[1]` and sell `prices[4]`, profit `= 7 - 1 = 6`.

### Example 2

```
Input: prices = [10,8,7,5,2]

Output: 0
```

Explanation: No profitable transactions can be made, thus the max profit is `0`.

### Constraints

- `1 <= prices.length <= 100`
- `0 <= prices[i] <= 100`

## My Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(0, len(prices)):
            for j in range(0, len(prices)):
                if(i>j):
                    if (prices[i] - prices[j]) > maxProfit:
                        maxProfit = prices[i] - prices[j]

                else:
                    continue
        return maxProfit
```
