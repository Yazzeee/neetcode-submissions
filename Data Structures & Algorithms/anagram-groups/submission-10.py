class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_enc = defaultdict(list) # dedaults to an empty list
        for i in range(len(strs)):
            # Order the word in alphabetical order
            sorted_word = ''.join(sorted(strs[i]))
            words_enc[sorted_word].append(strs[i])
        return list(words_enc.values())


        
        