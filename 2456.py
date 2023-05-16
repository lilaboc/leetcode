# https://leetcode.com/problems/most-popular-video-creator/
from collections import Counter, defaultdict
from typing import List


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creator_views_counter = Counter()
        creator_ids_views_counter = defaultdict(lambda: Counter())
        for c, i, v in zip(creators, ids, views):
            creator_views_counter[c] += v
            creator_ids_views_counter[c][i] += v
        most = creator_views_counter.most_common(1)[0][1]
        most_creators = [k for k, v in creator_views_counter.items() if v == most]
        result = []
        for creator in most_creators:
            most = creator_ids_views_counter[creator].most_common(1)[0][1]
            ids = [v for k, v in creator_ids_views_counter[creator].items() if v == most]
            result.append([creator, sorted(ids)[0]])
        return result




print(Solution().mostPopularCreator(["alice","bob","alice","chris"], ["one","two","three","four"], [5,10,5,4]))