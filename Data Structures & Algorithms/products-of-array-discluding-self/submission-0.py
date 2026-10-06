class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        prefix_product = 1
        for i in range(length):
            output[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(length - 1, -1, -1):
            output[i] *= suffix_product
            suffix_product *= nums[i]
            
        return output
