class Solution {
    public int distMoney(int money, int children) {
         // Check if there is enough money to give each child at least 1 dollar
        if (money < children) return -1;

        // Check if the money can be evenly divided among the children and each child can receive exactly 8 dollars
        if (money % 8 == 0 && money / 8 == children) return children;

        // Give money to as many children as possible, subtracting 8 dollars from the total money for each child
        int i = 0;
        for (i = 0; i < children && money - children + i >= 0; i++) {
            money = money - 8;
        }

        // If there is 4 dollars left and all children have been given money, take 8 dollars from two of the children
        if (money == -4 && i == children) return i - 2;

        // If not all children have been given money, add 8 dollars back to the total money until there is enough to give money to all children
        while (money - children + i < 0) {
            money += 8;
            i--;
        }

        // Check if all children have been given money and if so, return the number of children who received exactly 8 dollars
        // If not all children have been given money, return the number of children who did receive money
        return money > 0 && i == children ? i - 1 : i;

    }
}