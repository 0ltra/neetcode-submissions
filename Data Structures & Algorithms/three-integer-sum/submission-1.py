class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort first to handle duplicates and use two pointers
        
        for i in range(len(nums) - 2):
            # If the current number is > 0, the remaining numbers will also be > 0.
            # They can never sum up to 0, so we can break early.
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Two pointers for the remaining window
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate values for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif three_sum < 0:
                    left += 1  # Sum is too small, make it larger
                else:
                    right -= 1 # Sum is too big, make it smaller
                    
        return res

        