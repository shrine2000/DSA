#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def characterReplacement(self, S, K):
        # Code here
        freq = [0] * 26
        start = end = max_freq = result = 0

        for end in range(len(S)):
            freq[ord(S[end]) - ord('A')] += 1
            max_freq = max(max_freq, freq[ord(S[end]) - ord('A')])

            if end - start + 1 - max_freq > K:
                freq[ord(S[start]) - ord('A')] -= 1
                start += 1

            result = max(result, end - start + 1)

        return result
        
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range(t):
        S = input().strip()
        K = int(input())
        ob = Solution()
        res = ob.characterReplacement(S, K)
        print(res)
# } Driver Code Ends