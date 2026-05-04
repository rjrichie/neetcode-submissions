class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = {}
        hash2 = {}
        for letter in s:
            if hash1.get(letter) is None:
                hash1[letter] = 0
            hash1[letter] += 1
        for letter in t:
            if hash2.get(letter) is None:
                hash2[letter] = 0
            hash2[letter] += 1
        
        for letter in s:
            if hash2.get(letter) is None:
                return False
            if hash2[letter] != hash1[letter]:
                return False
        return True