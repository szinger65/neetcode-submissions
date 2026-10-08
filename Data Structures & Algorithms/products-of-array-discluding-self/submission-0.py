class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        j=0
        while j < len(nums):
            count = 1
            for i in range(1,len(nums)):
                count*=nums[i]
            output.append(count)
            temp = nums[0]
            nums.pop(0)
            nums.append(temp)
            j+=1
        return output

