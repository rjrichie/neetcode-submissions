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
            if s[i] == "#":
                j = i - 1
                while j > 0 and s[i].isnumeric():
                    j -= 1
                if j < i:
                    length = int(s[j:i])
                else:
                    length = 0
                strs.append(s[i + 1:i + 1 + length])
            i += 1

        return strs