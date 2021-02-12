# https://leetcode.com/problems/find-duplicate-file-in-system/

from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(lambda: [])
        for path in paths:
            path = path.split()
            root = path[0]
            for file in path[1:]:
                filename = file[:file.index('(')]
                content = file[file.index('(') + 1:-1]
                d[content].append(root + "/" + filename)
        return [v for v in d.values() if len(v) > 1]


print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
