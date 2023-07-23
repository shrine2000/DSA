class Solution {
    private char lower(int[] freq) {
        for (int i = 0; i < 26; i++) {
            if (freq[i] != 0) {
                return (char) ('a' + i);
            }
        }
        return 'a';
    }

    public String robotWithString(String s) {
        int[] freq = new int[26];

        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        StringBuilder ans = new StringBuilder();
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            stack.push(c);
            freq[c - 'a']--;

            while (!stack.isEmpty() && stack.peek() <= lower(freq)) {
                char x = stack.peek();
                ans.append(x);
                stack.pop();
            }
        }

        while (!stack.isEmpty()) {
            ans.append(stack.peek());
            stack.pop();
        }

        return ans.toString();
    }
}
