"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

# pop()返回队列中的一个元素，并将原始的队列去除这个元素，直接进行修改
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        myQuary = []
        myQuary.append(root)
        result=[]
        def searchchild(notelist):
            list=[]              # 开始的时候忘记初始化list了，如果搜不到子树后，返回的list将是不可控的
            if notelist.left != None:
                list.append(notelist.left)
            if notelist.right != None:
                list.append(notelist.right)
            return list
        list =[]
        while 1:
            result_temp=[]
            for j in myQuary:
                result_temp.append(j.val) # 使用append的时候需要对result_temp进行初始化
                list.extend(searchchild(j))
            result.append(float(sum(result_temp))/len(result_temp)) # 应该先计算，然后判断list是否为空
            if list == []:
                break
            myQuary=list
            list=[]
        return result




                               
