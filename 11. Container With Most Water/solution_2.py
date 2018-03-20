import time

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        l = 0
        r = len(height) - 1
        x = len(height)
        while l < r:
            x -= 1
            maxArea = max(min(height[l], height[r]) * x, maxArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea


if __name__ == "__main__":
    s = Solution()
    d1 = time.clock()
    print(s.maxArea([2,3,4,5,18,17,6]))
    d2 = time.clock()
    print(d2 - d1)


# Runtime: 72 ms