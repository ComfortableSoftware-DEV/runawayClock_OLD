

from FM import FM
__MODULE_NAME__ = "FM"
__FILENAME__ = "FM_TBGLST_FM.py"
TBGLST = [
	((__MODULE_NAME__, __FILENAME__), "FMAX_NOP", FM.FMAXFM_SCTN0101_AX_DEF, "ignore the remainder of the line"),
	((__MODULE_NAME__, __FILENAME__), "FMAXFM_SCTN0101_AX_DEF", FM.FMAXFM_SCTN0101_AX_DEF, "define a new FM action <NAC>",),
	((__MODULE_NAME__, __FILENAME__), "FMAXFM_SCTN0102_STR_DEF", FM.FMAXFM_SCTN0101_AX_DEF, "define a FM string <NAC><VALNAME><STR>",),
	((__MODULE_NAME__, __FILENAME__), "FMAXFM_SCTN0102_VAL_DEF", FM.FMAXFM_SCTN0101_AX_DEF, "define a FM _value_ <NAC><VALNAME><VAL>",),
	((__MODULE_NAME__, __FILENAME__), "FMAXFM_SCTN0103_DICT_DEF", FM.FMAXFM_SCTN0101_AX_DEF, "define a dict for FM <NAC>",),
	((__MODULE_NAME__, __FILENAME__), "FMAXFM_SCTN0104_LIST_DEF", FM.FMAXFM_SCTN0101_AX_DEF, "define a list in FM <NAC>",),
	((__MODULE_NAME__, __FILENAME__), "FMAXFM_SCTN0104_LIST_STR_ADD", FM.FMAXFM_SCTN0101_AX_DEF, "define a list in FM <NAC>",),
	((__MODULE_NAME__, __FILENAME__), "FMAXFM_SCTN0104_LIST_VAL_ADD", FM.FMAXFM_SCTN0101_AX_DEF, "define a list in FM <NAC>",),
	((__MODULE_NAME__, __FILENAME__), "FMAXFM_SCTN0105_LDICT_DEF", FM.FMAXFM_SCTN0101_AX_DEF, "define a dict for FM <NAC>",),
	((__MODULE_NAME__, __FILENAME__), "FMAXFM_SCTN0105_LDICT_VS_ADD", FM.FMAXFM_SCTN0101_AX_DEF, "define a dict for FM <NAC>",),
	((__MODULE_NAME__, __FILENAME__), "FMAXFM_SCTN0105_LDICT_VV_ADD", FM.FMAXFM_SCTN0101_AX_DEF, "define a dict for FM <NAC>",),
	((__MODULE_NAME__, __FILENAME__), "FMAXFM_SCTN0106_SCTN_DEF", FM.FMAXFM_SCTN0101_AX_DEF, "define the SCTN all over the place <NAC><SCTNNAME><DESCRIPTION0>",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0101_AX_CMNT_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "SCTN101 FMAX defined",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0101_AX_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "SCTN101 FMAX defined",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0102_VAL_CMNT_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "SCTN102 val",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0102_VAL_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "SCTN102 val",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0103_DICT_CMNT_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "SCTN103 dict defined",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0103_DICT_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "SCTN103 dict defined",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0104_LIST_CMNT_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "SCTN201 device defines",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0104_LIST_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "SCTN201 device defines",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0105_LDICT_CMNT_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "SCTN105 ldict defined",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0105_LDICT_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "SCTN105 ldict defined",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0106_SCTN_CLASS_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "holds anything under the h5:CLASS",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0106_SCTN_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "everything h3 and bigger, and their immediate subs not h4-h6",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0106_SCTN_FUNC_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "holds anything under the h5:FUNCTIONS",),
	((__MODULE_NAME__, __FILENAME__), "FMFM_SCTN0106_SCTN_VAR_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "holds anything under the h5:VARIABLES",),
	((__MODULE_NAME__, __FILENAME__), "FMVAL_FILENAMES_DICT", FM.FMAXFM_SCTN0103_DICT_DEF, "FILENAMES_DICT", "dict of filename: FD??",),
	((__MODULE_NAME__, __FILENAME__), "FMVAl_TABLEVEL", FM.FMAXFM_SCTN0102_STR_DEF, "TABLEVEL", "TABLEVEL", "key for tab levels",),
]
