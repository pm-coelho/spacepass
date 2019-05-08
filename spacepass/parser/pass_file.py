from .node import Node

class PassFile(Node):
    def __init__(self, path, name, shortcut):
        super(PassFile, self).__init__(path, name, shortcut)
