# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        v = []
        for i in s:
            if i in vowels:
                v.append(i)
        r = []
        for i in s:
            if i in vowels:
                r.append(v.pop())
            else:
                r.append(i)
        return "".join(r)

#print Solution().reverseVowels('aA')
