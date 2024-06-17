class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ps = 0
        sq = 0
        cu = 0
        stack = []

        for i in s:
            # parentheses
            if i == "(":
                ps += 1
                stack.append("ps")
            elif i == ")":
                if ps == 0:
                    return False
                elif stack.pop() != "ps":
                    return False
                else: 
                    ps -= 1
            # square brackets
            elif i == "[":
                sq += 1
                stack.append("sq")
            elif i == "]":
                if sq == 0:
                    return False
                elif stack.pop() != "sq":
                    return False
                else: 
                    sq -= 1
            # curly brackets
            elif i == "{":
                cu += 1
                stack.append("cu")
            elif i == "}":
                if cu == 0:
                    return False
                elif stack.pop() != "cu":
                    return False
                else: 
                    cu -= 1
            else:
                continue
        
        print(sq)

        if ps == 0 and sq == 0 and cu == 0:
            return True
        else:
            return False
        