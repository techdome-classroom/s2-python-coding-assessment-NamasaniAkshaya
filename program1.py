class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pass

def isValid(s: str) -> bool:
    # Dictionary to hold the matching pairs
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of opening brackets
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If the character is a closing bracket
        if char in matching_brackets:
            # Pop the top element from the stack if it's not empty; otherwise use a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the expected opening bracket
            if matching_brackets[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # If the stack is empty, all brackets were matched correctly
    return not stack





    



  

