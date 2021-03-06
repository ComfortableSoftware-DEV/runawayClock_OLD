

from Xlib import display as DISP
import gc
import PySimpleGUI as SG


from CF import CF


gc.enable()


#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * functions in this file
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * def getMousePos():
# * def splitBBoxToRaw(BBoxToSplit_):
# * def splitXYToRaw(XYToSplit_):
# * def fixTimeAtNext(timeToFix_):
# * def localTimes(hrs_=None, mins_=None):
# * def compareXY(XY1_, XY2_):
# * def compareBBox(BBox1_, BBox2_):
# * def getBBox(locnToBBox_, sizeToBBox_):
# * def getCloseBBox(location_, size_, closeEnough_=SZ_CLOSE):
# * def isInBBox(BBoxIn_, pointIn_):
# * def updateInterval(eventIndexToDo_):
# * def findNextAlarmEvent():
# * def doMidnightWork():
# * def doStartup():
# * def outerLoop():
# * def doit():

#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0900 DEF1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
__TIMEOUT__ = "__TIMEOUT__"  # default timeout key
APPMODE_CLOCKS = "APPMODE_CLOCKS"  # mode clocks only
APPMODE_EDIT = "APPMODE_EDIT"  # edit mode on top of main window
APPMODE_MAIN = "APPMODE_MAIN"  # main mode (xpand from clocks to this)
APPMODE_MOUSE_OVER = "APPMODE_MOUSE_OVER"  # mouseOver mode (xpand from clocks to this)
APPMODE_NEW_ALARMPOPUP = "APPMODE_NEW_ALARMPOPUP"  # main mode (xpand from clocks to this)
APPMODE_NONE = "APPMODE_NONE"  # NONE mode
APPMODE_THECLOCK = "APPMODE_THECLOCK"  # theClock mode (xpand from clocks to this)
COLOR_ALERT_BACKGROUND = "#662244"  # alert background color
COLOR_ALERT_TEXT = "#CC4466"  # color of text on alert popup
COLOR_BACKGROUND = "#331122"  # the background of the main frames
COLOR_BLACK = "#000000"  # black
COLOR_BTN_BACKGROUND = "#441133"  # background color on buttons by default
COLOR_BTN_TEXT = "#660044"  # text color on buttons by default
COLOR_CLOCK_BACKGROUND = "#221133"  # the background of the main frames
COLOR_GRAY3 = "#333333"  # gray 3
COLOR_GRAY6 = "#666666"  # gray 6
COLOR_GRAY9 = "#999999"  # gray 9
COLOR_GRAYC = "#CCCCCC"  # gray C
COLOR_TEXT_CURRENT_INTERVAL_COUNT_INACTIVE = "#999988"  # the GRAY color used when the next event is not an interval
COLOR_TEXT_HIGH = "#9900FF"  # the highlight color used in blinking bits when they are 'lit'
COLOR_TEXT_LOW = "#330022"  # the color the clock digits are
COLOR_TEXT_NORMAL = "#660044"  # the color the clock digits are
COLOR_TEXT_SPIN = "#CCFF66"  # the color the clock digits are
COLOR_TIME_CLOCK = "#CC66FF"  # color of the clock on any window/frame/etc.
COLOR_TIME_ELAPSED = "#447733"  # color of the clock on any window/frame/etc.
COLOR_TIME_TOGO = "#AA6600"  # color of the clock on any window/frame/etc.
COLOR_WHITE = "#FFFFFF"  # white
EVENTMODE_ALARM = "EVENTMODE_ALARM"  # 
EVENTMODE_INTERVAL = "EVENTMODE_INTERVAL"  # 
EVENTMODE_NONE = "EVENTMODE_NONE"  # what mode is this event
F___ENTER__ = "F___ENTER__"  # define __enter__
F___EXIT__ = "F___EXIT__"  # define __exit__ in CLOCKS
F___INIT__ = "F___INIT__"  # define a DPD at /
F_APPDSDECODE = "F_APPDSDECODE"  # fkey ENTRY appdsDecode
F_CHECKMOUSE = "F_CHECKMOUSE"  # define checkMouse
F_COMPAREBBOX = "F_COMPAREBBOX"  # FKEY entry compareBBox
F_COMPAREXY = "F_COMPAREXY"  # FKEY entry compareXY
F_DEBUGPRINT = "F_DEBUGPRINT"  # print debug info
F_DOIT = "F_DOIT"  # FKEY entry doit
F_DOMIDNIGHTWORK = "F_DOMIDNIGHTWORK"  # FKEY entry doMidnightWork
F_DOSTARTUP = "F_DOSTARTUP"  # FKEY entry doStartup
F_EASYUPDATE = "F_EASYUPDATE"  # load the whole thing from the file for easyUpdate
F_EASYUPDATEPARMS = "F_EASYUPDATEPARMS"  # load the whole thing from the file for easyUpdate
F_ENINT = "F_ENINT"  # convert any str in _DICTIN_ to int
F_ENSTRING = "F_ENSTRING"  # update _DICTINSTR_ or return strings converted from integers in _DICTIN_
F_FINDNEXTALARMEVENT = "F_FINDNEXTALARMEVENT"  # FKEY entry findNextAlarmEvent
F_FIXTIMEATNEXT = "F_FIXTIMEATNEXT"  # FKEY entry fixTimeAtNext
F_GETBBOX = "F_GETBBOX"  # FKEY entry getBBox
F_GETCLOSEBBOX = "F_GETCLOSEBBOX"  # FKEY entry getCloseBBox
F_GETMOUSEPOS = "F_GETMOUSEPOS"  # FKEY entry getMousePos
F_HANDLEEVENTS = "F_HANDLEEVENTS"  # turn interval count off
F_HANDLEVALUES = "F_HANDLEVALUES"  # turn interval count off
F_INNERLOOP = "F_INNERLOOP"  # FKEY entry doit
F_INTERVALCOUNTOFF = "F_INTERVALCOUNTOFF"  # turn interval count off
F_INTERVALCOUNTON = "F_INTERVALCOUNTON"  # turn interval count on
F_ISINBBOX = "F_ISINBBOX"  # FKEY entry isInBBox
F_LOCALTIMES = "F_LOCALTIMES"  # FKEY entry localTimes
F_MAKEINKEY = "F_MAKEINKEY"  # make a human key from a PSG key
F_MAKEOUTKEY = "F_MAKEOUTKEY"  # make a key used in PSG from a human key
F_MIDNIGHT = "F_MIDNIGHT"  # make a key used in PSG from a human key
F_OUTERLOOP = "F_OUTERLOOP"  # FKEY entry outerLoop
F_QUICKREAD = "F_QUICKREAD"  # read the frame and set self._RESULT_ etc
F_RUNAWAY = "F_RUNAWAY"  # define runaway
F_SETCHECKBOX = "F_SETCHECKBOX"  # define setCheckbox
F_SPLITBBOXTORAW = "F_SPLITBBOXTORAW"  # FKEY entry splitBBoxToRaw
F_SPLITXYTORAW = "F_SPLITXYTORAW"  # FKEY entry splitXYToRaw
F_UPDATE = "F_UPDATE"  # define the required update function
F_UPDATEFLIPPEDITEMS = "F_UPDATEFLIPPEDITEMS"  # update items which may have multiple values
F_UPDATEFROMDICT = "F_UPDATEFROMDICT"  # update the displayed info from a dict or the default _DICTIN_
F_UPDATEINTERVAL = "F_UPDATEINTERVAL"  # FKEY entry updateInterval
F_ZEROFLIPPED = "F_ZEROFLIPPED"  # update the displayed info from a dict or the default _DICTIN_
FORM_CLOCKS = "FORM_CLOCKS"  # holds all of clocks form entries
FORM_EDITENTRY = "FORM_EDITENTRY"  # holds all of form edit-entry entries
FORM_EDITOR = "FORM_EDITOR"  # holds all of form editor entries
FORM_MAIN = "FORM_MAIN"  # holds all of form main entries
FORM_POPUP01 = "FORM_POPUP01"  # holds all of form popup entries
FORM_POPUP02 = "FORM_POPUP02"  # holds all of form popup entries
FORM_POPUP03 = "FORM_POPUP03"  # holds all of form popup entries
FORM_POPUP04 = "FORM_POPUP04"  # holds all of form popup entries
FORM_POPUP05 = "FORM_POPUP05"  # holds all of form popup entries
FORM_THECLOCK = "FORM_THECLOCK"  # holds all of theclock form entries
INDEX_EAST = 2  # EAST
INDEX_NORTH = 1  # NORTH
INDEX_SOUTH = 3  # SOUTH
INDEX_WEST = 0  # WEST
INDEX_X = 0  # X
INDEX_Y = 1  # Y
K_ALARMPOPUP_TEXT_TEXT = "K_ALARMPOPUP_TEXT_TEXT"  # key for the text on a popup
K_ALERTING_LIST = "K_ALERTING_LIST"  # list that holds all currently alarming events
K_ALPHA_CHANNEL = "K_ALPHA_CHANNEL"  # 
K_ALPHA_HIGH = "K_ALPHA_HIGH"  # 
K_ALPHA_LOW = "K_ALPHA_LOW"  # 
K_APPMODE = "K_APPMODE"  # no appmode set
K_AUTO_CLOSE_DURATION = "K_AUTO_CLOSE_DURATION"  # time of this event
K_BBOX = "K_BBOX"  # 
K_BTN_DISMISS = "K_BTN_DISMISS"  # button xpand font
K_BTN_DOWN = "K_BTN_DOWN"  # focus on click
K_BTN_EDIT = "K_BTN_EDIT"  # button xpand key
K_BTN_QUIT_ALL = "K_BTN_QUIT_ALL"  # button xpand font
K_BTN_UP = "K_BTN_UP"  # button up key
K_BTN_XPAND = "K_BTN_XPAND"  # button xpand font
K_BTN_ZERO = "K_BTN_ZERO"  # button zero key
K_CHANGED_EVENTS = "K_CHANGED_EVENTS"  # comment
K_CHANGED_LOCATION = "K_CHANGED_LOCATION"  # comment
K_CHANGED_MOUSE_LOCATION = "K_CHANGED_MOUSE_LOCATION"  # comment
K_CHANGED_VALUES = "K_CHANGED_VALUES"  # comment
K_CHECKBOX_ALPHA_DIM = "K_CHECKBOX_ALPHA_DIM"  # value of the alphas dim checkbox
K_CHECKBOX_DISMISSED = "K_CHECKBOX_DISMISSED"  # set the key for the checkbox
K_CHECKBOX_ENABLED = "K_CHECKBOX_ENABLED"  # set the key for the checkbox
K_CHECKBOX_FIRSTRUN = "K_CHECKBOX_FIRSTRUN"  # set the key for the checkbox
K_CHECKBOX_HOVER_DATE = "K_CHECKBOX_HOVER_DATE"  # set the key for the checkbox
K_CHECKBOX_IS_ALERTING_NOW = "K_CHECKBOX_IS_ALERTING_NOW"  # set the key for the checkbox
K_CHECKBOX_PREDISMISSABLE = "K_CHECKBOX_PREDISMISSABLE"  # set the key for the checkbox
K_CHECKBOX_RUNAWAY = "K_CHECKBOX_RUNAWAY"  # value of runaway checkbox
K_CHECKBOX_SNOOZABLE = "K_CHECKBOX_SNOOZABLE"  # set the key for the checkbox
K_CHECKBOX_SNOOZED = "K_CHECKBOX_SNOOZED"  # set the key for the checkbox
K_CLOSE_BBOX = "K_CLOSE_BBOX"  # 
K_COLOR_ALERT_BACKGROUND = "K_COLOR_ALERT_BACKGROUND"  # alert background color
K_COLOR_ALERT_TEXT = "K_COLOR_ALERT_TEXT"  # color of text on alert popup
K_COLOR_BACKGROUND = "K_COLOR_BACKGROUND"  # the background of the main frames
K_COLOR_BLACK = "K_COLOR_BLACK"  # black
K_COLOR_BTN_BACKGROUND = "K_COLOR_BTN_BACKGROUND"  # background color on buttons by default
K_COLOR_BTN_TEXT = "K_COLOR_BTN_TEXT"  # text color on buttons by default
K_COLOR_CLOCK_BACKGROUND = "K_COLOR_CLOCK_BACKGROUND"  # the background of the main frames
K_COLOR_GRAY3 = "K_COLOR_GRAY3"  # gray 3
K_COLOR_GRAY6 = "K_COLOR_GRAY6"  # gray 6
K_COLOR_GRAY9 = "K_COLOR_GRAY9"  # gray 9
K_COLOR_GRAYC = "K_COLOR_GRAYC"  # gray C
K_COLOR_TEXT_CURRENT_INTERVAL_COUNT_INACTIVE = "K_COLOR_TEXT_CURRENT_INTERVAL_COUNT_INACTIVE"  # the GRAY color used when the next event is not an interval
K_COLOR_TEXT_HIGH = "K_COLOR_TEXT_HIGH"  # the highlight color used in blinking bits when they are 'lit'
K_COLOR_TEXT_LOW = "K_COLOR_TEXT_LOW"  # the color the clock digits are
K_COLOR_TEXT_NORMAL = "K_COLOR_TEXT_NORMAL"  # the color the clock digits are
K_COLOR_TEXT_SPIN = "K_COLOR_TEXT_SPIN"  # the color the clock digits are
K_COLOR_TIME_CLOCK = "K_COLOR_TIME_CLOCK"  # color of the clock on any window/frame/etc.
K_COLOR_TIME_ELAPSED = "K_COLOR_TIME_ELAPSED"  # color of the clock on any window/frame/etc.
K_COLOR_TIME_TOGO = "K_COLOR_TIME_TOGO"  # color of the clock on any window/frame/etc.
K_COLOR_WHITE = "K_COLOR_WHITE"  # white
K_COLORS_BTN_NORMAL = "K_COLORS_BTN_NORMAL"  # comment
K_COLORS_TEXT_HIGH = "K_COLORS_TEXT_HIGH"  # combined colors for a clock text element
K_COLORS_TEXT_LOW = "K_COLORS_TEXT_LOW"  # combined colors for a clock text element
K_COLORS_TEXT_NORMAL = "K_COLORS_TEXT_NORMAL"  # combined colors for a clock text element
K_COLORS_TIME_CLOCK = "K_COLORS_TIME_CLOCK"  # combined colors for a clock text element
K_COLORS_TIME_ELAPSED = "K_COLORS_TIME_ELAPSED"  # combined colors for a clock text element
K_COLORS_TIME_TOGO = "K_COLORS_TIME_TOGO"  # combined colors for a clock text element
K_COLUMN01A = "K_COLUMN01A"  # the column that puts the two smaller clocks below the main one
K_COLUMN01B = "K_COLUMN01B"  # the column that puts the two smaller clocks above the main one
K_COLUMN02 = "K_COLUMN02"  # the column that puts the two smaller clocks below the main one
K_CURRENT_EVENT = "K_CURRENT_EVENT"  # 
K_CURRENT_EVENTMODE = "K_CURRENT_EVENTMODE"  # 
K_CURRENT_EVENTMODE_VAL = "K_CURRENT_EVENTMODE_VAL"  # comment
K_CURRENT_FLIP_INFO = "K_CURRENT_FLIP_INFO"  # 
K_CURRENT_INTERVAL_COUNT = "K_CURRENT_INTERVAL_COUNT"  # comment
K_CURRENT_LOCATION = "K_CURRENT_LOCATION"  # 
K_CURRENT_MOUSE_LOCATION = "K_CURRENT_MOUSE_LOCATION"  # 
K_CURRENT_MOUSE_STATUS = "K_CURRENT_MOUSE_STATUS"  # 
K_CURRENT_VALUES = "K_CURRENT_VALUES"  # 
K_CURRENTLY_DIMMED = "K_CURRENTLY_DIMMED"  # 
K_DEVMODE = "K_DEVMODE"  # comment
K_DICT_ALL_THE_FORMS = "K_DICT_ALL_THE_FORMS"  # comment
K_DICT_KEYS = "K_DICT_KEYS"  # 
K_DICT_KEYS_REVERSE = "K_DICT_KEYS_REVERSE"  # 
K_DISMISSED = "K_DISMISSED"  # is this event dismissed
K_DPD_ROOT = "K_DPD_ROOT"  # DPD_ROOT defined
K_EMPTY_BBOX = "K_EMPTY_BBOX"  # empty XY dict
K_EMPTY_TUPDICT_FLIP_INFO = "K_EMPTY_TUPDICT_FLIP_INFO"  # easy dict for flip info in class passed as a list of these dicts
K_EMPTY_XY = "K_EMPTY_XY"  # empty XY dict
K_ENABLED = "K_ENABLED"  # is this event enabled
K_EVENT_ENTRIES = "K_EVENT_ENTRIES"  # 
K_EVENT_NAME = "K_EVENT_NAME"  # name of the event
K_EVENTMODE = "K_EVENTMODE"  # this entry's event_mode
K_EXITING = "K_EXITING"  # this class is currently being exited bool
K_FIRSTRUN = "K_FIRSTRUN"  # are we initializing or not
K_FONT_DEFAULT = "K_FONT_DEFAULT"  # default font my favorite readable font
K_FONTSZ_ALERT_TEXT = "K_FONTSZ_ALERT_TEXT"  # the font for the clocks only clock
K_FONTSZ_BTNS = "K_FONTSZ_BTNS"  # comment
K_FONTSZ_CLOCKS_CURRENT_INTERVAL_COUNT = "K_FONTSZ_CLOCKS_CURRENT_INTERVAL_COUNT"  # the font for the clocks only clock
K_FONTSZ_CLOCKS_TIME_S_CLOCK = "K_FONTSZ_CLOCKS_TIME_S_CLOCK"  # the font for the clocks only clock
K_FONTSZ_CLOCKS_TIME_S_ELAPSED = "K_FONTSZ_CLOCKS_TIME_S_ELAPSED"  # the font for the clocks only clock
K_FONTSZ_CLOCKS_TIME_S_TOGO = "K_FONTSZ_CLOCKS_TIME_S_TOGO"  # the font for the clocks only clock
K_FORMNAME = "K_FORMNAME"  # time of this event
K_INDEX_EAST = "K_INDEX_EAST"  # EAST
K_INDEX_NORTH = "K_INDEX_NORTH"  # NORTH
K_INDEX_OF_NEXT_EVENT = "K_INDEX_OF_NEXT_EVENT"  # holds events
K_INDEX_SOUTH = "K_INDEX_SOUTH"  # SOUTH
K_INDEX_WEST = "K_INDEX_WEST"  # WEST
K_INDEX_X = "K_INDEX_X"  # X
K_INDEX_Y = "K_INDEX_Y"  # Y
K_IS_ALERTING_NOW = "K_IS_ALERTING_NOW"  # count of number of times this has alerted since last reset
K_K_ALARMPOPUP_TEXT_TEXT = "K_K_ALARMPOPUP_TEXT_TEXT"  # alarm text for this event
K_K_EVENT_NAME = "K_K_EVENT_NAME"  # this entry's name
K_LIST_ALL_TIMES = "K_LIST_ALL_TIMES"  # list of all times
K_LIST_APPDS_MIDNIGHT_FIX_TIMES = "K_LIST_APPDS_MIDNIGHT_FIX_TIMES"  # list of times to be updated at midnight
K_LIST_CLOSE = "K_LIST_CLOSE"  # list with close statuses
K_LIST_DNUPDATE = "K_LIST_DNUPDATE"  # list of all element key not to update through the normal methods (checkboxes, etc. that need to be updated differently)
K_LIST_KEYS_TIME = "K_LIST_KEYS_TIME"  # 
K_LIST_POPUP = "K_LIST_POPUP"  # popup list
K_LIST_THIS_ALARM_POPUP_TEXT = "K_LIST_THIS_ALARM_POPUP_TEXT"  # collects the text to popup
K_MAINFRAME = "K_MAINFRAME"  # 
K_MLCN = "K_MLCN"  # short cut to get mouse position
K_MPX = "K_MPX"  # comment
K_NAME = "K_NAME"  # 
K_NAME_NEXT_EVENT = "K_NAME_NEXT_EVENT"  # interval count template
K_NAME_NEXT_EVENT_STR = "K_NAME_NEXT_EVENT_STR"  # comment
K_NOW_NOMS = "K_NOW_NOMS"  # comment
K_NOWM = "K_NOWM"  # comment
K_NOWMS = "K_NOWMS"  # comment
K_NOWS = "K_NOWS"  # comment
K_PERIODIC = "K_PERIODIC"  # 
K_PKLJAR = "K_PKLJAR"  # comment
K_PREDISMISSABLE = "K_PREDISMISSABLE"  # is this event dismissable in advance
K_SCREEN_DIMS = "K_SCREEN_DIMS"  # 
K_SIZE = "K_SIZE"  # 
K_SNOOZABLE = "K_SNOOZABLE"  # can this event be snoozed
K_SNOOZED = "K_SNOOZED"  # is this event snoozed
K_SZ_ALERT_TEXT = "K_SZ_ALERT_TEXT"  # font size of alert text
K_SZ_ALPHA_DIM = "K_SZ_ALPHA_DIM"  # default alpha dim state
K_SZ_ALPHA_HIGH = "K_SZ_ALPHA_HIGH"  # high alpha
K_SZ_ALPHA_LOW = "K_SZ_ALPHA_LOW"  # low alpha
K_SZ_BORDER_DEPTH = "K_SZ_BORDER_DEPTH"  # border depth
K_SZ_BTNS = "K_SZ_BTNS"  # font size for button text
K_SZ_CLOCKS_TIME_S_CLOCK = "K_SZ_CLOCKS_TIME_S_CLOCK"  # font size of the main clock on the clocks only floating widget
K_SZ_CLOCKS_TIME_S_ELAPSED = "K_SZ_CLOCKS_TIME_S_ELAPSED"  # font size of the elapsed clock on the clocks only floating widget
K_SZ_CLOCKS_TIME_S_TOGO = "K_SZ_CLOCKS_TIME_S_TOGO"  # font size of the main togo clock on the clocks only floating widget
K_SZ_CLOSE = "K_SZ_CLOSE"  # close enough to move from the mouse
K_SZ_CURRENT_INTERVAL_COUNT = "K_SZ_CURRENT_INTERVAL_COUNT"  # font size of the main interval count
K_SZ_EDIT_TIME_S_CLOCK = "K_SZ_EDIT_TIME_S_CLOCK"  # font size of the main clock on the clocks only floating widget
K_SZ_EDIT_TIME_S_ELAPSED = "K_SZ_EDIT_TIME_S_ELAPSED"  # font size of the elapsed clock on the clocks only floating widget
K_SZ_EDIT_TIME_S_TOGO = "K_SZ_EDIT_TIME_S_TOGO"  # font size of the main togo clock on the clocks only floating widget
K_SZ_MAIN_TIME_S_CLOCK = "K_SZ_MAIN_TIME_S_CLOCK"  # font size of the main clock on the clocks only floating widget
K_SZ_MAIN_TIME_S_ELAPSED = "K_SZ_MAIN_TIME_S_ELAPSED"  # font size of the elapsed clock on the clocks only floating widget
K_SZ_MAIN_TIME_S_TOGO = "K_SZ_MAIN_TIME_S_TOGO"  # font size of the main togo clock on the clocks only floating widget
K_SZ_MARGINS_ALL = "K_SZ_MARGINS_ALL"  # all margins default
K_SZ_MAX_DELTA = "K_SZ_MAX_DELTA"  # maximum possible change per move
K_SZ_MOVE_DIST = "K_SZ_MOVE_DIST"  # move by this pixels each jump
K_SZ_PAD_ALL = "K_SZ_PAD_ALL"  # add padding to all the things
K_SZ_PKLNAME_DEV = "K_SZ_PKLNAME_DEV"  # name of the pkl file for the app in dev
K_SZ_PKLNAME_PROD = "K_SZ_PKLNAME_PROD"  # name of the pkl file for the app in use
K_SZ_RUNAWAY = "K_SZ_RUNAWAY"  # default runaway state
K_SZ_TIME_MS_BETWEEN_FLIPS = "K_SZ_TIME_MS_BETWEEN_FLIPS"  # throttle flips
K_SZ_TIME_MS_BETWEEN_MOUSE_CHECKS = "K_SZ_TIME_MS_BETWEEN_MOUSE_CHECKS"  # throttle mouse checking
K_SZ_TIME_MS_BETWEEN_MOVES = "K_SZ_TIME_MS_BETWEEN_MOVES"  # time_ms between moves
K_SZ_TIME_MS_BETWEEN_UPDATES = "K_SZ_TIME_MS_BETWEEN_UPDATES"  # time_ms between updating windows/frames/etc
K_SZ_TIME_S_BETWEEN_PERIODIC_JOB = "K_SZ_TIME_S_BETWEEN_PERIODIC_JOB"  # time between periodic job runnings
K_SZ_TIMEOUT_MS = "K_SZ_TIMEOUT_MS"  # timeout for PSG
K_THIS_FORM_NAME = "K_THIS_FORM_NAME"  # adopt formName_
K_THIS_KEY_BASE = "K_THIS_KEY_BASE"  # adopt keyBase_
K_TIME_H_ADJUST_HRS = "K_TIME_H_ADJUST_HRS"  # comment
K_TIME_M_ADJUST_MINS = "K_TIME_M_ADJUST_MINS"  # comment
K_TIME_MS_AT_CHECK_MOUSE = "K_TIME_MS_AT_CHECK_MOUSE"  # 
K_TIME_MS_AT_FLIP = "K_TIME_MS_AT_FLIP"  # 
K_TIME_MS_AT_MOVE = "K_TIME_MS_AT_MOVE"  # 
K_TIME_MS_AT_NEXT_MOVE_VAL = "K_TIME_MS_AT_NEXT_MOVE_VAL"  # comment
K_TIME_MS_AT_NEXT_UPDATE_VAL = "K_TIME_MS_AT_NEXT_UPDATE_VAL"  # comment
K_TIME_MS_AT_UPDATE = "K_TIME_MS_AT_UPDATE"  # 
K_TIME_S_ADJUST_VALUE = "K_TIME_S_ADJUST_VALUE"  # comment
K_TIME_S_AT_ALARM = "K_TIME_S_AT_ALARM"  # time of this event if it an alarm
K_TIME_S_AT_LAST_RUN = "K_TIME_S_AT_LAST_RUN"  # time this alarm last ran, now if running
K_TIME_S_AT_NEXT_ALERT = "K_TIME_S_AT_NEXT_ALERT"  # interval count template
K_TIME_S_AT_NEXT_EVENT_VAL = "K_TIME_S_AT_NEXT_EVENT_VAL"  # comment
K_TIME_S_AT_NEXT_PERIODIC_JOB_VAL = "K_TIME_S_AT_NEXT_PERIODIC_JOB_VAL"  # seconds till next housekeeping, check for next times, etc.
K_TIME_S_AT_ZEROELAPSE = "K_TIME_S_AT_ZEROELAPSE"  # interval count template
K_TIME_S_CLOCK = "K_TIME_S_CLOCK"  # interval count template
K_TIME_S_ELAPSED = "K_TIME_S_ELAPSED"  # interval count template
K_TIME_S_INTERVAL = "K_TIME_S_INTERVAL"  # interval of this event
K_TIME_S_INTERVAL__BEGIN = "K_TIME_S_INTERVAL__BEGIN"  # time of the day this interval is made active
K_TIME_S_INTERVAL__END = "K_TIME_S_INTERVAL__END"  # time of the day this interval is no longer active
K_TIME_S_INTERVAL_START = "K_TIME_S_INTERVAL_START"  # time of the day this round of interval started
K_TIME_S_LEN_OF_ALERT = "K_TIME_S_LEN_OF_ALERT"  # length of time to alert this event before auto closing it
K_TIME_S_TOGO = "K_TIME_S_TOGO"  # interval count template
K_TITLE_ALARMPOPUP = "K_TITLE_ALARMPOPUP"  # string with window title for APPMODE_CLOCKS
K_TITLE_CLOCKS = "K_TITLE_CLOCKS"  # string with window title for APPMODE_CLOCKS
K_TITLE_EDIT = "K_TITLE_EDIT"  # string with window title for APPMODE_CLOCKS
K_TITLE_MAIN = "K_TITLE_MAIN"  # string with window title for APPMODE_CLOCKS
K_TITLE_THECLOCK = "K_TITLE_THECLOCK"  # string with window title for APPMODE_CLOCKS
K_VERSION = "K_VERSION"  # version number hex string
K_ZERO_CLOCK = "K_ZERO_CLOCK"  # all the zeros
K_ZERO_CLOCKSTR = "K_ZERO_CLOCKSTR"  # all the zeros
MOUSE_STATUS_CLOSE_E = "MOUSE_STATUS_CLOSE_E"  # mouse is east of checked element
MOUSE_STATUS_CLOSE_N = "MOUSE_STATUS_CLOSE_N"  # mouse is north of checked element
MOUSE_STATUS_CLOSE_NE = "MOUSE_STATUS_CLOSE_NE"  # mouse is northeast of checked element
MOUSE_STATUS_CLOSE_NW = "MOUSE_STATUS_CLOSE_NW"  # mouse is northwest of checked element
MOUSE_STATUS_CLOSE_S = "MOUSE_STATUS_CLOSE_S"  # mouse is south of checked element
MOUSE_STATUS_CLOSE_SE = "MOUSE_STATUS_CLOSE_SE"  # mouse is southeast of checked element
MOUSE_STATUS_CLOSE_SW = "MOUSE_STATUS_CLOSE_SW"  # mouse is southwest of checked element
MOUSE_STATUS_CLOSE_W = "MOUSE_STATUS_CLOSE_W"  # mouse is west of checked element
MOUSE_STATUS_E = "MOUSE_STATUS_E"  # mouse is east of checked element
MOUSE_STATUS_N = "MOUSE_STATUS_N"  # mouse is north of checked element
MOUSE_STATUS_NE = "MOUSE_STATUS_NE"  # mouse is northeast of checked element
MOUSE_STATUS_NONE = "MOUSE_STATUS_NONE"  # mouse is unknown
MOUSE_STATUS_NW = "MOUSE_STATUS_NW"  # mouse is northwest of checked element
MOUSE_STATUS_OVER = "MOUSE_STATUS_OVER"  # mouse is over top of checked element
MOUSE_STATUS_S = "MOUSE_STATUS_S"  # mouse is south of checked element
MOUSE_STATUS_SE = "MOUSE_STATUS_SE"  # mouse is southeast of checked element
MOUSE_STATUS_SW = "MOUSE_STATUS_SW"  # mouse is southwest of checked element
MOUSE_STATUS_W = "MOUSE_STATUS_W"  # mouse is west of checked element
SZ_ALERT_TEXT = 20  # font size of alert text
SZ_ALPHA_DIM = True  # default alpha dim state
SZ_ALPHA_HIGH = 1.0  # high alpha
SZ_ALPHA_LOW = 0.2  # low alpha
SZ_BORDER_DEPTH = 0  # border depth
SZ_BTNS = 6  # font size for button text
SZ_CLOCKS_TIME_S_CLOCK = 26  # font size of the main clock on the clocks only floating widget
SZ_CLOCKS_TIME_S_ELAPSED = 13  # font size of the elapsed clock on the clocks only floating widget
SZ_CLOCKS_TIME_S_TOGO = 13  # font size of the main togo clock on the clocks only floating widget
SZ_CLOSE = 80  # close enough to move from the mouse
SZ_CURRENT_INTERVAL_COUNT = 10  # font size of the main interval count
SZ_EDIT_TIME_S_CLOCK = 20  # font size of the main clock on the clocks only floating widget
SZ_EDIT_TIME_S_ELAPSED = 10  # font size of the elapsed clock on the clocks only floating widget
SZ_EDIT_TIME_S_TOGO = 10  # font size of the main togo clock on the clocks only floating widget
SZ_MAIN_TIME_S_CLOCK = 60  # font size of the main clock on the clocks only floating widget
SZ_MAIN_TIME_S_ELAPSED = 30  # font size of the elapsed clock on the clocks only floating widget
SZ_MAIN_TIME_S_TOGO = 30  # font size of the main togo clock on the clocks only floating widget
SZ_MARGINS_ALL = (0, 0)  # all margins default
SZ_MAX_DELTA = 100  # maximum possible change per move
SZ_MOVE_DIST = 50  # move by this pixels each jump
SZ_PAD_ALL = ((1, 1), (1, 1))  # add padding to all the things
SZ_PKLNAME_DEV = "runawayClock_DEV.pkl"  # name of the pkl file for the app in dev
SZ_PKLNAME_PROD = "runawayClock.pkl"  # name of the pkl file for the app in use
SZ_RUNAWAY = False  # default runaway state
SZ_TIME_MS_BETWEEN_FLIPS = 400  # throttle flips
SZ_TIME_MS_BETWEEN_MOUSE_CHECKS = 300  # throttle mouse checking
SZ_TIME_MS_BETWEEN_MOVES = 200  # time_ms between moves
SZ_TIME_MS_BETWEEN_UPDATES = 100  # time_ms between updating windows/frames/etc
SZ_TIME_S_BETWEEN_PERIODIC_JOB = 5000  # time between periodic job runnings
SZ_TIMEOUT_MS = 100  # timeout for PSG
TIME_H_ADJUST_HRS = 0  # comment
TIME_M_ADJUST_MINS = 0  # comment
TITLE_ALARMPOPUP = "ALERT"  # string with window title for APPMODE_CLOCKS
TITLE_CLOCKS = "CLOCKS"  # string with window title for APPMODE_CLOCKS
TITLE_EDIT = "edit an event"  # string with window title for APPMODE_CLOCKS
TITLE_MAIN = "Main window which is xpanded from CLOCKS window and pops up EDIT windows"  # string with window title for APPMODE_CLOCKS
TITLE_THECLOCK = "THECLOCK"  # string with window title for APPMODE_CLOCKS
ZERO_CLOCK = 0  # all the zeros
ZERO_CLOCKSTR = "00:00:00"  # all the zeros


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0901 DEF2
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
COLORS_BTN_NORMAL = (COLOR_TEXT_NORMAL, COLOR_BACKGROUND)  # comment
COLORS_TEXT_HIGH = (COLOR_TEXT_HIGH, COLOR_BACKGROUND)  # combined colors for a clock text element
COLORS_TEXT_LOW = (COLOR_TEXT_LOW, COLOR_BACKGROUND)  # combined colors for a clock text element
COLORS_TEXT_NORMAL = (COLOR_TEXT_NORMAL, COLOR_BACKGROUND)  # combined colors for a clock text element
COLORS_TIME_CLOCK = (COLOR_TIME_CLOCK, COLOR_CLOCK_BACKGROUND)  # combined colors for a clock text element
COLORS_TIME_ELAPSED = (COLOR_TIME_ELAPSED, COLOR_CLOCK_BACKGROUND)  # combined colors for a clock text element
COLORS_TIME_TOGO = (COLOR_TIME_TOGO, COLOR_CLOCK_BACKGROUND)  # combined colors for a clock text element
CURRENT_EVENTMODE_VAL = EVENTMODE_NONE  # comment
CURRENT_INTERVAL_COUNT = 0  # comment
DEVMODE = False  # comment
EMPTY_BBOX = (0, 0, 0, 0)  # empty XY dict
EMPTY_XY = (0, 0)  # empty XY dict
FONT_DEFAULT = "Source Code Pro"  # default font my favorite readable font
FONTSZ_ALERT_TEXT = (FONT_DEFAULT, SZ_ALERT_TEXT)  # the font for the clocks only clock
FONTSZ_BTNS = (FONT_DEFAULT, SZ_BTNS)  # comment
FONTSZ_CLOCKS_CURRENT_INTERVAL_COUNT = (FONT_DEFAULT, SZ_CURRENT_INTERVAL_COUNT)  # the font for the clocks only clock
FONTSZ_CLOCKS_TIME_S_CLOCK = (FONT_DEFAULT, SZ_CLOCKS_TIME_S_CLOCK)  # the font for the clocks only clock
FONTSZ_CLOCKS_TIME_S_ELAPSED = (FONT_DEFAULT, SZ_CLOCKS_TIME_S_ELAPSED)  # the font for the clocks only clock
FONTSZ_CLOCKS_TIME_S_TOGO = (FONT_DEFAULT, SZ_CLOCKS_TIME_S_TOGO)  # the font for the clocks only clock
MLCN = DISP.Display().screen().root.query_pointer  # short cut to get mouse position
NAME_NEXT_EVENT_STR = ""  # comment
NOW_NOMS = 0  # comment
NOWM = 0  # comment
NOWMS = 0  # comment
NOWS = 0  # comment
PKLJAR = None  # comment
TIME_MS_AT_NEXT_MOVE_VAL = 0  # comment
TIME_MS_AT_NEXT_UPDATE_VAL = 0  # comment
TIME_S_ADJUST_VALUE = lambda H_=0, M_=0: ((60 * 60 * H_) + (M_ * 60))  # comment
TIME_S_AT_NEXT_EVENT_VAL = 0  # comment
TIME_S_AT_NEXT_PERIODIC_JOB_VAL = 0  # seconds till next housekeeping, check for next times, etc.


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0910 DEF3
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
ALPHA_CHANNEL = "alpha_channel"  # 
AUTO_CLOSE = "auto_close"  # 
AUTO_CLOSE_DURATION = "auto_close_duration"  # 
AUTO_SIZE_BUTTON = "auto_size_button"  # 
AUTO_SIZE_BUTTONS = "auto_size_buttons"  # 
AUTO_SIZE_TEXT = "auto_size_text"  # 
BACKGROUND_COLOR = "background_color"  # 
BIND_RETURN_KEY = "bind_return_key"  # 
BORDER_DEPTH = "border_depth"  # 
BORDER_WIDTH = "border_width"  # 
BUTTON_COLOR = "button_color"  # 
BUTTON_TEXT = "button_text"  # 
BUTTON_TYPE = "button_type"  # 
CHANGE_SUBMITS = "change_submits"  # 
CHECKBOX_COLOR = "checkbox_color"  # color of background of the box that has the check mark in it. The checkmark is the same color as the text
CIRCLE_COLOR = "circle_color"  # 
CLICK_SUBMITS = "click_submits"  # 
DEBUGGER_ENABLED = "debugger_enabled"  # 
DEFAULT = "default"  # 
DEFAULT_BUTTON_ELEMENT_SIZE = "default_button_element_size"  # 
DEFAULT_ELEMENT_SIZE = "default_element_size"  # 
DEFAULT_EXTENSION = "default_extension"  # 
DEFAULT_VALUE = "default_value"  # 
DISABLE_CLOSE = "disable_close"  # 
DISABLE_MINIMIZE = "disable_minimize"  # 
DISABLED = "disabled"  # 
DISABLED_BUTTON_COLOR = "disabled_button_color"  # 
ELEMENT_JUSTIFICATION = "element_justification"  # 
ELEMENT_PADDING = "element_padding"  # 
ENABLE_CLOSE_ATTEMPTED_EVENT = "enable_close_attempted_event"  # 
ENABLE_EVENTS = "enable_events"  # 
ENABLED = "enabled"  # 
EXPAND_X = "expand_x"  # 
EXPAND_Y = "expand_y"  # 
FILE_TYPES = "file_types"  # 
FINALIZE = "finalize"  # 
FOCUS = "focus"  # 
FONT = "font"  # 
FORCE_TOPLEVEL = "force_toplevel"  # 
GRAB = "grab"  # 
GRAB_ANYWHERE = "grab_anywhere"  # 
GROUP_ID = "group_id"  # 
HIGHLIGHT_COLORS = "highlight_colors"  # 
ICON = "icon"  # 
IMAGE_DATA = "image_data"  # 
IMAGE_FILENAME = "image_filename"  # 
IMAGE_SIZE = "image_size"  # 
IMAGE_SUBSAMPLE = "image_subsample"  # 
INITIAL_FOLDER = "initial_folder"  # 
INITIAL_VALUE = "initial_value"  # 
JUSTIFICATION = "justification"  # 
JUSTIFICATION_CENTER = "center"  # comment
JUSTIFICATION_LEFT = "left"  # comment
JUSTIFICATION_RIGHT = "right"  # comment
K = "k"  # 
KEEP_ON_TOP = "keep_on_top"  # 
KEY = "key"  # 
LAYOUT = "layout"  # 
LOCATION = "location"  # 
MARGINS = "margins"  # 
METADATA = "metadata"  # 
MODAL = "modal"  # 
NO_TITLEBAR = "no_titlebar"  # 
NON_BLOCKING = "non_blocking"  # 
PAD = "pad"  # 
PROGRESS_BAR_COLOR = "progress_bar_color"  # 
READONLY = "readonly"  # 
RELIEF = "relief"  # 
RELIEF_FLAT = "flat"  # comment
RELIEF_GROOVE = "groove"  # 
RELIEF_RAISED = "raised"  # 
RELIEF_RIDGE = "ridge"  # 
RELIEF_SOLID = "solid"  # 
RELIEF_SUNKEN = "sunken"  # 
RESIZABLE = "resizable"  # 
RETURN_KEYBOARD_EVENTS = "return_keyboard_events"  # 
RIGHT_CLICK_MENU = "right_click_menu"  # 
RIGHT_CLICK_MENU_BACKGROUND_COLOR = "right_click_menu_background_color"  # 
RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR = "right_click_menu_disabled_text_color"  # 
RIGHT_CLICK_MENU_FONT = "right_click_menu_font"  # 
RIGHT_CLICK_MENU_SELECTED_COLORS = "right_click_menu_selected_colors"  # 
RIGHT_CLICK_MENU_TEAROFF = "right_click_menu_tearoff"  # 
RIGHT_CLICK_MENU_TEXT_COLOR = "right_click_menu_text_color"  # 
S = "s"  # 
SCROLLABLE = "scrollable"  # can this column be scrolled bool
SET_TO_INDEX = "set_to_index"  # change selection to a particular choice starting with index = 0
SIZE = "size"  # 
TARGET = "target"  # 
TEXT = "text"  # 
TEXT_COLOR = "text_color"  # 
TEXT_JUSTIFICATION = "text_justification"  # 
TIMEOUT_KEY = "timeout_key"  # 
TITLE = "title"  # 
TITLEBAR_BACKGROUND_COLOR = "titlebar_background_color"  # 
TITLEBAR_FONT = "titlebar_font"  # 
TITLEBAR_ICON = "titlebar_icon"  # 
TITLEBAR_TEXT_COLOR = "titlebar_text_color"  # 
TOOLTIP = "tooltip"  # 
TRANSPARENT_COLOR = "transparent_color"  # 
TTK_THEME = "ttk_theme"  # 
USE_CUSTOM_TITLEBAR = "use_custom_titlebar"  # 
USE_DEFAULT_FOCUS = "use_default_focus"  # 
USE_TTK_BUTTONS = "use_ttk_buttons"  # 
VALUE = "value"  # the value of the element
VALUES = "values"  # list of values
VERTICAL_ALIGNMENT = "vertical_alignment"  # 
VERTICAL_SCROLL_ONLY = "verticale_scroll_only"  # 
VISIBLE = "visible"  # visibility of elements


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0902 dicts
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
DICT_ALL_THE_FORMS = {  # comment
	FORM_CLOCKS: None,  # ENTRY IN FORMS
	FORM_POPUP01: None,  # ENTRY IN FORMS
	FORM_POPUP02: None,  # ENTRY IN FORMS
	FORM_POPUP03: None,  # ENTRY IN FORMS
	FORM_POPUP04: None,  # ENTRY IN FORMS
	FORM_POPUP05: None,  # ENTRY IN FORMS
}


