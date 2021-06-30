

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FM/TBGLST_D/01_01_CF_APPDS_runawayClock_C.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

from CF.CONSTANTS import NAMES as NAMES
from FM import FM

_class_ = "APPDS_runawayClock"
_filename_ = "FM/TBGLST_D/01_01_CF_APPDS_runawayClock_C.py"
_moduleName_ = "FM"
_newFilename_ = "FM/TBGLST_D/01_01_CF_APPDS_runawayClock_C_NEW.py"
_subd0_ = "TBGLST_D"
_subd1_ = "None"
_sub0_ = "01"
_sub1_ = "01"
_sub2_ = "CF"
_sub3_ = "None"
_sub4_ = "None"
_sub5_ = "None"


_ID_ = (
	(__CLASS__, _class_,),  # APPDS_runawayClock
	(__FILENAME__, _filename_,),  # FM/TBGLST_D/01_01_CF_APPDS_runawayClock_C.py
	(__MODULENAME__, _moduleName_,),  # FM
	(__NEWFILENAME__, _newFilename_,),  # FM/TBGLST_D/01_01_CF_APPDS_runawayClock_C_NEW.py
	(__SUBD0__, _subd0_,),  # TBGLST_D
	(__SUBD1__, _subd1_,),  # None
	(__SUB0__, _sub0_,),  # 01
	(__SUB1__, _sub1_,),  # 01
	(__SUB2__, _sub2_,),  # CF
	(__SUB3__, _sub3_,),  # None
	(__SUB4__, _sub4_,),  # None
	(__SUB5__, _sub5_,),  # None
)

