class Solution(object):
    def findSingle(self, nums):
        if nums is None:
            return None
        elif len(nums) == 1:
            return nums[0]
        
        setDict = dict()
        for num in nums:
            if num in setDict:
                setDict.pop(num)
            else:
                setDict[num] = 1
        if len(setDict) == 0:
            return None
        return list(setDict.keys())[0]

# nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
# print(Solution().findSingle(nums))
# 3