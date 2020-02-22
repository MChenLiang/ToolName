# ToolName
Development Template for 3D software  as maya houdini nuke used to python

# warning
Maya: please install PyQt5
Houdini: please install PySide2
python site package: pyfastcopy

# using:
# # houdini
from houdiniTools.scripts import openUI
reload(openUI)
openUI.show()

# # maya
1: drag install.mel to maya
2: or,
from mayaTools.scripts import openUI
reload(openUI)
openUI.show()

# intro:
openUI          : main ui operation
existsUI        : some operations on ui
baseFunctions   : commands outside the software
baseCommand     : commands of software

