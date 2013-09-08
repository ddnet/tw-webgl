#!/usr/bin/env python
import os
import sys
import re
from os.path import basename, splitext

from tml.tml import Teemap
from tml.constants import TML_DIR

def normalizeFilename(name):
  #return re.sub('[^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_]', '_', name)
  return re.sub('\W', '_', name)

map_path = sys.argv[1]
t = Teemap(map_path)

mapname = splitext(basename(map_path))[0]

try:
    os.mkdir(normalizeFilename(mapname))
except OSError, e:
    if e.errno != 17:
        raise e
for image in t.images:
    try:
        image.save(os.sep.join([normalizeFilename(mapname), normalizeFilename(image.name) + '.png']))
    except:
        pass
print 'Extracted {0} images.'.format(len(t.images))

