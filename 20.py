class Solution:
    def isValid(self, s: str) -> bool:
        sac = []
        for x in s :
            if x == "(" or x == "[" or x == "{":
                sac.append(x)
            else:
                if len(sac) == 0:
                    return False
                if x == ")" and sac.pop() != "(":
                    return False
                if x == "]" and sac.pop() != "[":
                    return False
                if x == "}" and sac.pop() != "{":
                    return False
        if len(sac) != 0:
            return False

        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))
    print(s.isValid("]"))
    print(s.isValid("(("))