DPD_ROOT = {  # DPD_ROOT defined
	F_COMPAREBBOX: False,  # DPD_ROOT entry compareBBox
	F_COMPAREXY: False,  # DPD_ROOT entry compareXY
	F_DOIT: False,  # DPD_ROOT entry doit
	F_DOMIDNIGHTWORK: False,  # DPD_ROOT entry doMidnightWork
	F_DOSTARTUP: False,  # DPD_ROOT entry doStartup
	F_FINDNEXTALARMEVENT: False,  # DPD_ROOT entry findNextAlarmEvent
	F_FIXTIMEATNEXT: False,  # DPD_ROOT entry fixTimeAtNext
	F_GETBBOX: False,  # DPD_ROOT entry getBBox
	F_GETCLOSEBBOX: False,  # DPD_ROOT entry getCloseBBox
	F_GETMOUSEPOS: False,  # DPD_ROOT entry getMousePos
	F_INNERLOOP: False,  # DPD_ROOT entry outerLoop
	F_ISINBBOX: False,  # DPD_ROOT entry isInBBox
	F_LOCALTIMES: False,  # DPD_ROOT entry localTimes
	F_OUTERLOOP: False,  # DPD_ROOT entry outerLoop
	F_SPLITBBOXTORAW: False,  # DPD_ROOT entry splitBBoxToRaw
	F_SPLITXYTORAW: False,  # DPD_ROOT entry splitXYToRaw
	F_UPDATEINTERVAL: False,  # DPD_ROOT entry updateInterval
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0903 lists
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
ALERTING_LIST = [  # list that holds all currently alarming events
]


LIST_ALL_TIMES = [  # list of all times
	K_TIME_MS_AT_CHECK_MOUSE,  # list of all times K_TIME_S_AT_CHECK_MOUSE
	K_TIME_MS_AT_FLIP,  # list of all times K_TIME_MS_AT_UPDATE
	K_TIME_MS_AT_MOVE,  # list of all times K_TIME_MS_AT_MOVE
	K_TIME_MS_AT_UPDATE,  # list of all times K_TIME_MS_AT_UPDATE
	K_TIME_S_AT_ALARM,  # list of all times K_TIME_S_AT_ALARM
	K_TIME_S_AT_LAST_RUN,  # list of all times TIME_S_AT_LAST_RUN
	K_TIME_S_AT_NEXT_ALERT,  # list of all times K_TIME_S_AT_NEXT_ALERT
	K_TIME_S_AT_ZEROELAPSE,  # list of all times K_TIME_S_AT_ZEROELAPSE
	K_TIME_S_CLOCK,  # list of all times K_TIME_S_CLOCK
	K_TIME_S_ELAPSED,  # list of all times K_TIME_S_ELAPSED
	K_TIME_S_INTERVAL,  # list of all times K_TIME_S_INTERVAL
	K_TIME_S_INTERVAL_START,  # list of all times K_TIME_S_INTERVAL_START
	K_TIME_S_INTERVAL__BEGIN,  # list of all times K_TIME_S_INTERVAL__BEGIN
	K_TIME_S_INTERVAL__END,  # list of all times K_TIME_S_INTERVAL__END
	K_TIME_S_LEN_OF_ALERT,  # list of all times K_TIME_S_LEN_OF_ALERT
	K_TIME_S_TOGO,  # list of all times K_TIME_S_TOGO
]


LIST_APPDS_MIDNIGHT_FIX_TIMES = [  # list of times to be updated at midnight
	K_TIME_MS_AT_CHECK_MOUSE,  # list of times to be updated at midnight
	K_TIME_MS_AT_MOVE,  # list of times to be updated at midnight
	K_TIME_MS_AT_UPDATE,  # list of times to be updated at midnight
	K_TIME_S_AT_NEXT_ALERT,  # list of times to be updated at midnight
]


LIST_CLOSE = [  # list with close statuses
	MOUSE_STATUS_CLOSE_E,  # easet close entry
	MOUSE_STATUS_CLOSE_N,  # easet close entry
	MOUSE_STATUS_CLOSE_NE,  # easet close entry
	MOUSE_STATUS_CLOSE_NW,  # easet close entry
	MOUSE_STATUS_CLOSE_S,  # easet close entry
	MOUSE_STATUS_CLOSE_SE,  # easet close entry
	MOUSE_STATUS_CLOSE_SW,  # easet close entry
	MOUSE_STATUS_CLOSE_W,  # easet close entry
]


LIST_DNUPDATE = [  # list of all element key not to update through the normal methods (checkboxes, etc. that need to be updated differently)
	K_CHECKBOX_ALPHA_DIM,  # checkbox for alpha under mouse
	K_CHECKBOX_DISMISSED,  # checkbox for dismissed from mouse behavior
	K_CHECKBOX_ENABLED,  # checkbox for dismissed from mouse behavior
	K_CHECKBOX_FIRSTRUN,  # checkbox for dismissed from mouse behavior
	K_CHECKBOX_HOVER_DATE,  # checkbox for dismissed from mouse behavior
	K_CHECKBOX_IS_ALERTING_NOW,  # checkbox for dismissed from mouse behavior
	K_CHECKBOX_PREDISMISSABLE,  # checkbox for dismissed from mouse behavior
	K_CHECKBOX_RUNAWAY,  # checkbox for runaway from mouse behavior
	K_CHECKBOX_SNOOZABLE,  # checkbox for dismissed from mouse behavior
	K_CHECKBOX_SNOOZED,  # checkbox for dismissed from mouse behavior
]


LIST_POPUP = [  # popup list
	FORM_POPUP01,  # popup list entry FORM_POPUP01
	FORM_POPUP02,  # popup list entry FORM_POPUP02
	FORM_POPUP03,  # popup list entry FORM_POPUP03
	FORM_POPUP04,  # popup list entry FORM_POPUP04
	FORM_POPUP05,  # popup list entry FORM_POPUP05
]


LIST_THIS_ALARM_POPUP_TEXT = [  # collects the text to popup
	"One or more events has alerted at %NOWS%",  # collects the text to popup
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0904 platform equalizers
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0905 tupdict
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTY_TUPDICT_FLIP_INFO structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY_TUPDICT_FLIP_INFOTUP = (
	(K_NAME_NEXT_EVENT, ""),  # name of next event in TUPDICT FLIP_INFO
	(K_CURRENT_INTERVAL_COUNT, 0),  # name of next event in TUPDICT FLIP_INFO
)

def EMPTY_TUPDICT_FLIP_INFODICT():
	return dict((x, y) for x, y in EMPTY_TUPDICT_FLIP_INFOTUP)


EMPTY_TUPDICT_FLIP_INFO_TDD = {
	K_NAME_NEXT_EVENT: "",  # name of next event in TUPDICT FLIP_INFO
	K_CURRENT_INTERVAL_COUNT: 0,  # name of next event in TUPDICT FLIP_INFO
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0913 right click menu options
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0906 button elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BTN_DISMISS20 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the DOWN button
	IMAGE_FILENAME: "res/dismiss20.png",  # filename for the button icon
	BORDER_WIDTH: 0,  # button xpand key
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: K_BTN_DISMISS,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_DOWN20 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the DOWN button
	IMAGE_FILENAME: "res/down20.png",  # filename for the button icon
	BORDER_WIDTH: 0,  # button xpand key
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FOCUS: True,  # focus on click
	KEY: K_BTN_DOWN,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_DOWN32 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the DOWN button
	IMAGE_FILENAME: "res/down32.png",  # filename for the button icon
	BORDER_WIDTH: 0,  # button xpand key
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: K_BTN_DOWN,  # focus on click
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_EDIT20 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the EDIT button
	IMAGE_FILENAME: "res/edit20.png",  # filename for the button icon
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: K_BTN_EDIT,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_EDIT32 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the EDIT button
	IMAGE_FILENAME: "res/edit32.png",  # filename for the button icon
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: K_BTN_EDIT,  # button xpand key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_QUIT20 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the QUIT button
	IMAGE_FILENAME: "res/quit20.png",  # filename for the button icon
	TOOLTIP: "quit the app",  # button_text empty for the QUIT button
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: K_BTN_QUIT_ALL,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_QUIT32 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the QUIT button
	IMAGE_FILENAME: "res/quit32.png",  # filename for the button icon
	TOOLTIP: "quit the app",  # button_text empty for the QUIT button
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: K_BTN_QUIT_ALL,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_UP20 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the UP button
	IMAGE_FILENAME: "res/up20.png",  # filename for the button icon
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: K_BTN_UP,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_UP32 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the UP button
	IMAGE_FILENAME: "res/up32.png",  # filename for the button icon
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: K_BTN_UP,  # button up key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_XPAND20 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the XPAND button
	IMAGE_FILENAME: "res/xpand20.png",  # filename for the button icon
	TOOLTIP: "expand to the big window from where you can edit events",  # tooltip
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: K_BTN_XPAND,  # focus on click
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_XPAND32 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the XPAND button
	IMAGE_FILENAME: "res/xpand32.png",  # filename for the button icon
	TOOLTIP: "expand to the big window from where you can edit events",  # tooltip
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: K_BTN_XPAND,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_ZERO20 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the ZERO button
	IMAGE_FILENAME: "res/zero20.png",  # filename for the button icon
	TOOLTIP: "zero the elapsed timer",  # tooltip
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: K_BTN_ZERO,  # button zero key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_ZERO32 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the ZERO button
	IMAGE_FILENAME: "res/zero32.png",  # filename for the button icon
	TOOLTIP: "zero the elapsed timer",  # tooltip
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: K_BTN_ZERO,  # button zero key
	PAD: SZ_PAD_ALL,  # button xpand key
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0907 spin box elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0908 checkbox elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
CHECKBOX_ALPHA_DIM01 = {  # checkbox for alpha under mouse
	TEXT: "K_ALPHA_LOW",  # simple text reminder
	TOOLTIP: "low alpha under mouse",  # comment
	DEFAULT: True,  # leave it on by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: K_CHECKBOX_ALPHA_DIM,  # set the key for the checkbox
}


CHECKBOX_DISMISSED01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "K_DISMISSED",  # text label
	TOOLTIP: "bool dismiss this event early",  # event has been dismissed bool
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: K_CHECKBOX_DISMISSED,  # set the key for the checkbox
}


CHECKBOX_ENABLED01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "ENABLED",  # text label
	TOOLTIP: "event enabled bool",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: K_CHECKBOX_ENABLED,  # set the key for the checkbox
}


CHECKBOX_FIRSTRUN01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "K_FIRSTRUN",  # text label
	TOOLTIP: "first run bool",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: K_CHECKBOX_FIRSTRUN,  # set the key for the checkbox
}


