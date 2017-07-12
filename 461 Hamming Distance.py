"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.


"""
# 首先想到的就是二进制和异或运算.
#在python中，有内置函数bin可以直接将一个数转化成二进制，但是可能效率并不是最高的。bin 只能操作整数和长整数

#1 直接使用bin内置函数，然后调用.count直接计算被转化成二进制中包含的1的多少




class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')


#### 计算时间为56ms，因为调用bin（）函数，效率并不一定高

#2

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n=0
        while x or y:
            n+=(x%2)^(y%2)
            x//=2
            y//=2
        return n
        
### 计算时间较高，36ms, 使用二进制转化的技巧，直接一位一位进行计算，每一次计算一位，然后将x和y除以2
### 注意使用的是//