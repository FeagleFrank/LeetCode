import time

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    s.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

        return s


if __name__ == '__main__':
    start = time.clock()
    s = Solution()
    # nums = [1,2,-2,-1]
    print(s.threeSum([-1,0,1,2,-1,-4]))
    end = time.clock()
    print(end - start)

# Runtime: 876 ms



