

from Xlib import display as DISP
import gc
import PySimpleGUI as SG


import CF


gc.enable()


#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0900 DEF1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
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
COLOR_TEXT_HIGH = "#9900FF"  # the highlight color used in blinking bits when they are 'lit'
COLOR_TEXT_INTERVAL_COUNT_INACTIVE = "#999988"  # the GRAY color used when the next event is not an interval
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
K_ALARMPOPUP_PROPER = "K_ALARMPOPUP_PROPER"  # key for the button return for the popup
K_ALARMPOPUP_TEXT_TEXT = "K_ALARMPOPUP_TEXT_TEXT"  # key for the text on a popup
K_ALPHA_CHANNEL = "K_ALPHA_CHANNEL"  # alpha channel key
K_ALPHA_HIGH = "K_ALPHA_HIGH"  # alphahigh key
K_ALPHA_LOW = "K_ALPHA_LOW"  # 
K_APPMODE = "K_APPMODE"  # app mode key
K_AUTO_CLOSE_DURATION = "K_AUTO_CLOSE_DURATION"  # 
K_BBOX = "K_BBOX"  # 
K_BTN_DISMISS = "K_BTN_DISMISS"  # 
K_BTN_DOWN = "K_BTN_DOWN"  # 
K_BTN_EDIT = "K_BTN_EDIT"  # 
K_BTN_QUIT_ALL = "K_BTN_QUIT_ALL"  # 
K_BTN_QUIT_EDITOR = "K_BTN_QUIT_EDITOR"  # 
K_BTN_UP = "K_BTN_UP"  # 
K_BTN_XPAND = "K_BTN_XPAND"  # 
K_BTN_ZERO = "K_BTN_ZERO"  # 
K_CHANGED_EVENTS = "K_CHANGED_EVENTS"  # 
K_CHANGED_VALUES = "K_CHANGED_VALUES"  # 
K_CHECKBOX_ALPHA_DIM = "K_CHECKBOX_ALPHA_DIM"  # is the clock transparent under mouse (ineffective if mouse is avoided)
K_CHECKBOX_DISMISSED = "K_CHECKBOX_DISMISSED"  # key for avoiding the mouse bool
K_CHECKBOX_ENABLED = "K_CHECKBOX_ENABLED"  # key for avoiding the mouse bool
K_CHECKBOX_FIRSTRUN = "K_CHECKBOX_FIRSTRUN"  # key for avoiding the mouse bool
K_CHECKBOX_HOVER_DATE = "K_CHECKBOX_HOVER_DATE"  # KEY FOR K_CHECKBOX_HOVER_DATE
K_CHECKBOX_IS_ALERTING_NOW = "K_CHECKBOX_IS_ALERTING_NOW"  # key for avoiding the mouse bool
K_CHECKBOX_PREDISMISSABLE = "K_CHECKBOX_PREDISMISSABLE"  # key for avoiding the mouse bool
K_CHECKBOX_RUNAWAY = "K_CHECKBOX_RUNAWAY"  # key for avoiding the mouse bool
K_CHECKBOX_SNOOZABLE = "K_CHECKBOX_SNOOZABLE"  # key for avoiding the mouse bool
K_CHECKBOX_SNOOZED = "K_CHECKBOX_SNOOZED"  # key for avoiding the mouse bool
K_CLOSE_BBOX = "K_CLOSE_BBOX"  # 
K_COLUMN01 = "K_COLUMN01"  # 
K_COLUMN02 = "K_COLUMN02"  # 
K_CURRENT_EVENT = "K_CURRENT_EVENT"  # 
K_CURRENT_EVENTMODE = "K_CURRENT_EVENTMODE"  # 
K_CURRENT_LOCATION = "K_CURRENT_LOCATION"  # 
K_CURRENT_MOUSE_LOCATION = "K_CURRENT_MOUSE_LOCATION"  # 
K_CURRENT_MOUSE_STATUS = "K_CURRENT_MOUSE_STATUS"  # 
K_CURRENT_VALUE = "K_CURRENT_VALUE"  # 
K_CURRENTLY_DIMMED = "K_CURRENTLY_DIMMED"  # 
K_DICT_KEYS_INT = "K_DICT_KEYS_INT"  # 
K_DICT_KEYS_TIME = "K_DICT_KEYS_TIME"  # 
K_DICTIN = "K_DICTIN"  # 
K_DICTINSTR = "K_DICTINSTR"  # 
K_DICTOUT = "K_DICTOUT"  # 
K_DISMISSED = "K_DISMISSED"  # alarm dismissed bool
K_ENABLED = "K_ENABLED"  # 
K_EVENT_ENTRIES = "K_EVENT_ENTRIES"  # 
K_EVENT_NAME = "K_EVENT_NAME"  # name of the event
K_EVENTMODE = "K_EVENTMODE"  # what mode is this event
K_FIRSTRUN = "K_FIRSTRUN"  # True if just started, false after init1()
K_FORM_NAME = "K_FORM_NAME"  # the name of the form
K_INDEX_OF_NEXT_EVENT = "K_INDEX_OF_NEXT_EVENT"  # index of the next event to alert
K_INTERVAL_COUNT = "K_INTERVAL_COUNT"  # count of the number of times since last reset this interval has triggered an alert
K_IS_ALERTING_NOW = "K_IS_ALERTING_NOW"  # 
K_KEY_DICT = "K_KEY_DICT"  # 
K_KEY_DICT_REVERSE = "K_KEY_DICT_REVERSE"  # 
K_KEY_LIST_TIMES = "K_KEY_LIST_TIMES"  # 
K_LAST_EVENT = "K_LAST_EVENT"  # 
K_LAST_LOCATION = "K_LAST_LOCATION"  # 
K_LAST_MOUSE_LOCATION = "K_LAST_MOUSE_LOCATION"  # 
K_LAST_MOUSE_STATUS = "K_LAST_MOUSE_STATUS"  # 
K_LAST_VALUES = "K_LAST_VALUES"  # 
K_LAYOUT = "K_LAYOUT"  # 
K_MAINFRAME = "K_MAINFRAME"  # 
K_MPX = "K_MPX"  # 
K_NAME = "K_NAME"  # 
K_NAME_NEXT_EVENT = "K_NAME_NEXT_EVENT"  # name of the next event up
K_PERIODIC = "K_PERIODIC"  # 
K_PREDISMISSABLE = "K_PREDISMISSABLE"  # event can be dismissed in advance
K_SCREEN_DIMS = "K_SCREEN_DIMS"  # 
K_SIZE = "K_SIZE"  # 
K_SNOOZABLE = "K_SNOOZABLE"  # can this event be snoozed
K_SNOOZED = "K_SNOOZED"  # is this event snoozed bool
K_TEXT_INTERVAL_COUNT = "K_TEXT_INTERVAL_COUNT"  # 
K_TEXT_NAME_NEXT_EVENT = "K_TEXT_NAME_NEXT_EVENT"  # 
K_TEXT_TIME_AT_NEXT_ALERT = "K_TEXT_TIME_AT_NEXT_ALERT"  # 
K_TEXT_TIME_AT_ZEROELAPSE = "K_TEXT_TIME_AT_ZEROELAPSE"  # 
K_TEXT_TIME_CLOCK = "K_TEXT_TIME_CLOCK"  # 
K_TEXT_TIME_ELAPSED = "K_TEXT_TIME_ELAPSED"  # 
K_TEXT_TIME_TOGO = "K_TEXT_TIME_TOGO"  # 
K_THIS_FORM_NAME = "K_THIS_FORM_NAME"  # 
K_THIS_KEY_BASE = "K_THIS_KEY_BASE"  # 
K_TIME_ALARM = "K_TIME_ALARM"  # the alarm time
K_TIME_AT_LAST_RUN = "K_TIME_AT_LAST_RUN"  # timeS of last alarm 
K_TIME_AT_NEXT_ALERT = "K_TIME_AT_NEXT_ALERT"  # what time is the next alarm, == KEY_TIME_ALARM is tomorrow
K_TIME_AT_ZEROELAPSE = "K_TIME_AT_ZEROELAPSE"  # the time at last zero to keep elapsed time accurate despite other things hogging CPU time
K_TIME_CLOCK = "K_TIME_CLOCK"  # the main clock time
K_TIME_ELAPSED = "K_TIME_ELAPSED"  # key for all clocks elapsed
K_TIME_INTERVAL = "K_TIME_INTERVAL"  # interval timer starting time, reset each time the interval goes off
K_TIME_INTERVAL__BEGIN = "K_TIME_INTERVAL__BEGIN"  # key for time interval starts alerting
K_TIME_INTERVAL__END = "K_TIME_INTERVAL__END"  # key for time an interval goes to leep and stops alerting
K_TIME_INTERVAL_START = "K_TIME_INTERVAL_START"  # interval timer starting time, reset each time the interval goes off
K_TIME_LEN_OF_ALERT = "K_TIME_LEN_OF_ALERT"  # length of alerting
K_TIME_TO_CHECK_MOUSE = "K_TIME_TO_CHECK_MOUSE"  # 
K_TIME_TO_MOVE = "K_TIME_TO_MOVE"  # 
K_TIME_TO_UPDATE = "K_TIME_TO_UPDATE"  # 
K_TIME_TOGO = "K_TIME_TOGO"  # down counter to next event on this window/alarm/interval/reminder
K_USE_THIS_KEY = "K_USE_THIS_KEY"  # 
K_WINDOW = "K_WINDOW"  # 
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
SZ_CLOCKS_TIME_CLOCK = 26  # font size of the main clock on the clocks only floating widget
SZ_CLOCKS_TIME_ELAPSED = 13  # font size of the elapsed clock on the clocks only floating widget
SZ_CLOCKS_TIME_TOGO = 13  # font size of the main togo clock on the clocks only floating widget
SZ_CLOSE = 80  # close enough to move from the mouse
SZ_EDIT_TIME_CLOCK = 20  # font size of the main clock on the clocks only floating widget
SZ_EDIT_TIME_ELAPSED = 10  # font size of the elapsed clock on the clocks only floating widget
SZ_EDIT_TIME_TOGO = 10  # font size of the main togo clock on the clocks only floating widget
SZ_INTERVAL_COUNT = 10  # font size of the main interval count
SZ_MAIN_TIME_CLOCK = 60  # font size of the main clock on the clocks only floating widget
SZ_MAIN_TIME_ELAPSED = 30  # font size of the elapsed clock on the clocks only floating widget
SZ_MAIN_TIME_TOGO = 30  # font size of the main togo clock on the clocks only floating widget
SZ_MARGINS_ALL = (0, 0)  # all margins default
SZ_MAX_DELTA = 100  # maximum possible change per move
SZ_MOVE_DIST = 50  # move by this pixels each jump
SZ_PAD_ALL = ((1, 1), (1, 1))  # add padding to all the things
SZ_RUNAWAY = False  # default runaway state
SZ_TIMEMS_BETWEEN_MOUSE_CHECKS = 300  # throttle mouse checking
SZ_TIMEMS_BETWEEN_MOVES = 500  # time_ms between moves
SZ_TIMEMS_BETWEEN_UPDATES = 500  # time_ms between updating windows/frames/etc
SZ_TIMEOUT_MS = 100  # timeout for PSG
SZ_TIMES_BTWN_PERIODIC_JOB = 900  # time between periodic job runnings
TIMEH_ADJUST_HRS = 0  # comment
TIMEM_ADJUST_MINS = 0  # comment
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
_pklJar_ = None  # comment
COLORS_BTN_NORMAL = (COLOR_TEXT_NORMAL, COLOR_BACKGROUND)  # comment
COLORS_TEXT_HIGH = (COLOR_TEXT_HIGH, COLOR_BACKGROUND)  # combined colors for a clock text element
COLORS_TEXT_LOW = (COLOR_TEXT_LOW, COLOR_BACKGROUND)  # combined colors for a clock text element
COLORS_TEXT_NORMAL = (COLOR_TEXT_NORMAL, COLOR_BACKGROUND)  # combined colors for a clock text element
COLORS_TIME_CLOCK = (COLOR_TIME_CLOCK, COLOR_CLOCK_BACKGROUND)  # combined colors for a clock text element
COLORS_TIME_ELAPSED = (COLOR_TIME_ELAPSED, COLOR_CLOCK_BACKGROUND)  # combined colors for a clock text element
COLORS_TIME_TOGO = (COLOR_TIME_TOGO, COLOR_CLOCK_BACKGROUND)  # combined colors for a clock text element
CURRENT_EVENTMODE_VAL = EVENTMODE_NONE  # comment
CURRENT_INTERVAL_COUNT = 0  # comment
EMPTY_BBOX = (0, 0, 0, 0)  # empty XY dict
EMPTY_XY = (0, 0)  # empty XY dict
FONT_DEFAULT = "Source Code Pro"  # default font my favorite readable font
FONTSZ_ALERT_TEXT = (FONT_DEFAULT, SZ_ALERT_TEXT)  # the font for the clocks only clock
FONTSZ_BTNS = (FONT_DEFAULT, SZ_BTNS)  # comment
FONTSZ_CLOCKS_INTERVAL_COUNT = (FONT_DEFAULT, SZ_INTERVAL_COUNT)  # the font for the clocks only clock
FONTSZ_CLOCKS_TIME_CLOCK = (FONT_DEFAULT, SZ_CLOCKS_TIME_CLOCK)  # the font for the clocks only clock
FONTSZ_CLOCKS_TIME_ELAPSED = (FONT_DEFAULT, SZ_CLOCKS_TIME_ELAPSED)  # the font for the clocks only clock
FONTSZ_CLOCKS_TIME_TOGO = (FONT_DEFAULT, SZ_CLOCKS_TIME_TOGO)  # the font for the clocks only clock
MLCN = DISP.Display().screen().root.query_pointer  # short cut to get mouse position
NOW_NOMS = 0  # comment
NOWM = 0  # comment
NOWMS = 0  # comment
NOWS = 0  # comment
TIME_S_ADJUST_VALUE = lambda H_=0, M_=0: ((60 * 60 * H_) + (M_ * 60))  # comment
TIME_S_AT_NEXT_EVENT = 0  # comment
TIME_S_AT_NEXT_PERIODIC_JOB = 0  # seconds till next housekeeping, check for next times, etc.
TIMEMS_NEXT_MOUSE_CHECK = 0  # comment
TIMEMS_NEXT_MOVED = 0  # comment
TIMEMS_NEXT_UPDATED = 0  # comment
TIMES_ADJUST_VALUE = lambda H_=0, M_=0: ((60 * 60 * H_) + (M_ * 60))  # comment


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
K_LAYOUT = "layout"  # 
K_SIZE = "size"  # 
KEEP_ON_TOP = "keep_on_top"  # 
KEY = "key"  # 
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
ALL_THE_FORMS = {  # comment
	FORM_CLOCKS: None,  # ENTRY IN FORMS
	FORM_EDITENTRY: None,  # ENTRY IN FORMS
	FORM_EDITOR: None,  # ENTRY IN FORMS
	FORM_MAIN: None,  # ENTRY IN FORMS
	FORM_POPUP01: None,  # ENTRY IN FORMS
	FORM_POPUP02: None,  # ENTRY IN FORMS
	FORM_POPUP03: None,  # ENTRY IN FORMS
	FORM_POPUP04: None,  # ENTRY IN FORMS
	FORM_POPUP05: None,  # ENTRY IN FORMS
	FORM_THECLOCK: None,  # ENTRY IN FORMS
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0903 lists
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
ALERTING_LIST = [  # list that holds all currently alarming events
]


APPDS_TIMES_LIST = [  # build the list of all times in APPDS_MAIN that need midnight attention
	K_TIME_AT_NEXT_ALERT,  # build the list of all times in APPDS_MAIN
]


CLOSE_LIST = [  # list with close statuses
	MOUSE_STATUS_CLOSE_E,  # easet close entry
	MOUSE_STATUS_CLOSE_N,  # easet close entry
	MOUSE_STATUS_CLOSE_NE,  # easet close entry
	MOUSE_STATUS_CLOSE_NW,  # easet close entry
	MOUSE_STATUS_CLOSE_S,  # easet close entry
	MOUSE_STATUS_CLOSE_SE,  # easet close entry
	MOUSE_STATUS_CLOSE_SW,  # easet close entry
	MOUSE_STATUS_CLOSE_W,  # easet close entry
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0904 platform equalizers
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0905 tupdict
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
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
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: K_CHECKBOX_DISMISSED,  # set the key for the checkbox
}


CHECKBOX_ENABLED01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "ENABLED",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: K_CHECKBOX_ENABLED,  # set the key for the checkbox
}


