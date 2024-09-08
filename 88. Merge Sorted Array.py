class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.m = m
        self.n = n
        if m!=0 and n>0:
            nums1[m:] = nums2
        elif n <=0:
            nums1[m:] = []
            nums1
        elif m == 0:
            nums1[m:] = []
            nums1[:m] = nums2
        nums1.sort()
