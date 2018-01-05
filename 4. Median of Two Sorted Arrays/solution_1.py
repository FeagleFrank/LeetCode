class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        l = len(nums) // 2
        m = float(nums[l] + nums[-l-1]) / 2
        return m


if __name__ == "__main__":
    s = Solution()
    input_nums1 = [2]
    input_nums2 = [3, 4]
    print(s.findMedianSortedArrays(input_nums1,input_nums2))

# Run Time: 169 ms
