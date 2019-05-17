import os
from .parser.pass_root import PassRoot
from .gui.dir_window import DirWindow
from .config import Config

def main():
    options = Config().parse()
    print(options)
    content = PassRoot(options['pass_dir'])
    window = DirWindow(options['pass_dir'], content, options)
    window.draw()
