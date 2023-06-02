class Solution {
    
    // TODO - not covered
    // link - https://leetcode.com/problems/rearrange-words-in-a-sentence/discuss/3320102/Using-Priority-Queue
    
    
  public class Word implements Comparable<Word> {
        int index;
        String word;

        Word(int index, String word) {
            this.index = index;
            this.word = word;
        }

        public int compareTo(Word w) {
            if (w.word.length() == this.word.length()) {
                return this.index - w.index;
            }
            return this.word.length() - w.word.length();
        }
    }
    public String arrangeWords(String text) {
        String answer = "";
        String str[] = text.split(" ");
        PriorityQueue<Word> pq = new PriorityQueue<>();
        for (int i=0;i<str.length;i++) 
        pq.add(new Word(i, str[i]));

        
        while (!pq.isEmpty()) {
            Word w = pq.remove();
            if (answer.length() == 0) {
                char c = w.word.charAt(0);
                int val = (int) (c);
                if (val > 90) {
                    int newVal = val - 32;
                    char c1 = (char) newVal;
                    answer += ""+c1+w.word.substring(1);
                } else {
                    answer += w.word;
                }
            } else {
                answer += w.word.toLowerCase();
            }
            if (!pq.isEmpty()) answer += " ";
        }
        return answer;
    }

}