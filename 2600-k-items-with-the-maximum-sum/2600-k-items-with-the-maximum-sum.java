class Solution {
    public int kItemsWithMaximumSum(int ones, int zeros, int negOnes, int k) {
            int sum = 0;
            // Pick items one by one until k items are picked
            while(k-- > 0){
                if(ones > 0){
                    // Pick an item with "1" written on it if available
                    sum++;
                    ones--;
                }else if(zeros > 0){
                    // Pick an item with "0" written on it if available
                    zeros--;
                }else{
                    // Pick an item with "-1" written on it if available
                    sum--;
                    negOnes--;
                }
            }
            return sum;
        }
}