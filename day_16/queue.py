
class MyQueue:
    def __init__(self):
        self.container = []

    def add(self, value):
        self.container.append(value)

    def get_last(self):
        return self.get_element_by_index(len(self.container) - 1)

    def get_first(self):
        return self.get_element_by_index(0)

    def get_element_by_index(self, a):
        if len(self.container) > 0:
            element = self.container.pop(a)
        else:
            element = None
        return element