CHECKBOX_FIRSTRUN01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "K_FIRSTRUN",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
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
TEXT_INTERVAL_COUNT = {  # define the text element for CLOCKS_CLOCK_TIME
	TEXT: "0000",  # the text to fill in
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: False,  # this is clickable
	FONT: FONTSZ_CLOCKS_INTERVAL_COUNT,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	K_SIZE: (4, 1),  # characters, lines size line
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_TOGO,  # the text color for a clock_time element
}


TEXT_NAME_NEXT_EVENT = {  # define the text element for CLOCK_TIME
	TEXT: "",  # the text to fill in
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: False,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_TOGO,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	K_SIZE: (16, 1),  # characters, lines size line
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_TOGO,  # the text color for a clock_time element
}


TEXT_TIME_AT_NEXT_ALERT = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: False,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_TOGO,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	K_SIZE: (8, 1),  # characters, lines size line
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_TOGO,  # the text color for a clock_time element
}


TEXT_TIME_AT_ZEROELAPSE = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: False,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_ELAPSED,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	K_SIZE: (8, 1),  # characters, lines size line
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_ELAPSED,  # the text color for a clock_time element
}


TEXT_TIME_CLOCK = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: True,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_CLOCK,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	K_SIZE: (8, 1),  # characters, lines size line
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_CLOCK,  # the text color for a clock_time element
}


