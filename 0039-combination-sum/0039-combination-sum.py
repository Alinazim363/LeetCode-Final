class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:  
                result.append(list(path))
                return
            if target < 0:  
                return
        
            for i in range(start, len(candidates)):
                path.append(candidates[i])  
                backtrack(i, target - candidates[i], path)  
                path.pop() 
    
        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result   