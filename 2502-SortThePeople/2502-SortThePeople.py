# Last updated: 8/2/2025, 12:05:41 AM
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        z=list(zip(heights,names))
        z.sort(reverse=True)
        return [names for heights,names in z]
    