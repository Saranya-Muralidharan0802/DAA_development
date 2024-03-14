class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        current = self.head
        print("Linked list elements:")
        while current:
            print(current.data)
            current = current.next

def linked_list_main():
    linked_list = SinglyLinkedList()

    print("Inserting elements into the linked list:")
    for i in range(1, 6):
        linked_list.insert_at_beginning(i)
        linked_list.display()

if __name__ == "__main__":
    linked_list_main()
