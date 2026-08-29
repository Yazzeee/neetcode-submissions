class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_enc = {}
        for i in range(len(strs)):
            # Order the word in alphabetical order
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word not in words_enc:
                words_enc[sorted_word] = []
            words_enc[sorted_word].append(i)
        main_list = []
        for word_info, indices in words_enc.items():
            word_sublist = []
            for index in indices:
                word_sublist.append(strs[index])
            main_list.append(word_sublist)
        return main_list


        
        