class Solution {
    public boolean areNumbersAscending(String s) {
        String[] tokens = s.split(" ");
        int previousNumber = 0;

        for (String token : tokens) {
            if (Character.isDigit(token.charAt(0))) {
                int currentNumber = Integer.parseInt(token);
                if (currentNumber <= previousNumber) {
                    return false;
                } else {
                    previousNumber = currentNumber;
                }
            }
        }

        return true;
    }
}
