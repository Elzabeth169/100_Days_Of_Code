class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        letters = []
        for i in range(length):
            letters.append(word1[i])
            letters.append(word2[i])

        if i < len(word1):
            for i in range(length, len(word1)):
                letters.append(word1[i])

        if i < len(word2):
            for i in range(length, len(word2)):
                letters.append(word2[i])

        return "".join(letters)

# merged = [a + b for a, b in zip(word1, word2)]


#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         if len(word1)<len(word2):n=len(word1)
#         else:n=len(word2)
#         res=""
#         for i in range(0,n):
#             res=res+word1[i]+word2[i]
#         if len(word1)>n:
#             for i in range(n,len(word1)):
#                 res=res+word1[i]
#         elif(len(word2)>n):
#             for i in range(n,len(word2)):
#                 res=res+word2[i]
#         return res