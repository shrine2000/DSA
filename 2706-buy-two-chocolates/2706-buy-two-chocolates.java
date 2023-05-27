class Solution {
    public int buyChoco(int[] prices, int money) {
        int ans = -1,n = prices.length;
        for(int i = 0;i < n;i++){
            for(int j = i + 1;j < n;j++){
                if(prices[i] + prices[j] <= money){
                    ans = Math.max(ans,money - prices[i] - prices[j]);
                }
            }
        }
        return ans == -1 ? money : ans;
    }
}