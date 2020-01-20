class Solution:
    def moveZeros(self, nums):
        # finalResult = []
        # zeros = []
        # for num in nums:
        #     if num == 0:
        #         zeros.append(num)
        #     else:
        #         finalResult.append(num)

        # test = finalResult + zeros
        # nums = finalResult + zeros

        if nums is None:
            return None

        firstZero = 0
        currentIndex = 0

        for num in nums:
            if num == 0:
                currentIndex += 1
            else:
                nums[currentIndex] = 0
                nums[firstZero] = num
                firstZero += 1
                currentIndex += 1

# nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
# Solution().moveZeros(nums)
# print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]