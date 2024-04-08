class DynamicArray:
    def __init__(self):
        self.arr = []
        self.size = 0

    def push_back(self, value):
        self.arr.append(value)
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError("Array is empty")
        self.arr.pop()
        self.size -= 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        self.arr.insert(index, value)
        self.size += 1

    def remove(self, value):
        try:
            self.arr.remove(value)
            self.size -= 1
        except ValueError:
            raise ValueError("Value not found in array")

    def resize(self, new_size):
        if new_size < 0:
            raise ValueError("New size must be non-negative")
        self.arr = self.arr[:new_size]
        self.size = min(new_size, self.size)

    def at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.arr[index]

    def getSize(self):
        return self.size


def main():
    dynArray = DynamicArray()

    for i in range(1, 6):
        dynArray.push_back(i)

    print("Initial array:")
    for i in range(dynArray.getSize()):
        print(dynArray.at(i), end=" ")
    print()

    dynArray.insert(2, 10)
    print("\nArray after inserting 10 at index 2:")
    for i in range(dynArray.getSize()):
        print(dynArray.at(i), end=" ")
    print()

    # Remove an element
    dynArray.remove(3)
    print("\nArray after removing 3:")
    for i in range(dynArray.getSize()):
        print(dynArray.at(i), end=" ")
    print()

    dynArray.resize(3)
    print("\nArray after resizing to 3 elements:")
    for i in range(dynArray.getSize()):
        print(dynArray.at(i), end=" ")
    print()

    dynArray.pop_back()
    print("\nArray after popping the last element:")
    for i in range(dynArray.getSize()):
        print(dynArray.at(i), end=" ")
    print()


if __name__ == "__main__":
    main()
