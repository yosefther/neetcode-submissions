import operator
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack  =[]
        op = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),  # truncate toward zero
        }
        for i in range(len(tokens)) :
            if tokens[i] not in op :
                stack.append(int(tokens[i]))
            elif tokens[i] in op  :
                right = stack.pop()
                left = stack.pop()
                stack.append(op[tokens[i]](left, right))
                
        return stack[0]