class Solution {
    public int lastStoneWeight(int[] stones) {
        if (stones == null || stones.length == 0) {
            return 0;
        }
        
        if (stones.length == 1) {
            return stones[0];
        }
        
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        for(int stone : stones){
            maxHeap.add(stone);
        }

        while(maxHeap.size() > 1){
            int heaviest = maxHeap.poll();
            int secondHeaviest = maxHeap.poll();
            
            if(heaviest != secondHeaviest) {
                int remaining = heaviest - secondHeaviest;
                maxHeap.add(remaining);
            }
        }
        
        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
    }
}
