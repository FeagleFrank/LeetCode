import time

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        for ds in range(len(height)):
            for dn in range(len(height)):
                if ds == dn:
                    continue
                if height[ds] <= height[dn]:
                    area = abs(dn - ds) * height[ds]
                    maxArea = area if maxArea < area else maxArea
                    continue
        return maxArea


if __name__ == "__main__":
    s = Solution()
    d1 = time.clock()
    print(s.maxArea([2, 1]))
    d2 = time.clock()
    print(d2 - d1)


# Runtime:Time Limit Exceeded