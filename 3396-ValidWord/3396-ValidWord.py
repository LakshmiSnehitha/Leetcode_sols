# Last updated: 7/28/2025, 3:28:39 PM
# class Solution:
#     def isValid(self, word: str) -> bool:
#         if len(word) < 3:
#             return False

#         vowels = 'aeiouAEIOU'
#         consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

#         has_vowel = False
#         has_consonant = False

#         for ch in word:
#             if not ch.isalnum():
#                 return False
#             if ch in vowels:
#                 has_vowel = True
#             if ch in consonants:
#                 has_consonant = True

#         return has_vowel and has_consonant
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = 'aeiouAEIOU'
        has_vowel = False
        has_consonant = False

        for ch in word:
            if not ch.isalnum():
                return False
            if ch in vowels:
                has_vowel = True
            elif ch.isalpha():
                has_consonant = True

        return has_vowel and has_consonant
