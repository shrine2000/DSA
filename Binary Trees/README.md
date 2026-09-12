https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/

https://leetcode.com/discuss/study-guide/1820334/Become-Master-in-Tree

* Inorder (Left, Root, Right) 
* Preorder (Root, Left, Right)
* Postorder (Left, Right, Root)


[Tree of Space – Locking and Unlocking N-Ary Tree](https://www.geeksforgeeks.org/tree-of-space-locking-and-unlocking-n-ary-tree/)

https://leetcode.com/discuss/study-guide/2879240/lessUPDATEDgreater-TREE-QUESTION-PATTERN-2024-oror-TREE-STUDY-GUIDE

https://leetcode.com/discuss/study-guide/3614433/Tree-oror-Binary-Tree-Binary-Search-Tree-oror-Concepts-with-all-curated-problems

https://leetcode.com/tag/tree/discuss/1337373/Tree-question-pattern-oror2021-placement

```

Maximum Depth        -> return height                  -> return 1 + max(left, right)

Diameter             -> left_height + right_height    -> diameter = max(diameter, left + right)

Balanced Tree        -> height + balance check        -> abs(left - right) <= 1

Validate BST         -> propagate (low, high)         -> low < node.val < high

LCA Binary Tree      -> find p/q in both subtrees     -> if left and right: return node

LCA BST              -> use ordering property         -> if p,q < root go left; if p,q > root go right

Level Order          -> BFS queue                     -> for _ in range(len(queue))

Same Tree            -> compare recursively           -> p.val == q.val and left and right

Invert Tree          -> swap children                 -> node.left, node.right = node.right, node.left

Kth Smallest BST     -> inorder traversal             -> inorder => sorted order

Search BST           -> BST navigation                -> root = root.left/right based on target

Min Depth            -> shortest root-to-leaf path    -> leaf => return 1

Path Sum             -> DFS with remaining target     -> remaining -= node.val

Subtree of Tree      -> Same Tree + DFS               -> isSame(root, subRoot)

Serialize Tree       -> preserve structure            -> preorder + "#" for nulls

Construct Tree       -> traversal reconstruction      -> root = preorder[0]

Max Path Sum         -> left gain + right gain        -> ans = max(ans, node.val + left + right)

Count Good Nodes     -> carry max_so_far              -> if node.val >= max_so_far

Right Side View      -> BFS / DFS right-first         -> first node seen at each level

Zigzag Level Order   -> level order traversal         -> reverse every alternate level


```