CHECKBOX_HOVER_DATE01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "DT on hover",  # text label
	TOOLTIP: "show date when hovering over clock",  # tooltip
	DEFAULT: True,  # leave it on by default
	ENABLE_EVENTS: True,  # set the events on for the checkbox
	KEY: K_CHECKBOX_HOVER_DATE,  # set the key for the checkbox
}


CHECKBOX_IS_ALERTING_NOW01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "IS_ALERTING_NOW",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: K_CHECKBOX_IS_ALERTING_NOW,  # set the key for the checkbox
}


CHECKBOX_PREDISMISSABLE01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "K_PREDISMISSABLE",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: K_CHECKBOX_PREDISMISSABLE,  # set the key for the checkbox
}


CHECKBOX_RUNAWAY01 = {  # checkbox for runaway from mouse behavior
	TEXT: "RUNAWAY",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: K_CHECKBOX_RUNAWAY,  # set the key for the checkbox
}


CHECKBOX_SNOOZABLE01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "K_SNOOZABLE",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: K_CHECKBOX_SNOOZABLE,  # set the key for the checkbox
}


CHECKBOX_SNOOZED01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "K_SNOOZED",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: K_CHECKBOX_SNOOZED,  # set the key for the checkbox
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0909 text elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
TEXT_ALARM_POPUP = {  # the alarm popup text bits
	TEXT: "",  # the text in the middle of the window
	BACKGROUND_COLOR: COLOR_ALERT_BACKGROUND,  # background color for the alerts
	ENABLE_EVENTS: False,  # bool is clickable
	FONT: FONTSZ_ALERT_TEXT,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # padding
	SIZE: (40, 5),  # characters, lines size line
	TEXT_COLOR: COLOR_ALERT_TEXT,  # the text color for an alert
}


