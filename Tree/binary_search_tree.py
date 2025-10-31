from logging import raiseExceptions

class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, val) -> None:
        # try:
            if (self.data == val):
                print("Duplicate Entry is not allowed in BST")

            if val < self.data:
                if self.left:
                    self.left.add_child(val)
                else:
                    self.left = BinarySearchTreeNode(val)
            
            if val > self.data:
                if self.right:
                    self.right.add_child(val)
                else:
                    self.right = BinarySearchTreeNode(val)

        # except Exception:
        #     # Print the full traceback to the console
        #     print("--- Full Traceback ---")
        #     traceback.print_exc()
        #     print("--- End Traceback ---")



    def inorder_traversal(self):     
        elements = []   
        #traverse left subtree
        if self.left:
            elements += self.left.inorder_traversal()

        #print root data
        elements.append(self.data)

        #traverse right subtree
        if self.right:
            elements += self.right.inorder_traversal()

        return elements


        

def build_binary_tree(numbers):
    root = BinarySearchTreeNode(numbers[0])
    for i in range(1, len(numbers)):
        root.add_child(numbers[i])
    return root

if __name__ == '__main__':
    numbers = [4, 17, 8, 22, 56, 93, 1, 32, 44]
    
    root = build_binary_tree(numbers)


    print(root.inorder_traversal())