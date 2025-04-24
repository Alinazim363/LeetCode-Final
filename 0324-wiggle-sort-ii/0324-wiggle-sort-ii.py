class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        half = (len(nums) + 1) // 2
        first_half = nums[:half]
        second_half = nums[half:]
        nums[::2] = first_half[::-1]
        nums[1::2] = second_half[::-1]
    
        