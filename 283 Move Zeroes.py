"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_zero = 0
        while 1:
            if 0 not in nums:
                break
            else:
                index_0 = nums.index(0)
                num_zero += 1
                del nums[index_0]
        for i in range(num_zero):
            nums.append(0)
        
        