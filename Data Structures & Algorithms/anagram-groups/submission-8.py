class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_enc = {}
        for i in range(len(strs)):
            # Order the word in alphabetical order
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word not in words_enc:
                words_enc[sorted_word] = []
            words_enc[sorted_word].append(strs[i])
        return list(words_enc.values())


        
        