# https://leetcode.com/problems/rearrange-words-in-a-sentence/

from collections import defaultdict
class Solution:
    def arrangeWords(self, text: str) -> str:
        d = defaultdict(lambda : [])
        [d[len(i)].append(i.lower()) for i in text.split(" ")]
        result = ' '.join([' '.join(d[i]) for i in sorted(d.keys())])
        result = result[0].upper() + result[1:]
        return result


print(Solution().arrangeWords("To be or not to be"))



                

