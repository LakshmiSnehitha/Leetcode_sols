# Last updated: 8/17/2025, 2:19:15 PM
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
        