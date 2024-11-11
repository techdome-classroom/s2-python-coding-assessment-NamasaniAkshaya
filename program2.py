class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass

def romanToInt(s: str) -> int:
    # Mapping of Roman numerals to integers
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Iterate through each character in the Roman numeral string
    for char in s:
        # Get the integer value of the current Roman numeral
        current_value = roman_values[char]
        
        # If the current value is greater than the previous value, adjust for subtraction
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        
        # Update previous value for the next iteration
        prev_value = current_value
    
    return total

