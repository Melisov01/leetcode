from collections import Counter

class Solution:
    def checkInclusion(self, s1:str, s2:str) -> bool:
        if len(s1) > len(s2):
            return False
        
        left = 0
        target_count = Counter(s1)
        window_count = Counter()

        window_size = len(s1)
        
        for right in range(len(s2)):
            window_count[s2[right]] +=1

            if right - left + 1 > window_size:
                window_count[s2[left]] -= 1

                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                
                left+=1
            
            if right - left + 1 == window_size:
                if window_count == target_count:
                    return True 
        
        return False
    

sol = Solution()

s1 = "ab"
s2 = "eidbaooo"

print(sol.checkInclusion(s1,s2))
            