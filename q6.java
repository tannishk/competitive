//Function to check whether a tree is a complete binary tree.
// class Node {
//     int key;
//     Node left;
//     Node right;
//
//     public Node(int item) {
//         this.key = item;
//         this.left = this.right = null;
//     }
// }

boolean isCompleteBinaryTree(Node root) {

    if(root == null) //empty tree condition
        return true;

    if(root.left == null && root.right == null) //if both left and right are null then true.
        return true;

    if(root.left != null && root.right != null) //check in subtrees.
        return isCompleteBinaryTree(root.left) && isCompleteBinaryTree(root.right);
    return false; //if the previous conditions fail.
}
