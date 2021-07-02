

from CF.CONSTANTS import MARKERS as M
from CF.CONSTANTS import NAMES as N
from CF.CONSTANTS import VALS as V


from FM import FM


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FM TBGLST_D _02
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

_moduleName_ = "FM"
_subd0_ = "TBGLST_D"
_sub0_ = "_02"
_sub1_ = "FM"
# ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱ ⟱
_filename_ = f"""{N.MAKE_NAME(
	__MODULE_NAME__=_moduleName_,
	__SUBD0__=_subd0_,
	__SUB0__=_sub0_,
	__SUB1__=_sub1_,
)}"""  # FM/TBGLST_D/_02_FM.py
# ⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱
_newFilename_ = f"""{N.MAKE_NAME(
	isNew_=True,
	__MODULE_NAME__=_moduleName_,
	__SUBD0__=_subd0_,
	__SUB0__=_sub0_,
	__SUB1__=_sub1_,
)}"""  # FM/TBGLST_D/_02_FM_NEW.py
# ⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱⟰⟱
__ID__ = N.MAKE_ID(
	("__FILENAME__", _filename_,),  # FM/TBGLST_D/_02_FM.py
	("__MODULE_NAME__", _moduleName_,),  # FM
	("__NEW_FILENAME__", _newFilename_,),  # FM/TBGLST_D/_02_FM_NEW.py
	("__SUBD0__", _subd0_,),  # TBGLST_D
	("__SUB0__", _sub0_,),  # _02
	("__SUB1__", _sub1_,),  # FM
)
# ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱
TBGLST = [
	(("FMAXFM_SCTN0101", FM.FMAX.SCTN0106_SCTN_DEF, "SCTN0101", "FM AX defines",), __ID__,),
	(("FMAX.SCTN0101_AX_DEF", FM.FMAX.SCTN0101_AX_DEF, "define a new FM action <NAC>",), __ID__),
	(("FMAXFM_SCTN0102", FM.FMAX.SCTN0106_SCTN_DEF, "SCTN0102", "FM defines",), __ID__,),
	(("FMAX.SCTN0102_STR_DEF", FM.FMAX.SCTN0101_AX_DEF, "define a FM string <NAC><VALNAME><STR>",), __ID__),
	(("FMAX.SCTN0102_VAL_DEF", FM.FMAX.SCTN0101_AX_DEF, "define a FM _value_ <NAC><VALNAME><VAL>",), __ID__),
	(("FMAXCF_SCTN0103", FM.FMAX.SCTN0106_SCTN_DEF, "SCTN0103", "FM dict defines",), __ID__,),
	(("FMAX.SCTN0103_DICT_DEF", FM.FMAX.SCTN0101_AX_DEF, "define a dict for FM <NAC><DICTNAME>",), __ID__),
	(("FMAXCF_SCTN0104", FM.FMAX.SCTN0106_SCTN_DEF, "SCTN0104", "FM list defines",), __ID__,),
	(("FMAX.SCTN0104_LIST_DEF", FM.FMAX.SCTN0101_AX_DEF, "define a list in FM <NAC><LISTNAME>",), __ID__),
	(("FMAX.SCTN0104_LIST_STR_ADD", FM.FMAX.SCTN0101_AX_DEF, "define a list in FM <NAC>",), __ID__),
	(("FMAX.SCTN0104_LIST_VAL_ADD", FM.FMAX.SCTN0101_AX_DEF, "define a list in FM <NAC>",), __ID__),
	(("FMAXCF_SCTN0105", FM.FMAX.SCTN0106_SCTN_DEF, "SCTN0105", "FM LDICT (local dicts) defines",), __ID__,),
	(("FMAX.SCTN0105_LDICT_DEF", FM.FMAX.SCTN0101_AX_DEF, "define a dict for FM <NAC>",), __ID__),
	(("FMAX.SCTN0105_LDICT_VS_ADD", FM.FMAX.SCTN0101_AX_DEF, "define a dict for FM <NAC>",), __ID__),
	(("FMAX.SCTN0105_LDICT_VV_ADD", FM.FMAX.SCTN0101_AX_DEF, "define a dict for FM <NAC>",), __ID__),
	(("FMAXCF_SCTN0106", FM.FMAX.SCTN0106_SCTN_DEF, "SCTN0106", "FM SCTN defines",), __ID__,),
	(("FMAX.SCTN0106_SCTN_DEF", FM.FMAX.SCTN0101_AX_DEF, "define the SCTN all over the place <NAC><SCTNNAME><DESCRIPTION0>",), __ID__),
	(("FMAX.NOP", FM.FMAX.SCTN0101_AX_DEF, "ignore the remainder of the line",), __ID__),
	(("FMAX.SCTNS_DEF", FM.FMAX.SCTN0101_AX_DEF, "define the sections <NAC><SCTN><MODULE><SUB0><SUB1><SUB2><DESCRIPTION>",), __ID__),
	(("FMFM_SCTN0101_AX_CMNT_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0101_AX_CMNT_DICT", "SCTN101 FMAX defined",), __ID__),
	(("FMFM_SCTN0101_AX_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0101_AX_DICT", "SCTN101 FMAX defined",), __ID__),
	(("FMFM_SCTN0102_VAL_CMNT_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0102_VAL_CMNT_DICT", "SCTN102 val",), __ID__),
	(("FMFM_SCTN0102_VAL_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0102_VAL_DICT", "SCTN102 val",), __ID__),
	(("FMFM_SCTN0103_DICT_CMNT_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0103_DICT_CMNT_DICT", "SCTN103 dict defined",), __ID__),
	(("FMFM_SCTN0103_DICT_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0103_DICT_DICT", "SCTN103 dict defined",), __ID__),
	(("FMFM_SCTN0104_LIST_CMNT_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0104_LIST_CMNT_DICT", "SCTN201 device defines",), __ID__),
	(("FMFM_SCTN0104_LIST_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0104_LIST_DICT", "SCTN201 device defines",), __ID__),
	(("FMFM_SCTN0105_LDICT_CMNT_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0105_LDICT_CMNT_DICT", "SCTN105 ldict defined",), __ID__),
	(("FMFM_SCTN0105_LDICT_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0105_LDICT_DICT", "SCTN105 ldict defined",), __ID__),
	(("FMFM_SCTN0106_SCTN_CLASS_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0106_SCTN_CLASS_DICT", "holds anything under the h5:CLASS",), __ID__),
	(("FMFM_SCTN0106_SCTN_DICT_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0106_SCTN_DICT_DICT", "everything h3 and bigger, and their immediate subs not h4-h6",), __ID__),
	(("FMFM_SCTN0106_SCTN_FUNC_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0106_SCTN_FUNC_DICT", "holds anything under the h5:FUNCTIONS",), __ID__),
	(("FMFM_SCTN0106_SCTN_VAR_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FMFM_SCTN0106_SCTN_VAR_DICT", "holds anything under the h5:VARIABLES",), __ID__),
	(("FMVAL_FILENAMES_DICT", FM.FMAX.SCTN0103_DICT_DEF, "FILENAMES_DICT", "dict of filename: FD??",), __ID__),
	(("FMVAl_TABLEVEL", FM.FMAX.SCTN0102_STR_DEF, "TABLEVEL", "TABLEVEL", "key for tab levels",), __ID__),
]


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of FM/TBGLST_D/_02_FM_NEW.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


#
