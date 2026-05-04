class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
        
        st = s if len(s) > len(t) else t
        for letter in st:
            if hash2.get(letter) is None or hash1.get(letter) is None:
                return False
            if hash2[letter] != hash1[letter]:
                return False
        return True