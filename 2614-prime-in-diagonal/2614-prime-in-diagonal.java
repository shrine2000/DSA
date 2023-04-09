class Solution {
     public boolean isPrime(int n){
        if (n <= 1) return false;
        for(int i = 2;i * i <= n;i++) if(n % i == 0) return false;
        return true;
    }
    
    public int diagonalPrime(int[][] nums) {
        int n = nums.length;
        int maxPrime = 0;
        
        // check main diagonal
        for(int i = 0;i < n;i++){
            int num = nums[i][i];
            if(isPrime(num)) maxPrime = Math.max(maxPrime, num);
        }
        
        // check secondary diagonal
        for(int i = 0;i < n;i++){
            int num = nums[i][n - i - 1];
            if(isPrime(num)) maxPrime = Math.max(maxPrime, num);
        }
        
        return maxPrime;
    }

 
}