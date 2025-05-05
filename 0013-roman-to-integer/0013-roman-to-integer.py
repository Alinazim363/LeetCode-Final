class Solution(object):
    def romanToInt(self, s):
        value = 0

        replacement = {"IV":"IIII","IX":"VIIII","XL":"XXXX","XC":"LXXXX","CD":"CCCC","CM":"DCCCC"}
        
        conversion = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        for i in replacement:
            s=s.replace(i,replacement[i])

        for char in s:
            value += conversion[char]
        
        return value       