
struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
     struct TreeNode* splitTree(int* preorder_index, int ileft, int iright) {
        if (ileft > iright) {
            return NULL;
        }
        
        int rval = preorder[(*preorder_index)++];
        struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        root->val = rval;
        root->left = NULL;
        root->right = NULL;
        
        int imid;
        for (imid = ileft; imid <= iright; imid++) {
            if (inorder[imid] == rval) {
                break;
            }
        }
        
        root->left = splitTree(preorder_index, ileft, imid - 1);
        root->right = splitTree(preorder_index, imid + 1, iright);
        
        return root;
    }
    
  
    int preorder_index = 0;
    
    return splitTree(&preorder_index, 0, inorderSize - 1);
}


void inorderTraversal(struct TreeNode* node) {
    if (node) {
        inorderTraversal(node->left);
        printf("%d ", node->val);
        inorderTraversal(node->right);
    }
}