TBGLST = [
	(("APPDS_runawayClock_00", FM.FMAXPSG_SCTN090C_APPDS_DEF, "APPDS_runawayClock", "the struct holding everything passed betwixt PySimpleGUI and this app",), __ID__),
	(("APPDS_runawayClock_01", FM.FMAXPSG_SCTN090C_APPDS_VS_ADD, "APPDS_runawayClock", "K_VERSION", "00000013", "version number hex string",), __ID__),
	(("APPDS_runawayClock_01", FM.FMAXPSG_SCTN090C_APPDS_VV_ADD, "APPDS_runawayClock", "K_APPMODE", "APPMODE_NONE", "no appmode set",), __ID__),
	(("APPDS_runawayClock_01", FM.FMAXPSG_SCTN090C_APPDS_VV_ADD, "APPDS_runawayClock", "K_CHECKBOX_ALPHA_DIM", "True", "dim when mouse over bool",), __ID__),
	(("APPDS_runawayClock_01", FM.FMAXPSG_SCTN090C_APPDS_VV_ADD, "APPDS_runawayClock", "K_CHECKBOX_HIDE", "True", "hide under the mouse bool",), __ID__),
	(("APPDS_runawayClock_01", FM.FMAXPSG_SCTN090C_APPDS_VV_ADD, "APPDS_runawayClock", "K_CHECKBOX_HOVER_DATE", "True", "show date when the mouse hovers",), __ID__),
	(("APPDS_runawayClock_01", FM.FMAXPSG_SCTN090C_APPDS_VV_ADD, "APPDS_runawayClock", "K_CHECKBOX_RUNAWAY", "False", "runaway from the mouse bool",), __ID__),
	(("APPDS_runawayClock_01", FM.FMAXPSG_SCTN090C_APPDS_VV_ADD, "APPDS_runawayClock", "K_INDEX_OF_NEXT_EVENT", "0", "index of the next event to alert",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_DEF, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "holds events",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_ALARMPOPUP_TEXT_TEXT", "time to move a bit", "alarm text for this event",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_EVENT_NAME", "MOVE", "this entry's name",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_AUTO_CLOSE_DURATION", "10", "time of this event",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_CURRENT_INTERVAL_COUNT", "0", "count of number of times this has alerted since last reset",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_DISMISSED", "False", "is this event dismissed",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_ENABLED", "True", "is this event enabled",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_EVENTMODE", "EVENTMODE_INTERVAL", "this entry's event_mode",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_FIRSTRUN", "True", "are we initializing or not",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_FORMNAME", "None", "time of this event",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_IS_ALERTING_NOW", "False", "count of number of times this has alerted since last reset",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_PREDISMISSABLE", "True", "is this event dismissable in advance",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_SNOOZABLE", "False", "can this event be snoozed",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_SNOOZED", "False", "is this event snoozed",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_TIME_S_AT_ALARM", "0", "time of this event if it an alarm",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_TIME_S_AT_LAST_RUN", "0", "time this alarm last ran, now if running",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_TIME_S_AT_NEXT_ALERT", "ZERO_CLOCK", "time next time this alarm goes off",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_TIME_S_INTERVAL", "CF.HALFHOUR_S", "interval of this event",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_TIME_S_INTERVAL_START", "ZERO_CLOCK", "time of the day this round of interval started",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_TIME_S_INTERVAL__BEGIN", "ZERO_CLOCK", "time of the day this interval is made active",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_TIME_S_INTERVAL__END", "ZERO_CLOCK", "time of the day this interval is no longer active",), __ID__),
	(("APPDS_runawayClock_02", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "0", "K_TIME_S_LEN_OF_ALERT", "ZERO_CLOCK", "length of time to alert this event before auto closing it",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_DEF, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "holds events",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_ALARMPOPUP_TEXT_TEXT", "pee, hydrate", "alarm text for this event",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_EVENT_NAME", "WATER", "this entry's name",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_AUTO_CLOSE_DURATION", "10", "time of this event",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_CURRENT_INTERVAL_COUNT", "0", "count of number of times this has alerted since last reset",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_DISMISSED", "False", "is this event dismissed",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_ENABLED", "True", "is this event enabled",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_EVENTMODE", "EVENTMODE_INTERVAL", "this entry's event_mode",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_FIRSTRUN", "True", "are we initializing or not",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_FORMNAME", "None", "time of this event",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_IS_ALERTING_NOW", "False", "count of number of times this has alerted since last reset",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_PREDISMISSABLE", "True", "is this event dismissable in advance",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_SNOOZABLE", "False", "can this event be snoozed",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_SNOOZED", "False", "is this event snoozed",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_TIME_S_AT_ALARM", "0", "time of this event if it an alarm",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_TIME_S_AT_LAST_RUN", "0", "time this alarm last ran, now if running",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_TIME_S_AT_NEXT_ALERT", "ZERO_CLOCK", "time next time this alarm goes off",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_TIME_S_INTERVAL", "4 * CF.HOUR_S", "interval of this event",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_TIME_S_INTERVAL_START", "ZERO_CLOCK", "time of the day this round of interval started",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_TIME_S_INTERVAL__BEGIN", "ZERO_CLOCK", "time of the day this interval is made active",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_TIME_S_INTERVAL__END", "ZERO_CLOCK", "time of the day this interval is no longer active",), __ID__),
	(("APPDS_runawayClock_03", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "1", "K_TIME_S_LEN_OF_ALERT", "ZERO_CLOCK", "length of time to alert this event before auto closing it",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_DEF, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "holds events",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_ALARMPOPUP_TEXT_TEXT", "clean up for bed", "alarm text for this event",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_EVENT_NAME", "PREBED", "this entry's name",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_TIME_S_AT_ALARM", "03:30:00", "time of this event if it an alarm",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_AUTO_CLOSE_DURATION", "0", "auto close alert time of this event",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_CURRENT_INTERVAL_COUNT", "0", "count of number of times this has alerted since last reset",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_DISMISSED", "False", "is this event dismissed",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_ENABLED", "True", "is this event enabled",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_EVENTMODE", "EVENTMODE_ALARM", "this entry's event_mode",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_FIRSTRUN", "True", "are we initializing or not",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_FORMNAME", "None", "time of this event",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_IS_ALERTING_NOW", "False", "count of number of times this has alerted since last reset",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_PREDISMISSABLE", "True", "is this event dismissable in advance",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_SNOOZABLE", "False", "can this event be snoozed",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_SNOOZED", "False", "is this event snoozed",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_TIME_S_AT_LAST_RUN", "0", "time this alarm last ran, now if running",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_TIME_S_AT_NEXT_ALERT", "ZERO_CLOCK", "time next time this alarm goes off",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_TIME_S_INTERVAL", "None", "interval of this event",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_TIME_S_INTERVAL_START", "ZERO_CLOCK", "time of the day this round of interval started",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_TIME_S_INTERVAL__BEGIN", "ZERO_CLOCK", "time of the day this interval is made active",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_TIME_S_INTERVAL__END", "ZERO_CLOCK", "time of the day this interval is no longer active",), __ID__),
	(("APPDS_runawayClock_04", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "2", "K_TIME_S_LEN_OF_ALERT", "ZERO_CLOCK", "length of time to alert this event before auto closing it",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_DEF, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "holds events",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_ALARMPOPUP_TEXT_TEXT", "off to bed", "alarm text for this event",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_EVENT_NAME", "TOBED", "this entry's name",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_TIME_S_AT_ALARM", "04:00:00", "time of this event if it an alarm",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_AUTO_CLOSE_DURATION", "0", "auto close alert time of this event",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_CURRENT_INTERVAL_COUNT", "0", "count of number of times this has alerted since last reset",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_DISMISSED", "False", "is this event dismissed",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_ENABLED", "True", "is this event enabled",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_EVENTMODE", "EVENTMODE_ALARM", "this entry's event_mode",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_FIRSTRUN", "True", "are we initializing or not",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_FORMNAME", "None", "time of this event",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_IS_ALERTING_NOW", "False", "count of number of times this has alerted since last reset",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_PREDISMISSABLE", "True", "is this event dismissable in advance",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_SNOOZABLE", "False", "can this event be snoozed",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_SNOOZED", "False", "is this event snoozed",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_TIME_S_AT_LAST_RUN", "0", "time this alarm last ran, now if running",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_TIME_S_AT_NEXT_ALERT", "ZERO_CLOCK", "time next time this alarm goes off",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_TIME_S_INTERVAL", "None", "interval of this event",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_TIME_S_INTERVAL_START", "ZERO_CLOCK", "time of the day this round of interval started",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_TIME_S_INTERVAL__BEGIN", "ZERO_CLOCK", "time of the day this interval is made active",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_TIME_S_INTERVAL__END", "ZERO_CLOCK", "time of the day this interval is no longer active",), __ID__),
	(("APPDS_runawayClock_05", FM.FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_runawayClock", "K_EVENT_ENTRIES", "3", "K_TIME_S_LEN_OF_ALERT", "ZERO_CLOCK", "length of time to alert this event before auto closing it",), __ID__),
]


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of FM/TBGLST_D/01_01_CF_APPDS_runawayClock_C_NEW.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


#
