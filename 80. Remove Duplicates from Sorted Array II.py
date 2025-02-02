class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous = nums[0]
        repeat   = 0 
        dels = 0
        for i in range(1,len(nums)):
            if previous == nums[i-dels]:
                repeat += 1
            if previous != nums[i-dels]:
                repeat = 0
                previous = nums[i-dels]
            if repeat >= 2:
                del nums[i-dels]
                dels+=1
        
