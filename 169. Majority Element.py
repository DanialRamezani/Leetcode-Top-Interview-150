class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        repeat = 0
        
        if len(nums) == 1:
            return nums[0]
        else:
            for i in range(1,len(nums)):
                if nums[i-1] == nums[i]:
                    repeat +=1
                else:
                    repeat = 0
                if repeat >= len(nums)/2:
                    return nums[i]                
                    break


        
