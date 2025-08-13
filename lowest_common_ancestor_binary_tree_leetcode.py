# given a binary tree and 2 integers which is the nodes in the tree p and q tells the anseptors of this nodes make a pair and return the lowest node val 
# for example input = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# output = 6 (because the 2 and 8 are the only one and same anseptors)
# note right side node in the tree have always high values and left side always smaller , return the closet common anseptor between the p and q



class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 


def lowest_common_anseptor(tree : TreeNode, p:int,q:int): 
    node = tree  
    while (node != None):
        if p.val > node.val and q.val > node.val:
            node = node.right 
        elif p.val < node.val and q.val < node.val:
            node = node.left 
        
        else:
            return node
    




tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(8)


tree.left.left = TreeNode(0)
tree.left.right = TreeNode(1)

tree.right.left = TreeNode(14)
tree.right.right = TreeNode(16)



p = tree.left
q = tree.right
lca = lowest_common_anseptor(tree, p, q)
print(lca)



# another way to do that 
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 


def solution(tree,p,q):
    def closest_anseptor(tree,p,q):
        node = tree 
        if node == None:
            return None 
        
        if p.val > tree.val and q.val > tree.val:
            return closest_anseptor(tree.right,p,q) 
        elif p.val < tree.val and q.val < tree.val:
            return closest_anseptor(tree.left,p,q)
        else:
            return node 
        
    return closest_anseptor(tree,p,q)





tree = TreeNode(5)
tree.left = TreeNode(2)
tree.right = TreeNode(8)

tree.left.left = TreeNode(0)
tree.left.right = TreeNode(0)

tree.right.left = TreeNode(12)
tree.right.right = TreeNode(17) 

p = tree.right.left
q = tree.right



s = solution(tree,p,q)
print(s)