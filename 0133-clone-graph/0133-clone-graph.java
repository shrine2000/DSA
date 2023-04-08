/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node originalNode) {
        if(originalNode == null) {
            return null;
        }
        
        Queue<Node> bfsQueue = new ArrayDeque<>(Arrays.asList(originalNode));
        Map<Node, Node> originalToCloneMap = new HashMap<>();
        originalToCloneMap.put(originalNode, new Node(originalNode.val));
        
        while(!bfsQueue.isEmpty()){
            Node currentNode = bfsQueue.poll();
            Node clonedNode = originalToCloneMap.get(currentNode);
            
            for(Node originalNeighbor : currentNode.neighbors) {
                if(!originalToCloneMap.containsKey(originalNeighbor)) {
                    Node clonedNeighbor = new Node(originalNeighbor.val);
                    originalToCloneMap.put(originalNeighbor, clonedNeighbor);
                    bfsQueue.offer(originalNeighbor);
                }
                clonedNode.neighbors.add(originalToCloneMap.get(originalNeighbor));
            }
        }
        
        return originalToCloneMap.get(originalNode);
    }
}
