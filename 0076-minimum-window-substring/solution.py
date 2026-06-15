from collections import Counter, defaultdict

class Soluiton:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        

        need_count = Counter(t)
        window = defaultdict(int)

        have = 0
        need = len(need_count)

        best_length = float('inf')
        best_left = 0
        best_right = 0

        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] +=1

            if char in need_count and window[char] == need_count[char]:
                have +=1
            
            while have == need:
                current_length = right - left + 1
                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right
                
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need_count and window[left_char] < need_count[left_char]:
                    have -=1
                
                left+=1
            
        if best_length == float("inf"):
                return ""
            
        return s[best_left:best_right+1]
    
s = "OUZODYXAZV"
t = "XYZ"

sol = Soluiton()

print(sol.minWindow(s,t))
