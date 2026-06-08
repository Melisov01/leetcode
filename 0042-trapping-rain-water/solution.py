from typing import List

height = [0,1,0,2,1,0,1,3,2,1,2,1]
test = [0,1,0,2]
test2 = [4,2,0,3,2,5]

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftmax = 0
        rightmax = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    water += leftmax - height[left]

                left+=1
            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    water += rightmax - height[right]
            
                right-=1
            
        return water
                

        

sol = Solution()

print(sol.trap(test2))