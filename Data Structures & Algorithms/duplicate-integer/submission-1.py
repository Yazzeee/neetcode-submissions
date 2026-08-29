class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        if len(num_set) == len(nums):
            return False
        return True
        # for num in nums:
        #     if num in num_set:
        #         return True
        #     num_set.add(num)
        # return False
        