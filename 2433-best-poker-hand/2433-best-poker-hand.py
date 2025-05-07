class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        all_same_suit = True
        first_suit = suits[0]
        
        for s in suits:
            if s != first_suit:
                all_same_suit = False
                break
        if all_same_suit:
            return "Flush"
    
        rank_counts = {}
        for r in ranks:
            if r in rank_counts:
                rank_counts[r] += 1
            else:
                rank_counts[r] = 1
    
        for count in rank_counts.values():
            if count >= 3:
                return "Three of a Kind"
    
        for count in rank_counts.values():
            if count == 2:
                return "Pair"
    
        return "High Card"    