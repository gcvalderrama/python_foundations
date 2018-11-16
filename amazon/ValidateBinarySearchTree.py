class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_bst(node, lower_limit=None, upper_limit=None):
    if lower_limit and node.val <= lower_limit:
        return False
    if upper_limit and node.val >= upper_limit:
        return False
    is_left_bt = True
    is_right_bt = True
    if node.left:
        is_left_bt = is_bst(node.left, lower_limit, node.val)
    if is_left_bt and node.right:
        is_right_bt = is_bst(node.right, node.val, upper_limit)
    return is_left_bt and is_right_bt



if __name__ == '__main__':

    print([1,2,3,4][:])

    root = TreeNode(1)
    root.left = TreeNode(1)
    is_bst(root)


