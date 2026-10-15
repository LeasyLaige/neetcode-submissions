class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']

        if tokens == None or tokens[0] in operators:
            return -300
        
        stack = []
        output = None

        for token in tokens:
            if token in operators:
                num_one = None
                num_two = None

                if stack:
                    num_two = stack.pop()
                if stack:
                    num_one = stack.pop()

                if num_one != None and num_two != None:
                    if token == "+":
                        output = int(num_one) + int(num_two)
                        stack.append(output)
                    elif token == "-":
                        output = int(num_one) - int(num_two)
                        stack.append(output)
                    elif token == "*":
                        output = int(num_one) * int(num_two)
                        stack.append(output)
                    elif token == "/":
                        output = int(int(num_one) / int(num_two))
                        stack.append(output)
                else:
                    stack.append(num_one or num_two)
            else:
                stack.append(token)

        return int(stack.pop()) if stack else -300