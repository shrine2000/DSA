class Solution {
    public int[] diStringMatch(String s) {
        int n = s.length();
        int[] arr = new int[n+1];
        int start = 0;
        int end = n;
        char[] ch = s.toCharArray();
        for(int i=0; i<n; i++) {
            if(ch[i] == 'I') {
                arr[i] = start++;
            } else {
                arr[i] = end--;
            }
        }
        arr[n] = start;
        return arr;
    }
}