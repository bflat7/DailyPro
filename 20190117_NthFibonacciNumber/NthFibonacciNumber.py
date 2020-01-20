class Solution():
    def fibonacci(self, n):
        first = 0
        second = 1
        if n is None:
            return None
        elif n == 0:
            return first
        elif n == 1:
            return second

        current = 0
        while n - 1 > 0:
            current = first + second
            first = second
            second = current
            n -= 1
        
        return current

n = 9
print(Solution().fibonacci(n))
# 34