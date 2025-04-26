class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []

        word_length = len(words[0])
        total_length = word_length * len(words)
        word_count = Counter(words)
        result = []

        for offset in range(word_length):
            start = offset
            seen = Counter()
            count = 0
            for end in range(offset, len(s), word_length):
                word = s[end:end + word_length]
                if word in word_count:
                    seen[word] += 1
                    count += 1

                    while seen[word] > word_count[word]:
                        left_word = s[start:start + word_length]
                        seen[left_word] -= 1
                        count -= 1
                        start += word_length
                
                    if count == len(words):
                        result.append(start)
                else:
                    seen.clear()
                    count = 0
                    start = end + word_length

        return result    