TEXT_TIME_ELAPSED = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	FONT: FONTSZ_CLOCKS_TIME_ELAPSED,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	K_SIZE: (8, 1),  # characters, lines size line
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_ELAPSED,  # the text color for a clock_time element
}


TEXT_TIME_TOGO = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	FONT: FONTSZ_CLOCKS_TIME_TOGO,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	K_SIZE: (8, 1),  # characters, lines size line
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
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
# * SCTN09FF classes
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


class CLASS_CLOCKS(object):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	global \
		ALL_THE_FORMS

	def __init__(self, keyBase_, formName_):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		self._THIS_KEY_BASE_ = keyBase_  # adopt keyBase_
		self._USE_THIS_KEY_ = lambda __KEY_TEXT__: f"""{__KEY_TEXT__}{self._THIS_KEY_BASE_}"""  # make a local key sourcer
		self._THIS_FORM_NAME_ = formName_  # adopt formName_

		self._ALPHA_CHANNEL_ = SZ_ALPHA_HIGH  # 
		self._ALPHA_HIGH_ = SZ_ALPHA_HIGH  # 
		self._ALPHA_LOW_ = SZ_ALPHA_LOW  # 
		self._BBOX_ = EMPTY_BBOX  # 
		self._CHANGED_EVENTS_ = False  # comment
		self._CHANGED_VALUES_ = False  # comment
		self._CHECKBOX_ALPHA_DIM_ = SZ_ALPHA_DIM  # 
		self._CHECKBOX_RUNAWAY_ = SZ_RUNAWAY  # 
		self._CLOSE_BBOX_ = EMPTY_BBOX  # 
		self._CURRENTLY_DIMMED_ = False  # 
		self._CURRENT_EVENTMODE_ = None  # 
		self._CURRENT_EVENT_ = None  # 
		self._CURRENT_LOCATION_ = EMPTY_XY  # 
		self._CURRENT_MOUSE_LOCATION_ = EMPTY_XY  # 
		self._CURRENT_MOUSE_STATUS_ = MOUSE_STATUS_NONE  # 
		self._CURRENT_VALUES = {}  # 
		self._KEY_DICT_ = {}  # 
		self._KEY_DICT_REVERSE_ = {}  # 
		self._KEY_LIST_TIMES_ = []  # 
		self._LAST_EVENT_ = None  # 
		self._LAST_LOCATION_ = EMPTY_XY  # 
		self._LAST_MOUSE_LOCATION_ = EMPTY_XY  # 
		self._LAST_MOUSE_STATUS_ = MOUSE_STATUS_NONE  # 
		self._LAST_VALUES_ = {}  # 
		self._MAINFRAME_ = None  # 
		self._MPX_ = EMPTY_XY  # comment
		self._SCREEN_DIMS_ = EMPTY_XY  # 
		self._SIZE_ = EMPTY_XY  # 
		self._TIME_TO_CHECK_MOUSE_ = ZERO_CLOCK  # 
		self._TIME_TO_MOVE_ = ZERO_CLOCK  # 
		self._TIME_TO_UPDATE_ = ZERO_CLOCK  # 

		self._DICTIN_ = {
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			K_NAME_NEXT_EVENT: "",  # name of next event
			K_CHECKBOX_ALPHA_DIM: False,  # value of the alphas dim checkbox
			K_CHECKBOX_RUNAWAY: False,  # value of runaway checkbox
			K_INTERVAL_COUNT: 0,  # interval count
			K_TIME_AT_NEXT_ALERT: ZERO_CLOCK,  # time at next event
			K_TIME_AT_ZEROELAPSE: ZERO_CLOCK,  # time at last zero of elapsed timer
			K_TIME_CLOCK: ZERO_CLOCK,  # time clock or wall clock
			K_TIME_ELAPSED: ZERO_CLOCK,  # time elapsed
			K_TIME_TOGO: ZERO_CLOCK,  # countdown to next event
		}
# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._DICTINSTR_ = {
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			f"""{self._USE_THIS_KEY_(K_NAME_NEXT_EVENT)}""": "",  # name of next event
			K_CHECKBOX_ALPHA_DIM: False,  # value of the alphas dim checkbox
			K_CHECKBOX_RUNAWAY: False,  # value of runaway checkbox
			f"""{self._USE_THIS_KEY_(K_INTERVAL_COUNT)}""": 0,  # interval count
			f"""{self._USE_THIS_KEY_(K_TIME_AT_NEXT_ALERT)}""": ZERO_CLOCK,  # time at next event
			f"""{self._USE_THIS_KEY_(K_TIME_AT_ZEROELAPSE)}""": ZERO_CLOCK,  # time at last zero of elapsed timer
			f"""{self._USE_THIS_KEY_(K_TIME_CLOCK)}""": ZERO_CLOCK,  # time clock or wall clock
			f"""{self._USE_THIS_KEY_(K_TIME_ELAPSED)}""": ZERO_CLOCK,  # time elapsed
			f"""{self._USE_THIS_KEY_(K_TIME_TOGO)}""": ZERO_CLOCK,  # countdown to next event
		}
# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._DICTOUT_ = {  # holds the values for the clocks frame
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			K_CHECKBOX_ALPHA_DIM: "True",  # name of next event
			K_CHECKBOX_RUNAWAY: False,  # interval count
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._DICT_KEYS_INT_ = {  # dict of integer keys and their format
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			K_INTERVAL_COUNT: "04d",  # intervalCount:04d
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._DICT_KEYS_TIME_ = {  # dict of time keys and their max value int seconds
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			K_TIME_AT_NEXT_ALERT: CF.DAYSECS,  # comment
			K_TIME_AT_ZEROELAPSE: CF.DAYSECS,  # comment
			K_TIME_CLOCK: CF.DAYSECS,  # 
			K_TIME_ELAPSED: CF.TIME995959,  # 
			K_TIME_TOGO: CF.DAYSECS,  # 
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._PERIODIC_ = {  # periodic updates dict for the clocks frame
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			K_TIME_AT_NEXT_ALERT: ZERO_CLOCK,  # time at next event
			K_TIME_AT_ZEROELAPSE: ZERO_CLOCK,  # time at last zero of elapsed timer
			K_TIME_CLOCK: ZERO_CLOCK,  # time clock or wall clock
			K_TIME_ELAPSED: ZERO_CLOCK,  # time elapsed
			K_TIME_TOGO: ZERO_CLOCK,  # countdown to next event
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._TEXT_INTERVAL_COUNT_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_INTERVAL_COUNT,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(K_INTERVAL_COUNT)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._KEY_DICT_[K_INTERVAL_COUNT] = f"""{self._USE_THIS_KEY_(K_INTERVAL_COUNT)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(K_INTERVAL_COUNT)}"""] = K_INTERVAL_COUNT

		self._TEXT_NAME_NEXT_EVENT_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_NAME_NEXT_EVENT,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(K_NAME_NEXT_EVENT)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._KEY_DICT_[K_NAME_NEXT_EVENT] = f"""{self._USE_THIS_KEY_(K_NAME_NEXT_EVENT)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(K_NAME_NEXT_EVENT)}"""] = K_NAME_NEXT_EVENT

		self._TEXT_TIME_AT_NEXT_ALERT_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_TIME_AT_NEXT_ALERT,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(K_TIME_AT_NEXT_ALERT)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._KEY_LIST_TIMES_.append(TEXT_TIME_AT_NEXT_ALERT)
		self._KEY_LIST_TIMES_.append(self._USE_THIS_KEY_(TEXT_TIME_AT_NEXT_ALERT))
		self._KEY_DICT_[K_TIME_AT_NEXT_ALERT] = f"""{self._USE_THIS_KEY_(K_TIME_AT_NEXT_ALERT)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(K_TIME_AT_NEXT_ALERT)}"""] = K_TIME_AT_NEXT_ALERT

		self._TEXT_TIME_AT_ZEROELAPSE_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_TIME_AT_ZEROELAPSE,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(K_TIME_AT_ZEROELAPSE)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._KEY_LIST_TIMES_.append(TEXT_TIME_AT_ZEROELAPSE)
		self._KEY_LIST_TIMES_.append(self._USE_THIS_KEY_(TEXT_TIME_AT_ZEROELAPSE))
		self._KEY_DICT_[K_TIME_AT_ZEROELAPSE] = f"""{self._USE_THIS_KEY_(K_TIME_AT_ZEROELAPSE)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(K_TIME_AT_ZEROELAPSE)}"""] = K_TIME_AT_ZEROELAPSE

		self._TEXT_TIME_CLOCK_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_TIME_CLOCK,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(K_TIME_CLOCK)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._KEY_LIST_TIMES_.append(TEXT_TIME_CLOCK)
		self._KEY_LIST_TIMES_.append(self._USE_THIS_KEY_(TEXT_TIME_CLOCK))
		self._KEY_DICT_[K_TIME_CLOCK] = f"""{self._USE_THIS_KEY_(K_TIME_CLOCK)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(K_TIME_CLOCK)}"""] = K_TIME_CLOCK

		self._TEXT_TIME_ELAPSED_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_TIME_ELAPSED,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(K_TIME_ELAPSED)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._KEY_LIST_TIMES_.append(TEXT_TIME_ELAPSED)
		self._KEY_LIST_TIMES_.append(self._USE_THIS_KEY_(TEXT_TIME_ELAPSED))
		self._KEY_DICT_[K_TIME_ELAPSED] = f"""{self._USE_THIS_KEY_(K_TIME_ELAPSED)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(K_TIME_ELAPSED)}"""] = K_TIME_ELAPSED

		self._TEXT_TIME_TOGO_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_TIME_TOGO,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(K_TIME_TOGO)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._KEY_LIST_TIMES_.append(TEXT_TIME_TOGO)
		self._KEY_LIST_TIMES_.append(self._USE_THIS_KEY_(TEXT_TIME_TOGO))
		self._KEY_DICT_[K_TIME_TOGO] = f"""{self._USE_THIS_KEY_(K_TIME_TOGO)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(K_TIME_TOGO)}"""] = K_TIME_TOGO

		self._COLUMN01_ = [  # the column that puts the two smaller clocks below the main one
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			[
				SG.Text(  # add a new TEXT element to clocks column
					**self._TEXT_TIME_CLOCK_  # add the main clock
				),
			],
			[
				SG.Text(  # add a new row to clocks column
					**self._TEXT_TIME_AT_ZEROELAPSE_  # add time to go
				),
				SG.Text(  # add a new text element to row01 clocks column
					**self._TEXT_TIME_ELAPSED_  # add elapsed time
				),
			],
			[
				SG.Text(  # add a new text element to row01 clocks column
					**self._TEXT_TIME_TOGO_  # add elapsed time
				),
				SG.Text(  # add a new row to clocks column
					**self._TEXT_TIME_AT_NEXT_ALERT_  # add time to go
				),
			],
			[
				SG.Text(  # add a new text element to row01 clocks column
					**self._TEXT_NAME_NEXT_EVENT_  # add the main clock
				),
			],
			[
				SG.Checkbox(  # add a new text element to row01 clocks column
					**CHECKBOX_RUNAWAY01  # add elapsed time
				),
				SG.Checkbox(  # add a new text element to row01 clocks column
					**CHECKBOX_ALPHA_DIM01  # add elapsed time
				),
			],
		]
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._COLUMN02_ = [  # the column that puts the two smaller clocks below the main one
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			[
				SG.Button(  # add a button element to clocks column
					**BTN_QUIT20  # add the xpand button to clocks
				),
			],
			[
				SG.Button(  # add reset button for elapsed time
					**BTN_ZERO20  # add the zero button to clocks
				),
			],
			[
				SG.Button(  # add reset button for elapsed time
					**BTN_XPAND20  # add the zero button to clocks
				),
			],
			[
				SG.Text(  # add reset button for elapsed time
					**self._TEXT_INTERVAL_COUNT_  # add the zero button to clocks
				),
			],
		]
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._LAYOUT_ = [  # layout for APPMODE_CLOCKS
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			[
				SG.Column(  # add a column
					layout=self._COLUMN01_,  # comment
					pad=SZ_PAD_ALL,  # comment
				),
				SG.Column(  # add a column
					layout=self._COLUMN02_,  # comment
					pad=SZ_PAD_ALL,  # comment
				),
			],
		]
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._WINDOW_ = {  # define the clocks window
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			ALPHA_CHANNEL: SZ_ALPHA_HIGH,  # set the high alpha as the default
			BACKGROUND_COLOR: COLOR_BACKGROUND,  # eliminate all not useful on the floating clocks
			BORDER_DEPTH: SZ_BORDER_DEPTH,  # border depth to zero
			ELEMENT_PADDING: SZ_PAD_ALL,  # all padding for elements ((1, 1), (1, 1)) by default
			FORCE_TOPLEVEL: None,  # 
			GRAB_ANYWHERE: True,  # eliminate all not useful on the floating clocks
			KEEP_ON_TOP: True,  # eliminate all not useful on the floating clocks
			K_LAYOUT: self._LAYOUT_,  # add the layout for CLOCKS_WINDOW
			MARGINS: SZ_MARGINS_ALL,  # 
			NO_TITLEBAR: True,  # no titlebar on APPMODE_CLOCKS window
			TITLE: TITLE_CLOCKS,  # 
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self.__CDS__ = {
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			K_COLUMN01: self._COLUMN01_,  # the column that puts the two smaller clocks below the main one
			K_COLUMN02: self._COLUMN02_,  # the column that puts the two smaller clocks below the main one
			K_DICTOUT: self._DICTOUT_,  # holds the values for the clocks frame
			K_DICT_KEYS_INT: self._DICT_KEYS_INT_,  # dict of integer keys and their format
			K_DICT_KEYS_TIME: self._DICT_KEYS_TIME_,  # dict of time keys and their max value int seconds
			K_DICTIN: self._DICTIN_,
			K_DICTINSTR: self._DICTINSTR_,
			K_THIS_KEY_BASE: self._THIS_KEY_BASE_,
			K_USE_THIS_KEY: self._USE_THIS_KEY_,
			K_THIS_FORM_NAME: self._THIS_FORM_NAME_,
			K_ALPHA_CHANNEL: self._ALPHA_CHANNEL_,
			K_ALPHA_HIGH: self._ALPHA_HIGH_,
			K_ALPHA_LOW: self._ALPHA_LOW_,
			K_BBOX: self._BBOX_,
			K_CHANGED_EVENTS: self._CHANGED_EVENTS_,
			K_CHANGED_VALUES: self._CHANGED_VALUES_,
			K_CHECKBOX_ALPHA_DIM: self._CHECKBOX_ALPHA_DIM_,
			K_CHECKBOX_RUNAWAY: self._CHECKBOX_RUNAWAY_,
			K_CLOSE_BBOX: self._CLOSE_BBOX_,
			K_CURRENTLY_DIMMED: self._CURRENTLY_DIMMED_,
			K_CURRENT_EVENTMODE: self._CURRENT_EVENTMODE_,
			K_CURRENT_EVENT: self._CURRENT_EVENT_,
			K_CURRENT_LOCATION: self._CURRENT_LOCATION_,
			K_CURRENT_MOUSE_LOCATION: self._CURRENT_MOUSE_LOCATION_,
			K_CURRENT_MOUSE_STATUS: self._CURRENT_MOUSE_STATUS_,
			K_CURRENT_VALUE: self._CURRENT_VALUES,
			K_KEY_DICT: self._KEY_DICT_,
			K_KEY_DICT_REVERSE: self._KEY_DICT_REVERSE_,
			K_KEY_LIST_TIMES: self._KEY_LIST_TIMES_,
			K_LAST_EVENT: self._LAST_EVENT_,
			K_LAST_LOCATION: self._LAST_LOCATION_,
			K_LAST_MOUSE_LOCATION: self._LAST_MOUSE_LOCATION_,
			K_LAST_MOUSE_STATUS: self._LAST_MOUSE_STATUS_,
			K_LAST_VALUES: self._LAST_VALUES_,
			K_MAINFRAME: self._MAINFRAME_,
			K_MPX: self._MPX_,
			K_SCREEN_DIMS: self._SCREEN_DIMS_,
			K_SIZE: self._SIZE_,
			K_TIME_TO_CHECK_MOUSE: self._TIME_TO_CHECK_MOUSE_,
			K_TIME_TO_MOVE: self._TIME_TO_MOVE_,
			K_TIME_TO_UPDATE: self._TIME_TO_UPDATE_,
			K_LAYOUT: self._LAYOUT_,  # layout for APPMODE_CLOCKS
			K_PERIODIC: self._PERIODIC_,  # periodic updates dict for the clocks frame
			K_TEXT_INTERVAL_COUNT: self._TEXT_INTERVAL_COUNT_,  # class text for interval count
			K_TEXT_NAME_NEXT_EVENT: self._TEXT_NAME_NEXT_EVENT_,  # class text for interval count
			K_TEXT_TIME_AT_NEXT_ALERT: self._TEXT_TIME_AT_NEXT_ALERT_,  # class text for interval count
			K_TEXT_TIME_AT_ZEROELAPSE: self._TEXT_TIME_AT_ZEROELAPSE_,  # class text for interval count
			K_TEXT_TIME_CLOCK: self._TEXT_TIME_CLOCK_,  # class text for interval count
			K_TEXT_TIME_ELAPSED: self._TEXT_TIME_ELAPSED_,  # class text for interval count
			K_TEXT_TIME_TOGO: self._TEXT_TIME_TOGO_,  # class text for interval count
			K_WINDOW: self._WINDOW_,  # define the clocks window
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	def __enter__(self):
		global \
			ALL_THE_FORMS
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		self._MAINFRAME_ = SG.Window(**self._WINDOW_).finalize()
		ALL_THE_FORMS[self._THIS_FORM_NAME_] = self
		# return self
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def __exit__(self, *args_):
		global \
			ALL_THE_FORMS
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		self._MAINFRAME_.close()
		ALL_THE_FORMS[self._THIS_FORM_NAME_] = None
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def checkMouse(self):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if NOWMS < self._TIME_TO_CHECK_MOUSE_:
			return

		self._TIME_TO_CHECK_MOUSE_ = NOWMS + SZ_TIMEMS_BETWEEN_MOUSE_CHECKS
		_statusToRtn_ = None
		_mpxToRtn_ = (0, 0)
		_TLcn_ = self._LOCATION_
		_TSizeX_, _TSizeY_ = _TSize_ = self._SIZE_
		_TMouseLcnX_, _TMouseLcnY_ = _TMouseLcn_ = getMousePos()
		_TBBoxWest_, _TBBoxNorth_, _TBBoxEast_, _TBBoxSouth_ = _TBBox_ = self._BBOX_
		_TCloseBBox_ = self._CLOSE_BBOX_
		_isInCloseBBox_ = isInBBox(_TCloseBBox_, _TMouseLcn_)

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (_TBBoxWest_ < _TMouseLcnX_ < _TBBoxEast_) and (_TMouseLcnY_ < _TBBoxNorth_):
			_mpxToRtn_ = (0, 1)
			if _isInCloseBBox_ is True:
				_statusToRtn_ = MOUSE_STATUS_CLOSE_N
			else:
				_statusToRtn_ = MOUSE_STATUS_N

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif ( _TBBoxWest_ < _TMouseLcnX_ < _TBBoxEast_) and (_TMouseLcnY_ > _TBBoxSouth_):
			_mpxToRtn_ = (0, -1)
			if _isInCloseBBox_ is True:
				_statusToRtn_ = MOUSE_STATUS_CLOSE_S
			else:
				_statusToRtn_ = MOUSE_STATUS_S

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_TMouseLcnX_ < _TBBoxWest_) and (_TBBoxNorth_< _TMouseLcnY_ < _TBBoxSouth_):
			_mpxToRtn_ = (1, 0)
			if _isInCloseBBox_ is True:
				_statusToRtn_ = MOUSE_STATUS_CLOSE_W
			else:
				_statusToRtn_ = MOUSE_STATUS_W

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_TMouseLcnX_ > _TBBoxEast_) and (_TBBoxNorth_< _TMouseLcnY_ < _TBBoxSouth_):
			_mpxToRtn_ = (-1, 0)
			if _isInCloseBBox_ is True:
				_statusToRtn_ = MOUSE_STATUS_CLOSE_E
			else:
				_statusToRtn_ = MOUSE_STATUS_E

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_TMouseLcnY_ > _TBBoxSouth_) and (_TMouseLcnX_ < _TBBoxWest_):
			_mpxToRtn_ = (1, -1)
			if _isInCloseBBox_ is True:
				_statusToRtn_ = MOUSE_STATUS_CLOSE_SW
			else:
				_statusToRtn_ = MOUSE_STATUS_SW

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_TMouseLcnY_ > _TBBoxSouth_) and (_TMouseLcnX_ > _TBBoxEast_):
			_mpxToRtn_ = (-1, -1)
			if _isInCloseBBox_ is True:
				_statusToRtn_ = MOUSE_STATUS_CLOSE_SE
			else:
				_statusToRtn_ = MOUSE_STATUS_SE

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_TMouseLcnY_ < _TBBoxNorth_) and (_TMouseLcnX_ < _TBBoxWest_):
			_mpxToRtn_ = (1, 1)
			if _isInCloseBBox_ is True:
				_statusToRtn_ = MOUSE_STATUS_CLOSE_NW
			else:
				_statusToRtn_ = MOUSE_STATUS_NW

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_TMouseLcnY_ < _TBBoxNorth_) and (_TMouseLcnX_ > _TBBoxEast_):
			_mpxToRtn_ = (-1, 1)
			if _isInCloseBBox_ is True:
				_statusToRtn_ = MOUSE_STATUS_CLOSE_NE
			else:
				_statusToRtn_ = MOUSE_STATUS_NE

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif isInBBox(_TBBox_, _TMouseLcn_) is True:
			_mpxToRtn_ = (0, 0)
			_statusToRtn_ = MOUSE_STATUS_OVER
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (_statusToRtn_ == MOUSE_STATUS_OVER) and (self._LAST_MOUSE_STATUS_ != MOUSE_STATUS_OVER) and (self._CHECKBOX_ALPHA_DIM_ is True):
			self._MAINFRAME_.AlphaChannel = self._ALPHA_LOW_
			self._DIMMED_ = True

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif ((_statusToRtn_ != MOUSE_STATUS_OVER) and (self._LAST_MOUSE_STATUS_ == MOUSE_STATUS_OVER)) or ((self._LAST_MOUSE_STATUS_ == MOUSE_STATUS_OVER) and (self._DIMMED_ is True) and (self._CHECKBOX_ALPHA_DIM_ is False)):
			self._MAINFRAME_.AlphaChannel = self._ALPHA_HIGH_
			alphaMode = False
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self._LAST_MOUSE_STATUS_ = _statusToRtn_
		self._MOUSE_STATUS_ = _statusToRtn_
		self._MPX_ = _mpxToRtn_

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def easyUpdate(self,
			checkboxAlphaDim_=None,
			checkboxRunaway_=None,
			eventMode_=None,
			currentIntervalCount_=None,
			nameNextEvent_=None,
			timeAtNextAlert_=None,
			timeAtZeroelapse_=None,
			timeClock_=None,
			timeElapsed_=None,
			timeTogo_=None,
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if nameNextEvent_ is not None:
			self._DICTIN_[K_NAME_NEXT_EVENT] = nameNextEvent_

		if checkboxAlphaDim_ is not None:
			self._DICTIN_[K_CHECKBOX_ALPHA_DIM] = checkboxAlphaDim_

		if checkboxRunaway_ is not None:
			self._DICTIN_[K_CHECKBOX_RUNAWAY] = checkboxRunaway_

		if eventMode_ is not None:
			self.CURRENT_EVENTMODE = eventMode_

			if currentIntervalCount_ is not None:
				self._DICTIN_[K_INTERVAL_COUNT] = currentIntervalCount_

			if (eventMode_ == EVENTMODE_INTERVAL):
				self.intervalCountOn()
			else:
				self.intervalCountOff()

		if timeAtNextAlert_ is not None:
			self._DICTIN_[K_TIME_AT_NEXT_ALERT] = timeAtNextAlert_

		if timeAtZeroelapse_ is not None:
			self._DICTIN_[K_TIME_AT_ZEROELAPSE] = timeAtZeroelapse_

		if timeClock_ is not None:
			self._DICTIN_[K_TIME_CLOCK] = timeClock_

		if timeElapsed_ is not None:
			self._DICTIN_[K_TIME_ELAPSED] = timeElapsed_

		if timeTogo_ is not None:
			self._DICTIN_[K_TIME_TOGO] = timeTogo_

		self.enint()
		self.updateFromDict()
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def enint(self):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		_thisDictin_ = self._DICTIN_
		_dictToRtn_ = {}
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisKey_, _thisVal_ in _thisDictin_.items():
			_isInstanceOfStr_ = isinstance(_thisDictin_[_thisKey_], str)
			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if (_isInstanceOfStr_ is True):
				if (_thisKey_ in self._DICT_KEYS_TIME_):
					_dictToRtn_[_thisKey_] = CF.HMSToNrmlInt(_thisDictin_[_thisKey_])

				elif (_thisKey_ in self._DICT_KEYS_INT_):
					_dictToRtn_[self._DICT_KEYS_TIME_[_thisKey_]] = int(_thisDictin_[_thisKey_])

				else:
					_dictToRtn_[_thisKey_] = _thisDictin_[_thisKey_]

		self._DICTIN_ = _dictToRtn_
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def enstring(self):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		for _thisKey_, _thisVal_ in self._DICTIN_.items():

			if (_thisKey_ in self._DICT_KEYS_TIME_):
				self._DICTINSTR_[self._KEY_DICT_[_thisKey_]] = CF.nrmlIntToHMS(_thisVal_)

			elif (_thisKey_ in self._DICT_KEYS_INT_):
				self._DICTINSTR_[self._KEY_DICT_[_thisKey_]] = f"""{_thisVal_:self._DICT_KEYS_INT_[_thisKey_]}"""

			else:
				self._DICTINSTR_[self._KEY_DICT_[_thisKey_]] = f"""{_thisVal_}"""

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def intervalCountOff(self):
		global \
				ALL_THE_FORMS
		# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
		ALL_THE_FORMS[self._THIS_FORM_NAME_][K_INTERVAL_COUNT].update(text_color=COLOR_TEXT_INTERVAL_COUNT_INACTIVE)
		self._DICTIN_[K_INTERVAL_COUNT] = 0
		self.updateFromDict()
		# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	def intervalCountOn(self):
		global \
			ALL_THE_FORMS
		# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
		ALL_THE_FORMS[self._THIS_FORM_NAME_]._MAINFRAME_[self._USE_THIS_KEY_(K_INTERVAL_COUNT)].update(text_color=COLOR_TIME_TOGO)
		self.updateFromDict()
		# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	def quickRead(self):
		self._RESULT_ = self._MAINFRAME_.Read(timeout=SZ_TIMEOUT_MS)

	def readToDict(self, dictToReadTo_=None, setLocalDict_=True):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		_dictToRtn_ = {}
		if dictToReadTo_ is None:
			dictToReadTo_ = self._DICTOUT_

		for _key_ in dictToReadTo_:
			_dictToRtn_[_key_] = self._MAINFRAME_[_key_]
			if (setLocalDict_ is True):
				self._DICTOUT_[_key_] = _dictToRtn_[_key_]
		return _dictToRtn_
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def runaway(self):
# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if NOWMS < self._TIME_TO_MOVE_:
			return  # only move at minimum  SZ_TIME_BETWEEN_MOVES apart

		self._TIME_TO_MOVE_ = NOWMS + SZ_TIMEMS_BETWEEN_MOVES
		_screenSZX_, _screenSZY_ = self._SCREEN_DIMS_
		_sizeX_, _sizeY_ = self._SIZE_
		_lcnX_, _lcnY_ = self._LOCATION_
		_moveToX_ = _lcnX_ + (self._MPX_[INDEX_X] * SZ_MOVE_DIST)
		_moveToY_ = _lcnY_ + (self._MPX_[INDEX_Y] * SZ_MOVE_DIST)

		if _moveToX_ < 0:
			_moveToX_ = 0
		elif _moveToX_ > (_screenSZX_ - _sizeX_):
			_moveToX_ = (_screenSZX_ - _sizeX_)

		if _moveToY_ < 0:
			_moveToY_ = 0
		elif _moveToY_ > (_screenSZY_ - _sizeY_):
			_moveToY_ = (_screenSZY_ - _sizeY_)

		if (abs(_moveToX_ - _lcnX_) > SZ_MAX_DELTA) or (abs(_moveToY_ - _lcnY_) > SZ_MAX_DELTA):
			return

		self._MAINFRAME_.Move(_moveToX_, _moveToY_)
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def updateFromDict(self, dictToUpdateFrom_=None):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if dictToUpdateFrom_ is not None:
			self._DICTIN_.update(dictToUpdateFrom_)

		self.enint()
		self.enstring()
		self._MAINFRAME_.fill(self._DICTINSTR_)
		__dummy__ = self._MAINFRAME_.Read(timeout=1)
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def update(self):
# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if (NOWMS >= self._TIME_TO_UPDATE_):
			return

		self._TIME_TO_UPDATE_ = NOWMS + SZ_TIMEMS_BETWEEN_UPDATES
		self._LOCATION_ = self._MAINFRAME_.CurrentLocation()
		self._BBOX_ = getBBox(self._LOCATION_, self._SIZE_)
		self._CLOSE_BBOX_ = getCloseBBox(self._LOCATION_, self._SIZE_)
		self.checkMouse()
		if (self._CHECKBOX_RUNAWAY_ is True):
			self.runaway()
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090C APPDS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
APPDS_MAIN = {  # the struct holding everything passed betwixt PySimpleGUI and this app
	K_APPMODE: APPMODE_NONE,  # default mode is clocks
	K_EVENT_ENTRIES: {  # holds events
		0: {
			K_ALARMPOPUP_PROPER: None,  # time of this event
			K_ALARMPOPUP_TEXT_TEXT: "get up, move around",  # alarm text for this event
			K_AUTO_CLOSE_DURATION: 10,  # time of this event
			K_DISMISSED: False,  # is this event dismissed
			K_ENABLED: True,  # is this event enabled
			K_EVENT_NAME: "MOVE",  # this entry's name
			K_EVENTMODE: EVENTMODE_INTERVAL,  # this entry's event_mode
			K_FIRSTRUN: True,  # are we initializing or not
			K_FORM_NAME: None,  # time of this event
			K_INTERVAL_COUNT: 0,  # count of number of times this has alerted since last reset
			K_IS_ALERTING_NOW: False,  # count of number of times this has alerted since last reset
			K_PREDISMISSABLE: True,  # is this event dismissable in advance
			K_SNOOZABLE: False,  # can this event be snoozed
			K_SNOOZED: False,  # is this event snoozed
			K_TIME_ALARM: 0,  # time of this event if it an alarm
			K_TIME_AT_LAST_RUN: 0,  # time this alarm last ran, now if running
			K_TIME_AT_NEXT_ALERT: ZERO_CLOCK,  # time next time this alarm goes off
			K_TIME_AT_ZEROELAPSE: ZERO_CLOCK,  # time next time this alarm goes off
			K_TIME_ELAPSED: ZERO_CLOCK,  # time next time this alarm goes off
			K_TIME_INTERVAL: CF.HALFHOURSECS,  # interval of this event
			K_TIME_INTERVAL__BEGIN: ZERO_CLOCK,  # time of the day this interval is made active
			K_TIME_INTERVAL__END: ZERO_CLOCK,  # time of the day this interval is no longer active
			K_TIME_INTERVAL_START: ZERO_CLOCK,  # time of the day this round of interval started
			K_TIME_LEN_OF_ALERT: ZERO_CLOCK,  # length of time to alert this event before auto closing it
		},
	},
	K_INDEX_OF_NEXT_EVENT: 0,  # default to first entry as next until the app can sort through them
}


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed sections of PSG.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


