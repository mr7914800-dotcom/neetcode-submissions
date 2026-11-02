class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word=strs[0]
        lcp=''
        for i,c in enumerate(first_word):
            check_all=True
            for word in strs:
                if i>=len(word) or word[i]!=c:
                    check_all=False
            if check_all==False:
                return lcp
            else:
                lcp+=c
        return lcp




             