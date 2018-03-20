def checkBST(root):
    return test(root,float('-inf'),float('+inf'))

def test(node, min, max):
    if node == None:
        return True
    elif node.data <= min or node.data >= max:
        return False
    return test(node.left, min, node.data) and test(node.right, node.data, max)
