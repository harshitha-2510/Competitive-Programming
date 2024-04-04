class TreeNode:
    def __init__(self, value):
        self.val=value
        self.left=None
        self.right=None
def print_leaves(root,result):
    if root:
        print_leaves(root.left, result)
        if not root.left and not root.right:
            result.append(root.val)
        print_leaves(root.right, result)
def print_left_boundary(root, result):
    if root:
        if root.left:
            result.append(root.val)
            print_left_boundary(root.left, result)
        elif root.right:
            result.append(root.val)
            print_left_boundary(root.right, result)
def print_right_boundary(root, result):
     if root:
        if root.right:
            print_right_boundary(root.right, result)
            result.append(root.val)
        elif root.left:
            print_right_boundary(root.left, result)
            result.append(root.val)
def boundary_traversal(root):
    if not root:
        return[]
    result= [root.val]
    print_left_boundary(root.left, result)
    print_leaves(root,result)
    print_right_boundary(root.right, result)
    return result
root=TreeNode(20)
root.left=TreeNode(8)
root.left.left=TreeNode(4)
root.left.right=TreeNode(12)
root.left.right.left=TreeNode(10)
root.left.right.right=TreeNode(14)
root.right=TreeNode(6)
root.right.right=TreeNode(5)
