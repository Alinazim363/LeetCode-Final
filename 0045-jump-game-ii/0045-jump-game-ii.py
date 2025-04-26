class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0
    
        for i in range(n - 1):  # We don't need to process the last element
            farthest = max(farthest, i + nums[i])
        
            if i == current_end:  # Time to make a jump
                jumps += 1
                current_end = farthest
    
        return jumps