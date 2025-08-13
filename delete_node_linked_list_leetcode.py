# given a node in the linked list , delete this node in the linked list and there are no access to the other nodes in the linked list, the node which is deleted is not the last in the list 
# means given node which can delete is not the tail of the liked_list 


class Linked_list:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 


def delete_node(d):
    node = d 
    node.val = node.next.val 
    node.next = node.next.next
    print(node.val)
    return node



def pprint(nodes):
    while nodes:
        print(nodes.val, "->")
        nodes = nodes.next 

    



linked = Linked_list(4)
linked.next = Linked_list(8)
linked.next.next = Linked_list(12)
linked.next.next.next = Linked_list(16)


d = linked.next.next 


dn = delete_node(d)
pp = pprint(dn)
