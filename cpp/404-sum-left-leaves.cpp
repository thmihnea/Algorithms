struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        bool left_leaf = isLeaf(root->left);
        return left_leaf ? 
            root->left->val + sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right) :
            sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
    }

    bool isLeaf(TreeNode* node) {
        if (node == nullptr) {
            return false;
        }

        if (node->left == nullptr && node->right == nullptr) {
            return true;
        }

        return false;
    }
};