class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def size_(self):
        return self.size
    
    def is_empty(self):
        return self.head is None
    
    def peek(self):
        return self.head.data
    
    def dislay(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def reverse_rec(self):
        def insert_at_bottom(stack,item):
            if stack.size == 0:
                stack.push(item)
            else:
                temp = stack.pop()
                insert_at_bottom(stack,item)
                stack.push(temp)
        if self.size == 0:
            return
        temp = self.pop()
        self.reverse_rec()
        insert_at_bottom(self,temp)
