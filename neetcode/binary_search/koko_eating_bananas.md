# Koko Eating Bananas

https://neetcode.io/problems/eating-bananas/question

## Question

You are given an integer array `piles` where `piles[i]` is the number of bananas in the `i`th pile. You are also given an integer `h`, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of `k`. Each hour, you may choose a pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer `k` such that you can eat all the bananas within `h` hours.

### Example 1

```
Input: piles = [1,4,3,2], h = 9

Output: 2
```

Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds `h=9`), thus the minimum eating rate is 2.

### Example 2

```
Input: piles = [25,10,23,4], h = 4

Output: 25
```

### Constraints

- `1 <= piles.length <= 10,000`
- `piles.length <= h <= 1,000,000,000`
- `1 <= piles[i] <= 1,000,000,000`

## My Solution

```python
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if(len(piles)) == h:
            return max(piles)

        l = 1
        r = max(piles)
        res = r

        while l<=r:
            mid = (l+r)//2
            print("mid in while: ",mid)
            time_to_eat=0

            for i in piles:
                time_to_eat+=ceil(i/mid)

            if time_to_eat <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
```
