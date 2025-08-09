# given a head of binary tree, invert this tree (means change or shift the values of tree from left to right and right to left ) and return their root 

# for example tree 1 head 2 left 3 right change this tree to 1 head 3 left and 2 right and given this head 

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 
        



def solution(tree):
    def invert(tree):
        if tree == None:
            return None
        left_root = invert(tree.left)
        right_root = invert(tree.right)

        tree.left = right_root 
        tree.right = left_root 
        return tree 
    
    return invert(tree)


def pprint(tree):
    if tree:
        print(tree.val)
        pprint(tree.left)
        pprint(tree.right)




tree = TreeNode(2)
tree.left = TreeNode(3)
tree.right = TreeNode(4)

tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7) 



s = solution(tree)

p = pprint(s)
print(p)



# another way to do that
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 




def invert_tree(tree : TreeNode):
    l = []
    l.append(tree)
    while (len(l) != 0):
        node = l.pop(0)
        if node:
            if node.val:
                print(node.val)
            node.left,node.right = node.right,node.left 
            if node.left:
                print(node.left.val)
                l.append(node.left)
            if node.right:    
                l.append(node.right)
                print(node.right.val)
        
    print(l)

    return tree 



# def pprint(l):
#     while l:
#         print(l.val)
#         pprint(l.left)
#         pprint(l.right)


tree = TreeNode(4)
tree.left = TreeNode(6)
tree.right = TreeNode(8)


tree.left.left = TreeNode(10)
tree.left.right = TreeNode(12)

tree.right.left = TreeNode(14)
tree.left.right = TreeNode(16)




i = invert_tree(tree)
pp = pprint(i)
# print(i)