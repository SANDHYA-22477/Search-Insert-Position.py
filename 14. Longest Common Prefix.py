class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        smallest = min(len(s) for s in strs)
        result = ""

        for i in range(smallest):
            if all(strs[j][i] == strs[0][i] for j in range(len(strs))):
                result = result + strs[0][i]
            else:
                break
