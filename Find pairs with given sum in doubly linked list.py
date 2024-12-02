class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) ->List[List[int]]:
        # initializing two iterators ptr1 and ptr2 at the head of the linked list
        ptr1 = head
        ptr2 = head

        # moving ptr2 to the last element of the linked list
        while (ptr2.next):
            ptr2 = ptr2.next
        
        # initializing an empty list to store the pairs with the given sum
        res = []
        
        # iterating until ptr1 and ptr2 meet or ptr2's previous node becomes ptr1
        while (ptr1 != ptr2 and ptr2.next != ptr1):
            
            # calculating the sum of the current pair of nodes
            sum = ptr1.data + ptr2.data

            # if the sum is equal to the target value,
            # add the pair of nodes to the result list and move ptr1 and ptr2
            if (sum == target):
                res.append([ptr1.data, ptr2.data])
                ptr1 = ptr1.next
                ptr2 = ptr2.prev
            
            # if the sum is less than the target value, move ptr1 to the next node
            elif (sum < target):
                ptr1 = ptr1.next
            
            # if the sum is greater than the target value, move ptr2 to the previous node
            else:
                ptr2 = ptr2.prev
        
        # return the list of pairs with the given sum
        return res
