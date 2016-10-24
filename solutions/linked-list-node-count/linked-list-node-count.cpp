#include <bits/stdc++.h>
using namespace std;

struct ListNode {
	int data;
	ListNode *next;

	ListNode(int val) {
		data=val;
		next=NULL;
	}
};

int count_nodes(ListNode *head) {
	int count = 0;
	while(head!=NULL) {
		head = head->next;
		count++;
	}
	return count;
}

int main() {
	ListNode *head = new ListNode(10);
	assert(count_nodes(head) == 1);

	for(int i=0; i<5; i++) {
		ListNode *newElem = new ListNode(i);
		newElem->next = head;
		head = newElem;
	}
	assert(count_nodes(head) == 6);
	return 0;
}
