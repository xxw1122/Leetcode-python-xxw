"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1,num2 = num2,num1
        lst1 = list(num1)
        lst1.reverse()
        lst2 = list(num2)
        lst2.reverse()
        lst = []
        counter = 0
        print lst1,lst2
        for i in xrange(min(len(num1),len(num2))):
            sum_both = ord(lst1[i]) + ord(lst2[i]) - 2*ord('0')
            lst.append(str((sum_both + counter) % 10))
            counter = (sum_both + counter) / 10
        print lst,counter
        if len(num1) == len(num2):
            if counter == 1:
                lst.append(str(counter))
        elif len(num1) > len(num2):
            for j in xrange(len(num1)-len(num2)):
                sum_both = ord(lst1[len(num2)+j]) - ord('0') +counter
                print sum_both
                lst.append(str(sum_both%10))
                counter = sum_both /10
            if counter == 1:
                lst.append(str(1))
       
        lst.reverse()
        return ''.join(lst)