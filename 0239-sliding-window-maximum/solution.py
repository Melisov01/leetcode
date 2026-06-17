from typing import List
from collections import deque

nums = [1,3,-1,-3,5,3,6,7]
k = 3

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        left = 0
        candidates = deque()

        for right in range(len(nums)):
            while candidates and nums[candidates[-1]] < nums[right]:
                candidates.pop()

            candidates.append(right)

            if candidates[0] < left:
                candidates.popleft()

            if right - left + 1 == k:
                output.append(nums[candidates[0]])
                left+=1
        
        return output



sol = Solution()
print(sol.maxSlidingWindow(nums, k))

