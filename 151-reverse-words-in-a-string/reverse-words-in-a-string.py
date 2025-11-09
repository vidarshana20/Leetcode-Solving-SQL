class Solution:
    def reverseWords(self, s: str) -> str:
        n=s.split()
        print(n)
        l=0
        r=len(n)-1
        while l < r:
            n[l],n[r]=n[r],n[l]
            l+=1
            r-=1
            
        s = " ".join(n)
        return s


# class Solution:
#     def reverseWords(self, s: str) -> str:
#         n = s.split()        # split on any whitespace, removes empty strings
#         n.reverse()          # reverse the list
#         s = " ".join(n)      # join back with a single space
#         return s
