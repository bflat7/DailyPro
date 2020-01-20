import sys

class Solution():
    # def __init__(self):

    def romanToInt(self, s):
        if s is None:
            return None
        
        s = s.upper()
        total = 0
        currentHighest = sys.maxsize * -1
        index = len(s) - 1
        while index > -1:
            currentValue = self.romanSwitcher(s[index])
            if currentValue >= currentHighest:
                total += currentValue
                currentHighest = currentValue
            else:
                total -= currentValue
            index -= 1

        return total

    def romanSwitcher(self, argument):
        switcher = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        return switcher.get(argument, "Argument not supported")

    
        
    
n = 'MCMX'
print(Solution().romanToInt(n))
# 1910