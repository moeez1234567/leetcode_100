# given a head of singly linked list, return true if this linked_list is the palindrome (means same on bthe both sides forward and the backword) and false if this linked list is not palindrome 
# for example 1,2,2,1 
# output = True (because if we reverse this then it make 1221 which is same so thats why it is true)


class Linked_List:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 


def link_list(head:Linked_List):
    val = []
    current = head 
    while current:
        val.append(current.val)
        current = current.next 

    

    if val == val[::-1]:
        return True
    else:
        return False





linked = Linked_List(2)
linked.next = Linked_List(5)
linked.next.next = Linked_List(12)
linked.next.next.next = Linked_List(19) 



ll = link_list(linked)
print(ll)




# another way to do that 
class Linked_List:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 



def linked_list(head:Linked_List):
    stack = []
    slow = head 
    fast = head 
    current = head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
    mid = slow 
    while (mid != None):
        stack.append(mid.val)
        mid = mid.next 

    while (len(stack) > 0):
        if stack.pop() != current.val:
            return False
        current = current.next 
         
    return True



head = Linked_List(4)
head.next = Linked_List(2)
head.next.next = Linked_List(2)
head.next.next.next = Linked_List(4) 


l = linked_list(head)
print(l)

