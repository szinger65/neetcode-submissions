class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
    
        for i in range(len(nums)):
            complement = target - nums[i]
        
        # Check if the needed value has already been seen
            if complement in values:
            # Return the smaller index first
                return [values[complement], i]
            
        # Store the current value and its index
            values[nums[i]] = i
        
            