class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = 0
        while 1:
            if nums ==[]:
                break
            if 1 in nums:
                index_1 = nums.index(1)
                if index_1 != 0:
                    nums[0:index_1]=[]
                if 0 in nums:
                    maxnum = max(maxnum, nums.index(0))
                else:
                    maxnum = max(maxnum, len(nums))
                    break
            else:
                break
        return maxnum