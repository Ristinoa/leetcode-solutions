from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # make both sentences into lists of words
        s1_text = s1.split()
        s2_text = s2.split()

        # combine both lists of words into a single list of all words
        combined = s1_text + s2_text

        # use counter to count occurrences of elements within the list
        count = Counter(combined)

        # return a list of all words with only one occurrence in counter
        return [word for word in count if count[word] == 1]
    
s1 = "this apple is sweet"
s2 = "this apple is sour"

solution = Solution()

print(solution.uncommonFromSentences(s1,s2)) # Prints ['sweet', 'sour']