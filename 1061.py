# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        keys = []
        for a, b in zip(s1, s2):
            to_merge = []
            no_merge = []
            found = False
            for key in keys:
                if a in key or b in key:
                    to_merge.append(key)
                else:
                    no_merge.append(key)
            if len(to_merge) == 0:
                keys.append(set([a, b]))
            else:
                keys = [set().union(*to_merge, a, b)] + no_merge
        translator = {}
        for key in keys:
            smallest = sorted(key)[0]
            for i in key:
                translator[i] = smallest
        return "".join([translator[i] if i in translator else i for i in baseStr ])



# print(Solution().smallestEquivalentString("parker", "morris", "parser"))
# print(Solution().smallestEquivalentString("hello", "world", "hold"))
# print(Solution().smallestEquivalentString("leetcode", "programs", "sourcecode"))
print(Solution().smallestEquivalentString("adbfgjdi", "bccgheej", "abcdefgheij"))  # "aaaaafffaaa"


