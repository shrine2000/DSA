class Solution {
      public int longestSemiRepetitiveSubstring(String s) {
      int ans = 0, c = 0;
      Stack<Character> st = new Stack<>();
      for(int i = 0; i < s.length(); i++) {
        if(st.size() == 0) {
            st.push(s.charAt(i));
        }
        else{
            if(st.peek() == s.charAt(i)) {   // When Semi-R Occurence Found
                if(c == 1) {      // count 1 means already one occurence is exist in stack
                     ans = Math.max(ans,  st.size());
                     int remove = st.remove(0);
                     while(st.get(0) != remove) {   // So remove the elements from left side to remove previous occurence and put the current index character which makes one occurence again
                          remove = st.remove(0);     }
                         st.push(s.charAt(i));
                }
                else if(c == 0) {  // when first occurence encountered which makes count as 1
                   c = 1;
                   st.push(s.charAt(i));
                   ans = Math.max(ans, st.size());
                }
            }
            else{    // until no occurence found take max length
                st.push(s.charAt(i));
                ans = Math.max(ans, st.size());     }    }
    }
    ans = Math.max(ans,  st.size());
    return ans;
 }
}