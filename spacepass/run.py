from .parser.pass_root import PassRoot
from .gui.dir_window import DirWindow

def main():
    pass_dir = '/home/enemabandit/.password-store'
    content = PassRoot(pass_dir)
    window = DirWindow(pass_dir, content)
    window.draw()
