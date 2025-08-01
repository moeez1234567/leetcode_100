# given the head of two singly linked-lists return the point in which this boyh list are intersetcs with the each other and if its not intersets with each other return None 
# for example input  listA = [1,9,1,2,4] , listB = [3,2,4]
# output = 2 (because this two list a and b are intersets with the each other at the node 2)
# 
# input, listA = [3,4,5,6], listB = [7,8,3,1]
# output = Null (because this 2 listy are not same or not interach with each othewr at any point)



class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 

def check_linklist_intersects(a, b):
    if not a or not b:
        return None 
    

    ha = a 
    hb = b 

    while (ha is not hb):
        ha = ha.next if ha else b
        hb = hb.next if hb else a 

    return hb.val 



# def show_list(ha):
#     while ha:
#         print(ha.val, end = "->")
#         ha = ha.next 

    


shared = LinkedList(2)
shared.next = LinkedList(4)


a = LinkedList(1)
a.next = LinkedList(9)
a.next.next = LinkedList(1)
a.next.next.next = shared 



b = LinkedList(3)
b.next = shared 



c = check_linklist_intersects(a,b)
print(c)




# another approch to do this 

class Linked_List:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 


def check_interseps(l1, l2):
    set_for_b = set()
    print(set_for_b)

    while l1 is not None:
        set_for_b.add(l1)
        l1 = l1.next 
    
    while l2 is not None:
        if l2 in set_for_b:
            return l2 
        
        l2 = l2.next 
    
    return None


linked = Linked_List(1)
linked.next = Linked_List(5)



l1 = Linked_List(3)
l1.next = Linked_List(5)
l1.next.next = linked 


l2 = linked 

def print_interseps_node(l2):
    while l2:
        print(l2.val, end="->")
        l2 = l2.next
    else:
        None


ci = check_interseps(l1, l2)
print_interseps_node(ci)

