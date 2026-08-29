class Solution:
    def HelperFunction(self, s: str):
        freq_s = {}
        for char in s:
            if char in freq_s:
                freq_s[char] += 1
            else:
                freq_s[char] = 1
        return freq_s

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = self.HelperFunction(s)
        freq_t = self.HelperFunction(t)
        for char, freq in freq_s.items():
            if char not in freq_t:
                return False
            if freq_t[char] != freq:
                return False
        return True

        
