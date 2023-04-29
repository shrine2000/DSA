class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int sum = 0, max = 0;
        
        // Handle edge case where k >= n
        if(k >= n){
            for(int i : cardPoints) sum += i;
            return sum;
        }
        
        // Calculate initial sum of first k elements
        for(int i = 0; i < k; i++){
            sum += cardPoints[i];
        }
        
        // Move sliding window to the right and update max sum
        int ptr = k - 1;
        max = sum;
        int j = n - 1;
        int loop = 0;
        while(loop < k && ptr >=0){
            sum = sum + cardPoints[j] - cardPoints[ptr];
            if(max < sum) max = sum;
            
            ptr--;
            j--;
            loop++;
        }
        
        return max;
        
      
    }
}