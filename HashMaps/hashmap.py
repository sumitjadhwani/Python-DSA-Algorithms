class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for x in range(1, self.Max)]

    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        h = h%self.Max
        return h

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    

t = HashTable()
t['march 6'] = 20
t['dec 16'] = 25
t['May 20'] = 1896734786134

print(t['march 6'])
del t['march 6']

print(t['march 6'])