class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_ex = nums.copy()
        for index_1, i in enumerate(nums):
            del nums_ex[0]
            for index_2, j in enumerate(nums_ex):
                if i + j == target:
                    return index_1, index_2 + index_1 + 1


if __name__ == '__main__':
    input_nums = [2, 7, 11, 15]
    input_target = 17
    s = Solution()
    print(s.twoSum(input_nums, input_target))

# Run Time: 7492 ms

