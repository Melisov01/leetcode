from typing import List
from collections import deque

temperatures = [73,74,75,71,69,72,76,73]
#       Output: [1,1,4,2,1,1,0,0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = deque()
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if not stack:   
                answer.appendleft(0)
            else:
                answer.appendleft(stack[-1] - i)
            
            stack.append(i)
        
        return list(answer)
                


                

