"""
                                      '||
... ...  .... ... ... ... ...  ....    ||
 ||'  ||  '|.  |   ||  ||  |  '' .||   ||
 ||    |   '|.|     ||| |||   .|' ||   ||
 ||...'     '|       |   |    '|..'|' .||.
 ||      .. |
''''      ''
Created by Dylan Araps.
"""

import os
import platform


__version__ = "2.0.4"
__cache_version__ = "1.1.0"


HOME = os.getenv("HOME", os.getenv("USERPROFILE"))
CACHE_DIR = os.path.join(HOME, ".cache", "wal")
MODULE_DIR = os.path.dirname(__file__)
CONF_DIR = os.path.join(HOME, ".config", "wal")
OS = platform.uname()[0]
