# Container With Most Water

## Question

You are given an integer array `heights` where `heights[i]` represents the height of the `i`th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

### Example 1

```
Input: height = [1,7,2,5,4,7,3,6]
Output: 36
```

Explanation: The bars at indices 1 and 7 have heights 7 and 6. The container has width `7 - 1 = 6` and height `min(7, 6) = 6`, so it can store `6 * 6 = 36` units of water. This is the maximum possible area.

### Example 2

```
Input: height = [2,2,2]
Output: 4
```

### Constraints

- `2 <= height.length <= 100,000`
- `0 <= height[i] <= 10,000`

## My Solution

```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_ptr, right_ptr = 0, len(heights)-1
        res = 0
        while left_ptr != right_ptr:
            temp = heights[right_ptr]*(right_ptr-left_ptr)
            if(heights[left_ptr] > heights[right_ptr]):
                res = temp if temp >res else res
                right_ptr-=1
                continue
            elif(heights[left_ptr] == heights[right_ptr]):
                res = temp if temp >res else res
                left_ptr+=1
                continue
            elif(heights[left_ptr] < heights[right_ptr]):
                temp = heights[left_ptr]*(right_ptr-left_ptr)
                res = temp if temp >res else res
                left_ptr+=1
                continue

        return res
```
