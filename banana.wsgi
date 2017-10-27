import os
import sys

wd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, wd)

from banana import app as application
