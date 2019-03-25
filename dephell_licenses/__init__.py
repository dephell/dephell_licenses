# https://github.com/hroncok/license/blob/master/license/licenses.py
# https://github.com/spdx/license-list-data/blob/master/json/licenses.json

from ._licenses import Licenses
from ._license import License


licenses = Licenses()

__all__ = ['Licenses', 'License', 'licenses']
