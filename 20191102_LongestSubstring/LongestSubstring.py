class Solution:
    def lengthOfLongestSubstring(self, s):
        if s is None:
            return None
        
        currentCombination = dict()
        longest = 0
        for c in s:
            if c in currentCombination:
                currentCount = len(currentCombination)
                if currentCount > longest:
                    longest = currentCount
                currentCombination = dict()
                currentCombination[c] = 0
            else:
                currentCombination[c] = 0
            
        return longest if longest > 0 else len(currentCombination)

# print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# # 10