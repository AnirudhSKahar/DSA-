# Operations on stack

class stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def is_empty(self):
        return len(self.stack) == 0
      
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1]

    def print_stack(self):
        print("Stack elements (bottom → top):")
        for item in self.stack:
            if item is not self.top():
                print(item, end=" -> ")
            else:
                print(self.top())

      



s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

s.print_stack()
print("Size : ",s.size())
print("Popped :", s.pop())
print("IsEmpty : ",s.is_empty())
print("Size : ",s.size())
print("Top : ",s.top())