import java.util.*;

class Solution {
    public int minimumCardPickup(int[] cards) {
        // Map to keep track of the last index where each card value appears
        Map<Integer, Integer> lastSeen = new HashMap<>();
        int minPickup = Integer.MAX_VALUE; // Initialize minimum pickup to maximum possible value

        for (int i = 0; i < cards.length; i++) {
            int card = cards[i];
            if (lastSeen.containsKey(card)) {
                // If we have already seen this card value before, calculate the number of cards picked up
                // between the last and current occurrences of the card value
                int pickup = i - lastSeen.get(card) + 1;
                minPickup = Math.min(minPickup, pickup);
            }
            // Update the last index where the card value appears
            lastSeen.put(card, i);
        }

        // If we didn't find a matching pair, return -1
        if (minPickup == Integer.MAX_VALUE) {
            return -1;
        }

        return minPickup;
    }
}
