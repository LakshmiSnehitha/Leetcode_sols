# Last updated: 9/3/2025, 11:23:58 AM
from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag_sq = -1  # store diagonal squared to avoid sqrt
        best_area = 0
        for w, h in dimensions:
            diag_sq = w*w + h*h
            area = w*h
            if diag_sq > max_diag_sq or (diag_sq == max_diag_sq and area > best_area):
                max_diag_sq = diag_sq
                best_area = area
        return best_area       