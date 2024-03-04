#include <vector>

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
    void search(TreeNode* node, int maximum_value, std::vector<TreeNode*>& solution) {
        if (node == nullptr)
            return;

        if (node->val >= maximum_value) {
            solution.push_back(node);
        }

        int new_maximum = std::max(maximum_value, node->val);

        search(node->left, new_maximum, solution);
        search(node->right, new_maximum, solution);
    }

    int goodNodes(TreeNode* root) {
        auto solution = std::vector<TreeNode*>();
        int lower_limit = -(1 << 16);
        search(root, lower_limit, solution);
        return solution.size();
    }
};