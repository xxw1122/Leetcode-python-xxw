Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1‘s at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)


#第一反应是应该想到递归，在类中定义一个函数后，发现无法递归depth，所以还需要增加一个函数。在判断一个数值是否
#为整数时，我们使用isinstance(i,int)

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
         def depthSum_iter(nestedList,depth):
            sum_list = 0
            #for i in range(len(nestedList)) 可以不用这么写，本来list就是可以迭代的，我们可以每次选取其中一个
            for i in nestedList:
                if isinstance(i,int):
                    sum_list += i*depth
                    #return sum_list   #在函数中，遇到第一个return的时候，函数就被终止了，这里不需要写return，for循环结束后统一返回
                else:
                    sum_list +=depthSum_iter(i,depth+1)
            return sum_list
        return depthSum_iter(nestedList,1) #在第一个depthSum函数中，需要一个返回值，我们直接返回调用迭代的函数，并将深度置成1

