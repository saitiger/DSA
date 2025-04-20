class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def mergeTwoLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data < head2.data:
        result = head1
        result.bottom = mergeTwoLists(head1.bottom, head2)
    else:
        result = head2
        result.bottom = mergeTwoLists(head1, head2.bottom)

    return result

def flatten(head):
    if head is None:
        return head

    temp = flatten(head.next)

    return mergeTwoLists(head, temp)
