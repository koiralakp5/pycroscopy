# Not supporting for __all__
# __all__= ['processing', 'analysis', 'io', 'viz']

import analysis
import io
import processing
import viz
# TODO: need to figure out what to do with external libs: numpy_groupies and pyqtgraph.

from __version__ import version as __version__
from __version__ import date as __date__
