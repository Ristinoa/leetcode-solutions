class Solution(object):
    def kthDistinct(self, arr, k):
        unique = []
        duplicate = []
        # Build the unique and duplicate arrays
        for i in arr:
            if i in duplicate:
                pass
            elif i in unique and i not in duplicate:
                unique.remove(i)
                duplicate.append(i)
            else:
                unique.append(i)
            
        if len(unique) >= k:
            return(unique[k-1])
        else:
            return ""
    
soln = Solution()
input = ["d","b","c","b","c","a"]
k = 2

print(soln.kthDistinct(input, k)) # prints a (correct answer)

# ! Someone's one-line soltuion I found, courtesy of MikPosp

# class Solution:
#     def kthDistinct(self, a: List[str], k: int) -> str:
#         return len(q:=[s for s,c in Counter(a).items() if c<2])>=k and q[k-1] or ''

# ? Requires counter??