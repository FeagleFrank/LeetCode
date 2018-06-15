import time

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        nums.sort()
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if (- nums[i] - nums[j]) in nums:
                    if nums[i] * 2 == -nums[j] and nums.count(nums[i]) <= 1:
                        continue
                    elif nums[j] * 2 == -nums[i] and nums.count(nums[j]) <= 1:
                        continue
                    elif nums[i] == 0 and nums[j] == 0 and nums.count(0) <=2:
                        continue
                    else:
                        item = sorted([nums[i], nums[j], -nums[i] - nums[j]])
                        if item not in l:
                            l.append(item)
        return l


if __name__ == '__main__':
    start = time.clock()
    s = Solution()
    # nums = [1,2,-2,-1]
    print(s.threeSum([-1,0,1,2,-1,-4]))
    end = time.clock()
    print(end - start)

# Runtime: Time Limit Exceeded


# [1,2,-2,-1]
# [-1,0,1,2,-1,-4]
# [-2,0,0,2,2]
# [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
# [4,4,3,-5,0,0,0,-2,3,-5,-5,0]
