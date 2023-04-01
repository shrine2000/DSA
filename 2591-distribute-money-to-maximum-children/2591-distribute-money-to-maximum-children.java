class Solution {
    public int distMoney(int money, int children) {
        money = money - children;

        if (money < 0) return -1;

        if (money < 7) return 0;

        int count = money / 7;

        if (count >= children) {
            return children - (money > children * 7 ? 1 : 0);
        }
        if ((money % 7) == 3) {
            return count - (children - count > 1 ? 0 : 1);
        }

        return count;

    }
}