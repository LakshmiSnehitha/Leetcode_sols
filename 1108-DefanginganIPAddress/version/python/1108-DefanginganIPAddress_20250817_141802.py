# Last updated: 8/17/2025, 2:18:02 PM
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
        