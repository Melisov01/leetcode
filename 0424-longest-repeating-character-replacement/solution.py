class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        counter = {}
        left = 0
        max_counter = 0

        for right in range(len(s)):
            r_character = s[right]
            counter[r_character] = counter.get(r_character,0) + 1

            window_length = right - left + 1
            max_counter = max(max_counter, counter[r_character])

            while window_length - max_counter > k:
                counter[s[left]] -=1
                left+=1
                window_length = right - left + 1
            
            best = max(best, window_length)
        
        return best
    
sol = Solution()

s = "AAABABB"
k = 1

print(sol.characterReplacement(s,k))