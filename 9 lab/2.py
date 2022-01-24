class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def __str__(self):
        return str(self.value)

class BinTree:
    def __init__ (self):
        self.start = None
        self.length = 0
        self.last = None

    def add(self, value):
        elem = Node(value)
        if self.start is None:
            self.start = elem
        else:
            self.current = self.start
            while True:
                if self.current.value >= value:
                    if self.current.left == None:
                        self.current.left = elem
                        break
                    else:
                        self.current = self.current.left
                else:
                    if self.current.right == None:
                        self.current.right = elem
                        break
                    else:
                        self.current = self.current.right
        self.length += 1

    def __len__(self):
        return self.length

    def __iter__(self):
        self.__curr = self.start
        if self.start is None:
            return
        stack = [None]
        while True:
            if stack == []:
                break
            val = self.__curr.get_value()
            yield val
            stack.append(self.__curr.right)
            if self.__curr.left is not None:
                self.__curr = self.__curr.left
            else:
                while True:
                    self.__curr = stack.pop()
                    if self.__curr is not None or stack == []:
                        break


lst = BinTree()
for i in range(10):
    lst.add(i*i)
lst.add(-10)
lst.add(-40)

new = BinTree()

for i in lst:
    print(i)

for i in new:
    print(i)