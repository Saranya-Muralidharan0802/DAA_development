class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class HashTable:
    def __init__(self, initial_capacity=10):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash_function(self, key):
        # Multiplication hash function
        A = 0.61803398875  # Golden ratio
        return int(self.capacity * ((key * A) % 1))

    def insert(self, key, value):
        index = self.hash_function(key)
        node = self.buckets[index]
        new_node = Node(key, value)

        if node is None:
            self.buckets[index] = new_node
        else:
            while node.next:
                node = node.next
            node.next = new_node
            new_node.prev = node
        self.size += 1

        #Resize 
        if self.size >= self.capacity * 0.75:
            self.resize(self.capacity * 2)

    def remove(self, key):
        index = self.hash_function(key)
        node = self.buckets[index]

        while node:
            if node.key == key:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.buckets[index] = node.next
                if node.next:
                    node.next.prev = node.prev
                self.size -= 1
                return
            node = node.next

    def get(self, key):
        index = self.hash_function(key)
        node = self.buckets[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def resize(self, new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.size = 0
        self.buckets = [None] * self.capacity

        for node in old_buckets:
            while node:
                self.insert(node.key, node.value)
                node = node.next

        del old_buckets

    def __str__(self):
        result = ''
        for node in self.buckets:
            while node:
                result += f'({node.key}: {node.value}) -> '
                node = node.next
        return result + 'None'


hash_table = HashTable()
hash_table.insert(10, 12)
hash_table.insert(20, 47)
hash_table.insert(30, 23)
print(hash_table.get(20))
hash_table.remove(20)
print(hash_table.get(20))
