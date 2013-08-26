#!/usr/bin/env python
import os
import sys

from tml.tml import Teemap
from tml.constants import TML_DIR

map_path = sys.argv[1]
t = Teemap(map_path)
try:
    os.mkdir('images')
except OSError, e:
    if e.errno != 17:
        raise e
for image in t.images:
    try:
        image.save(os.sep.join(['images', image.name + '.png']))
    except:
        pass
print 'Extracted {0} images.'.format(len(t.images))

