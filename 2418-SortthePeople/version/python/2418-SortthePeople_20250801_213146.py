# Last updated: 8/1/2025, 9:31:46 PM
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        z=list(zip(heights,names))
        z.sort(reverse=True)
        return [names for heights,names in z]
    