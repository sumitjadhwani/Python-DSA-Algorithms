# Search a 2D Matrix

https://neetcode.io/problems/search-2d-matrix

## Question

You are given an `m x n` 2-D integer array `matrix` and an integer `target`.

- Each row in `matrix` is sorted in non-decreasing order.
- The first integer of every row is greater than the last integer of the previous row.

Return `true` if `target` exists within `matrix` or `false` otherwise.

Can you write a solution that runs in `O(log(m * n))` time?

### Example 1

```
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
```

### Example 2

```
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
```

### Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10000 <= matrix[i][j], target <= 10000`

## My Solution

### Solution 1

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l,r = 0, len(matrix)-1
        target_list = []

        while l<=r:
            mid = l + (r-l)//2
            len_mid_mat = len(matrix[mid])
            if target >= matrix[mid][0] and target <= matrix[mid][len_mid_mat-1]:
                if(target == matrix[mid][0]) or (target == matrix[mid][len_mid_mat-1]):
                    return True
                target_list = matrix[mid]
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        if target_list:
            left, right = 0, len(target_list)-1

            while left <= right:
                mid = left + (right - left)//2
                # print(mid)

                if target_list[mid] == target:
                    return True
                elif target_list[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
```

### Solution 2 (Clean Version)

```python
class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		left_index = 0
		rows = len(matrix)
		cols = len(matrix[0])
		total_elements = rows * cols
		right_index = total_elements - 1


		while right_index >= left_index:
			mid_index = (left_index + right_index) // 2
			new_rows = mid_index // cols
			new_cols = mid_index % cols

			if  target == matrix[new_rows][new_cols]:
				return True
			elif target > matrix[new_rows][new_cols]:
				left_index = mid_index + 1
			elif target < matrix[new_rows][new_cols]:
				right_index = mid_index - 1
		return False
```
