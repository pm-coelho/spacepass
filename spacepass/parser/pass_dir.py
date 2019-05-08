from random import choice
from os import listdir
from os.path import join, isfile, isdir, splitext

from .node import Node
from .pass_file import PassFile

class PassDir(Node):
    def __init__(self, path, name):
        super(PassDir, self).__init__(path, name, None)
        self.dirs = []
        self.files = []

        self.parse_dir(path)


    def parse_dir(self, path):
        for c_name in listdir(path):
            c_path = join(path, c_name)
            name = splitext(c_name)[0]

            if (isdir(c_path) and c_name[0] != '.'):
                self.dirs.append(PassDir(c_path, name))
            elif (isfile(c_path) and c_name[0] != '.'):
                self.files.append(PassFile(c_path, name, None))
