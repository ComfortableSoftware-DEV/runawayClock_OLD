#!/usr/bin/python


import imp
import os


from CF.CONSTANTS import MARKERS as M
from CF.CONSTANTS import NAMES as N
from CF.CONSTANTS import VALS as V


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# modules defined in FM.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# FM.py is copied, along with the appropriate FMxxxxxx.py file from CONFIGDIR to local by pythonUnitsLink.py
# make sure if you change the modules, you also update the stored copy FMxxxxxx.py TBGLST file when you update FM.py
# CF.py is always linked, make sure to update CFTOP.py and SCTN0102 when FM.py or CF.py are changed
# all other units are loaded dynamically by pythonUnitsLink.py using the SCTN16 structure, FMSCTNENABLED.py file locally, etc.
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * def doErrorItem(message_, itemToError_):
# * def explodeItem(itemToExplode_):
# * def makeAComment(comment_):
# * def makeADict(dictName_, dictComment_, dictItems_):
# * def makeAList(listName_, listComment_, listItems_):
# * def makeATupDict(tupDictName_, tupDictItems_, tupDictSidecar_):
# * def makeAWideComment(comment_):
# * def makeCF():
# * def makeDBSQLT()
# * def makeDO():
# * def makeDOHBI():
# * def makeFM():
# * def makeFO():
# * def makeSP():
# * def parseTBGLST(FDTBGLST):
# * def readFileToStr(FILENAME_):
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * def __main__():


#
