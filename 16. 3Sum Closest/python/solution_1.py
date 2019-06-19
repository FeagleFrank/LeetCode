import time

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        ret = 0
        l = len(nums)
        s = float("inf")
        for i in range(0,l-2):
            for j in range(i+1,l-1):
                sf = 0
                for k in range(j+1,l):
                    st = nums[i] + nums[j] + nums[k] - target
                    if st == 0:
                        return target
                    if abs(st) < s:
                        s = abs(st)
                        ret = nums[i] + nums[j] + nums[k]
                        continue
                    if st > 0:
                        break
        return ret


if __name__ == '__main__':
    start = time.clock()
    s = Solution()
    print(s.threeSumClosest([1,1,1,0], -100))
    end = time.clock()
    print(end - start)

# Runtime: Time Limit Exceeded


# [-1, 2, 1, -4], 1
# [0, 0, 0], 1
# [1,2,4,8,16,32,64,128], 82



