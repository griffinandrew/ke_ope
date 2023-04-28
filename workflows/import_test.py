#!/usr/bin/env python

try:
    from IPython.core.display import HTML, Markdown, TextDisplayObject, Javascript
except ImportError:
    raise ImportError('core.display modules failed to load')

from IPython.display import display, IFrame, Image
import ipywidgets as widgets
from ipywidgets import interact, fixed, Layout
import os, requests, pty, re, subprocess, struct, sys, fcntl, termios, select
from notebook.notebookapp import list_running_servers
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import pandas as pd
import time
import array

def main():

    for item in dir():
        print(item)




if __name__ == "__main__":
    main()
