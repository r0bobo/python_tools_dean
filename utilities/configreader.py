#!/usr/bin/env python3

import os
import collections
import configparser


class ConfigReader(configparser.ConfigParser):
    """Read properties from .dean.ini.

    Default file location is: ~/.config/dean/dean.ini.
    dean.ini file with default values is created if missing.
    """

    def __init__(self):
        super().__init__(allow_no_value=True)

    def readconf(self, filename=None):
        """."""
        default_config = collections.OrderedDict()
        default_config['GENERAL'] = {
            '# general settings': None
            }
        default_config['DL-YT-PLAYLIST'] = {
            'youtube_playlist': 'https://www.youtube.com/playlist?list=PL1qRR_Q0qopRh_CE3FvXSFOHohDAYH_GN',
            'download_location': '{:s}'.format(
                os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube_Videos')),
            'download_log': '{:s}'.format(
                os.path.join(os.path.expanduser('~'), 'youtube_dl.log'))
            }
        default_config['SSH-LOGGER'] = {
            'auth_log': '/var/log/auth.log'
            }

        if not filename:
            config_file = os.path.join(
                os.path.expanduser('~'), '.config', 'dean', 'dean.ini'
                )
        else:
            config_file = os.path.expanduser(filename)

        try:
            with open(config_file) as fp:
                super().read_file(fp)
        except FileNotFoundError:
            super().read_dict(default_config)
            os.makedirs(os.path.dirname(config_file), exist_ok=True)
            with open(config_file, 'w') as fp:
                super().write(fp)