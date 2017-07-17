# Time:  O(n)
# Space: O(n)

# Given an integer array with even length, where different numbers 
# in this array represent different kinds of candies.
# Each number means one candy of the corresponding kind.
# You need to distribute these candies equally in number to brother and sister.
# Return the maximum number of kinds of candies the sister could gain.
#
# Example 1:
# Input: candies = [1,1,2,2,3,3]
# Output: 3
# Explanation:
# There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
# Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
# The sister has three different kinds of candies. 
#
# Example 2:
# Input: candies = [1,1,2,3]
# Output: 2
# Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
# The sister has two different kinds of candies, the brother has only one kind of candies. 
#
# Note:
# The length of the given array is in range [2, 10,000], and will be even.
# The number in given array is in range [-100,000, 100,000].

# class Solution(object):
#     def distributeCandies(self, candies):
#         """
#         :type candies: List[int]
#         :rtype: int
#         """
#         candies_kind = []
#         for i in candies:
#             if i not in candies_kind:
#                 candies_kind.append(i)
#         if len(candies_kind) >= len(candies)/2:
#             return len(candies)/2
#         else:
#             return len(candies_kind)

### 超时，而且明显经验不足，没有考虑到set可以直接过滤到所有重复的，set是可以迭代的。最后的for循环太土了，一个min就可以解决了


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candies_kind = [i for i in set(candies)] # set可以直接去掉重复的
        
        return min(len(candies_kind),len(candies)/2)
