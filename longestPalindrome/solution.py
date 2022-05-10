class Solution:
    def longestPalindrome(self, s: str) -> str:
        S = []
        for i in s:
            S.append("#")
            S.append(i)
        S.append("#")
        Lens = len(S)
        i,j=0,0
        R = [0]*Lens
        maxs = 0
        while i<Lens:
            while i-j>=0 and i+j<Lens and S[i-j]==S[i+j]:
                j+=1
            R[i] = j
            if j >maxs:
                maxs=j
                index = i
            k = 1
            while i-k>=0 and i+k<Lens and R[i-k]+k <j:
                R[i+k] = R[i-k]
                k+=1
                
            i+=k
            j-=k
        
        left = (index-maxs+1)>>1
        right = maxs-1
        return s[left:left+right]
