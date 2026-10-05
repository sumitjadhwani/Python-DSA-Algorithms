# Longest Repeating Character Replacement

https://neetcode.io/problems/longest-repeating-substring-with-replacement/question

## Question

You are given a string `s` consisting of only uppercase english characters and an integer `k`. You can choose up to `k` characters of the string and replace them with any other uppercase English character.

After performing at most `k` replacements, return the length of the longest substring which contains only one distinct character.

### Example 1

```
Input: s = "XYYX", k = 2

Output: 4
```

Explanation: Either replace the `'X'`s with `'Y'`s, or replace the `'Y'`s with `'X'`s.

### Example 2

```
Input: s = "AAABABB", k = 1

Output: 5
```

### Constraints

- `1 <= s.length <= 100,000`
- `0 <= k <= s.length`
- `s` consists of only uppercase english characters.

## My Solution

### Brute Force

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count = {}
            max_f = 0
            for j in range(i,len(s)):
                count[s[j]]=count.get(s[j], 0) + 1
                max_f = max(max_f, count[s[j]])
                if(j-i+1)-max_f<=k:
                    res = max(res, j-i+1)
                else:
                    break
        return res
```

### Sliding Window

```python
def max_frequency(count):
    max_f = 0
    for key,values in count.items():
        max_f = max(max_f,values)
    return max_f
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = {}
        # max_f = 0

        for r in range(len(s)):
            max_f = max_frequency(count)
            count[s[r]]=count.get(s[r], 0) + 1
            max_f = max(max_f, count[s[r]])
            while (r-l+1)-max_f>k:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res
```

## Notes

```python
# Core logic of the sliding window (in simple words):
#
# We keep a window [l, r]. Inside the window we count how many times each
# character appears. The character that appears the MOST (max_f) is the one we
# will NOT replace - we turn every other character into it.
#
# So the number of characters we must replace = (window size) - (max_f).
#   window size        = r - l + 1
#   chars to replace   = (r - l + 1) - max_f
#
# The window is valid when chars to replace <= k, which means:
#   (r - l + 1) - max_f <= k
#   => r - l + 1 <= max_f + k
#
# In plain words: the best window we can ever form is at most (max_f + k).
# max_f counts how many of the most common char we already have, and k is how
# many other chars we are allowed to change. So the window size is bounded by
# max_f + k.
#
# Algorithm steps:
#   1. Grow the window to the right (r++), updating counts.
#   2. Track the largest frequency seen so far (max_f).
#   3. If the window becomes invalid ((r-l+1) - max_f > k), shrink from the
#      left (l++) until it is valid again.
#   4. Answer is the largest valid window we ever saw.
#
# Note: the "more optimal" version does NOT recompute max_f on every run.
# max_f is a maximum over the whole string, so it never needs to go DOWN while
# the window slides. We just keep the best max_f seen so far and, instead of
# shrinking the window, only move l forward when the window is invalid. This
# keeps the window size from ever decreasing, so the final window length is the
# answer. This avoids scanning the count map (26 chars) on every step, giving a
# clean O(n) single pass.
```
