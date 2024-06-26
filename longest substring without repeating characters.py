class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=[None]*128
        left=right=0
        res=0
        while right<len(s):
            r=s[right]
            index=chars[ord(r)]
            if index!=None and index>=left and index<right:
                left=index+1
            res=max(res,right-left+1)
            chars[ord(r)]=right
            right+=1
        return res
