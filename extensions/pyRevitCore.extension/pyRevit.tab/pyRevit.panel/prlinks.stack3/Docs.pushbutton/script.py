"""Opens the documentation page."""
from pyrevit import coreutils


__context__ = 'zerodoc'


url = 'http://pyrevit.readthedocs.io/en/latest/'
coreutils.open_url(url)