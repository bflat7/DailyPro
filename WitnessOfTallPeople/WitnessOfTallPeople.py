def witnesses(heights):
    if heights is None:
        return None
    visibleWit = 0
    heightToBeat = 0
    index = len(heights) - 1
    while index >= 0:
        if heights[index] > heightToBeat:
            heightToBeat = heights[index]
            visibleWit += 1
        index -= 1
    return visibleWit

print(witnesses([3, 6, 3, 4, 1]))
# 3