"""Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

# 这招实在是太笨了，竟然想到用字符串处理数字相加


class Solution(object):
    def addDigits(self, num):
        strnum = str(num)
        while len(strnum) > 1:
            num_temp = 0
            for i in range(len(strnum)):
                num_temp = num_temp + int(strnum[i])
            strnum = str(num_temp)
        return int(strnum)
""" 上述为第一种解法，不符合要求；
    思路：把数字转化成字符串，计算字符串的大小，从而提取每一位数
   (1): 如何计算时间复杂度；
        常见的时间复杂度，按数量级递增排列依次为：常数阶O(1)、
        对数阶O(log2n)、线性阶O(n)、线性对数阶O(nlog2n)、
        平方阶O(n^2)、立方阶O(n^3)、k次方阶O(n^k)、指数阶O(2^n)
   (2): 字符串的长度用len(b)
   (3): 列表生成式：[x*x for x in range(1,11) if x %2 == 0] 
        还有dict 的 iteritems()可以同时迭代key和value
        [k + '=' + v for k,v in d.iteritems()]
   错误总结:
   （1）:在第一次写的时候忘记了类中的函数传入num这个参数时候忘记了赋值，
        应该加入self.num = num
    (2):在for循环中，strnum要始终保持是string类型的，所以别忘了把num_temp
        转换成string格式的

"""

# 逐位相加，除以10，第一个/的结果是除了个位数，将后面求出的个位数加到
# 前面的结果，相当于后两位相加，直到结果小于10


class Solution(object):
    def addDigits(self, num):
        while num > 10:
            num = num / 10 + num % 10

        return num


# 第二种要求在O(1)时间复杂度内计算出这个问题
# 时间复杂度为O(1)代表着算法的执行时间不随着问题规模n的增加而增加
"""
思路：这种情况一般能再O(1)时间复杂度内完成的，都是有规律的，
     需要寻找规律，规律就是9的余数，整除9时结果就是9
"""


class Solution(object):
    def addDigits(self, num):
        digit = num%9
        if digit ==0 and num != 0:
            return 9
        else:
            return digit
