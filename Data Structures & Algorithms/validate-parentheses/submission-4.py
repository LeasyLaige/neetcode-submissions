class Solution:
    def isValid(self, s: str) -> bool:
        if s == None or len(s) <= 0:
            return False

        stack = []
        open_parenthesis = ["(", "[", "{"]
        closing_parenthesis = [")", "]", "}"]

        for char in s:
            if char in open_parenthesis:
                stack.append(char)
            
            if char in closing_parenthesis:
                if len(stack) <= 0:
                    return False

                if char == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif char == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                elif char == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        
        if stack or len(stack) > 0:
            return False
        
        return True