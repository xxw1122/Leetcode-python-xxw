
"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_temp=list(s)
        s_temp.reverse()
        return ''.join(s_temp)