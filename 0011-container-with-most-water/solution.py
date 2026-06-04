from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        best_area = 0
        while left < right:
            area = (right-left) * min(height[left], height[right])
            if area > best_area:
                best_area = area
            
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        
        return best_area


sol = Solution()

height = [1,8,6,2,5,4,8,3,7]

print(sol.maxArea(height))
