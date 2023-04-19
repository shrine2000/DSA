class Solution {
    public boolean areNumbersAscending(String s) {
        int previousNumber = Integer.MIN_VALUE;
        for (int i = 0; i < s.length(); i++) {
            int currentChar = s.charAt(i);
            int currentNumber = 0;
            int j = i;
            if (currentChar >= 48 && currentChar <= 57) {
                while (currentChar >= 48 && currentChar <= 57 && i < s.length()) {
                    currentNumber = currentNumber * 10 + (currentChar - 48);
                    i++;
                    if (i == s.length()) {
                        break;
                    }
                    currentChar = s.charAt(i);
                }
                if (currentNumber <= previousNumber) {
                    return false;
                }
                previousNumber = currentNumber;
            }
        }
        return true;
    }
}
