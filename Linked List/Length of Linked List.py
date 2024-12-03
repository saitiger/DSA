class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
def length_of_linked_list(head):
    cnt = 0
    temp = head
    while temp is not None:
        temp = temp.next
        cnt += 1
    return cnt
