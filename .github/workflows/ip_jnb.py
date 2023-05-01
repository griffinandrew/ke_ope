#!/usr/bin/env python

try:
    from IPython.core.display import HTML, Markdown, TextDisplayObject, Javascript
except ImportError:
    raise ImportError('core.display modules failed to load')

try: 
    from IPython.display import display, IFrame, Image
except ImportError:
    raise ImportError('display not loaded')

try: 
    import ipywidgets as widgets
except ImportError:
    raise ImportError('ipywidgets fail')

try:
    from ipywidgets import interact, fixed, Layout
except ImportError:
    raise ImportError('interact, fixed layout failed')

try:
    import os, requests, pty, re, subprocess, struct, sys, fcntl, termios, select
except ImportError:
    raise ImportError(" os, requests, pty, re, subprocess, struct, sys, fcntl, termios, select failed")

try: 
    from notebook.notebookapp import list_running_servers
except ImportError:
    raise ImportError("notebook.notebookapp import list_running_servers failed")

try:
    import matplotlib
except ImportError:
    raise ImportError("import matplotlib failed")

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("import matplotlib.pyplot as plt failed")

try:
    from matplotlib import animation
except ImportError:
    raise ImportError("from matplotlib import animation failed")

try:
    import numpy as np
except ImportError:
    raise ImportError("import numpy as np failed")

try:
    import pandas as pd
except ImportError:
    raise ImportError(" import pandas as pd failed")

try:
    import time
except ImportError:
    raise ImportError("import time failed")

try:
    import array
except ImportError:
    raise ImportError("import array failed")


#!/bin/bash
jupyter notebook stop 





