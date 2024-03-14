class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [0] * max_size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, value):
        if self.is_full():
            raise Exception("Stack is full")
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[self.top]

def stack_main():
    stack = Stack(5)

    print("Pushing elements onto the stack:")
    for i in range(1, 6):
        stack.push(i)
        print("Top of the stack after push:", stack.peek())

    print("\nPopping elements from the stack:")
    for _ in range(2):
        print("Popped element:", stack.pop())
        print("Top of the stack after pop:", stack.peek())

if __name__ == "__main__":
    stack_main()
