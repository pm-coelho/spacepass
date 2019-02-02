from random import choice
from os import listdir
from os.path import join, isfile, isdir, splitext

from .node import Node
from .pass_file import PassFile

class PassDir(Node):
    def __init__(self, back, path, name):
        super(PassDir, self).__init__(path, name, name[0])
        self.back = back
        self.files = []
        self.dirs = []
        self.parse_dir(path)


    def parse_dir(self, path):
        dir_content = listdir(path)
        [self.add_file(path, f) for f in dir_content if isfile(join(path,f))]
        [self.add_dir(path, d) for d in dir_content if isdir(join(path,d))]


    def add_file(self, path, name):
        if (name[0] == '.'): return
        file_name = splitext(name)[0]
        self.files.append(PassFile('{}/{}'.format(path, file_name), name, self.gen_shortcut(file_name)))


    def add_dir(self, path, name):
        if(name[0] == '.'): return
        self.dirs.append(PassDir(path, '{}/{}'.format(path, name), name))


    def gen_shortcut(self, name):
        # TODO: this turns into an infinite loop when no more letters are available
        if name == '': return self.gen_shortcut(choice(string.letters))

        shortcut = name[0]
        used_shortcuts = self.get_used_shortcuts()
        if (shortcut not in used_shortcuts):
            return shortcut
        elif (shortcut.swapcase() not in used_shortcuts):
            return shortcut.swapcase()
        else:
            return self.gen_shortcut(name[1:])


    def get_used_shortcuts(self):
        return map(lambda x: x._shortcut, self.files + self.dirs + [self])
