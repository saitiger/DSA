def kAltReverse(head, k):
    temp = head
    prevLast = None
    reverse = True # Toggles between on and off to alternate reversal

    while temp is not None:
        if reverse:  # Reverse the current group of k nodes
            segmentHead = temp
            prev = None
            for _ in range(k):
                if temp is None:
                    break
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            if prevLast is None:
                head = prev
            else:
                prevLast.next = prev
            prevLast = segmentHead
        else:  # Skip the next group of k nodes
            prevLast.next = temp
            for _ in range(k):
                if temp is None:
                    break
                prevLast = temp
                temp = temp.next
        reverse = not reverse # Switching the flag modes 
    return head
