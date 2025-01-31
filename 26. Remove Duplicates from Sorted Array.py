class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        pointer = 0
        for elm in s:
            nums[pointer] = elm
            pointer+=1
        del nums[pointer:]
        nums.sort()
