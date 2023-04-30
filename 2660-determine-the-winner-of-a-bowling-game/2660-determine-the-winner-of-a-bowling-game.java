public class Solution {
    public int calculateScore(int[] player) {
        int last1 = 0;
        int last2 = 0;
        int sum = 0;

        for (int i = 0; i < player.length; i++) {
            int current = player[i];

            if (last1 == 10 || last2 == 10) {
                sum += current * 2;
            } else {
                sum += current;
            }

            last2 = last1;
            last1 = current;
        }

        return sum;
    }

    public int isWinner(int[] player1, int[] player2) {
        int sum1 = calculateScore(player1);
        int sum2 = calculateScore(player2);

        if (sum1 > sum2) {
            return 1;
        } else if (sum2 > sum1) {
            return 2;
        } else {
            return 0;
        }
    }
}
