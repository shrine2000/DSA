class Solution {
    public int partitionString(String s) {
        int charMap = 0;
        int count = 1;
        for(char c : s.toCharArray()) {
            if((charMap & (1 << c)) != 0) {
                count++;
                charMap = 0;
            }
            charMap ^= (1 << c);
        }
        return count;
    }

}