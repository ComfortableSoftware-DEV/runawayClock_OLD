

from FM import FM


_class_ = "CLOCKS"
_moduleName_ = "FM"
_sub0_ = "TBGLST"
_sub1_ = "PSG"

_filename_ = f"""{FM.NAME_LCL_SELF_SUB1_CLASS_PY(
	__CLASS__=_class_,
	__MODULE_NAME__=_moduleName_,
	__SUB0__=_sub0_,
	__SUB1__=_sub1_,
)}"""  # FM/FM_TBGLST_PSG_CLOCKS_C.py

_newFilename_ = f"""{FM.NAME_LCL_SELF_SUB1_CLASS_NEW_PY(
	__CLASS__=_class_,
	__MODULE_NAME__=_moduleName_,
	__SUB0__=_sub0_,
	__SUB1__=_sub1_,
)}"""  # FM/FM_TBGLST_PSG_CLOCKS_C_NEW.py

__ID__ = (
	("__CLASS__", _class_,),  # CLOCKS
	("__FILENAME__", _filename_,),  # FM/FM_TBGLST_PSG_CLOCKS_C.py
	("__MODULE_NAME__", _moduleName_,),  # FM
	("__NEW_FILENAME__", _newFilename_,),  # FM/FM_TBGLST_PSG_CLOCKS_C_NEW.py
	("__SUB0__", _sub0_,),  # TBGLST
	("__SUB1__", _sub1_,),  # PSG
)


