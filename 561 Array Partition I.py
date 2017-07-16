Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

#最直接的思路就是直接排序后，然后从小到大，每两个组队，所以只要返回奇数项的和就可以了

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_temp=sorted(nums) #nums这个参数是在类内部的，不用加self
        sum1 = 0
        for i in range(len(nums)/2):
            sum1 += nums_temp[2*i]  #我能说啥好呢，2*i，不能直接写成2i啊      
        return sum1


# 能不能将上面的进行缩写
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])#对排序好的nums数列进行切片，范围所有的，间隔是2