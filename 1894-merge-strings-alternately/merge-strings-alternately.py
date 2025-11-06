class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        mini = min(len(word1), len(word2))
        
        for i in range(mini):
            merged.append(word1[i])
            merged.append(word2[i])
        
        merged.append(word1[mini:])
        merged.append(word2[mini:])
        
        return ''.join(merged)



        