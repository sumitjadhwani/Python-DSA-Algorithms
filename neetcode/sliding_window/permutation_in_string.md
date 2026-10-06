# Permutation in String

https://neetcode.io/problems/permutation-string/question

## Question

You are given two strings `s1` and `s2`.

Return `true` if `s2` contains a permutation of `s1`, or `false` otherwise. That means if a permutation of `s1` exists as a substring of `s2`, then return `true`.

Both strings only contain lowercase letters.

### Example 1

```
Input: s1 = "abc", s2 = "lecabee"

Output: true
```

Explanation: The substring `"cab"` is a permutation of `"abc"` and is present in `"lecabee"`.

### Example 2

```
Input: s1 = "abc", s2 = "lecaabee"

Output: false
```

### Constraints

- `1 <= s1.length, s2.length <= 10000`

## My Solution

### Optimized (Sliding Window)

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        if len(s1) > len(s2):
            return False

        count_s1 = [0]*26
        count_window = [0]*26
        l = 0
        matches=0

        for r in range(0 , len(s1)):
            count_s1[ord(s1[r]) - ord('a')] = count_s1[ord(s1[r]) - ord('a')]+1
            count_window[ord(s2[r]) - ord('a')] = count_window[(ord(s2[r]) - ord('a'))]+1

        for r in range(0,26):
            if count_s1[r] == count_window[r]:
                matches+=1

        if matches == 26:
            return True
        print(matches)
        for r in range(len(s1),len(s2)):
          #add right element
            index_r=ord(s2[r]) - ord('a')
            count_window[index_r]+=1
            if count_window[index_r] == count_s1[index_r]:
                matches+=1
            elif count_window[index_r] == count_s1[index_r]+1:
                matches-=1

            #move left pointer
            index_l=ord(s2[l]) - ord('a')
            count_window[index_l]-=1
            if count_window[index_l] == count_s1[index_l]:
                matches+=1
            elif count_window[index_l] == count_s1[index_l]-1:
                matches-=1

            l+=1

            if matches == 26:
                return True
        print(matches)
        return False
```

### Brute Force

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        for c in s1:
            count_s1[c] = count_s1.get(c, 0)+1
        print(count_s1)

        len_s1 = len(s1)

        for l in range(0,len(s2)-len_s1+1):
            count_window = {}
            for r in range(l,l+len_s1):
                count_window[s2[r]] = count_window.get(s2[r],0)+1
            if count_s1 == count_window:
                return True
            continue
        return False
```
