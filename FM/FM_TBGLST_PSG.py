

__FILENAME__ = "FM_TBGLST_PSG.py"
TBGLST = [
	(__FILENAME__, ("FMAXPSG", FMAX_NOP, "FMAXPSG_BEGINS",),),
	(__FILENAME__, ("FMAXPSG_SCTN0900_KEY_DEF", FMAXFM_SCTN0101_AX_DEF, "put a key in def1 of PSG.py",),),
	(__FILENAME__, ("FMAXPSG_SCTN0900_STR_DEF", FMAXFM_SCTN0101_AX_DEF, "define a string in the first section (colors, etc.) of defines in PSG.py <NAC><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0900_VAL_DEF", FMAXFM_SCTN0101_AX_DEF, "define a value in the first define section in PSG.py <NAC><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0901_DUBLT_SS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0901_DUBLT_SV_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0901_DUBLT_VS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0901_DUBLT_VV_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0901_KEY_DEF", FMAXFM_SCTN0101_AX_DEF, "define a key in the second section of defines in PSG.py <NAC><VALNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0901_STR_DEF", FMAXFM_SCTN0101_AX_DEF, "define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0901_VAL_DEF", FMAXFM_SCTN0101_AX_DEF, "define a value in the second define section in PSG.py <NAC><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0902_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a dict in PSG <NAC><DICTNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0902_DICT_SS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str-str to a dict <NAC><DICTNAME><STR><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0902_DICT_SV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str-val to a dict <NAC><DICTNAME><STR><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0902_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a dict <NAC><DICTNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0902_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a dict in PSG <NAC><DICTNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0903_LIST_DEF", FMAXFM_SCTN0101_AX_DEF, "define a list in PSG <NAC><LISTNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0903_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a list in PSG <NAC><LISTNAME><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0903_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a list in PSG <NAC><LISTNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0904_PLATEQ_ELIF_ADD", FMAXFM_SCTN0101_AX_DEF, "platform equalizer define an elif <NAC><STRUCTNAME><CONDITION><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0904_PLATEQ_ELSE_ADD", FMAXFM_SCTN0101_AX_DEF, "platform equalizer define an else <NAC><STRUCTNAME><CONDITION>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0904_PLATEQ_FUNC_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a function string line <NAC><STRUCTNAME><CONDITION>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0904_PLATEQ_IF_ADD", FMAXFM_SCTN0101_AX_DEF, "add the 1st if to a platform equalizer <NAC><STRUCTNAME><CONDITION>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0904_PLATEQ_PLAT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a platform equalizer struct <NAC><STRUCTNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0904_PLATEQ_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a string to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0904_PLATEQ_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0905_TDD_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "define a ddict <NAC><TUPDICTNAME><KEY><VAL><DDICTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0905_TDD_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "define a ddict <NAC><TUPDICTNAME><KEY><VAL><DDICTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0905_TUPDICT_DDICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a ddict <NAC><TUPDICTNAME><KEY><DDICTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0905_TUPDICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a TUPDICT in the second define section in PSG.py <NAC><TUPDICTNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0905_TUPDICT_DICT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a tupdict <NAC><TUPDICTNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0905_TUPDICT_SS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a tupdict <NAC><TUPDICTNAME><STR><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0905_TUPDICT_SV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a tupdict <NAC><TUPDICTNAME><STR><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0905_TUPDICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a tupdict <NAC><TUPDICTNAME><KEY><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0905_TUPDICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a tupdict <NAC><TUPDICTNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0906_BTN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a button <NAC><BTNNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0906_BTN_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0906_BTN_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0907_SPIN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a spin box entry <NAC><SPINNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0907_SPIN_DICT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a STR to the SPINDICT <NAC><SPINNAME><KEY><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0907_SPIN_DICT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a VAL to the SPINDICT <NAC><SPINNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0907_SPIN_VALUES_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a STR to the values list <NAC><SPINNAME><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0907_SPIN_VALUES_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a VAL to the values list <NAC><SPINNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0908_CHECKBOX_DEF", FMAXFM_SCTN0101_AX_DEF, "define a checkbox <NAC><CHECKBOXNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0908_CHECKBOX_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a checkbox <NAC><CHECKBOXNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a checkbox <NAC><CHECKBOXNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0909_TEXT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a text <NAC><TEXTNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0909_TEXT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a text element <NAC><TEXTNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0909_TEXT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a text element <NAC><TEXTNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090A_RADIO_DEF", FMAXFM_SCTN0101_AX_DEF, "define a radio button element",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_BUTTON_ADD", FMAXFM_SCTN0101_AX_DEF, "add a button to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_CHECKBOX_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_COLUMN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_COLUMN_PARM_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column parm to the column to a row <NAC><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_COLUMN_PARM_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column parm to the column to a row <NAC><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_COMBO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a column <NAC><COLUMNNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_KEY_ADD", FMAXFM_SCTN0101_AX_DEF, "add a key to a column element 'key=' will be added automatically <NAC><COLUMNNAME><ROWKEY><ELEMENTKEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_PACKEDPARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add packedparms to a column entry <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_PARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add parms to a column entry <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_RADIO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a radio to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_ROW_ADD", FMAXFM_SCTN0101_AX_DEF, "add a row [] to a column <NAC><COLUMNNAME><ROWKEY><LEVEL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_SPIN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a spinbox to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090B_COLUMN_TEXT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a text element to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090C_APPDS_DEF", FMAXFM_SCTN0101_AX_DEF, "add a nested dict holding all of the variables passed between PySimpleGUI and this app",),),
	(__FILENAME__, ("FMAXPSG_SCTN090C_APPDS_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "add a dict to the mainapp dict <NAC><DICTNAME",),),
	(__FILENAME__, ("FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a string to a dict mainapp dict <NAC><DICTNAME><KEY><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a dict mainapp dict <NAC><DICTNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090C_APPDS_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a string to the mainapp dict <NAC><KEY><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090C_APPDS_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to the mainapp dict <NAC><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090D_FORMMAIN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a frame <NAC><FRAMENAME><_WINDOW_><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)",),),
	(__FILENAME__, ("FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD", FMAXFM_SCTN0101_AX_DEF, "add a button to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090E_LAYOUT_CHECKBOX_ADD", FMAXFM_SCTN0101_AX_DEF, "add a checkbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090E_LAYOUT_COMBO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090E_LAYOUT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a layout <NAC><LAYOUTNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090E_LAYOUT_KEY_ADD", FMAXFM_SCTN0101_AX_DEF, "add a key to a layout element 'key=' will be added automatically <NAC><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090E_LAYOUT_PACKEDPARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add packedparms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add parms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090E_LAYOUT_RADIO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a radio to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090E_LAYOUT_ROW_ADD", FMAXFM_SCTN0101_AX_DEF, "add a row [] to a layout <NAC><LAYOUTNAME><ROWKEY><LEVEL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090E_LAYOUT_SPIN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a spinbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090E_LAYOUT_TEXT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a text element to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090F_WINDOW_DEF", FMAXFM_SCTN0101_AX_DEF, "define a window element <NAC><WINDOWNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090F_WINDOW_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the window element <NAC><WINDOWNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN090F_WINDOW_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the window element <NAC><WINDOWNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0910_DUBLT_SS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0910_DUBLT_SV_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0910_DUBLT_VS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0910_DUBLT_VV_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0910_STR_DEF", FMAXFM_SCTN0101_AX_DEF, "define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0910_VAL_DEF", FMAXFM_SCTN0101_AX_DEF, "define a value in the second define section in PSG.py <NAC><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0911_COMBO_DEF", FMAXFM_SCTN0101_AX_DEF, "define a combo box <NAC><COMBOBOXNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0912_FRAMEELEMENT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a frame element <NAC><FENAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0913_RCMENU_DEF", FMAXFM_SCTN0101_AX_DEF, "define a right click menu <NAC><RCMENUNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0913_RCMENU_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a right click menu <NAC><RCMENUNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0914_FORMPOPUP_DEF", FMAXFM_SCTN0101_AX_DEF, "define a frame <NAC><FRAMENAME><_WINDOW_><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)",),),
	(__FILENAME__, ("FMAXPSG_SCTN0915_PUDLG_DEF", FMAXFM_SCTN0101_AX_DEF, "define a popup dialog <NAC><POPUPNAME><POPUPTYPE>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0915_PUDLG_DICT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a text element <NAC><POPUPNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a text element <NAC><POPUPNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0915_PUDLG_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a text element <NAC><POPUPNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN0915_PUDLG_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a text element <NAC><POPUPNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_BTN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a button <NAC><CLASSNAME><BTNNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_BTN_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_BTN_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_CHECKBOX_DEF", FMAXFM_SCTN0101_AX_DEF, "define a checkbox <NAC><CLASSNAME><CHECKBOXNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_CHECKBOX_PARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add a parameter to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_CHECKBOX_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_CHECKBOX_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_BUTTON_ADD", FMAXFM_SCTN0101_AX_DEF, "add a button to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_CHECKBOX_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_PARM_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_PARM_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_COMBO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a column <NAC><CLASSNAME><COLUMNNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_KEY_ADD", FMAXFM_SCTN0101_AX_DEF, "add a key to a column element 'key=' will be added automatically <NAC><CLASSNAME><COLUMNNAME><ROWKEY><ELEMENTKEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_PACKEDPARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add packedparms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add parms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_RADIO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a radio to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD", FMAXFM_SCTN0101_AX_DEF, "add a row [] to a column <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_SPIN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a spinbox to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a text element to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_COMBO_DEF", FMAXFM_SCTN0101_AX_DEF, "define a combo box <NAC><COMBOBOXNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a dict in PSG <NAC><CLASSNAME><DICTNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_DICT_SS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str-str to a dict <NAC><CLASSNAME><DICTNAME><STR><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_DICT_SV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str-val to a dict <NAC><CLASSNAME><DICTNAME><STR><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a dict <NAC><CLASSNAME><DICTNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a dict in PSG <NAC><CLASSNAME><DICTNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_DPD_DEF", FMAXFM_SCTN0101_AX_DEF, "define a DPD debugPrintDict in PSG <NAC><CLASSNAME><DPDNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_DPD_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a DPD debugPrintDict in PSG <NAC><CLASSNAME><DPDNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FORMMAIN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class mainframe",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FORMPOPUP_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class mainframe",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FRAMEELEMENT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a frame element",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FUNCTION_BLANKLINE", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><FUNCNAME><PARMS>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><FUNCNAME><PARMS>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><FUNCNAME><FILENAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FUNCTION_LAMBDA1_DEF", FMAXFM_SCTN0101_AX_DEF, "add a lambda to the top of a function, usually for absorbing things",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FUNCTION_LAMBDA2_DEF", FMAXFM_SCTN0101_AX_DEF, "add a lambda to the top of a function, usually for absorbing things",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FUNCTION_LINE_ADD", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><FUNCNAME><LINE>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FUNCTION_READ_FROM_FILE", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><FUNCNAME><FILENAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FUNCTION_STR1_DEF", FMAXFM_SCTN0101_AX_DEF, "define a string in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FUNCTION_STR2_DEF", FMAXFM_SCTN0101_AX_DEF, "define a string in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FUNCTION_VAL1_DEF", FMAXFM_SCTN0101_AX_DEF, "define a value in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_FUNCTION_VAL2_DEF", FMAXFM_SCTN0101_AX_DEF, "define a value in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LAMBDA", FMAXFM_SCTN0101_AX_DEF, "define a string in the class <NAC><CLASSNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LINE", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><LINE>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_READ_FROM_FILE", FMAXFM_SCTN0101_AX_DEF, "read a section of __init__ from a file in res/functions <NAC><CLASSNAME><FILENAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_STR", FMAXFM_SCTN0101_AX_DEF, "define a string in the class <NAC><CLASSNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL", FMAXFM_SCTN0101_AX_DEF, "define a value in the class <NAC><CLASSNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_SS", FMAXFM_SCTN0101_AX_DEF, "add a str-str to a dict <NAC><CLASSNAME><STR><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_SV", FMAXFM_SCTN0101_AX_DEF, "add a str-val to a dict <NAC><CLASSNAME><STR><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VS", FMAXFM_SCTN0101_AX_DEF, "add a str to a dict <NAC><CLASSNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV", FMAXFM_SCTN0101_AX_DEF, "add a val to a dict in PSG <NAC><CLASSNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY", FMAXFM_SCTN0101_AX_DEF, "add values to _DICT_KEYS, _DICT_KEYS_REVERSE_ for external elements like buttons and checkboxes <NAC><CLASSNAME><KEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_LAMBDA", FMAXFM_SCTN0101_AX_DEF, "define a value in the class <NAC><CLASSNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_LINE", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><LINE>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_READ_FROM_FILE", FMAXFM_SCTN0101_AX_DEF, "read a section of __init__ from a file in res/functions <NAC><CLASSNAME><FILENAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_STR", FMAXFM_SCTN0101_AX_DEF, "define a string in the class <NAC><CLASSNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL", FMAXFM_SCTN0101_AX_DEF, "define a value in the class <NAC><CLASSNAME><VALNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><LINE>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_INIT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><PARMS>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_BUTTON_ADD", FMAXFM_SCTN0101_AX_DEF, "add a button to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_CHECKBOX_ADD", FMAXFM_SCTN0101_AX_DEF, "add a checkbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_COLUMN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_COMBO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a layout <NAC><CLASSNAME><LAYOUTNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_DEF", FMAXFM_SCTN0101_AX_DEF, "define layouts",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_KEY_ADD", FMAXFM_SCTN0101_AX_DEF, "add a key to a layout element 'key=' will be added automatically <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_PACKEDPARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add packedparms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add parms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_RADIO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a radio to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_ROW_ADD", FMAXFM_SCTN0101_AX_DEF, "add a row [] to a layout <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_SPIN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a spinbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LAYOUT_TEXT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a text element to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LIST_DEF", FMAXFM_SCTN0101_AX_DEF, "define a list in PSG <NAC><CLASSNAME><LISTNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a list in PSG <NAC><CLASSNAME><LISTNAME><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a list in PSG <NAC><CLASSNAME><LISTNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_RADIO_DEF", FMAXFM_SCTN0101_AX_DEF, "define a radio button element",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_RCMENU_DEF", FMAXFM_SCTN0101_AX_DEF, "define a right click menu",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a right click menu",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_SPIN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a spin box entry <NAC><CLASSNAME><SPINNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_SPIN_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a STR to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_SPIN_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a VAL to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_SPIN_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a STR to the values list <NAC><CLASSNAME><SPINNAME><STR>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_SPIN_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a VAL to the values list <NAC><CLASSNAME><SPINNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_TEXT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a text <NAC><CLASSNAME><TEXTNAME><ISATIME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add a PARM to a text element <NAC><CLASSNAME><TEXTNAME><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_TEXT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a text element <NAC><CLASSNAME><TEXTNAME><KEY><VAL>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a text element <NAC><CLASSNAME><TEXTNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_WINDOW_DEF", FMAXFM_SCTN0101_AX_DEF, "define a main dictdict <NAC><CLASSNAME><MAINNAME>",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_WINDOW_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),),
	(__FILENAME__, ("FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),),
	(__FILENAME__, ("FMPSG", FMAX_NOP, "FMPSG_BEGINS",),),
	(__FILENAME__, ("FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)",),),
	(__FILENAME__, ("FMPSG_SCTN0900_DEF1_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0900_DEF1_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0901_DEF2_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0901",),),
	(__FILENAME__, ("FMPSG_SCTN0901_DEF2_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0901",),),
	(__FILENAME__, ("FMPSG_SCTN0902_DICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0902",),),
	(__FILENAME__, ("FMPSG_SCTN0902_DICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0902",),),
	(__FILENAME__, ("FMPSG_SCTN0903_LIST_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0903",),),
	(__FILENAME__, ("FMPSG_SCTN0903_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0903",),),
	(__FILENAME__, ("FMPSG_SCTN0904_PLATEQ_INNER_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0904",),),
	(__FILENAME__, ("FMPSG_SCTN0904_PLATEQ_INNER_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0904",),),
	(__FILENAME__, ("FMPSG_SCTN0904_PLATEQ_OUTER_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0904",),),
	(__FILENAME__, ("FMPSG_SCTN0904_PLATEQ_OUTER_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0904",),),
	(__FILENAME__, ("FMPSG_SCTN0905_TUPDICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0905",),),
	(__FILENAME__, ("FMPSG_SCTN0905_TUPDICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0905",),),
	(__FILENAME__, ("FMPSG_SCTN0905_TUPDICT_TDD_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0905",),),
	(__FILENAME__, ("FMPSG_SCTN0906_BTNS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0906_BTNS_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0907_SPIN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)f",),),
	(__FILENAME__, ("FMPSG_SCTN0907_SPIN_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)",),),
	(__FILENAME__, ("FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)",),),
	(__FILENAME__, ("FMPSG_SCTN0908_CHECKBOX_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0908_CHECKBOX_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0909_TEXT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0909_TEXT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN090A_RADIO_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN090A_RADIO_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN090B_COLUMN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN090B_COLUMN_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN090B_COLUMN_PARMS_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN090C_APPDSDICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "the main app dict+dict for this app",),),
	(__FILENAME__, ("FMPSG_SCTN090C_APPDS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "the main app dict for this app",),),
	(__FILENAME__, ("FMPSG_SCTN090C_APPDS_DICT", FMAXFM_SCTN0103_DICT_DEF, "the main app dict for this app",),),
	(__FILENAME__, ("FMPSG_SCTN090D_FORMMAIN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN090D_FORMMAIN_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN090E_LAYOUT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN090E_LAYOUT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN090F_WINDOW_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN090F_WINDOW_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0910_DEF3_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0910_DEF3_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0911_COMBO_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0911_COMBO_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0912_FRAME_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0912_FRAME_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0913_RCMENU_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0913_RCMENU_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0914_FORMPOPUP_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0914_FORMPOPUP_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0915_PUDLG_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0915_PUDLG_DICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0915_PUDLG_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN0915_PUDLG_TYPE_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_BTNS_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_BTNS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_BTNS_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_CHECKBOX_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_CHECKBOX_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_COLUMN_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_COLUMN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_COLUMN_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_COLUMN_PARMS_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_COMBO_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_COMBO_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_COMBO_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_DEF_DICT", FMAXFM_SCTN0103_DICT_DEF, "str and val defines in a class",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_DICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_FRAME_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_FRAME_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_FRAME_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_FUNCTION_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_FUNCTION_DEF1_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_FUNCTION_DEF2_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_FUNCTION_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_INIT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_INIT_DEF3_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_INIT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_LAYOUT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_LAYOUT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_LIST_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_RADIO_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_RADIO_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_RADIO_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_RCMENU_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_RCMENU_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_RCMENU_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_SPIN_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_SPIN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)f",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_SPIN_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_TEXT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_TEXT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_WINDOW_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_SCTN09FF_CLASS_WINDOW_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),),
	(__FILENAME__, ("FMPSG_____", FMAX_NOP, "FMPSG_ENDS",),),
]
