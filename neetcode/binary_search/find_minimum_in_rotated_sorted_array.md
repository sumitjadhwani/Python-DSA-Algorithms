# Find Minimum in Rotated Sorted Array

https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question

## Question

You are given an array of length `n` which was originally sorted in ascending order. It has now been rotated between `1` and `n` times. For example, the array `nums = [1,2,3,4,5,6]` might become:

- `[3,4,5,6,1,2]` if it was rotated 4 times.
- `[1,2,3,4,5,6]` if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array `nums` are unique, return the minimum element of this array.

A solution that runs in `O(n)` time is trivial, can you write an algorithm that runs in `O(log n)` time?

## My Solution

### Solution 1

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # Binary search loop
        while l < r:
            mid = (l + r) // 2

            # If mid element is greater than the rightmost element,
            # the minimum element must be on the right side.
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the minimum is either at mid or to its left.
            else:
                r = mid

        # When l == r, they point to the minimum element.
        return nums[l]
```

### Solution 2

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        if (nums[l] < nums[r]) or r == 0:
            return nums[0]
        while l<=r:
            mid = (l+r)//2

            if (nums[l] < nums[mid]):
                l = mid
                continue
            elif (nums[mid] < nums[r]):
                r = mid
                continue
            elif (nums[l]==nums[mid]) and (nums[l] > nums[r]):
                return nums[r]
```

### Solution 3 (Handle Duplicate Elements, Worst Case O(n), Average O(log n))

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # Case 1: The minimum is strictly to the right side
            if nums[mid] > nums[r]:
                l = mid + 1

            # Case 2: The minimum is at mid or to the left side
            elif nums[mid] < nums[r]:
                r = mid

            # Case 3: nums[mid] == nums[r]
            # We can't decide the direction, so safely shrink the window from the right.
            else:
                r -= 1

        return nums[l]
```
