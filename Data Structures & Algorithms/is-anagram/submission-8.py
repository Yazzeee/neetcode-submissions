class Solution:
    # def HelperFunction(self, s: str):
    #     freq_s = {}
    #     for char in s:
    #         if char in freq_s:
    #             freq_s[char] += 1
    #         else:
    #             freq_s[char] = 1
    #     return freq_s

    def isAnagram(self, s: str, t: str) -> bool:
        freq_s, freq_t = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1
            
        # for char, freq in freq_s.items():
        #     if char not in freq_t:
        #         return False
        #     if freq_t[char] != freq:
        #         return False
        return freq_s == freq_t


# O(N) + O(N) + O(N) -> O(N)
        
