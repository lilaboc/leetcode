# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def __init__(self):
        self.th = {"MMM": 3, "MM": 2, "M":1}
        self.th_k = sorted(self.th, key=len, reverse=True)
        self.h = {"C": 1, "CC": 2, "CCC": 3, "CD": 4, "D": 5, "DC": 6, "DCC": 7, "DCCC": 8, "CM": 9, "": 0}
        self.h_k = sorted(self.h, key=len, reverse=True)
        self.t = {"X": 1, "XX": 2, "XXX": 3, "XL": 4, "L": 5, "LX": 6, "LXX": 7, "LXXX": 8, "XC": 9, "": 0}
        self.t_k = sorted(self.t, key=len, reverse=True)
        self.o = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "": 0}
        self.o_k = sorted(self.o, key=len, reverse=True)

    def romanToInt(self, s: str) -> int:
        result = 0
        index = 0
        for k, v in {1000: [self.th_k, self.th], 100: [self.h_k, self.h], 10: [self.t_k, self.t], 1: [self.o_k, self.o]}.items():
            for o in v[0]:
                if s[index: index + len(o)] == o:
                    result += v[1][o] * k
                    index += len(o)
                    break
        return result

            


print(Solution().romanToInt("MCMXCIV"))
        