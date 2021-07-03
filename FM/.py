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
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN003 TYPEs and lambda
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN101 FMAX _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN102 VAL _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
TABLEVEL = "TABLEVEL"  # key for tab levels


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN103 _DICT_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FILENAMES_DICT = {}  # dict of filename: FD??
FMCF_SCTN0003_TYPE_CMNT_DICT = {}  # SCTN009 types comments
FMCF_SCTN0003_TYPE_DICT = {}  # SCTN003 types
FMCF_SCTN0201_DEF_CMNT_DICT = {}  # SCTN201 defines comments dict
FMCF_SCTN0201_DEF_DICT = {}  # SCTN201 defines dict
FMCF_SCTN0202_OPTIONS_CMNT_DICT = {}  # SCTN202 OPTIONS comments dict
FMCF_SCTN0202_OPTIONS_DICT = {}  # SCTN202 OPTIONS dict
FMCF_SCTN0202_OPTIONSDICT_CMNT_DICT = {}  # SCTN202 OPTIONSDICT comments dict
FMCF_SCTN0202_OPTIONSDICT_DICT = {}  # SCTN202 OPTIONSDICT
FMCF_SCTN0202_OPTIONSHELPDICT_DICT = {}  # SCTN202 OPTIONS HELPDICT
FMCF_SCTN0203_DICT_CMNT_DICT = {}  # SCTN203 dict comments dict
FMCF_SCTN0203_DICT_DICT = {}  # SCTN203 dict dict
FMCF_SCTN0204_LIST_CMNT_DICT = {}  # SCTN204 list comments dict
FMCF_SCTN0204_LIST_DICT = {}  # SCTN204 list dict
FMCF_SCTN02FF_CLASS_CMNT_DICT = {}  # 
FMCF_SCTN02FF_CLASS_DEF_DICT = {}  # str and val defines in a class
FMCF_SCTN02FF_CLASS_DICT = {}  # 
FMCF_SCTN02FF_CLASS_DICT_CMNT_DICT = {}  # 
FMCF_SCTN02FF_CLASS_DICT_DICT = {}  # 
FMCF_SCTN02FF_CLASS_FUNCTION_CMNT_DICT = {}  # 
FMCF_SCTN02FF_CLASS_FUNCTION_DEF1_DICT = {}  # 
FMCF_SCTN02FF_CLASS_FUNCTION_DEF2_DICT = {}  # 
FMCF_SCTN02FF_CLASS_FUNCTION_DICT = {}  # 
FMCF_SCTN02FF_CLASS_GROUP_DICT = {}  # 
FMCF_SCTN02FF_CLASS_INIT_CMNT_DICT = {}  # 
FMCF_SCTN02FF_CLASS_INIT_DEF1_DICT = {}  # 
FMCF_SCTN02FF_CLASS_INIT_DEF2_DICT = {}  # 
FMCF_SCTN02FF_CLASS_INIT_DEF3_DICT = {}  # 
FMCF_SCTN02FF_CLASS_INIT_DICT = {}  # 
FMCF_SCTN02FF_CLASS_INIT_DICTIN_DICT = {}  # 
FMCF_SCTN02FF_CLASS_INIT_DICTINSTR_DICT = {}  # 
FMCF_SCTN02FF_CLASS_LIST_CMNT_DICT = {}  # 
FMCF_SCTN02FF_CLASS_LIST_DICT = {}  # 
FMFM_SCTN0101_AX_CMNT_DICT = {}  # SCTN101 FMAX defined
FMFM_SCTN0101_AX_DICT = {}  # SCTN101 FMAX defined
FMFM_SCTN0102_VAL_CMNT_DICT = {}  # SCTN102 val
FMFM_SCTN0102_VAL_DICT = {}  # SCTN102 val
FMFM_SCTN0103_DICT_CMNT_DICT = {}  # SCTN103 dict defined
FMFM_SCTN0103_DICT_DICT = {}  # SCTN103 dict defined
FMFM_SCTN0104_LIST_CMNT_DICT = {}  # SCTN201 device defines
FMFM_SCTN0104_LIST_DICT = {}  # SCTN201 device defines
FMFM_SCTN0105_LDICT_CMNT_DICT = {}  # SCTN105 ldict defined
FMFM_SCTN0105_LDICT_DICT = {}  # SCTN105 ldict defined
FMFM_SCTN0106_SCTN_CLASS_DICT = {}  # holds anything under the h5:CLASS
FMFM_SCTN0106_SCTN_DICT_DICT = {}  # everything h3 and bigger, and their immediate subs not h4-h6
FMFM_SCTN0106_SCTN_FUNC_DICT = {}  # holds anything under the h5:FUNCTIONS
FMFM_SCTN0106_SCTN_VAR_DICT = {}  # holds anything under the h5:VARIABLES
FMPSG_SCTN0900_DEF1_CMNT_DICT = {}  # 
FMPSG_SCTN0900_DEF1_DICT = {}  # 
FMPSG_SCTN0901_DEF2_CMNT_DICT = {}  # define the dict to hold everything in SCTN0901
FMPSG_SCTN0901_DEF2_DICT = {}  # define the dict to hold everything in SCTN0901
FMPSG_SCTN0902_DICT_CMNT_DICT = {}  # define the dict to hold everything in SCTN0902
FMPSG_SCTN0902_DICT_DICT = {}  # define the dict to hold everything in SCTN0902
FMPSG_SCTN0903_LIST_CMNT_DICT = {}  # define the dict to hold everything in SCTN0903
FMPSG_SCTN0903_LIST_DICT = {}  # define the dict to hold everything in SCTN0903
FMPSG_SCTN0904_PLATEQ_INNER_CMNT_DICT = {}  # define the dict to hold everything in SCTN0904
FMPSG_SCTN0904_PLATEQ_INNER_DICT = {}  # define the dict to hold everything in SCTN0904
FMPSG_SCTN0904_PLATEQ_OUTER_CMNT_DICT = {}  # define the dict to hold everything in SCTN0904
FMPSG_SCTN0904_PLATEQ_OUTER_DICT = {}  # define the dict to hold everything in SCTN0904
FMPSG_SCTN0905_TUPDICT_CMNT_DICT = {}  # define the dict to hold everything in SCTN0905
FMPSG_SCTN0905_TUPDICT_DICT = {}  # define the dict to hold everything in SCTN0905
FMPSG_SCTN0905_TUPDICT_TDD_DICT = {}  # define the dict to hold everything in SCTN0905
FMPSG_SCTN0906_BTNS_CMNT_DICT = {}  # 
FMPSG_SCTN0906_BTNS_DICT = {}  # 
FMPSG_SCTN0907_SPIN_CMNT_DICT = {}  # holds the spin element stuffs (TUPDICT)f
FMPSG_SCTN0907_SPIN_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN0908_CHECKBOX_CMNT_DICT = {}  # 
FMPSG_SCTN0908_CHECKBOX_DICT = {}  # 
FMPSG_SCTN0909_TEXT_CMNT_DICT = {}  # 
FMPSG_SCTN0909_TEXT_DICT = {}  # 
FMPSG_SCTN090A_RADIO_CMNT_DICT = {}  # 
FMPSG_SCTN090A_RADIO_DICT = {}  # 
FMPSG_SCTN090B_COLUMN_CMNT_DICT = {}  # 
FMPSG_SCTN090B_COLUMN_DICT = {}  # 
FMPSG_SCTN090B_COLUMN_PARMS_DICT = {}  # 
FMPSG_SCTN090C_APPDS_CMNT_DICT = {}  # the main app dict for this app
FMPSG_SCTN090C_APPDS_DICT = {}  # the main app dict for this app
FMPSG_SCTN090C_APPDSDICT_DICT = {}  # the main app dict+dict for this app
FMPSG_SCTN090D_FORMMAIN_CMNT_DICT = {}  # 
FMPSG_SCTN090D_FORMMAIN_DICT = {}  # 
FMPSG_SCTN090E_LAYOUT_CMNT_DICT = {}  # 
FMPSG_SCTN090E_LAYOUT_DICT = {}  # 
FMPSG_SCTN090F_WINDOW_CMNT_DICT = {}  # 
FMPSG_SCTN090F_WINDOW_DICT = {}  # 
FMPSG_SCTN0910_DEF3_CMNT_DICT = {}  # 
FMPSG_SCTN0910_DEF3_DICT = {}  # 
FMPSG_SCTN0911_COMBO_CMNT_DICT = {}  # 
FMPSG_SCTN0911_COMBO_DICT = {}  # 
FMPSG_SCTN0912_FRAME_CMNT_DICT = {}  # 
FMPSG_SCTN0912_FRAME_DICT = {}  # 
FMPSG_SCTN0913_RCMENU_CMNT_DICT = {}  # 
FMPSG_SCTN0913_RCMENU_DICT = {}  # 
FMPSG_SCTN0914_FORMPOPUP_CMNT_DICT = {}  # 
FMPSG_SCTN0914_FORMPOPUP_DICT = {}  # 
FMPSG_SCTN0915_PUDLG_CMNT_DICT = {}  # 
FMPSG_SCTN0915_PUDLG_DICT_DICT = {}  # 
FMPSG_SCTN0915_PUDLG_LIST_DICT = {}  # 
FMPSG_SCTN0915_PUDLG_TYPE_DICT = {}  # 
FMPSG_SCTN0916_CLASS_SPIN_LIST_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN09FF_BTNS_ADDON_DICT = {}  # 
FMPSG_SCTN09FF_BTNS_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_BTNS_DICT = {}  # 
FMPSG_SCTN09FF_CHECKBOX_ADDON_DICT = {}  # 
FMPSG_SCTN09FF_CHECKBOX_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_CHECKBOX_DICT = {}  # 
FMPSG_SCTN09FF_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_COLUMN_ADDON_DICT = {}  # 
FMPSG_SCTN09FF_COLUMN_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_COLUMN_DICT = {}  # 
FMPSG_SCTN09FF_COLUMN_PARMS_DICT = {}  # 
FMPSG_SCTN09FF_COMBO_ADDON_DICT = {}  # 
FMPSG_SCTN09FF_COMBO_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_COMBO_DICT = {}  # 
FMPSG_SCTN09FF_DEF_DICT = {}  # str and val defines in a class
FMPSG_SCTN09FF_DICT = {}  # 
FMPSG_SCTN09FF_DICT_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_DICT_DICT = {}  # 
FMPSG_SCTN09FF_FRAME_ADDON_DICT = {}  # 
FMPSG_SCTN09FF_FRAME_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_FRAME_DICT = {}  # 
FMPSG_SCTN09FF_FUNCTION_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_FUNCTION_DEF1_DICT = {}  # 
FMPSG_SCTN09FF_FUNCTION_DEF2_DICT = {}  # 
FMPSG_SCTN09FF_FUNCTION_DICT = {}  # 
FMPSG_SCTN09FF_GROUP_DICT = {}  # 
FMPSG_SCTN09FF_INIT_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_INIT_DEF1_DICT = {}  # 
FMPSG_SCTN09FF_INIT_DEF2_DICT = {}  # 
FMPSG_SCTN09FF_INIT_DEF3_DICT = {}  # 
FMPSG_SCTN09FF_INIT_DICT = {}  # 
FMPSG_SCTN09FF_INIT_DICTIN_DICT = {}  # 
FMPSG_SCTN09FF_INIT_DICTINSTR_DICT = {}  # 
FMPSG_SCTN09FF_LAYOUT_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_LAYOUT_DICT = {}  # 
FMPSG_SCTN09FF_LIST_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_LIST_DICT = {}  # 
FMPSG_SCTN09FF_RADIO_ADDON_DICT = {}  # 
FMPSG_SCTN09FF_RADIO_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_RADIO_DICT = {}  # 
FMPSG_SCTN09FF_RCMENU_ADDON_DICT = {}  # 
FMPSG_SCTN09FF_RCMENU_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_RCMENU_DICT = {}  # 
FMPSG_SCTN09FF_SPIN_ADDON_DICT = {}  # 
FMPSG_SCTN09FF_SPIN_CMNT_DICT = {}  # holds the spin element stuffs (TUPDICT)f
FMPSG_SCTN09FF_SPIN_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN09FF_TEXT_ADDON_DICT = {}  # 
FMPSG_SCTN09FF_TEXT_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_TEXT_DICT = {}  # 
FMPSG_SCTN09FF_WINDOW_CMNT_DICT = {}  # 
FMPSG_SCTN09FF_WINDOW_DICT = {}  # 


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN104 _LIST_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed portions of FM.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


