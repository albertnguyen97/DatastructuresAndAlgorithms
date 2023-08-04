class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "inserted at the end queue"

    def dequeue(self):
        if self.isEmpty():
            return "empty"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "empty"
        else:
            return self.items[0]

    def delete(self):
        self.items = None