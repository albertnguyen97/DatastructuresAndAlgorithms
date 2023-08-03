class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(i) for i in self.list]
        return "\n".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return "The element has been inserted"

    def pop(self):
        if self.isEmpty():
            return "don't have any element in the stack"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "empty"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None
        return self.list
