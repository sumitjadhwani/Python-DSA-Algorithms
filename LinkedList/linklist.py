'''
In an object-oriented approach, a linked list requires TWO SEPARATE CLASSES to clearly define the responsibilities of the data structure and its individual components. 
A Node class defines the structure of a single element, while a LinkedList class manages the entire collection of nodes. 


Node class: The building block
The Node class is a self-contained unit that represents a single item in the list. It has a very limited and specific role: to store data and a pointer (or reference) to the next node in the sequence. 


LinkedList class: The manager
The LinkedList class is a "wrapper" or manager for the entire list. It contains a reference to the first node, known as the head, and uses this entry point to perform all operations on the list. 

'''

class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None

class LinkedList:
    def __init__(self):
        self.Head = None

    def insert_at_start(self, data):
        newNode = Node(data)
        newNode.Next = self.Head 
        self.Head = newNode
    
    def insert_at_end(self):
        pass

    def insert_at_index(self, index):
        pass

    def print_list(self):
        itr = self.Head
        list_str=""
        while itr:
            list_str+=str(itr.Data)
            if itr.Next:
                list_str+='-->'
            itr  = itr.Next
            # print('inside while ',itr.Data,itr.Next)
        print(list_str)

    def remove_from_start(self):
        self.Head = self.Head.Next

    def length(self):
        len = 0
        itr = self.Head
        while itr:
            len+=1
            itr = itr.Next
        print(f'Length of linked list is: {len}')

    ''' [data,ref] --> [data,ref] --> [data,ref] '''

    def reverse(self):
        prev = None
        itr = self.Head
        next_node= self.Head

        while itr:
            next_node = itr.Next                    #Saves next node 
            
            #Reverse Node           
            itr.Next = prev
            prev = itr                              #save current node as previous
            itr = next_node                         #update iterable with nextnode
        
        self.Head = prev                            #Change head to last node which is prev in this case

        

    def detect_loop(self):
         
        pass



if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_start(5)
    ll.insert_at_start(10)
    ll.insert_at_start(11)
    ll.print_list()

    ll.reverse()
    ll.print_list()