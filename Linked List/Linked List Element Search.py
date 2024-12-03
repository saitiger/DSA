class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1
def check_if_present(head, desired_element):
    temp = head

    while temp is not None:
        if temp.data == desired_element:
            return 1  
        temp = temp.next
    return 0  
