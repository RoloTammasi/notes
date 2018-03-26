# run like this: python compiler.py build
import cx_Freeze
import sys
import bs4
import numpy

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("tkinter_test.py", base=base)]

cx_Freeze.setup(
    name = "TkinterTest",
    options = {"build_exe": {"packages":["Tkinter","bs4","numpy"], "include_files": []}},
    version = "0.1",
    description = "Simple Tkinter application.",
    executables = executables
)