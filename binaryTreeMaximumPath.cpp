/**
 * 124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

*/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int max = INT_MIN;
    int childPath,r;
public:
    int helper(TreeNode* root) {
        if (!root) return 0;
        int l = helper(root->left);
        r = helper(root->right);
        childPath = std::max(l,r);
        if (childPath<0) childPath = 0;
        max = std::max(max,l+r+root->val); 
        max = std::max(max,childPath+root->val);
        return childPath+root->val;
    }
    int maxPathSum(TreeNode* root) {
        if (!root) return 0;
        helper(root);
        return max;
    }
};