# Create an explicit path modification.
# This is important and gives individual scripts the ability
# to import core without any issues via import context

import os
import sys

# Replace with core directory name
import core_template

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
