class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        best = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            
            seen.add(s[r])
            best = max(best, r-l+1)
        
        return best


        

sol = Solution()

s = "zxyzxyz"

print(sol.lengthOfLongestSubstring(s))