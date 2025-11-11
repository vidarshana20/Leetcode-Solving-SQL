class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0      # index to write compressed output
        read = 0       # index to scan input

        while read < n:
            ch = chars[read]
            count = 0

            # count consecutive occurrences of chars[read]
            while read < n and chars[read] == ch:
                read += 1
                count += 1

            # write the character
            chars[write] = ch
            write += 1

            # write the count digits if > 1
            if count > 1:
                for d in str(count):      # handles multi-digit counts: 12 -> '1','2'
                    chars[write] = d
                    write += 1

        return write


# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         inputarr=[]
#         i=0
#         while i < len(chars):
#             c=chars.count(chars[i])
    
#             if c==1:
#                 inputarr.append(chars[i])
#             elif c>1 and c<10:
#                 inputarr.extend([chars[i],c])  
#             elif c>10:
#                 a, b = map(int, str(c))
#                 inputarr.extend([chars[i], a, b])
#             i+=c
        
#         return(len(inputarr))

        