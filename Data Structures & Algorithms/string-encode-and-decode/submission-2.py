class Solution:
    # Length Prefixing
    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res = res + str(len(st)) + "#" + st
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
       
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            i = j + 1
            strs.append(s[i:i+num])
            i += num

        return strs