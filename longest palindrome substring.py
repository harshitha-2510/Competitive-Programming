class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp=''
        dp=[[0]*len(str) for _ in range(len(str))]
        print(dp)
        for i in range(len(str)):
            dp[i][j]=True
            lp=str[i]
        for i in range(len(str)-1,-1,-1):
            for j in range(i+1,len(str)):
                print(i,j)
                if str[i]==str[j]:
                    if j-i==1 or dp[i+1][j-1] is True:
                        dp[i][j]=True
                        if len(lp)<len(str[i:j+1]):
                            lp=str[i:j+1]
        return lp
