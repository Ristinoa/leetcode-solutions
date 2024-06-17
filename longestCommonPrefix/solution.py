class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        output = strs[0]
        output_len = len(output)

        for s in strs[1:]:
            while output != s[0:output_len]:
                output_len -= 1
                if output_len == 0:
                    return ""

                output = output[0:output_len]
            
        return output

solution = Solution()

input1 = ["flower","flow","flight"]
input2 = ["dog","racecar","car"]
input3 = ["a"]
input4 = ["ab", "a"]

solution.longestCommonPrefix(input1)
solution.longestCommonPrefix(input2)
solution.longestCommonPrefix(input3)
solution.longestCommonPrefix(input4)