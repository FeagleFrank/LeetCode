import time

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        c = []
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums)-1
            if nums[i] + nums[l] + nums[l+1] > target:
                c.append(nums[i] + nums[l] + nums[l+1])
            elif nums[i] + nums[r-1] + nums[r] < target:
                c.append(nums[i] + nums[r-1] + nums[r])
            else:
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    c.append(s)
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        return target

        c.sort(key=lambda x: abs(x - target))
        return c[0]


if __name__ == '__main__':
    start = time.clock()
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    end = time.clock()
    print(end - start)

# Runtime: 44ms


# [-1, 2, 1, -4], 1
# [0, 0, 0], 1
# [1,2,4,8,16,32,64,128], 82



