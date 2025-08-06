# Last updated: 8/6/2025, 11:43:50 AM
class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = {}
        count=0

        # Step 1: Count frequency using dictionary
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Step 2: Initialize max frequencies
        vowels = 'aeiou'
        max_vowel = 0
        max_cons = 0

        # Step 3: Loop through the dictionary to find max vowel & consonant
        for ch, count in freq.items():
            if ch in vowels:
                max_vowel = max(max_vowel, count)
            else:
                max_cons = max(max_cons, count)

        # Step 4: Return the sum
        return max_vowel + max_cons
