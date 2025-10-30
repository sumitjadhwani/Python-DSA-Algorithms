''' 
Tree Node is basic node structure of a tree comprising of data, child, parent,

add_child(node)


'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.child.append(child)

    def get_level(self):
        level = 0
        node  = self.parent
        while node!=None:
            level+=1
            node = node.parent
        return level

    def print_tree(self):
        prefix = ' ' * self.get_level() * 3
        if prefix != '':
            prefix = prefix + '|__' 
        print(prefix + self.data)
        for child in self.child:
            child.print_tree()


if __name__ == '__main__':
    electronics = TreeNode('Electronics')
    laptop = TreeNode('Laptop')
    mobile = TreeNode('mobile')
    ac = TreeNode('ac')

    lenovo = TreeNode('lenovo')
    hp = TreeNode('hp')
    mac = TreeNode('mac')

    nothing = TreeNode('nothing')
    pixel = TreeNode('pixel')
    apple = TreeNode('apple')

    haier = TreeNode('haier')
    daiken = TreeNode('daiken')
    voltas = TreeNode('voltas')

    electronics.add_child(laptop)
    electronics.add_child(mobile)
    electronics.add_child(ac)

    laptop.add_child(lenovo)
    laptop.add_child(hp)
    laptop.add_child(mac)

    mobile.add_child(nothing)
    mobile.add_child(pixel)
    mobile.add_child(apple)

    ac.add_child(haier)
    ac.add_child(daiken)
    ac.add_child(voltas)

    electronics.print_tree()

'''
Electronics
   |__Laptop
      |__lenovo
      |__hp
      |__mac
   |__mobile
      |__nothing
      |__pixel
      |__apple
   |__ac
      |__haier
      |__daiken
      |__voltas

'''





        
         

