class BinaryTree:
    """
    
    >>> BinaryTree.delete(self,2)
     14
     30
     100
     130
    
    
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # def PrintTree(self):
    #     print(self.data)

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # def remove(self, data):
    #     if self.data == data:
    #         return self.data
    #     print(data)
                
    def _findMin(self, parent):

        """ return the minimum node in the current tree and its parent """

        # we use an ugly trick: the parent node is passed in as an argument
        # so that eventually when the leftmost child is reached, the
        # call can return both the parent to the successor and the successor

        if self.left:
            return self.left._findMin(self)
        else:
            return [parent, self]
    #Deletes node
    def delete(self, data):
        """ delete the node with the given key and return the
        root node of the tree """

        if self.data == data:
            # found the node we need to delete

            if self.right and self.left:

                # get the successor node and its parent
                [psucc, succ] = self.right._findMin(self)

                # splice out the successor
                # (we need the parent to do this)

                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right

                # reset the left and right children of the successor

                succ.left = self.left
                succ.right = self.right

                return succ

            else:
                # "easier" case
                if self.left:
                    return self.left  # promote the left subtree
                else:
                    return self.right  # promote the right subtree
        else:
            if self.data > data:  # key should be in the left subtree
                if self.left:
                    self.left = self.left.delete(data)
                # else the key is not in the tree

            else:  # key should be in the right subtree
                if self.right:
                    self.right = self.right.delete(data)

        return self    


    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
    

# Use the insert method to add nodes

values = None
root = BinaryTree(values)
root.insert(30)
root.insert(14)
root.insert(2)
root.insert(100)
root.insert(130)


root.delete(2)

root.PrintTree()
