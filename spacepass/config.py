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
        config.add_argument('-p','--pass-dir',type=str, help='Path for the password-store repository')

        #OUTER SHAPE
        config.add_argument('--margin-left', type=str, help='Sets outer left margin (px)')
        config.add_argument('--margin-right', type=str, help='Sets outer right margin (px)')
        config.add_argument('--margin-bottom', type=str, help='Sets outer bottom margin (px)')

        #INNER SHAPE
        config.add_argument('--inner-margin', type=int, help='Inner margin for the window (px)')
        config.add_argument('--column-spacing', type=int,  help='Spacing between each column')
        config.add_argument('--row-spacing', type=int, help='Spacing between each row')
        config.add_argument('--max-columns', type=int, help='Maximum number of columns to display')
        config.add_argument('--row-height', type=int, help='The size for the buttons in each row')
        config.add_argument('--font', type=str, help='')

        #COLORS
        config.add_argument('--background-color',type=str, help='The color for the window background (rrggbb)')
        config.add_argument(
            '--button-background-color',
            type=str,
            help='The color for the button background (rrggbb)'
        )
        config.add_argument('--button-text-color', type=str, help='The color for the text of the buttons(rrggbb)')

        self._config = config

    def parse(self):
        self._parsed = self._config.parse()

        if (not self._parsed.pass_dir):
            self._parsed.pass_dir = '{}/.password-store'.format(os.path.expanduser('~'))

        return vars(self._parsed)
