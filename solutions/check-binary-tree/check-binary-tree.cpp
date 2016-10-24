#include <iostream>
#include <algorithm>

struct node{
	node* left;
	node* right;

	node(){
		left = right = NULL;
	}
};

int count_childrens(node* n){
	if(n == NULL) return 0;
	return 1 + count_childrens(n->left) + count_childrens(n->right);
}

int height(node* n){
	if(n == NULL) return 0;
	return 1 + std::max(height(n->left), height(n->right));
}

bool is_complete_tree(node root){
	int h = height(&root);
	int count = count_childrens(&root);

	return count >= (1<<(h-1)) && count < (1<<h);
}

int main(){
	std::string answer[] = {"This is not a complete binary tree\n", "This is a complete binary tree\n"};

	node root;
	root.left = new node;
	root.right = new node;
	root.left->right = new node;

	std::cout<<answer[is_complete_tree(root)];

	root.right->right = new node;
	root.right->right->left = new node;

	std::cout<<answer[is_complete_tree(root)];
}