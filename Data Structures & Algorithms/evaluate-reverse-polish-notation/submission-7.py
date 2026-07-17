class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []

        for t in tokens:
            if t not in "+-/*":
                stack.append(int(t))
            else:
                op2, op1 = stack.pop(), stack.pop()

                if t == "+":
                    stack.append(op1+op2)
                elif t == "-":
                    stack.append(op1-op2)
                elif t == "*":
                    stack.append(op1*op2)
                else:
                    stack.append(int(op1/op2))

            
        return stack[-1]
