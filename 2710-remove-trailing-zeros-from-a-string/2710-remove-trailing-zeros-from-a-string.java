class Solution {
   public String removeTrailingZeros(String num) {
        int index = 0;
        for (int i = num.length() - 1; i >= 0; i--) {
            if (num.charAt(i) == '0') {
                index++;
            } else {
                break;
            }
        }
        
        String result = num.substring(0, num.length() - index);
        return result;
    }
}