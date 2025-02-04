class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        added = 0
        for i in range(k):
            nums.insert(added, nums[len(nums)-k+i])
            del nums[len(nums)-k+i]
            added += 1
