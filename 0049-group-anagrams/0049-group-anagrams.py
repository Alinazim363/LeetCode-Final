class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {} 
    
        for string in strs:
            sorted_string = ''.join(sorted(string)) 
            if sorted_string not in anagram_map:
                anagram_map[sorted_string] = []
            anagram_map[sorted_string].append(string)  
    
        return list(anagram_map.values())