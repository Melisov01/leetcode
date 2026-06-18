from typing import List
import operator

tokens = ["2","1","+","3","*"]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "*" : operator.mul,
            "+" : operator.add,
            "-": operator.sub,
            "/": operator.truediv
        }

        for element in tokens:
            if element not in {"*", "/", "-", "+"}:
                stack.append(int(element))
            else:
                right = stack.pop()
                left = stack.pop()
                if element == "/":
                    result = int(left / right)
                else:
                    result = operations[element](left,right)

                stack.append(result)
        
        return stack[-1]