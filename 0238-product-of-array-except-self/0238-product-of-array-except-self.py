class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

    # Compute prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

    # Compute suffix products and combine
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer