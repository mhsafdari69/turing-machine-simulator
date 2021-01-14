class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, state, head, string, iter_count):
        self.queue.append((state, head, string, iter_count))

    def dequeue(self):
        item = self.queue[0]
        self.queue = self.queue[1:]
        return item

    def is_empty(self):
        return len(self.queue) == 0
