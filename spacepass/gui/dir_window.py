from spacemenu.window import Window

# TODO: read options from config
class DirWindow():
    def __init__(self, pass_dir, content, options):
        self.pass_dir = pass_dir
        self._root_window = Window(self._parse_content(content), options)


    def _parse_content(self, content):
        return {
            'label': 'SpacePass',
            'branches': self._parse_dirs(content.dirs),
            'leaves': self._parse_files(content.files)
        }


    def _parse_dirs(self, directories):
        return [
            {
                'label': d.name,
                'branches': self._parse_dirs(d.dirs),
                'leaves': self._parse_files(d.files)
            } for d in directories
        ]


    def _parse_files(self, files):
        return [
            {
                'label': f.name,
                'command': 'pass show -c {}'.format(f.path[len(self.pass_dir)+1:-4])
            } for f in files
        ]


    def draw(self):
        self._root_window.draw()
