def convert_arr_to_ll(arr):
    head = Node(arr[0]) # Initializing the node 
    curr = head  # Pointing to head
    for i in range(1, len(arr)):
        temp = Node(arr[i])  # Creating new node every time
        curr.next = temp  # Updating the pointer 
        curr = curr.next  # Moving to the next node
    return head
