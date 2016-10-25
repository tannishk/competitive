package main

import "fmt"

// Node struct used to represent a Node
type Node struct {
	Data int
	Next *Node
}

// HasNext determines if there is another Node in the list
func (n *Node) HasNext() bool {
	return n.Next != nil
}

func getLinkedListLength(n *Node) int {
	if !n.HasNext() {
		return 0
	}
	return 1 + getLinkedListLength(n.Next)

}

func main() {
	node := &Node{
		Data: 1, Next: &Node{
			Data: 2, Next: &Node{
				Data: 3, Next: &Node{},
			},
		},
	}
	fmt.Printf("%d\n", getLinkedListLength(node))
}
