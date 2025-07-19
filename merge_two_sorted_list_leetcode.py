# Merging a 2 sorted list in the asending order for example
# a = [1,5,7] , b = [0 , 6, 7, 8]
# list are given in the ascending order


class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoList(self, l1: LinkedList, l2: LinkedList):
        head = LinkedList()

        tmp1, tmp2, tmp3 = l1, l2, head

        while tmp1 is not None and tmp2 is not None:
            if tmp1.val <= tmp2.val:
                tmp3.next = tmp1
                tmp1 = tmp1.next

            else:
                tmp3.next = tmp2
                tmp2 = tmp2.next

            tmp3 = tmp3.next

        if tmp1 is not None:
            tmp3.next = tmp1
            tmp1 = tmp1.next

        if tmp2 is not None:
            tmp3.next = tmp2
            tmp2 = tmp2.next

        head = head.next
        return head

    


def prepare_linked_list(arr):
    if not arr:
        return None

    head = LinkedList(arr[0])
    current = head

    for val in arr[1:]:
        current.next = LinkedList(val)
        current = current.next

    return head


def print_linked_list(head):
    while head:
        print(head.val, end=">")
        head = head.next
    print(None)


l1 = prepare_linked_list([6, 7, 8])
l2 = prepare_linked_list([6, 7, 8])


s = Solution()

merge = s.mergeTwoList(l1 , l2)
print(print_linked_list(merge))

