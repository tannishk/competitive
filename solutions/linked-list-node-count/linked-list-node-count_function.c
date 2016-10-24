int getCount(struct node* head)
{
    int count = 0;  // Initializing count to be zero initially
    struct node* current = head;  // Initializing current node to head
    while (current != NULL)
    {
        count++;    //Incrementing count
        current = current->next;  //traversing next of the current node
    }
    return count; // returning total count
}
