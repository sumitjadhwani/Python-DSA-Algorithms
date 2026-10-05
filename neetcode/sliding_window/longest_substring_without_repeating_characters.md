# Longest Substring Without Repeating Characters

## Question

Given a string `s`, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

### Example 1

```
Input: s = "zxyzxyz"

Output: 3
```

Explanation: The string `"xyz"` is the longest without duplicate characters.

### Example 2

```
Input: s = "xxxx"

Output: 1
```

### Constraints

- `0 <= s.length <= 50,000`
- `s` may consist of printable ASCII characters.

## My Solution

### Solution 1

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
```

### Solution 2

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_char = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in unique_char:
                unique_char.remove(s[l])
                l=l+1
            unique_char.add(s[r])

            res = max(res, r - l + 1)
        return res
```
