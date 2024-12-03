def delete_tail(head):
    if head is None or head.next is None:
        return None  # If the list is empty or has only one node, return None

    tail = head
    while tail.next is not None:
        # Traverse to the last node (tail)
        tail = tail.next

    new_tail = tail.back
    new_tail.next = None
    tail.back = None

    # Free memory of the deleted node
    del tail

    return head