TEXT_ALARM_TIME = {  # the alarm popup text bits
	TEXT: "",  # the text in the middle of the window
	BACKGROUND_COLOR: COLOR_ALERT_BACKGROUND,  # background color for the alerts
	ENABLE_EVENTS: False,  # bool is clickable
	FONT: FONTSZ_ALERT_TEXT,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # padding
	SIZE: (8, 1),  # characters, lines size line
	TEXT_COLOR: COLOR_ALERT_TEXT,  # the text color for an alert
}


TEXT_ALARM_TIME_ELAPSED = {  # the alarm popup text bits
	TEXT: "",  # the text in the middle of the window
	BACKGROUND_COLOR: COLOR_ALERT_BACKGROUND,  # background color for the alerts
	ENABLE_EVENTS: False,  # bool is clickable
	FONT: FONTSZ_ALERT_TEXT,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # padding
	SIZE: (8, 1),  # characters, lines size line
	TEXT_COLOR: COLOR_ALERT_TEXT,  # the text color for an alert
}


TEXT_ALARM_TIME_TILL_DISMISS = {  # the alarm popup text bits
	TEXT: "",  # the text in the middle of the window
	BACKGROUND_COLOR: COLOR_ALERT_BACKGROUND,  # background color for the alerts
	ENABLE_EVENTS: False,  # bool is clickable
	FONT: FONTSZ_ALERT_TEXT,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # padding
	SIZE: (8, 1),  # characters, lines size line
	TEXT_COLOR: COLOR_ALERT_TEXT,  # the text color for an alert
}


