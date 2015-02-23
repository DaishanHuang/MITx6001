## Lesson 11, Problem 6

class Queue(object):
    
    def __init__(self):
        self.elems = []
        
    def insert(self, e):
        self.elems.append(e)
        
    def remove(self):
        if len(self.elems) == 0:
            raise ValueError('Queue is empty')
        return self.elems.pop(0)
