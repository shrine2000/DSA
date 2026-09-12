# Binary Trees

### Resources / Guides

* [Find the Maximum Depth or Height of a Tree](https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/)
* [Become Master in Tree](https://leetcode.com/discuss/study-guide/1820334/Become-Master-in-Tree)
* [Tree of Space – Locking and Unlocking N-Ary Tree](https://www.geeksforgeeks.org/tree-of-space-locking-and-unlocking-n-ary-tree/)
* [\<UPDATED\> TREE QUESTION PATTERN 2024 || TREE STUDY GUIDE](https://leetcode.com/discuss/study-guide/2879240/lessUPDATEDgreater-TREE-QUESTION-PATTERN-2024-oror-TREE-STUDY-GUIDE)
* [Tree || Binary Tree, Binary Search Tree || Concepts with all curated problems](https://leetcode.com/discuss/study-guide/3614433/Tree-oror-Binary-Tree-Binary-Search-Tree-oror-Concepts-with-all-curated-problems)
* [Tree question pattern || 2021 placement](https://leetcode.com/tag/tree/discuss/1337373/Tree-question-pattern-oror2021-placement)

### Traversals

* Inorder (Left, Root, Right) 
* Preorder (Root, Left, Right)
* Postorder (Left, Right, Root)

### Common Patterns

| Pattern | Concept | Snippet |
|---------|---------|---------|
| [Maximum Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | return height | `return 1 + max(left, right)` |
| [Diameter](https://leetcode.com/problems/diameter-of-binary-tree/) | left_height + right_height | `diameter = max(diameter, left + right)` |
| [Balanced Tree](https://leetcode.com/problems/balanced-binary-tree/) | height + balance check | `abs(left - right) <= 1` |
| [Validate BST](https://leetcode.com/problems/validate-binary-search-tree/) | propagate (low, high) | `low < node.val < high` |
| [LCA Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | find p/q in both subtrees | `if left and right: return node` |
| [LCA BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | use ordering property | `if p,q < root go left; if p,q > root go right` |
| [Level Order](https://leetcode.com/problems/binary-tree-level-order-traversal/) | BFS queue | `for _ in range(len(queue))` |
| [Same Tree](https://leetcode.com/problems/same-tree/) | compare recursively | `p.val == q.val and left and right` |
| [Invert Tree](https://leetcode.com/problems/invert-binary-tree/) | swap children | `node.left, node.right = node.right, node.left` |
| [Kth Smallest BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | inorder traversal | `inorder => sorted order` |
| [Search BST](https://leetcode.com/problems/search-in-a-binary-search-tree/) | BST navigation | `root = root.left/right based on target` |
| [Min Depth](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | shortest root-to-leaf path | `leaf => return 1` |
| [Path Sum](https://leetcode.com/problems/path-sum/) | DFS with remaining target | `remaining -= node.val` |
| [Subtree of Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Same Tree + DFS | `isSame(root, subRoot)` |
| [Serialize Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | preserve structure | `preorder + "#" for nulls` |
| [Construct Tree](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | traversal reconstruction | `root = preorder[0]` |
| [Max Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | left gain + right gain | `ans = max(ans, node.val + left + right)` |
| [Count Good Nodes](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | carry max_so_far | `if node.val >= max_so_far` |
| [Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | BFS / DFS right-first | `first node seen at each level` |
| [Zigzag Level Order](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | level order traversal | `reverse every alternate level` |
