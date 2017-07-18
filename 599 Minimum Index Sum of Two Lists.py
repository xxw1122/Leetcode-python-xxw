"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list3=list(set(list1)&set(list2))
        nums = 200000
        choose =[]
        if list3 != []:
            for i in list3:
                nums_add = list1.index(i)+list2.index(i)
                if nums > nums_add:
                    choose=[] # 可能是之前有过两个餐馆排序是一样的，所以要清除
                    choose.append(i)
                    nums = nums_add
                elif nums == nums_add:
                    choose.append(i) # 因为分数一样，所以要直接增加，而不用重新置零
        return choose
            
### 重要的一点是还得考虑两个餐馆的搜索排序是一样的         
