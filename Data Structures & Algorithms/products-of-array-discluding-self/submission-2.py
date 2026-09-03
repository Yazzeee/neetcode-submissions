class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We begin by doing a left pass and storing it in the output
        output = [1]
        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            output.append(prefix)
        suffix = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i+1]
            output[i] *= suffix
        return output





        