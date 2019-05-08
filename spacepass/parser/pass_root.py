from .pass_dir import PassDir

class PassRoot(PassDir):
    def __init__(self, path):
        self._root_path = path
        super(PassRoot, self).__init__(path, 'pass')
