# https://leetcode.com/problems/additive-number/
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num_str = str(num)
        if len(num_str) <= 2:
            return False
        for i in xrange(1, len(num_str)):
            for o in xrange(i + 1, len(num_str)):
                #print num_str[: i]
                #print num_str[i: o]
                #print num_str[o:]
                if self.try_this(num_str[: i], num_str[i:o], num_str[o:]) == True:
                    return True
        return False


        #while True:
        #    pass
        #    #for i in xrange(a_start, len(num_str) - a_start - a_length)

    def try_this(self, a, b, num):
        if (len(str(a)) > 1 and str(a).startswith('0')) or (len(str(b)) > 1 and str(b).startswith('0')):
            return False
        a = int(a)
        b = int(b)
        num_str = str(num)
        sum = a + b
        sum_str = str(sum)
        #print a
        #print b
        #print sum_str
        if num_str[: len(sum_str)].startswith('0'):
            return False
        if int(num_str[: len(sum_str)]) == sum:
            if len(sum_str) == len(num_str):
                return True
            else:
                return self.try_this(b, sum,  num_str[len(sum_str):])

        else:
            return False

#print Solution().isAdditiveNumber(112358)
#print Solution().isAdditiveNumber(112359)
#print Solution().isAdditiveNumber(199100199)
#print Solution().isAdditiveNumber(100011001)
#print Solution().isAdditiveNumber(121224036)
#print Solution().isAdditiveNumber(12345678)
#print Solution().isAdditiveNumber(198019823962)
#print Solution().isAdditiveNumber(101)
#print Solution().try_this(1, 1, 235)
#print Solution().try_this(1, 1, 236)
