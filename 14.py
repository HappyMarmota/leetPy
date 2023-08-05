from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_l = min([len(x) for x in strs])
        for i in range(min_l):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:min_l]



if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))
    print(s.longestCommonPrefix(["dog","dog","dog"]))