class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = {}
        for this in nums:
            if this in counts:
                counts[this] += 1
            else:
                counts[this] = 1

        total = 0
        for this, that in counts.items():
            if that == 1:
                total += this

        return total        