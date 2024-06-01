/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isBST(struct TreeNode* node, long minVal, long maxVal) {
    if (node == NULL) {
        return true;
    }
    if (node->val <= minVal || node->val >= maxVal) {
        return false;
    }
    return isBST(node->left, minVal, node->val) && isBST(node->right, node->val, maxVal);
}

bool isValidBST(struct TreeNode* root) {
    return isBST(root, LONG_MIN, LONG_MAX);
}