# https://leetcode.com/problems/number-of-recent-calls/

from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()
        

    def ping(self, t: int) -> int:
        self.q.append(t)
        while t - self.q[0] > 3000:
            self.q.popleft()
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))

