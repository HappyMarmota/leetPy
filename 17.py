from typing import List

pb = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
        }


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        return self.dfs(digits)

    def dfs(self, digits):
        if len(digits) == 0:
            return [""]
        ans = []
        for x in pb[digits[0]]:
            for v in self.dfs(digits[1:]):
                ans.append(x + v)

        return ans

if __name__ == '__main__':
    # print(Solution().letterCombinations("23"))
    print(Solution().letterCombinations(""))