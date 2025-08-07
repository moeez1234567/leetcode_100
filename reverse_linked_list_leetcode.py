# given a head of linked list, return the reverse of this linked list 
# for example input =  1->3->5->7 
# ouytput = 7->5->3->1 


class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 


def reverse_linklist(head):
    l = []
    current = head 
    while current:
        l.append(current.val)
        current = current.next 

    val = []

    for i in l[::-1]:
        val.append(i)


    return val

def linked_list(head_reverse):
    head = LinkedList(head_reverse[0])
    current = head
    for curr in head_reverse[1:]:
        current.next = LinkedList(curr)
        current = current.next 

    return head 


def pprint(reverse_linked_list):
    string = ""
    while reverse_linked_list:
        string += str(reverse_linked_list.val) + "->"
        reverse_linked_list = reverse_linked_list.next 


    return string



head = LinkedList(1)
head.next = LinkedList(3)
head.next.next = LinkedList(5)
head.next.next.next = LinkedList(7)   


rl = reverse_linklist(head)
print(rl)
ll = linked_list(rl)
pp = pprint(ll)
print(pp)

