

class UnionFind:
    def __init__(self, n_nodes) -> None:
        # Link tells you the next element in the chain
        # Size tells you how big is a given set.
        self.link = []
        self.size = []
        for i in range(n_nodes):
            self.link[i] = i
            self.size[i] = 1
    def find(self, x):
        while(x != self.link[x]):
            x = self.link[x]
        return x

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        # a and b must be in different sets
        # Here a is the larger set.
        # We are appending the smaller set to the larger set.
        a = self.find(a)
        b = self.find(b)
        if (self.size[a] < self.size[b]):
            c = a
            a = b
            b = c
        self.size[a] += self.size[b]
        self.link[b] = a
    
