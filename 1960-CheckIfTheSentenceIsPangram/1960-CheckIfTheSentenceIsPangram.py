# Last updated: 7/28/2025, 3:29:10 PM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # for ch in 'abcdefghijklmnopqrstuvwxyz':
        #     if ch not in sentence:
        #         return False
            
        # return True
        return len(set(sentence))  ==26   