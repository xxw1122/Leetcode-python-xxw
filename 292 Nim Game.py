"""You are playing the following Nim Game with your friend:
There is a heap of stones on the table, each time one of you
take turns to remove 1 to 3 stones. The one who removes the
last stone will be the winner. You will take the first turn
to remove the stones.
Both of you are very clever and have optimal strategies for
the game. Write a function to determine whether you can win
the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will
never win the game: no matter 1, 2, or 3 stones you remove, the
last stone will always be removed by your friend."""


class Solution(object):
    def canWinNim(self, n):
        return n % 4 != 0

"""
思路：遇到这种题，一般是找规律，所以将序列写出来，寻找规律
     如1，2，3，肯定是先走的人赢；4则是后者赢；
     5的话先者则先走一步，则后者面临4的情况，6，7同5；
     8的话则不管怎么出，后者都可以赢，9，10，11则可以将后者
     置于8的境地，先者赢；12同上则是先者输，所以总结规律就是4
     倍数，则先者输
总结：（1)python 注释可以使用#
     （2）除法3/2结果是1，3./2结果是1.5
     （3）False和True是python中保留的关键字，python3中禁止赋值
"""
