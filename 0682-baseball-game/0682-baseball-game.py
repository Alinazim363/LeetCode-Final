class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = [] 
    
        for op in operations:
            if op == "+":  
                last = record[-1]
                second_last = record[-2]
                record.append(last + second_last)
            elif op == "D":
                last = record[-1]
                record.append(2 * last)
            elif op == "C":
                record.pop()
            else:
                score = int(op)
                record.append(score)
    
        total = sum(record)
        return total    