# coding=utf8
#launch from cmd: python setup.py build

from cx_Freeze import setup, Executable

setup(name = "Android Tool",
      version = "0.1",
      description = "Android Tool for Windows x64",
      #executables = [Executable("AndroidTool.py")])
      executables = [Executable("AndroidTool.py",base = "Win32GUI")]) # <-- base hide console!