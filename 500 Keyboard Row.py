# Given a List of words, return the words that can be typed
# using letters of alphabet on only one row's of American keyboard like the image below.
#
# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        row=[row1,row2,row3]
        words_return=[]
        for word in words:
            index =0
            for i in xrange(len(row)):
                if word[0].lower() in row[i]:
                    index = i
                    break
            for j in word:
                if j.lower() not in row[index]:
                    break
            else:                               # for循环也是可以增加else的，for完成遍历后才运行else，如果中间跳出则不运行
                words_return.append(word)        
        return words_return

#在判断每个字符的时候需要小写，调用string中的lower()方法。
#在选择row的时候，不一定需要迭代完，所以使用xrange，而不是range
#首先确定属于第几个row,然后针对word中每一个字母判断是不是在选择的row中，如果不在，则break，那么else也不会执行，所以就不会增加进去。