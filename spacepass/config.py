import configargparse
import os
import getpass

class Config:
    def __init__(self):
        config = configargparse.ArgParser(
            default_config_files = ['{}/spacepass/config'.format(
                os.getenv('XDG_CONFIG_HOME', '{}/.config'.format(os.path.expanduser("~")))
            )
        ])

        config.add('-c', '--config', required=False, is_config_file=True, help='config file path')

        config.add_argument('-p','--pass-dir', help='Path for the password-store repository')

        config.add_argument('--margin', help='inner margin for the window')
        config.add_argument('--column-spacing', help='Column gutter size')
        config.add_argument('--row-spacing', help='Row gutter size')
        config.add_argument('--max-columns', help='Maximum number of columns to display')
        config.add_argument('--row-height', help='The size for each row')

        self._config = config

    def parse(self):
        self._parsed = self._config.parse()

        if (not self._parsed.pass_dir):
            self._parsed.pass_dir = '{}/.password-store'.format(os.path.expanduser('~'))

        return vars(self._parsed)
