# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            nums = [int(i) for i in str(num)]
            nums.sort()
            if nums[0] == 0:
                for k, v in enumerate(nums):
                    if v != 0:
                        nums[0] = v
                        nums[k] = 0
                        break
            return int(''.join([str(i) for i in nums]))
        elif num < 0:
            nums = [int(i) for i in str(num)[1:]]
            return -int(''.join([str(i) for i in sorted(nums)[::-1]]))
        else:
            return 0

print(Solution().smallestNumber(310))
print(Solution().smallestNumber(-7605))
