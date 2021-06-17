

from FM import FM


__MODULE_NAME__ = "FM"
__SUB__ = "TBGLST"
__SUB1__ = "PSG"

__FILENAME__ = f"""{FM.NAME_LCL_SUB1_PY(__MODULE_NAME__, __SUB__, __SUB1__)}"""  #
__NEW_FILENAME__ = f"""{FM.NAME_LCL_SUB1_NEW_PY(__MODULE_NAME__, __SUB__, __SUB1__)}"""  #

__ID__ = (
	"filename_", __FILENAME__,  #
	"moduleName_", __MODULE_NAME__,  # FM
	"newFilename_", __NEW_FILENAME__,  #
	"sub_", __SUB__,  # TBGLST
	"sub1_", __SUB1__,  # CF
)

TBGLST = [
	((__MODULE_NAME__, __FILENAME__), ("CLASS_POPUP_ALERT", FMAXPSG_SCTN09FF_CLASS_DEF, __CLASS__, "start the POPUP_ALERT class",),),
	((__MODULE_NAME__, __FILENAME__), ("POPUP_ALERT_COL0100", FMAXPSG_SCTN09FF_CLASS_COLUMN_DEF, __CLASS__, "COL01", "comment",),),
]
