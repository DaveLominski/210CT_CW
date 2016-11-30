class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None



def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)


def in_order(tree):
    s = []                              #initializing an empty stack

    while True:
        if tree != None:                #if tree does not equal None
            s.append(tree)              #add the tree value to the stack
            tree = tree.left            #move to the left value
        else:                           #if there is nothing to the left of the tree value
            if len(s) > 0:              #if length of s is more than 0
                tree = s.pop()          # pop from the stack
                print(tree.value)       #print the tree value
                tree = tree.right       #move to the right of the tree value

            else:
                return False


if __name__ == '__main__':

    t=tree_insert(None,6);
    tree_insert(t,10)
    tree_insert(t,5)
    tree_insert(t,2)
    tree_insert(t,3)
    tree_insert(t,4)
    tree_insert(t,11)
    in_order(t)