TEXT_CURRENT_INTERVAL_COUNT = {  # define the text element for CLOCKS_CLOCK_TIME
	TEXT: "0000",  # the text to fill in
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: False,  # this is clickable
	FONT: FONTSZ_CLOCKS_CURRENT_INTERVAL_COUNT,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (4, 1),  # characters, lines size line
	TEXT_COLOR: COLOR_TIME_TOGO,  # the text color for a clock_time element
}


TEXT_NAME_NEXT_EVENT = {  # define the text element for CLOCK_TIME
	TEXT: "",  # the text to fill in
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: False,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_S_TOGO,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (16, 1),  # characters, lines size line
	TEXT_COLOR: COLOR_TIME_TOGO,  # the text color for a clock_time element
}


TEXT_TIME_S_AT_NEXT_ALERT = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: False,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_S_TOGO,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (8, 1),  # characters, lines size line
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_TOGO,  # the text color for a clock_time element
}


TEXT_TIME_S_AT_ZEROELAPSE = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: False,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_S_ELAPSED,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (8, 1),  # characters, lines size line
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_ELAPSED,  # the text color for a clock_time element
}


TEXT_TIME_S_CLOCK = {  # define the text element for CLOCKS_CLOCK_TIME
	TOOLTIP: "Tue_March(03)_10_1964",  # date in the tooltip for the clock
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: True,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_S_CLOCK,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (8, 1),  # characters, lines size line
	SIZE: (8, 1),  # characters, lines size line
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_CLOCK,  # the text color for a clock_time element
}


