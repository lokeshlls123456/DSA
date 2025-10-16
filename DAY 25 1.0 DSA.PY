class Solution(object):
    def maxFreqSum(self, s):
        vowels = set('aeiou')
        freq = {}

        # Count frequency of each character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        max_vowel = 0
        max_consonant = 0

        for ch, count in freq.items():
            if ch in vowels:
                if count > max_vowel:
                    max_vowel = count
            else:
                if count > max_consonant:
                    max_consonant = count

        return max_vowel + max_consonant
