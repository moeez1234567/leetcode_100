# given a sorted linked list with the duplicates values return the linked list with the remove duplicates and in the sorted form , linked list may be have negative values 

# for example l = [3,4,5,6,6]
# output = [3,4,5,6]


# for example l = [-3,-2,-1,0,0,1,2,2,3]
# output l = [-3,-2,-1,0,1,2,3,]

class Node:
    def __init__(self , val):
        self.val = val
        self.next = None 


def create_linked_list(val):
    if not val:
        return None 
    
    head = Node(val[0])

    current = head 

    for curr in val[1:]:
        current.next = Node(curr)
        current = current.next 

    return head 


def display_linkedlist(head):
    array = []
    current = head
    while current:
        print(current.val, end = "->")
        array.append(current.val)

        current = current.next 

    return head, array




def remove_duplicates_linkedlist(head):
    current = head 

    while  current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next

        else: 
            current = current.next


    return head


create = create_linked_list([-1,-0,1,1,2,2,3])
rd = remove_duplicates_linkedlist(create)
display_linkedlist(rd)
