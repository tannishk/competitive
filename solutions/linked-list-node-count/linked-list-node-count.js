// create a singly linked list
function SLL(){
	this.head = null;
}

// create a new node
function Node(val){
	this.val = val;
	this.next = null;
}

// function to add nodes to the front of a singly linked list
// we'll need this to create a list for testing
function addNode(SLL, val){
	var someNode = new Node(val);
	someNode.next = SLL.head;
	SLL.head = someNode;
	return this;
}

// get a count of the nodes in a linked list
function getCount(SLL){
	var count = 0;
	var current = SLL.head;
	while(current){
		count++;
		current = current.next;
	}
	return count;
}


// test cases creating a new list, adding nodes, and getting count of nodes
var mySLL = new SLL();
console.log(getCount(mySLL)); // should print 0
addNode(mySLL,2);
console.log(getCount(mySLL)); // should print 1
addNode(mySLL,4);
console.log(getCount(mySLL)); // should print 2