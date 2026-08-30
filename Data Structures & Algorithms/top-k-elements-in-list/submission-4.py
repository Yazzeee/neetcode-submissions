class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        sorted_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))
        sorted_list = list(sorted_dict.keys())
        return sorted_list[0:k]

        