# https://leetcode.com/problems/minimum-index-sum-of-two-lists/#/description

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = {}
        d2 = {k: v for v, k in enumerate(list2)}
        for k1, v1 in {k: v for v, k in enumerate(list1)}.items():
            if k1 in d2:
                result[k1] = v1 + d2[k1]
        #print result
        from collections import defaultdict
        lastresult = defaultdict(lambda: [])
        for k, v in result.items():
            lastresult[v].append(k)
        return lastresult[sorted(lastresult)[0]]

#print Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
print Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"])


