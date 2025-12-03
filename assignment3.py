# DYNAMIC ARRAY ASSIGNMENT
class DynamicArray:
    def __init__(self):
        self.capacity = 2       # initial capacity
        self.size = 0           # number of elements
        self.array = [0] * self.capacity

    def insert(self, value):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = value
        self.size += 1

    def resize(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def display(self):
        print(self.array[:self.size])

# Testing
values = [10, 20, 30, 40, 50]
da = DynamicArray()
for v in values:
    da.insert(v)
    da.display()
