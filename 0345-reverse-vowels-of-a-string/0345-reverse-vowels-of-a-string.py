class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        st,end = 0 ,len(s)-1
        arr = list(s)

        while st<end:
            if arr[st] not in vowels:
                st+=1
            elif arr[end] not in vowels:
                end -=1
            else:
                arr[st],arr[end] = arr[end],arr[st]
                st +=1
                end -=1
        res = ''.join(arr)
        return res
        