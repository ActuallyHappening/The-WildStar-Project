class Command():
    def __init__(self, asioDo, cleanup=lambda: ..., name=None):
        self.asioDo = asioDo
        self.cleanup = cleanup
