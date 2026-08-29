class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in nums_dict:
                return [nums_dict[remain], i]
            nums_dict[nums[i]] = i