TEXT_TIME_S_ELAPSED = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	FONT: FONTSZ_CLOCKS_TIME_S_ELAPSED,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (8, 1),  # characters, lines size line
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_ELAPSED,  # the text color for a clock_time element
}


TEXT_TIME_S_TOGO = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	FONT: FONTSZ_CLOCKS_TIME_S_TOGO,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (8, 1),  # characters, lines size line
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_TOGO,  # the text color for a clock_time element
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090A radio elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090B column elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090E layout elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090F window
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090D mainframe
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0914 popupframe
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090C APPDS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
APPDS_MAIN = {  # the struct holding everything passed betwixt PySimpleGUI and this app
	K_APPMODE: APPMODE_NONE,  # no appmode set
	K_CHECKBOX_ALPHA_DIM: True,  # dim when mouse over bool
	K_CHECKBOX_RUNAWAY: False,  # runaway from the mouse bool
	K_EVENT_ENTRIES: {  # holds events
		0: {
			K_ALARMPOPUP_TEXT_TEXT: "first event",  # alarm text for this event
			K_AUTO_CLOSE_DURATION: 10,  # time of this event
			K_CURRENT_INTERVAL_COUNT: 0,  # count of number of times this has alerted since last reset
			K_DISMISSED: False,  # is this event dismissed
			K_ENABLED: True,  # is this event enabled
			K_EVENT_NAME: "event 1",  # this entry's name
			K_EVENTMODE: EVENTMODE_INTERVAL,  # this entry's event_mode
			K_FIRSTRUN: True,  # are we initializing or not
			K_FORMNAME: None,  # time of this event
			K_IS_ALERTING_NOW: False,  # count of number of times this has alerted since last reset
			K_PREDISMISSABLE: True,  # is this event dismissable in advance
			K_SNOOZABLE: False,  # can this event be snoozed
			K_SNOOZED: False,  # is this event snoozed
			K_TIME_S_AT_ALARM: 0,  # time of this event if it an alarm
			K_TIME_S_AT_LAST_RUN: 0,  # time this alarm last ran, now if running
			K_TIME_S_AT_NEXT_ALERT: ZERO_CLOCK,  # time next time this alarm goes off
			K_TIME_S_INTERVAL: 30,  # interval of this event
			K_TIME_S_INTERVAL__BEGIN: ZERO_CLOCK,  # time of the day this interval is made active
			K_TIME_S_INTERVAL__END: ZERO_CLOCK,  # time of the day this interval is no longer active
			K_TIME_S_INTERVAL_START: ZERO_CLOCK,  # time of the day this round of interval started
			K_TIME_S_LEN_OF_ALERT: ZERO_CLOCK,  # length of time to alert this event before auto closing it
		},
		1: {
			K_ALARMPOPUP_TEXT_TEXT: "get up, move around",  # alarm text for this event
			K_AUTO_CLOSE_DURATION: 10,  # time of this event
			K_CURRENT_INTERVAL_COUNT: 0,  # count of number of times this has alerted since last reset
			K_DISMISSED: False,  # is this event dismissed
			K_ENABLED: True,  # is this event enabled
			K_EVENT_NAME: "2nd event",  # this entry's name
			K_EVENTMODE: EVENTMODE_INTERVAL,  # this entry's event_mode
			K_FIRSTRUN: True,  # are we initializing or not
			K_FORMNAME: None,  # time of this event
			K_IS_ALERTING_NOW: False,  # count of number of times this has alerted since last reset
			K_PREDISMISSABLE: True,  # is this event dismissable in advance
			K_SNOOZABLE: False,  # can this event be snoozed
			K_SNOOZED: False,  # is this event snoozed
			K_TIME_S_AT_ALARM: 0,  # time of this event if it an alarm
			K_TIME_S_AT_LAST_RUN: 0,  # time this alarm last ran, now if running
			K_TIME_S_AT_NEXT_ALERT: ZERO_CLOCK,  # time next time this alarm goes off
			K_TIME_S_INTERVAL: 15,  # interval of this event
			K_TIME_S_INTERVAL__BEGIN: ZERO_CLOCK,  # time of the day this interval is made active
			K_TIME_S_INTERVAL__END: ZERO_CLOCK,  # time of the day this interval is no longer active
			K_TIME_S_INTERVAL_START: ZERO_CLOCK,  # time of the day this round of interval started
			K_TIME_S_LEN_OF_ALERT: ZERO_CLOCK,  # length of time to alert this event before auto closing it
		},
	},
	K_INDEX_OF_NEXT_EVENT: 0,  # index of the next event to alert
	K_VERSION: "0000000D",  # version number hex string
}


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed sections of PSG.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


