"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

#这里的难点主要在于如何保留空格
#split()函数，将字符串，按照空格将每个单词组成成列表，这样就没有了中间的空格符
#.reverse()是列表的方法，而不是字符串的方法,而且是直接对列表进行修改，不返回任何值
#reversed()函数返回的是一个迭代器