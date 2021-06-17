

from FM import FM


_moduleName_ = "FM"
_sub0_ = "TBGLST"
_sub1_ = "CF"

_filename_ = f"""{FM.NAME_LCL_SELF_SUB1_PY(
	__MODULE_NAME__=_moduleName_,  # FM
	__SUB0__=_sub0_,  # TBGLST
	__SUB1__=_sub1_,  # CF
)}"""  # FM/FM_TBGLST_CF.py

_newFilename_ = f"""{FM.NAME_LCL_SELF_SUB1_NEW_PY(
	__MODULE_NAME__=_moduleName_,  # FM
	__SUB0__=_sub0_,  # TBGLST
	__SUB1__=_sub1_,  # CF
)}"""  # FM/FM_TBGLST_CF_NEW.py

__ID__ = (
	("__FILENAME__", _filename_,),  # FM/FM_TBGLST_CF.py
	("__MODULE_NAME__", _moduleName_,),  # FM
	("__NEW_FILENAME__", _newFilename_,),  # FM/FM_TBGLST_CF_NEW.py
	("__SUB0__", _sub0_,),  # TBGLST
	("__SUB0__", _sub1_,),  # CF
)

TBGLST = [
	(("CFVAL", FMAX_NOP, "CFVAL_BEGINS",), __ID__),
	(("CFVAL_____", FMAX_NOP, "CFVAL_ENDS",), __ID__),
	(("FMAXCF", FMAX_NOP, "FMAXCF_BEGINS",), __ID__),
	(("FMAXCF_SCTN0003_LAMBDA_DEF", FMAXFM_SCTN0101_AX_DEF, "define a lambda function <NAC><K_EVENT_NAME><lambda str>",), __ID__),
	(("FMAXCF_SCTN0003_TYPE_DEF", FMAXFM_SCTN0101_AX_DEF, "define a fake type used in the translation dict <NAC><K_EVENT_NAME><TYPE>",), __ID__),
	(("FMAXCF_SCTN0201_STR_DEF", FMAXFM_SCTN0101_AX_DEF, "define a STR in SCTN0201 <NAC><K_EVENT_NAME><str>",), __ID__),
	(("FMAXCF_SCTN0201_VAL_DEF", FMAXFM_SCTN0101_AX_DEF, "define a VAL in SCTN0201 <NAC><K_EVENT_NAME><VAL>",), __ID__),
	(("FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "define a OPTNAME: 'str' in SCTN0202 <NAC><KEY><PARM><STRDEFAULT>",), __ID__),
	(("FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a OPTNAME: VAL in SCTN0202 <NAC><KEY><PARM><VALDEFAULT>",), __ID__),
	(("FMAXCF_SCTN0202_OPTIONS_ADD_HELP_LINE", FMAXFM_SCTN0101_AX_DEF, "add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>",), __ID__),
	(("FMAXCF_SCTN0202_OPTIONS_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>",), __ID__),
	(("FMAXCF_SCTN0202_OPTIONS_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>",), __ID__),
	(("FMAXCF_SCTN0203_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>",), __ID__),
	(("FMAXCF_SCTN0203_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "define a dict STR in SCTN203 <NAC><DICTNAME><STR>",), __ID__),
	(("FMAXCF_SCTN0203_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>",), __ID__),
	(("FMAXCF_SCTN0204_LIST_DEF", FMAXFM_SCTN0101_AX_DEF, "define a list in SCTN204 <NAC><LISTNAME>",), __ID__),
	(("FMAXCF_SCTN0204_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "define a list STR in SCTN204 <NAC><LISTNAME><STR>",), __ID__),
	(("FMAXCF_SCTN0204_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>",), __ID__),
	(("FMAXCF_____", FMAX_NOP, "FMAXCF_ENDS",), __ID__),
	(("FMCF", FMAX_NOP, "FMCF_BEGINS",), __ID__),
	(("FMCF_SCTN0003_TYPE_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0003_TYPE_CMNT_DICT", "SCTN009 types comments",), __ID__),
	(("FMCF_SCTN0003_TYPE_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0003_TYPE_DICT", "SCTN003 types",), __ID__),
	(("FMCF_SCTN0201_DEF_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0201_DEF_CMNT_DICT", "SCTN201 defines comments dict",), __ID__),
	(("FMCF_SCTN0201_DEF_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0201_DEF_DICT", "SCTN201 defines dict",), __ID__),
	(("FMCF_SCTN0202_OPTIONSDICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0202_OPTIONSDICT_CMNT_DICT", "SCTN202 OPTIONSDICT comments dict",), __ID__),
	(("FMCF_SCTN0202_OPTIONSDICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0202_OPTIONSDICT_DICT", "SCTN202 OPTIONSDICT",), __ID__),
	(("FMCF_SCTN0202_OPTIONSHELPDICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0202_OPTIONSHELPDICT_DICT", "SCTN202 OPTIONS HELPDICT",), __ID__),
	(("FMCF_SCTN0202_OPTIONS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0202_OPTIONS_CMNT_DICT", "SCTN202 OPTIONS comments dict",), __ID__),
	(("FMCF_SCTN0202_OPTIONS_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0202_OPTIONS_DICT", "SCTN202 OPTIONS dict",), __ID__),
	(("FMCF_SCTN0203_DICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0203_DICT_CMNT_DICT", "SCTN203 dict comments dict",), __ID__),
	(("FMCF_SCTN0203_DICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0203_DICT_DICT", "SCTN203 dict dict",), __ID__),
	(("FMCF_SCTN0204_LIST_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0204_LIST_CMNT_DICT", "SCTN204 list comments dict",), __ID__),
	(("FMCF_SCTN0204_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "FMCF_SCTN0204_LIST_DICT", "SCTN204 list dict",), __ID__),
	(("FMCF_____", FMAX_NOP, "FMCF_ENDS",), __ID__),
]


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of FM/FM_TBGLST_CF_NEW.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


#
