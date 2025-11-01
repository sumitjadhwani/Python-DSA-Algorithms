'''
1. find_min(): finds minimum element in entire binary tree
2. find_max(): finds maximum element in entire binary tree
3. calculate_sum(): calcualtes sum of all elements
4. post_order_traversal(): performs post order traversal of a binary tree
5. pre_order_traversal(): perofrms pre order traversal of a binary tree
'''


from logging import raiseExceptions
from math import inf
import traceback

class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, val) -> None:
        try:
            if (self.data == val):
                raise Exception("Duplicate Entry is not allowed in BST")

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

        except Exception:
            # Print the full traceback to the console
            print("--- Full Traceback ---")
            traceback.print_exc()
            print("--- End Traceback ---")

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

    def find_min(self):
        min_element = 0
        self = self.left
        while self.left!=None:
            self=self.left
        min_element = self.data
        return min_element

    def find_max(self):
        max_element = 0
        self = self.right
        while self.right!=None:
            self=self.right
        max_element = self.data
        return max_element

    def post_order_traversal(self):
        ## left subtree -> right subtree -> right subtree
        elements = [] 

        #traverse left subtree
        if self.left:
            elements += self.left.post_order_traversal()

        #traverse right subtree
        if self.right:
            elements += self.right.post_order_traversal()

        #add root element
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        ## root-> left subtree -> right subtree
        elements = []
        
        #add root element
        elements.append(self.data)

        #traverse left subtree
        if self.left:
            elements += self.left.pre_order_traversal()

        #traverse right subtree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        ## root-> left subtree -> right subtree
        elements = []
        
        #traverse left subtree
        if self.left:
            elements += self.left.post_order_traversal()

        #traverse right subtree
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        return elements



    # def delete_node(self, val):
    #     if(val < self.data):
    #         self.left.delete_node()


def build_binary_tree(numbers):
    root = BinarySearchTreeNode(numbers[0])
    for i in range(1, len(numbers)):
        root.add_child(numbers[i])
    return root

if __name__ == '__main__':
    numbers = [4, 17, 8,22, 56, 93, 1, 32, 44]
    
    root = build_binary_tree(numbers)

    print(f'Inorder Traversal: {root.inorder_traversal()}')
    print(f'Preorder Traversal: {root.pre_order_traversal()}')
    print(f'Postorder Traversal: {root.post_order_traversal()}')
    print(f'Min Element: {root.find_min()}')
    print(f'Max Element: {root.find_max()}')
    print(f'Sum of elements: {sum(root.inorder_traversal())}')