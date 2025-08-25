# Last updated: 8/25/2025, 7:36:23 PM
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        ans = []

        for d in range(m + n - 2 + 1):
            # collect indices on diagonal d where r + c = d
            tmp = []
            # r ranges within [max(0, d-(n-1)), min(m-1, d)]
            r_start = max(0, d - (n - 1))
            r_end = min(m - 1, d)
            for r in range(r_start, r_end + 1):
                c = d - r
                tmp.append(mat[r][c])
            # even diagonals go upwards (reverse)
            if d % 2 == 0:
                tmp.reverse()
            ans.extend(tmp)

        return ans