TBGLST = [
	(("PSGVAL__CLOCKS", FM.FMAXPSG_SCTN09FF_CLASS_DEF, "CLOCKS", "define clocks class",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0100", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_DEF, "CLOCKS", "_COLUMN01_", "the column that puts the two smaller clocks below the main one",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0101", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_00", "L03", "add a new row to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0102", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_00", "L04", "COLUMN01_E01", "add a new TEXT element to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0103", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_00", "L05", "COLUMN01_E01", "**self._TEXT_TIME_S_CLOCK_", "add the main clock",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0104", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_01", "L03", "add a new row to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0105", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_01", "L04", "COLUMN01_E02", "add a new row to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0106", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_01", "L05", "COLUMN01_E02", "**self._TEXT_TIME_S_AT_ZEROELAPSE_", "add time to go",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0107", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_01", "L04", "COLUMN01_E03", "add a new text element to row01 clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0108", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_01", "L05", "COLUMN01_E03", "**self._TEXT_TIME_S_ELAPSED_", "add elapsed time",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0109", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_02", "L03", "add a new row to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN010A", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_02", "L04", "COLUMN01_E04", "add a new text element to row01 clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN010B", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_02", "L05", "COLUMN01_E04", "**self._TEXT_TIME_S_TOGO_", "add elapsed time",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN010C", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_02", "L04", "COLUMN01_E05", "add a new row to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN010D", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_02", "L05", "COLUMN01_E05", "**self._TEXT_TIME_S_AT_NEXT_ALERT_", "add time to go",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN010E", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_03", "L03", "add a new row to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN010F", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_03", "L04", "COLUMN01_E08", "add a new text element to row01 clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0110", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_03", "L05", "COLUMN01_E08", "**self._TEXT_NAME_NEXT_EVENT_", "add the main clock",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0111", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_04", "L03", "add a new row to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0112", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_CHECKBOX_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_04", "L04", "COLUMN01_E06", "add a new text element to row01 clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0113", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_04", "L05", "COLUMN01_E06", "**PSG.CHECKBOX_RUNAWAY01", "add elapsed time",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0114", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_CHECKBOX_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_04", "L04", "COLUMN01_E07", "add a new text element to row01 clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0115", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_04", "L05", "COLUMN01_E07", "**PSG.CHECKBOX_ALPHA_DIM01", "add elapsed time",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN02", FM.FMAX_NOP, "the COLUMN02 for APPMODE_CLOCKS",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0200", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_DEF, "CLOCKS", "_COLUMN02_", "the column that puts the two smaller clocks below the main one",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0201", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_01", "L03", "add a new row to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0202", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_BUTTON_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_01", "L04", "COLUMN02_E01", "add a button element to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0203", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_01", "L05", "COLUMN02_E01", "**PSG.BTN_QUIT20", "add the xpand button to clocks",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0204", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_02", "L03", "add a new row to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0205", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_BUTTON_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_02", "L04", "COLUMN02_E02", "add reset button for elapsed time",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0206", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_02", "L05", "COLUMN02_E02", "**PSG.BTN_ZERO20", "add the zero button to clocks",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0207", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_03", "L03", "add a new row to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0208", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_BUTTON_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_03", "L04", "COLUMN02_E03", "add reset button for elapsed time",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN0209", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_03", "L05", "COLUMN02_E03", "**PSG.BTN_XPAND20", "add the zero button to clocks",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN020A", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_04", "L03", "add a new row to clocks column",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN020B", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_04", "L04", "COLUMN02_E04", "add reset button for elapsed time",), __ID__),
	(("PSGVAL__CLOCKS_COLUMN020C", FM.FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_04", "L05", "COLUMN02_E04", "**self._TEXT_CURRENT_INTERVAL_COUNT_", "add the zero button to clocks",), __ID__),
	(("PSGVAL__CLOCKS_DICT_KEYS_INT00", FM.FMAXPSG_SCTN09FF_CLASS_DICT_DEF, "CLOCKS", "_DICT_KEYS_INT_", "dict of integer keys and their format",), __ID__),
	(("PSGVAL__CLOCKS_DICT_KEYS_INT01", FM.FMAXPSG_SCTN09FF_CLASS_DICT_VS_ADD, "CLOCKS", "_DICT_KEYS_INT_", "PSG.K_CURRENT_INTERVAL_COUNT", "04d", "intervalCount:04d",), __ID__),
	(("PSGVAL__CLOCKS_DICT_KEYS_TIME00", FM.FMAXPSG_SCTN09FF_CLASS_DICT_DEF, "CLOCKS", "_DICT_KEYS_TIME_", "dict of time keys and their max value int seconds",), __ID__),
	(("PSGVAL__CLOCKS_DICT_KEYS_TIME01", FM.FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD, "CLOCKS", "_DICT_KEYS_TIME_", "PSG.K_TIME_S_AT_NEXT_ALERT", "CF.DAY_S", "comment",), __ID__),
	(("PSGVAL__CLOCKS_DICT_KEYS_TIME01", FM.FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD, "CLOCKS", "_DICT_KEYS_TIME_", "PSG.K_TIME_S_AT_ZEROELAPSE", "CF.DAY_S", "comment",), __ID__),
	(("PSGVAL__CLOCKS_DICT_KEYS_TIME01", FM.FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD, "CLOCKS", "_DICT_KEYS_TIME_", "PSG.K_TIME_S_CLOCK", "CF.DAY_S", "",), __ID__),
	(("PSGVAL__CLOCKS_DICT_KEYS_TIME01", FM.FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD, "CLOCKS", "_DICT_KEYS_TIME_", "PSG.K_TIME_S_ELAPSED", "CF.TIME_S_995959", "",), __ID__),
	(("PSGVAL__CLOCKS_DICT_KEYS_TIME01", FM.FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD, "CLOCKS", "_DICT_KEYS_TIME_", "PSG.K_TIME_S_TOGO", "CF.DAY_S", "",), __ID__),
	(("PSGVAL__CLOCKS_DICT_VALUES00", FM.FMAX_NOP, "FMAXPSG_SCTN09FF_CLASS_DICT_DEF", "CLOCKS", "_VALUES_", "dict to hold the virtual checkboxes etc.",), __ID__),
	(("PSGVAL__CLOCKS_DICT_VALUES01", FM.FMAX_NOP, "FMAXPSG_SCTN09FF_CLASS_DICT_DEF", "CLOCKS", "_VALUES_", "PSG.K_CHECKBOX_ALPHA_DIM", "True", "checkbox alpha dim",), __ID__),
	(("PSGVAL__CLOCKS_DICT_VALUES01", FM.FMAX_NOP, "FMAXPSG_SCTN09FF_CLASS_DICT_DEF", "CLOCKS", "_VALUES_", "PSG.K_CHECKBOX_RUNAWAY", "False", "checkbox alpha dim",), __ID__),
	(("PSGVAL__CLOCKS_DPD00", FM.FMAXPSG_SCTN09FF_CLASS_DPD_DEF, "CLOCKS", "_DPD_", "define a DPD CLOCKS:/",), __ID__),
	(("PSGVAL__CLOCKS_DPD01", FM.FMAXPSG_SCTN09FF_CLASS_DPD_VV_ADD, "CLOCKS", "_DPD_", "F___INIT__", "True", "define a DPD at /",), __ID__),
	(("PSGVAL__CLOCKS_FORMMAIN", FM.FMAX_NOP, "the form for clocks",), __ID__),
	(("PSGVAL__CLOCKS_FORMMAIN00", FM.FMAXPSG_SCTN09FF_CLASS_FORMMAIN_DEF, "CLOCKS", "_WINDOW_", "True", "the clocks form defined and done",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT", FM.FMAXPSG_SCTN09FF_CLASS_INIT_DEF, "CLOCKS", ",%ESCLN%%TAB3%keyBase_,%ESCLN%%TAB3%formName_%NEWLINE%%TAB2%", "init parms defined",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT000", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL, "CLOCKS", "_THIS_KEY_BASE_", "keyBase_", "adopt keyBase_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT001", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LAMBDA, "CLOCKS", "_USE_THIS_KEY_", "__KEY_TEXT__: %FTQ%%OBRCE%__KEY_TEXT__%CBRCE%%OBRCE%self._THIS_KEY_BASE_%CBRCE%%TQ%", "make a local key sourcer",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT002", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL, "CLOCKS", "_DICT_KEYS_", "{}", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT002", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL, "CLOCKS", "_DICT_KEYS_REVERSE_", "{}", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT002", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL, "CLOCKS", "_LIST_KEYS_TIME_", "[]", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT002", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL, "CLOCKS", "_THIS_FORM_NAME_", "formName_", "adopt formName_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_ALPHA_CHANNEL_", "PSG.SZ_ALPHA_HIGH", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_ALPHA_HIGH_", "PSG.SZ_ALPHA_HIGH", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_ALPHA_LOW_", "PSG.SZ_ALPHA_LOW", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_BBOX_", "PSG.EMPTY_BBOX", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CHANGED_EVENTS_", "False", "comment",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CHANGED_LOCATION_", "False", "comment",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CHANGED_MOUSE_LOCATION_", "False", "comment",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CHANGED_VALUES_", "False", "comment",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CLOSE_BBOX_", "PSG.EMPTY_BBOX", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENTLY_DIMMED_", "False", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_EVENTMODE_", "None", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_EVENT_", "None", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_FLIP_INDEX_", "0", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_LOCATION_", "PSG.EMPTY_XY", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_MOUSE_LOCATION_", "PSG.EMPTY_XY", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_MOUSE_STATUS_", "PSG.MOUSE_STATUS_NONE", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_VALUES_", "{}", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_MAINFRAME_", "None", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_MPX_", "PSG.EMPTY_XY", "comment",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_SCREEN_DIMS_", "PSG.EMPTY_XY", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_SIZE_", "PSG.EMPTY_XY", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_TIME_MS_AT_CHECK_MOUSE_", "PSG.ZERO_CLOCK", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_TIME_MS_AT_FLIP_", "PSG.ZERO_CLOCK", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_TIME_MS_AT_MOVE_", "PSG.ZERO_CLOCK", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_TIME_MS_AT_UPDATE_", "PSG.ZERO_CLOCK", "",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FM.FMAX_NOP, FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_CHECKBOX_ALPHA_DIM", "False", "False", "value of the alphas dim checkbox",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FM.FMAX_NOP, FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_CHECKBOX_RUNAWAY", "False", "False", "value of runaway checkbox",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FM.FMAX_NOP, FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_LIST_FLIP_INFO", "[]", "False", "the interval count and name list tup(K_CURRENT_INTERVAL_COUNT, K_NAME_NEXT_EVENT)",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FM.FMAX_NOP, FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_TIME_S_AT_NEXT_ALERT", "PSG.ZERO_CLOCK", "True", "time at next event",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FM.FMAX_NOP, FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_TIME_S_AT_ZEROELAPSE", "PSG.ZERO_CLOCK", "True", "time at last zero of elapsed timer",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FM.FMAX_NOP, FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_TIME_S_CLOCK", "PSG.ZERO_CLOCK", "True", "time clock or wall clock",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FM.FMAX_NOP, FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_TIME_S_ELAPSED", "PSG.ZERO_CLOCK", "True", "time elapsed",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FM.FMAX_NOP, FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_TIME_S_TOGO", "PSG.ZERO_CLOCK", "True", "countdown to next event",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT03_KEY01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY, "CLOCKS", "PSG.K_CHECKBOX_ALPHA_DIM", "False", "add foreign key for alpha dimming",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT03_KEY01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY, "CLOCKS", "PSG.K_CHECKBOX_RUNAWAY", "False", "add foreign key for runningaway",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT03_KEY01", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY, "CLOCKS", "PSG.K_CURRENT_INTERVAL_COUNT", "True", "add foreign key for CURRENT_INTERVAL_COUNT",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT03_LINE0100", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE, "CLOCKS", "if (self._DPD_[PSG.F___INIT__] is True):", "see if debug printing is on",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT03_LINE0101", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE, "CLOCKS", "%TAB1%self.debugPrint(", "debugPrint",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT03_LINE0102", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE, "CLOCKS", "%TAB2%title_=%DQ%__INIT__3%DQ%,", "print _DICT_KEYS_REVERSE_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT03_LINE0103", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE, "CLOCKS", "%TAB2%printDictinS_=True,", "print _DICT_KEYS_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT03_LINE0104", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE, "CLOCKS", "%TAB2%message_=%FTQ%self._DICT_KEYS {self._DICT_KEYS_}", "print _DICT_KEYS_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_00_INIT03_LINE0105", FM.FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE, "CLOCKS", "self._DICT_KEYS_REVERSE_ {self._DICT_KEYS_REVERSE_}%TQ%)", "print _DICT_KEYS_REVERSE_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_01_ENTER", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "__enter__", "__enter__.py", "False", "define __enter__",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_02_EXIT", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "__exit__", "__exit__.py", "False", "define __exit__ in CLOCKS",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_CHECK_MOUSE", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "checkMouse", "checkMouse.py", "True", "define checkMouse",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_DEBUG_PRINT", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "debugPrint", "debugPrint.py", "False", "read the frame and set self._RESULT_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_EASY_UPDATE", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "easyUpdate", "CLOCKS/easyUpdate.py", "False", "load the whole thing from the file for easyUpdate",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_EASY_UPDATEPARMS", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "easyUpdateParms", "easyUpdateParms.py", "False", "load the whole thing from the file for easyUpdate",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_ENINT", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "enint", "enint.py", "False", "read the frame and set self._RESULT_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_ENSTRING", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "enstring", "enstring.py", "False", "read the frame and set self._RESULT_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_INTERVALCOUNTOFF", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "intervalCountOff", "intervalCountOff.py", "False", "turn interval count off",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_INTERVALCOUNTON", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "intervalCountOn", "intervalCountOn.py", "False", "turn interval count on",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_QUICK_READ", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "quickRead", "quickRead.py", "False", "read the frame and set self._RESULT_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_RUNAWAY", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "runaway", "runaway.py", "True", "define runaway",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_SETCHECKBOX", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "setCheckbox", "setCheckbox.py", "True", "define setCheckbox",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_UPDATE_FLIPPED_ITEMS", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "updateFlippedItems", "updateFlippedItems.py", "False", "read the frame and set self._RESULT_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_UPDATE_FROM_DICT", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "updateFromDict", "updateFromDict.py", "False", "update the displayed info from a dict or the default _DICTIN_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_03_ZERO_FLIPPED", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "zeroFlipped", "zeroFlipped.py", "False", "update the displayed info from a dict or the default _DICTIN_",), __ID__),
	(("PSGVAL__CLOCKS_FUNC_FF_UPDATE", FM.FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "update", "CLOCKS/update.py", "False", "define the required update function",), __ID__),
	(("PSGVAL__CLOCKS_LAYOUT", FM.FMAX_NOP, "layout for APPMODE_CLOCKS",), __ID__),
	(("PSGVAL__CLOCKS_LAYOUT00", FM.FMAXPSG_SCTN09FF_CLASS_LAYOUT_DEF, "CLOCKS", "_LAYOUT_", "layout for APPMODE_CLOCKS",), __ID__),
	(("PSGVAL__CLOCKS_LAYOUT01", FM.FMAXPSG_SCTN09FF_CLASS_LAYOUT_ROW_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L03", "add a row to the layout",), __ID__),
	(("PSGVAL__CLOCKS_LAYOUT02", FM.FMAXPSG_SCTN09FF_CLASS_LAYOUT_COLUMN_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L04", "LAYOUT_E01", "add a column",), __ID__),
	(("PSGVAL__CLOCKS_LAYOUT03", FM.FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L05", "LAYOUT_E01", "layout", "self._COLUMN01_", "comment",), __ID__),
	(("PSGVAL__CLOCKS_LAYOUT04", FM.FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L05", "LAYOUT_E01", "pad", "PSG.SZ_PAD_ALL", "comment",), __ID__),
	(("PSGVAL__CLOCKS_LAYOUT05", FM.FMAXPSG_SCTN09FF_CLASS_LAYOUT_COLUMN_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L04", "LAYOUT_E02", "add a column",), __ID__),
	(("PSGVAL__CLOCKS_LAYOUT06", FM.FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L05", "LAYOUT_E02", "layout", "self._COLUMN02_", "comment",), __ID__),
	(("PSGVAL__CLOCKS_LAYOUT07", FM.FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L05", "LAYOUT_E02", "pad", "PSG.SZ_PAD_ALL", "comment",), __ID__),
	(("PSGVAL__CLOCKS_LIST_FLIPPABLE_KEYS00", FM.FMAXPSG_SCTN09FF_CLASS_LIST_DEF, "CLOCKS", "_LIST_FLIPPABLE_KEYS_", "list of the items that can be str|list[str, str, ..]",), __ID__),
	(("PSGVAL__CLOCKS_LIST_FLIPPABLE_KEYS01", FM.FMAXPSG_SCTN09FF_CLASS_LIST_VAL_ADD, "CLOCKS", "_LIST_FLIPPABLE_KEYS_", "PSG.K_TEXT_CURRENT_INTERVAL_COUNT", "list of the items that can be str|list[str, str, ..]",), __ID__),
	(("PSGVAL__CLOCKS_LIST_FLIPPABLE_KEYS01", FM.FMAXPSG_SCTN09FF_CLASS_LIST_VAL_ADD, "CLOCKS", "_LIST_FLIPPABLE_KEYS_", "PSG.K_TEXT_NAME_NEXT_EVENT", "list of the items that can be str|list[str, str, ..]",), __ID__),
	(("PSGVAL__CLOCKS_RCMENU01", FM.FMAXPSG_SCTN09FF_CLASS_RCMENU_DEF, "CLOCKS", "_RCMENU01_", "right click to do the things",), __ID__),
	(("PSGVAL__CLOCKS_RCMENU0101", FM.FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD, "CLOCKS", "_RCMENU01_", "PSG.K_BTN_QUIT_ALL", "quit by right click",), __ID__),
	(("PSGVAL__CLOCKS_RCMENU0101", FM.FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD, "CLOCKS", "_RCMENU01_", "PSG.K_BTN_XPAND", "quit by right click",), __ID__),
	(("PSGVAL__CLOCKS_RCMENU0101", FM.FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD, "CLOCKS", "_RCMENU01_", "PSG.K_BTN_ZERO", "quit by right click",), __ID__),
	(("PSGVAL__CLOCKS_RCMENU0101", FM.FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD, "CLOCKS", "_RCMENU01_", "PSG.K_CHECKBOX_ALPHA_DIM", "toggle K_CHECKBOX_ALPHA_DIM",), __ID__),
	(("PSGVAL__CLOCKS_RCMENU0101", FM.FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD, "CLOCKS", "_RCMENU01_", "PSG.K_CHECKBOX_RUNAWAY", "toggle K_CHECKBOX_RUNAWAY",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_CURRENT_INTERVAL_COUNT00", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_CURRENT_INTERVAL_COUNT_", "False", "class text for interval count",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_CURRENT_INTERVAL_COUNT01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_CURRENT_INTERVAL_COUNT_", "**PSG.TEXT_CURRENT_INTERVAL_COUNT", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_CURRENT_INTERVAL_COUNT01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_CURRENT_INTERVAL_COUNT_", "PSG.KEY", "PSG.K_CURRENT_INTERVAL_COUNT", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT00", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_NAME_NEXT_EVENT_", "False", "class text for interval count",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_NAME_NEXT_EVENT_", "**PSG.TEXT_NAME_NEXT_EVENT", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_NAME_NEXT_EVENT_", "PSG.KEY", "PSG.K_NAME_NEXT_EVENT", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_AT_ZERO00", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_TIME_S_AT_ZEROELAPSE_", "True", "class text for interval count",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_AT_ZERO01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_TIME_S_AT_ZEROELAPSE_", "**PSG.TEXT_TIME_S_AT_ZEROELAPSE", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_AT_ZERO01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_TIME_S_AT_ZEROELAPSE_", "PSG.KEY", "PSG.K_TIME_S_AT_ZEROELAPSE", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_S_AT_NEXT_ALERT00", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_TIME_S_AT_NEXT_ALERT_", "True", "class text for interval count",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_S_AT_NEXT_ALERT01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_TIME_S_AT_NEXT_ALERT_", "**PSG.TEXT_TIME_S_AT_NEXT_ALERT", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_S_AT_NEXT_ALERT01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_TIME_S_AT_NEXT_ALERT_", "PSG.KEY", "PSG.K_TIME_S_AT_NEXT_ALERT", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_S_CLOCK00", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_TIME_S_CLOCK_", "True", "class text for interval count",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_S_CLOCK01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_TIME_S_CLOCK_", "**PSG.TEXT_TIME_S_CLOCK", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_S_CLOCK01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_TIME_S_CLOCK_", "PSG.KEY", "PSG.K_TIME_S_CLOCK", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_S_ELAPSED00", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_TIME_S_ELAPSED_", "True", "class text for interval count",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_S_ELAPSED01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_TIME_S_ELAPSED_", "**PSG.TEXT_TIME_S_ELAPSED", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_S_ELAPSED01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_TIME_S_ELAPSED_", "PSG.KEY", "PSG.K_TIME_S_ELAPSED", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_S_TOGO00", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_TIME_S_TOGO_", "True", "class text for interval count",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_S_TOGO01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_TIME_S_TOGO_", "**PSG.TEXT_TIME_S_TOGO", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_TEXT_TIME_S_TOGO01", FM.FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_TIME_S_TOGO_", "PSG.KEY", "PSG.K_TIME_S_TOGO", "interval count template",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW", FM.FMAX_NOP, "the window for APPMODE_CLOCKS",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW00", FM.FMAXPSG_SCTN09FF_CLASS_WINDOW_DEF, "CLOCKS", "_WINDOW_", "define the clocks window",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW01", FM.FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "PSG.ALPHA_CHANNEL", "PSG.SZ_ALPHA_HIGH", "set the high alpha as the default",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW01", FM.FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "PSG.BACKGROUND_COLOR", "PSG.COLOR_BACKGROUND", "eliminate all not useful on the floating clocks",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW01", FM.FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "PSG.BORDER_DEPTH", "PSG.SZ_BORDER_DEPTH", "border depth to zero",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW01", FM.FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "PSG.ELEMENT_PADDING", "PSG.SZ_PAD_ALL", "all padding for elements ((1, 1), (1, 1)) by default",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW01", FM.FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "PSG.FORCE_TOPLEVEL", "None", "",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW01", FM.FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "PSG.GRAB_ANYWHERE", "True", "eliminate all not useful on the floating clocks",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW01", FM.FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "PSG.KEEP_ON_TOP", "True", "eliminate all not useful on the floating clocks",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW01", FM.FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "PSG.LAYOUT", "self._LAYOUT_", "add the layout for CLOCKS_WINDOW",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW01", FM.FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "PSG.MARGINS", "PSG.SZ_MARGINS_ALL", "",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW01", FM.FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "PSG.NO_TITLEBAR", "True", "no titlebar on APPMODE_CLOCKS window",), __ID__),
	(("PSGVAL__CLOCKS_WINDOW01", FM.FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "PSG.TITLE", "PSG.TITLE_CLOCKS", "",), __ID__),
]


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of FM/FM_TBGLST_PSG_CLOCKS_C_NEW.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


#
