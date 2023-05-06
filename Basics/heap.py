class Heap:
    def __init__(self):
        self.arr = []
        self.cur_size = 0

    def bubble_up(self, idx):
        stop = False
        while (idx - 1) // 2 >= 0 and not stop:
            parent = (idx - 1) // 2
            if self.arr[idx] < self.arr[parent]:
                self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
            else:
                stop = True
            idx = parent

    def bubble_down(self, idx):
        stop = False
        while ((idx * 2) + 1) < self.cur_size and not stop:
            left_child = idx * 2 + 1
            right_child = idx * 2 + 2
            if right_child >= self.cur_size:
                if self.arr[left_child] < self.arr[idx]:
                    self.arr[idx], self.arr[left_child] = self.arr[left_child], self.arr[idx]
                    idx = left_child
                else:
                    stop = True
            else:
                smaller_child = left_child if self.arr[left_child] < self.arr[right_child] else right_child
                if self.arr[idx] < self.arr[smaller_child]:
                    self.arr[idx], self.arr[smaller_child] = self.arr[smaller_child], self.arr[idx]
                    idx = smaller_child
                else:
                    stop = True
    def insert(self, x):
        self.arr.append(x)
        self.cur_size += 1
        self.bubble_up(self.cur_size - 1)
    
    def pop(self):
        if self.cur_size == 0:
            return "EMPTY"
        res = self.arr[0]
        self.arr[0], self.arr[self.cur_size - 1] = self.arr[self.cur_size - 1], self.arr[0]
        self.arr.pop()
        self.cur_size -= 1
        self.bubble_down(0)
        return res

    def peek(self):
        return self.arr[0]
    

obj = Heap()
obj.insert(3)
obj.insert(5)
obj.insert(1)
# Expect 1
print(obj.pop())
# Expect 3
print(obj.peek())
obj.insert(7)
# Expect 3
print(obj.peek())
obj.pop()
obj.pop()
# Expect 7
print(obj.peek())

