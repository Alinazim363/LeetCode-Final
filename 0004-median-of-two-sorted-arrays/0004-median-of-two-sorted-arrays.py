class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j = 0, 0
        len1, len2 = len(nums1), len(nums2)
    
        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
            
        if i < len1:
            merged.extend(nums1[i:])
        if j < len2:
            merged.extend(nums2[j:])

        n = len(merged)
        
        if n % 2 == 0:
            mid1 = merged[n // 2 - 1]
            mid2 = merged[n // 2]
            median = (mid1 + mid2) / 2
        else:
            median = merged[n // 2]
        return median 