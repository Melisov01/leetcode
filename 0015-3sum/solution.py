from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            fixed_number = nums[i]
            right = len(nums) - 1
            left = i + 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                if fixed_number + nums[right] + nums[left] > 0:
                    right-=1
                elif fixed_number + nums[right] + nums[left] < 0:
                    left+=1
                else:
                    result.append([fixed_number, nums[left], nums[right]])
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
        
        return result


nums = [-1,0,1,2,-1,-4]
sol = Solution()
func_call = sol.threeSum
print(func_call(nums))

            

        