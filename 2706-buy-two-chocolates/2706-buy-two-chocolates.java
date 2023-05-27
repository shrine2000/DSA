class Solution {
    public int buyChoco(int[] prices, int money) {
        Arrays.sort(prices);
        int lol = prices[0]+prices[1];
        if(money < lol)
            return money;
        return money-lol;
    }
}