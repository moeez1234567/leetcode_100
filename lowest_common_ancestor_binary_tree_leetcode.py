# given a binary tree and 2 integers which is the nodes in the tree p and q tells the anseptors of this nodes make a pair and return the lowest node val 
# for example input = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# output = 6 (because the 2 and 8 are the only one and same anseptors)


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 


def lowest_common_anseptor(tree : TreeNode, p:int,q:int): 
    def solution(tree, p,q):
        if tree.val == p or tree.val == q:
            return None 
        

        return solution(tree.left) and solution(tree.right) 
    
    return solution(tree,p,q)
    




tree = TreeNode(4)
tree.left = TreeNode(6)
tree.right = TreeNode(8)


tree.left.left = TreeNode(10)
tree.left.right = TreeNode(12)

tree.right.left = TreeNode(14)
tree.right.right = TreeNode(16)



p = TreeNode(10)
q = TreeNode(14)
lca = lowest_common_anseptor(tree, p, q)
print(lca)
