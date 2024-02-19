class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def build_min_heap(self, array):
        self.heap = array
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def pop_root(self):
        if not self.heap:
            return None
        root = self.heap[0]
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self.heapify(0)
        return root

    def insert(self, element):
        self.heap.append(element)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)



if __name__ == "__main__":
    min_heap = MinHeap()

    input_array = [4, 10, 3, 5, 17,87,93,12,6]

    # Building min heap
    min_heap.build_min_heap(input_array)
    print("Built Min Heap:", min_heap.heap)

    # Insert operation
    min_heap.insert(2)
    print("Inserted 2. Updated Min Heap:", min_heap.heap)

    # Pop operation
    while min_heap.heap:
        root = min_heap.pop_root()
        print("Popped Root:", root)
        print("Updated Min Heap:", min_heap.heap)
