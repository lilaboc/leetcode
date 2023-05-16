# https://leetcode.com/problems/decode-the-message/
import string


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen = set()
        table = {' ': ' '}
        pos = 0
        for i in key:
            if i == ' ':
                continue
            if i not in seen:
                table[i] = string.ascii_lowercase[pos]
                pos += 1
                seen.add(i)

        return ''.join(table[m] for m in message)


print(Solution().decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))