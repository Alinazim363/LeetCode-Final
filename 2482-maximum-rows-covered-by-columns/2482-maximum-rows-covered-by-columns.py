class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
    
        best_coverage = 0
    
        for selected_cols in combinations(range(n), numSelect):
            covered_rows = 0
        
            for row in matrix:
                if all(row[j] == 0 or j in selected_cols for j in range(n)):
                    covered_rows += 1
        
            best_coverage = max(best_coverage, covered_rows)
    
        return best_coverage