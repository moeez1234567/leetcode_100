# given a head of linked list and the number integer removes the nodes of the list where Node.val == val means that removes those nodes which is equals to the given value
#  and return new removed linked list

# for example input 6->4->7->3->2->3 , int = 3 
# output = 3->4->7->2 (because when we removing the 3 which is given input with the linked list then the remaing number in linked list is that)


class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 




def remove_elements_linkedlist(head , num):
    current = head 
    pas = 0 
    linke_l = []
    print(current.val)
    print(head.val)
    print(current.next.val)
    while current:
        if current.val == num:
            pas = current.val 
        else:
            linke_l.append(current.val)
        
        current = current.next
        
    return linke_l



def list_linkedlist(link_l : list):
    # i = 0
    # while (i < len(link_l)):
        h = LinkedList(link_l[0])
        curr = h 
        for j in link_l[1:]:
            curr.next = LinkedList(j)
            curr = curr.next  
        return h.next

        


def print_list(head):
    while head:
        print(head.val, end="")
        if head.next:
            print(end="->")
        head = head.next 

    return head


head = LinkedList(3)
head.next = LinkedList(5) 
head.next.next = LinkedList(8)
head.next.next.next = LinkedList(12)
head.next.next.next.next = LinkedList(3)


num = 3





r_e_l = remove_elements_linkedlist(head, num)
ll = list_linkedlist(r_e_l)
p = print_list(ll)
print(p)



# ANOTHER WAY TO DO THAT 
class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 




def remove_node_in_num(head, num):
    dummy = LinkedList(-1)
    dummy.next = head 
    current = dummy
    while current.next:
        if current.next.val == num:
            current.next = current.next.next 
        else:
            current = current.next 

        
        

    return dummy.next 



def pprint(linked_list):
    ll = ""
    while linked_list:
        ll += str(linked_list.val) + "->"
        # print(ll)
        linked_list = linked_list.next 

    return ll



head = LinkedList(1)
head.next = LinkedList(12)
head.next.next = LinkedList(6)
head.next.next.next = LinkedList(12)

num = 12

rnin = remove_node_in_num(head, num)
p = pprint(rnin)
print(p)