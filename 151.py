# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        inspace = False
        result = ""
        candidate = ""
        s = s.strip()
        for i in s[::-1]:
            if i == ' ':
                if inspace == True:
                    pass
                else:
                    # popup word
                    result += candidate[::-1]
                    candidate = ""
                inspace = True
            else:
                if inspace == True:
                    result += " "
                    inspace = False
                candidate += i
        if not inspace:
            result += candidate[::-1]
        return result

# TODO: use deque?
# TODO: use timeit?
#print Solution().reverseWords(" the  sky is blue ")
