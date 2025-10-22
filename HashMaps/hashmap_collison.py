class HashMap:
    def __init__(self):
        self.Max = 100
        self.arr = [[] for x in range(1,self.Max)]

    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        h=h%10
        return h

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False

        for id, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][id] = (key,value) 
        
        if not found:
            print("inside if")
            self.arr[h].append((key,value))

    def __getitem__(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h =self.get_hash(key)

        for id, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][id]

    
h = HashMap()
h['march 6'] = 20
h['march 17'] = 16
h['march 6'] = 5

print(h['march 6'])

del h['march 6']

print(h['march 6'])
print(h['march 17'])
