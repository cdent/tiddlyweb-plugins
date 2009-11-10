"""
adjust module path to account for virtual namespace

This is required for testing and building.
"""

import sys
import os


VIRTUAL_NAMESPACE = "tiddlywebplugins"

local_package = os.path.abspath(VIRTUAL_NAMESPACE)
sys.modules[VIRTUAL_NAMESPACE].__dict__["__path__"].append(local_package)
