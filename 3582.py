# https://leetcode.com/problems/generate-tag-for-video-caption/

class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if len(words) > 0:
            result = "#" + self.filter((words[0].lower())) + "".join((self.filter(self.snake(i)) for i in words[1:]))
            return result[:100]
        return "#"


    def snake(self, s: str) -> str:
        return s[0].upper() + s[1:].lower()

    def filter(self, s:str) -> str:
        return "".join((i for i in s if i.isalpha()))


print(Solution().generateTag("Leetcode daily streak achieved"))
