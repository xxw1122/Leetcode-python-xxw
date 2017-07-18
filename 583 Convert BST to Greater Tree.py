"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     1
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def search(root): 

#             if root == None:
#                 return a
            
#             a.append(root.val)
#             a = search(root.left, a)
#             a = search(root.right, a)

 
            
            # 应该是变量生命周期的问题 你添加a元素依靠的是 
            # return的赋值
            # 进入search(root.left, a)
            # 函数外部的a和函数内部的a是同一个数组对象的两个别名，共索引一块内存
            # 如果root==None什么都不做直接返回原值，这块内存一直都有索引，那么a和原来一样应该不存在问题
            # 而一旦root!=None，append，内部a对应内存中的值就改变了，是一个新的数组对象
            # 而return之后，外部a要指向一个新的内存（由内部a），内部a的生命结束了，外部a被赋值之前相当于之前这个数组被当做垃圾清空掉了
            # 这时候外部的a就已经是None了
            global a
            if root == None:
                return
            a.append(root.val)
            search(root.left)
            search(root.right)
            
            
        global a 
        a = []
        search(root)


        
        # def return_sum(a,num):
        #     for i in a:
        #         if i > num: # 在if语句中修改了num，但是后来还拿这判断，这样就不对了
        #             num+=i
        #     return num
        
        def return_sum(a,num):
            num_temp =num
            for i in a:
                if i > num_temp:
                    num+=i
            return num
        
        
        def covert_help(root,a):
            if not root:
                return 
            root.val = return_sum(a,root.val)
            
            covert_help(root.left,a)
            covert_help(root.right,a)
            
            
             
        covert_help(root,a)
        return root
## yis行

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def search(root): 
            global a
            if root == None:
                return
            a.append(root.val)
            search(root.left)
            search(root.right)
            
            
        global a 
        a = []
        search(root)
        a=sorted(list(set(a)))
        

        
        # def return_sum(a,num):
        #     for i in a:
        #         if i > num: # 在if语句中修改了num，但是后来还拿这判断，这样就不对了
        #             num+=i
        #     return num
        
        def return_sum(a,num):
            
            index_num = a.index(num)
            num += sum(a[(index_num)+1:])
            return num
        
        
        def covert_help(root,a):
            if not root:
                return 
            root.val = return_sum(a,root.val)
            
            covert_help(root.left,a)
            covert_help(root.right,a)
            
            
             
        covert_help(root,a)
        return root

        


