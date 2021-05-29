

from Xlib import display as DISP
import gc
import PySimpleGUI as SG


import CF


gc.enable()


#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0900 DEF1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
ALARMPOPUP_PROPER = "ALARMPOPUP_PROPER"  # key for the button return for the popup
ALARMPOPUP_TEXT_TEXT = "ALARMPOPUP_TEXT_TEXT"  # key for the text on a popup
ALPHA_HIGH = "ALPHA_HIGH"  # alphahigh key
ALPHA_LOW = "ALPHA_LOW"  # alphalow key
APPMODE = "APPMODE"  # app mode key
APPMODE_CLOCKS = "APPMODE_CLOCKS"  # mode clocks only
APPMODE_EDIT = "APPMODE_EDIT"  # edit mode on top of main window
APPMODE_MAIN = "APPMODE_MAIN"  # main mode (xpand from clocks to this)
APPMODE_MOUSE_OVER = "APPMODE_MOUSE_OVER"  # mouseOver mode (xpand from clocks to this)
APPMODE_NEW_ALARMPOPUP = "APPMODE_NEW_ALARMPOPUP"  # main mode (xpand from clocks to this)
APPMODE_NONE = "APPMODE_NONE"  # NONE mode
APPMODE_THECLOCK = "APPMODE_THECLOCK"  # theClock mode (xpand from clocks to this)
BTN_DISMISS = "BTN_DISMISS"  # key for all of the button xpand
BTN_DOWN = "BTN_DOWN"  # key for all of the button xpand
BTN_EDIT = "BTN_EDIT"  # key for all of the button xpand
BTN_QUIT_ALL = "BTN_QUIT_ALL"  # key for all of the button xpand
BTN_QUIT_EDITOR = "BTN_QUIT_EDITOR"  # key for all of the button xpand
BTN_UP = "BTN_UP"  # key for all of the button xpand
BTN_XPAND = "BTN_XPAND"  # key for all of the button xpand
BTN_ZERO = "BTN_ZERO"  # key for all of the button xpand
CHECKBOX_ALPHA_DIM = "CHECKBOX_ALPHA_DIM"  # is the clock transparent under mouse (ineffective if mouse is avoided)
CHECKBOX_DISMISSED = "CHECKBOX_DISMISSED"  # key for avoiding the mouse bool
CHECKBOX_ENABLED = "CHECKBOX_ENABLED"  # key for avoiding the mouse bool
CHECKBOX_FIRSTRUN = "CHECKBOX_FIRSTRUN"  # key for avoiding the mouse bool
CHECKBOX_HOVER_DATE = "CHECKBOX_HOVER_DATE"  # KEY FOR CHECKBOX_HOVER_DATE
CHECKBOX_IS_ALERTING_NOW = "CHECKBOX_IS_ALERTING_NOW"  # key for avoiding the mouse bool
CHECKBOX_PREDISMISSABLE = "CHECKBOX_PREDISMISSABLE"  # key for avoiding the mouse bool
CHECKBOX_RUNAWAY = "CHECKBOX_RUNAWAY"  # key for avoiding the mouse bool
CHECKBOX_SNOOZABLE = "CHECKBOX_SNOOZABLE"  # key for avoiding the mouse bool
CHECKBOX_SNOOZED = "CHECKBOX_SNOOZED"  # key for avoiding the mouse bool
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
DISMISSED = "DISMISSED"  # alarm dismissed bool
EVENT_ENTRIES = "EVENT_ENTRIES"  #
EVENT_NAME = "EVENT_NAME"  # name of the event
EVENTMODE = "EVENTMODE"  # what mode is this event
EVENTMODE_ALARM = "EVENTMODE_ALARM"  #
EVENTMODE_INTERVAL = "EVENTMODE_INTERVAL"  #
EVENTMODE_NONE = "EVENTMODE_NONE"  # what mode is this event
FIRSTRUN = "FIRSTRUN"  # True if just started, false after init1()
FORM_CLOCKS = "FORM_CLOCKS"  # holds all of clocks form entries
FORM_EDITENTRY = "FORM_EDITENTRY"  # holds all of form edit-entry entries
FORM_EDITOR = "FORM_EDITOR"  # holds all of form editor entries
FORM_MAIN = "FORM_MAIN"  # holds all of form main entries
FORM_NAME = "FORM_NAME"  # the name of the form
FORM_POPUP01 = "FORM_POPUP01"  # holds all of form popup entries
FORM_POPUP02 = "FORM_POPUP02"  # holds all of form popup entries
FORM_POPUP03 = "FORM_POPUP03"  # holds all of form popup entries
FORM_POPUP04 = "FORM_POPUP04"  # holds all of form popup entries
FORM_POPUP05 = "FORM_POPUP05"  # holds all of form popup entries
FORM_THECLOCK = "FORM_THECLOCK"  # holds all of theclock form entries
INDEX_EAST = 2  # EAST
INDEX_NORTH = 1  # NORTH
INDEX_OF_NEXT_EVENT = "INDEX_OF_NEXT_EVENT"  # index of the next event to alert
INDEX_SOUTH = 3  # SOUTH
INDEX_WEST = 0  # WEST
INDEX_X = 0  # X
INDEX_Y = 1  # Y
INTERVAL_COUNT = "INTERVAL_COUNT"  # count of the number of times since last reset this interval has triggered an alert
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
NAME_NEXT_EVENT = "NAME_NEXT_EVENT"  # name of the next event up
PREDISMISSABLE = "PREDISMISSABLE"  # event can be dismissed in advance
SNOOZABLE = "SNOOZABLE"  # can this event be snoozed
SNOOZED = "SNOOZED"  # is this event snoozed bool
SZ_ALERT_TEXT = 20  # font size of alert text
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
SZ_TIMEMS_BETWEEN_MOUSE_CHECKS = 300  # throttle mouse checking
SZ_TIMEMS_BETWEEN_MOVES = 500  # time_ms between moves
SZ_TIMEMS_BETWEEN_UPDATES = 500  # time_ms between updating windows/frames/etc
SZ_TIMEOUT_MS = 100  # timeout for PSG
SZ_TIMES_BTWN_PERIODIC_JOB = 900  # time between periodic job runnings
TIME_ALARM = "TIME_ALARM"  # the alarm time
TIME_AT_LAST_RUN = "TIME_AT_LAST_RUN"  # timeS of last alarm
TIME_AT_NEXT_ALERT = "TIME_AT_NEXT_ALERT"  # what time is the next alarm, == KEY_TIME_ALARM is tomorrow
TIME_AT_ZEROELAPSE = "TIME_AT_ZEROELAPSE"  # the time at last zero to keep elapsed time accurate despite other things hogging CPU time
TIME_CLOCK = "TIME_CLOCK"  # the main clock time
TIME_ELAPSED = "TIME_ELAPSED"  # key for all clocks elapsed
TIME_INTERVAL = "TIME_INTERVAL"  # interval timer starting time, reset each time the interval goes off
TIME_INTERVAL__BEGIN = "TIME_INTERVAL__BEGIN"  # key for time interval starts alerting
TIME_INTERVAL__END = "TIME_INTERVAL__END"  # key for time an interval goes to leep and stops alerting
TIME_INTERVAL_START = "TIME_INTERVAL_START"  # interval timer starting time, reset each time the interval goes off
TIME_LEN_OF_ALERT = "TIME_LEN_OF_ALERT"  # length of alerting
TIME_TOGO = "TIME_TOGO"  # down counter to next event on this window/alarm/interval/reminder
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
COLORS_BTN_NORMAL = (COLOR_TEXT_NORMAL, COLOR_BACKGROUND)  # comment
COLORS_TEXT_HIGH = (COLOR_TEXT_HIGH, COLOR_BACKGROUND)  # combined colors for a clock text element
COLORS_TEXT_LOW = (COLOR_TEXT_LOW, COLOR_BACKGROUND)  # combined colors for a clock text element
COLORS_TEXT_NORMAL = (COLOR_TEXT_NORMAL, COLOR_BACKGROUND)  # combined colors for a clock text element
COLORS_TIME_CLOCK = (COLOR_TIME_CLOCK, COLOR_CLOCK_BACKGROUND)  # combined colors for a clock text element
COLORS_TIME_ELAPSED = (COLOR_TIME_ELAPSED, COLOR_CLOCK_BACKGROUND)  # combined colors for a clock text element
COLORS_TIME_TOGO = (COLOR_TIME_TOGO, COLOR_CLOCK_BACKGROUND)  # combined colors for a clock text element
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
TIMES_NEXT_EVENT = 0  # comment
TIMES_NEXT_PERIODIC_JOB = 0  # seconds till next housekeeping, check for next times, etc.


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0910 DEF3
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
_LAYOUT_ = "layout"  #
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
	KEY: BTN_DISMISS,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_DOWN20 = {  #
	BUTTON_TEXT: "",  # button_text empty for the DOWN button
	IMAGE_FILENAME: "res/down20.png",  # filename for the button icon
	BORDER_WIDTH: 0,  # button xpand key
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FOCUS: True,  # focus on click
	KEY: BTN_DOWN,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_DOWN32 = {  #
	BUTTON_TEXT: "",  # button_text empty for the DOWN button
	IMAGE_FILENAME: "res/down32.png",  # filename for the button icon
	BORDER_WIDTH: 0,  # button xpand key
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_DOWN,  # focus on click
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_EDIT20 = {  #
	BUTTON_TEXT: "",  # button_text empty for the EDIT button
	IMAGE_FILENAME: "res/edit20.png",  # filename for the button icon
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_EDIT,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_EDIT32 = {  #
	BUTTON_TEXT: "",  # button_text empty for the EDIT button
	IMAGE_FILENAME: "res/edit32.png",  # filename for the button icon
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_EDIT,  # button xpand key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_QUIT20 = {  #
	BUTTON_TEXT: "",  # button_text empty for the QUIT button
	IMAGE_FILENAME: "res/quit20.png",  # filename for the button icon
	TOOLTIP: "quit the app",  # button_text empty for the QUIT button
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_QUIT_ALL,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_QUIT32 = {  #
	BUTTON_TEXT: "",  # button_text empty for the QUIT button
	IMAGE_FILENAME: "res/quit32.png",  # filename for the button icon
	TOOLTIP: "quit the app",  # button_text empty for the QUIT button
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_QUIT_ALL,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_UP20 = {  #
	BUTTON_TEXT: "",  # button_text empty for the UP button
	IMAGE_FILENAME: "res/up20.png",  # filename for the button icon
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_UP,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_UP32 = {  #
	BUTTON_TEXT: "",  # button_text empty for the UP button
	IMAGE_FILENAME: "res/up32.png",  # filename for the button icon
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_UP,  # button up key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_XPAND20 = {  #
	BUTTON_TEXT: "",  # button_text empty for the XPAND button
	IMAGE_FILENAME: "res/xpand20.png",  # filename for the button icon
	TOOLTIP: "expand to the big window from where you can edit events",  # tooltip
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_XPAND,  # focus on click
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_XPAND32 = {  #
	BUTTON_TEXT: "",  # button_text empty for the XPAND button
	IMAGE_FILENAME: "res/xpand32.png",  # filename for the button icon
	TOOLTIP: "expand to the big window from where you can edit events",  # tooltip
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_XPAND,  # button xpand font
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_ZERO20 = {  #
	BUTTON_TEXT: "",  # button_text empty for the ZERO button
	IMAGE_FILENAME: "res/zero20.png",  # filename for the button icon
	TOOLTIP: "zero the elapsed timer",  # tooltip
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_ZERO,  # button zero key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_ZERO32 = {  #
	BUTTON_TEXT: "",  # button_text empty for the ZERO button
	IMAGE_FILENAME: "res/zero32.png",  # filename for the button icon
	TOOLTIP: "zero the elapsed timer",  # tooltip
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_ZERO,  # button zero key
	PAD: SZ_PAD_ALL,  # button xpand key
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0907 spin box elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0908 checkbox elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
CHECKBOX_ALPHA_DIM01 = {  # checkbox for alpha under mouse
	TEXT: "ALPHA_LOW",  # simple text reminder
	TOOLTIP: "low alpha under mouse",  # comment
	DEFAULT: True,  # leave it on by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: CHECKBOX_ALPHA_DIM,  # set the key for the checkbox
}


CHECKBOX_DISMISSED01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "DISMISSED",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: CHECKBOX_DISMISSED,  # set the key for the checkbox
}


CHECKBOX_ENABLED01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "ENABLED",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: CHECKBOX_ENABLED,  # set the key for the checkbox
}


CHECKBOX_FIRSTRUN01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "FIRSTRUN",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: CHECKBOX_FIRSTRUN,  # set the key for the checkbox
}


CHECKBOX_HOVER_DATE01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "DT on hover",  # text label
	TOOLTIP: "show date when hovering over clock",  # tooltip
	DEFAULT: True,  # leave it on by default
	ENABLE_EVENTS: True,  # set the events on for the checkbox
	KEY: CHECKBOX_HOVER_DATE,  # set the key for the checkbox
}


CHECKBOX_IS_ALERTING_NOW01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "IS_ALERTING_NOW",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: CHECKBOX_IS_ALERTING_NOW,  # set the key for the checkbox
}


CHECKBOX_PREDISMISSABLE01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "PREDISMISSABLE",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: CHECKBOX_PREDISMISSABLE,  # set the key for the checkbox
}


CHECKBOX_RUNAWAY01 = {  # checkbox for runaway from mouse behavior
	TEXT: "RUNAWAY",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: CHECKBOX_RUNAWAY,  # set the key for the checkbox
}


CHECKBOX_SNOOZABLE01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "SNOOZABLE",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: CHECKBOX_SNOOZABLE,  # set the key for the checkbox
}


CHECKBOX_SNOOZED01 = {  # checkbox for dismissed from mouse behavior
	TEXT: "SNOOZED",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: False,  # leave it off by default
	ENABLE_EVENTS: True,  # set the key for the checkbox
	KEY: CHECKBOX_SNOOZED,  # set the key for the checkbox
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
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (4, 1),  # characters, lines size line
	TEXT_COLOR: COLOR_TIME_TOGO,  # the text color for a clock_time element
}


TEXT_NAME_NEXT_EVENT = {  # define the text element for CLOCK_TIME
	TEXT: "",  # the text to fill in
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: False,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_TOGO,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (16, 1),  # characters, lines size line
	TEXT_COLOR: COLOR_TIME_TOGO,  # the text color for a clock_time element
}


TEXT_TIME_AT_NEXT_ALERT = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: False,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_TOGO,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (8, 1),  # characters, lines size line
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_TOGO,  # the text color for a clock_time element
}


TEXT_TIME_AT_ZEROELAPSE = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: False,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_ELAPSED,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (8, 1),  # characters, lines size line
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_ELAPSED,  # the text color for a clock_time element
}


TEXT_TIME_CLOCK = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: True,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_CLOCK,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (8, 1),  # characters, lines size line
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_CLOCK,  # the text color for a clock_time element
}


TEXT_TIME_ELAPSED = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	FONT: FONTSZ_CLOCKS_TIME_ELAPSED,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (8, 1),  # characters, lines size line
	TEXT: ZERO_CLOCK,  # the text color for a clock_time element
	TEXT_COLOR: COLOR_TIME_ELAPSED,  # the text color for a clock_time element
}


TEXT_TIME_TOGO = {  # define the text element for CLOCKS_CLOCK_TIME
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	FONT: FONTSZ_CLOCKS_TIME_TOGO,  # font+size line
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
		self._CURRENT_EVENTMODE_ = None  #
		self._CURRENT_EVENT_ = None  #
		self._CURRENT_LOCATION_ = EMPTY_XY  #
		self._CURRENT_MOUSE_LOCATION_ = EMPTY_XY  #
		self._CURRENT_MOUSE_STATUS_ = MOUSE_STATUS_NONE  #
		self._CURRENT_VALUES = {}  #
		self._DIMMED_ = False  #
		self._KEY_DICT_ = {}  #
		self._KEY_DICT_REVERSE_ = {}  #
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
			NAME_NEXT_EVENT: "",  # name of next event
			CHECKBOX_ALPHA_DIM: False,  # value of the alphas dim checkbox
			CHECKBOX_RUNAWAY: False,  # value of runaway checkbox
			INTERVAL_COUNT: 0,  # interval count
			TIME_AT_NEXT_ALERT: ZERO_CLOCK,  # time at next event
			TIME_AT_ZEROELAPSE: ZERO_CLOCK,  # time at last zero of elapsed timer
			TIME_CLOCK: ZERO_CLOCK,  # time clock or wall clock
			TIME_ELAPSED: ZERO_CLOCK,  # time elapsed
			TIME_TOGO: ZERO_CLOCK,  # countdown to next event
		}
# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._DICTINSTR_ = {
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			NAME_NEXT_EVENT: "",  # name of next event
			CHECKBOX_ALPHA_DIM: False,  # value of the alphas dim checkbox
			CHECKBOX_RUNAWAY: False,  # value of runaway checkbox
			INTERVAL_COUNT: 0,  # interval count
			TIME_AT_NEXT_ALERT: ZERO_CLOCK,  # time at next event
			TIME_AT_ZEROELAPSE: ZERO_CLOCK,  # time at last zero of elapsed timer
			TIME_CLOCK: ZERO_CLOCK,  # time clock or wall clock
			TIME_ELAPSED: ZERO_CLOCK,  # time elapsed
			TIME_TOGO: ZERO_CLOCK,  # countdown to next event
		}
# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._DICTOUT_ = {  # holds the values for the clocks frame
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			CHECKBOX_ALPHA_DIM: "True",  # name of next event
			CHECKBOX_RUNAWAY: False,  # interval count
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._DICT_KEYS_INT_ = {  # dict of integer keys and their format
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			INTERVAL_COUNT: "04d",  # intervalCount:04d
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._DICT_KEYS_TIME_ = {  # dict of time keys and their max value int seconds
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			TIME_AT_NEXT_ALERT: DAYSECS,  # comment
			TIME_AT_ZEROELAPSE: DAYSECS,  # comment
			TIME_CLOCK: DAYSECS,  #
			TIME_ELAPSED: TIME995959,  #
			TIME_TOGO: DAYSECS,  #
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._PERIODIC_ = {  # periodic updates dict for the clocks frame
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			TIME_AT_NEXT_ALERT: ZERO_CLOCK,  # time at next event
			TIME_AT_ZEROELAPSE: ZERO_CLOCK,  # time at last zero of elapsed timer
			TIME_CLOCK: ZERO_CLOCK,  # time clock or wall clock
			TIME_ELAPSED: ZERO_CLOCK,  # time elapsed
			TIME_TOGO: ZERO_CLOCK,  # countdown to next event
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._TEXT_INTERVAL_COUNT_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_INTERVAL_COUNT,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(INTERVAL_COUNT)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._KEY_DICT_[INTERVAL_COUNT] = f"""{self._USE_THIS_KEY_(INTERVAL_COUNT)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(INTERVAL_COUNT)}"""] = INTERVAL_COUNT

		self._TEXT_NAME_NEXT_EVENT_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_NAME_NEXT_EVENT,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(NAME_NEXT_EVENT)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._KEY_DICT_[NAME_NEXT_EVENT] = f"""{self._USE_THIS_KEY_(NAME_NEXT_EVENT)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(NAME_NEXT_EVENT)}"""] = NAME_NEXT_EVENT

		self._TEXT_TIME_AT_NEXT_ALERT_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_TIME_AT_NEXT_ALERT,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(TIME_AT_NEXT_ALERT)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._TIME_KEY_LIST_.append(_TEXT_TIME_AT_NEXT_ALERT_)
		self._TIME_KEY_LIST_.append(self._USE_THIS_KEY_(_TEXT_TIME_AT_NEXT_ALERT_))
		self._KEY_DICT_[TIME_AT_NEXT_ALERT] = f"""{self._USE_THIS_KEY_(TIME_AT_NEXT_ALERT)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(TIME_AT_NEXT_ALERT)}"""] = TIME_AT_NEXT_ALERT

		self._TEXT_TIME_AT_ZEROELAPSE_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_TIME_AT_ZEROELAPSE,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(TIME_AT_ZEROELAPSE)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._TIME_KEY_LIST_.append(_TEXT_TIME_AT_ZEROELAPSE_)
		self._TIME_KEY_LIST_.append(self._USE_THIS_KEY_(_TEXT_TIME_AT_ZEROELAPSE_))
		self._KEY_DICT_[TIME_AT_ZEROELAPSE] = f"""{self._USE_THIS_KEY_(TIME_AT_ZEROELAPSE)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(TIME_AT_ZEROELAPSE)}"""] = TIME_AT_ZEROELAPSE

		self._TEXT_TIME_CLOCK_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_TIME_CLOCK,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(TIME_CLOCK)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._TIME_KEY_LIST_.append(_TEXT_TIME_CLOCK_)
		self._TIME_KEY_LIST_.append(self._USE_THIS_KEY_(_TEXT_TIME_CLOCK_))
		self._KEY_DICT_[TIME_CLOCK] = f"""{self._USE_THIS_KEY_(TIME_CLOCK)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(TIME_CLOCK)}"""] = TIME_CLOCK

		self._TEXT_TIME_ELAPSED_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_TIME_ELAPSED,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(TIME_ELAPSED)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._TIME_KEY_LIST_.append(_TEXT_TIME_ELAPSED_)
		self._TIME_KEY_LIST_.append(self._USE_THIS_KEY_(_TEXT_TIME_ELAPSED_))
		self._KEY_DICT_[TIME_ELAPSED] = f"""{self._USE_THIS_KEY_(TIME_ELAPSED)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(TIME_ELAPSED)}"""] = TIME_ELAPSED

		self._TEXT_TIME_TOGO_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**TEXT_TIME_TOGO,  # interval count template
			KEY: f"""{self._USE_THIS_KEY_(TIME_TOGO)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._TIME_KEY_LIST_.append(_TEXT_TIME_TOGO_)
		self._TIME_KEY_LIST_.append(self._USE_THIS_KEY_(_TEXT_TIME_TOGO_))
		self._KEY_DICT_[TIME_TOGO] = f"""{self._USE_THIS_KEY_(TIME_TOGO)}"""
		self._KEY_DICT_REVERSE_[f"""{self._USE_THIS_KEY_(TIME_TOGO)}"""] = TIME_TOGO

		self._COLUMN01_ = [  # the column that puts the two smaller clocks below the main one
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			[
				SG.Spin(  # add a new TEXT element to clocks column
					**self._TEXT_TIME_CLOCK_  # add the main clock
				),
			],
			[
				SG.Spin(  # add a new row to clocks column
					**self._TEXT_TIME_AT_ZEROELAPSE_  # add time to go
				),
				SG.Spin(  # add a new text element to row01 clocks column
					**self._TEXT_TIME_ELAPSED_  # add elapsed time
				),
			],
			[
				SG.Spin(  # add a new text element to row01 clocks column
					**self._TEXT_TIME_TOGO_  # add elapsed time
				),
				SG.Spin(  # add a new row to clocks column
					**self._TEXT_TIME_AT_NEXT_ALERT_  # add time to go
				),
			],
			[
				SG.Spin(  # add a new text element to row01 clocks column
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
				SG.Spin(  # add reset button for elapsed time
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
			MARGINS: SZ_MARGINS_ALL,  #
			NO_TITLEBAR: True,  # no titlebar on APPMODE_CLOCKS window
			TITLE: TITLE_CLOCKS,  #
			_LAYOUT_: self._LAYOUT_,  # add the layout for CLOCKS_WINDOW
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self.__CDS__ = {
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			COLUMN01: self._COLUMN01_,  # the column that puts the two smaller clocks below the main one
			COLUMN02: self._COLUMN02_,  # the column that puts the two smaller clocks below the main one
			DICTOUT: self._DICTOUT_,  # holds the values for the clocks frame
			DICT_KEYS_INT: self._DICT_KEYS_INT_,  # dict of integer keys and their format
			DICT_KEYS_TIME: self._DICT_KEYS_TIME_,  # dict of time keys and their max value int seconds
			THIS_KEY_BASE: self._THIS_KEY_BASE_,
			USE_THIS_KEY: self._USE_THIS_KEY_,
			THIS_FORM_NAME: self._THIS_FORM_NAME_,
			ALPHA_CHANNEL: self._ALPHA_CHANNEL_,
			ALPHA_HIGH: self._ALPHA_HIGH_,
			ALPHA_LOW: self._ALPHA_LOW_,
			BBOX: self._BBOX_,
			CHANGED_EVENTS: self._CHANGED_EVENTS_,
			CHANGED_VALUES: self._CHANGED_VALUES_,
			CHECKBOX_ALPHA_DIM: self._CHECKBOX_ALPHA_DIM_,
			CHECKBOX_RUNAWAY: self._CHECKBOX_RUNAWAY_,
			CLOSE_BBOX: self._CLOSE_BBOX_,
			CURRENT_EVENTMODE: self._CURRENT_EVENTMODE_,
			CURRENT_EVENT: self._CURRENT_EVENT_,
			CURRENT_LOCATION: self._CURRENT_LOCATION_,
			CURRENT_MOUSE_LOCATION: self._CURRENT_MOUSE_LOCATION_,
			CURRENT_MOUSE_STATUS: self._CURRENT_MOUSE_STATUS_,
			CURRENT_VALUE: self._CURRENT_VALUES,
			DIMMED: self._DIMMED_,
			KEY_DICT: self._KEY_DICT_,
			KEY_DICT_REVERSE: self._KEY_DICT_REVERSE_,
			LAST_EVENT: self._LAST_EVENT_,
			LAST_LOCATION: self._LAST_LOCATION_,
			LAST_MOUSE_LOCATION: self._LAST_MOUSE_LOCATION_,
			LAST_MOUSE_STATUS: self._LAST_MOUSE_STATUS_,
			LAST_VALUES: self._LAST_VALUES_,
			MAINFRAME: self._MAINFRAME_,
			MPX: self._MPX_,
			SCREEN_DIMS: self._SCREEN_DIMS_,
			SIZE: self._SIZE_,
			TIME_TO_CHECK_MOUSE: self._TIME_TO_CHECK_MOUSE_,
			TIME_TO_MOVE: self._TIME_TO_MOVE_,
			TIME_TO_UPDATE: self._TIME_TO_UPDATE_,
			LAYOUT: self._LAYOUT_,  # layout for APPMODE_CLOCKS
			PERIODIC: self._PERIODIC_,  # periodic updates dict for the clocks frame
			TEXT_INTERVAL_COUNT: self._TEXT_INTERVAL_COUNT_,  # class text for interval count
			TEXT_NAME_NEXT_EVENT: self._TEXT_NAME_NEXT_EVENT_,  # class text for interval count
			TEXT_TIME_AT_NEXT_ALERT: self._TEXT_TIME_AT_NEXT_ALERT_,  # class text for interval count
			TEXT_TIME_AT_ZEROELAPSE: self._TEXT_TIME_AT_ZEROELAPSE_,  # class text for interval count
			TEXT_TIME_CLOCK: self._TEXT_TIME_CLOCK_,  # class text for interval count
			TEXT_TIME_ELAPSED: self._TEXT_TIME_ELAPSED_,  # class text for interval count
			TEXT_TIME_TOGO: self._TEXT_TIME_TOGO_,  # class text for interval count
			WINDOW: self._WINDOW_,  # define the clocks window
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	def __enter__(self):
		global \
			ALL_THE_FORMS
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		self._MAINFRAME_ = SG.Window(**self._WINDOW_).finalize()
		ALL_THE_FORMS[self._THIS_FORM_NAME_] = self._MAINFRAME_
		self.init()
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
			self._MAINFRAME_.AlphaChannel = APPDS[ALPHA_HIGH]
			alphaMode = False
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self._LAST_MOUSE_STATUS_ = _statusToRtn_
		self._MOUSE_STATUS_ = _statusToRtn_
		self._MPX_ = _mpxToRtn_

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def easyUpdate(self,
			checkboxAlphaDim_=None,
			checkboxRunaway_=None,
			eventmode_=None,
			intervalCount_=None,
			nameNextEvent_=None,
			timeAtNext_=None,
			timeAtZeroelapse_=None,
			timeClock_=None,
			timeElapsed_=None,
			timeTogo_=None,
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if nameNextEvent_ is not None:
			self._DICTIN_[NAME_NEXT_EVENT] = nameNextEvent_

		if checkboxAlphaDim_ is not None:
			self._DICTIN_[CHECKBOX_ALPHA_DIM] = checkboxAlphaDim_

		if checkboxRunaway_ is not None:
			self._DICTIN_[CHECKBOX_RUNAWAY] = checkboxRunaway_

		if eventmode_ is not None:
			self.CURRENT_EVENTMODE = eventmode_

			if intervalCount_ is not None:
				self._DICTIN_[INTERVAL_COUNT] = intervalCount_

			if (eventmode_ == EVENTMODE_INTERVAL):
				self.intervalCountOn()
			else:
				self.intervalCountOff()

		if time_at_next_ is not None:
			self._DICTIN_[TIME_AT_NEXT] = time_at_next_

		if timeAtZeroelapse_ is not None:
			self._DICTIN_[TIME_AT_ZEROELAPSE] = timeAtZeroelapse_

		if timeClock_ is not None:
			self._DICTIN_[TIME_CLOCK] = timeClock_

		if timeElapsed_ is not None:
			self._DICTIN_[TIME_ELAPSED] = timeElapsed_

		if timeTogo_ is not None:
			self._DICTIN_[TIME_TOGO] = timeTogo_

		self.enint()
		self.updateFromDict()
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def enint(self):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisKey_ in self._DICT_KEYS_TIME_:
			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if (isinstance(self._DICTIN_[_thisKey_], str) is True):
				self._DICTIN_[_thisKey_] = CF.HMSToNrmlInt(self._DICTIN_[_thisKey_])
			self._DICTINSTR_[_thisKey_] = CF.nrmlIntToHMS(self._DICTIN_[_thisKey_])
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisKey_ in self._DICT_KEYS_INT_:
			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if (isinstance(self.dictToInt_[_thisKey_], str) is True):
				self._DICTIN_[_thisKey_] = int(dictToInt_[_thisKey_])
			self._DICTINSTR_[_thisKey_] = f"""{self._DICTIN_[_thisKey_]:self._DICT_KEYS_INT_[_thisKey_]}"""
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def enstring(self):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		for _thisKey_, _thisVal_ in self._DICT_KEYS_TIME_.items():
			_DICTINSTR_[_thisKey_] = CF.nrmlIntToHMS((thisVal_ % CF._DICT_KEYS_TIME_))

		for _thisKey_, _thisVal_ in self._DICT_KEYS_INT_.items():
			_DICTINSTR_[_thisKey_] = f"""{self._DICTIN_[_thisKey_]:_thisVal_}"""
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

def intervalCountOff():
	global \
			ALL_THE_FORMS
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	ALL_THE_FORMS[self._THIS_FORM_NAME_][INTERVAL_COUNT].update(text_color=COLOR_TEXT_INTERVAL_COUNT_INACTIVE)
	self._DICTIN_[INTERVAL_COUNT] = 0
	self._MAINFRAME_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

def intervalCountOn(formToCountOn_):
	global \
		ALL_THE_FORMS, \
		CLOCKS_DICT
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	ALL_THE_FORMS[formToCountOn_][INTERVAL_COUNT].update(text_color=COLOR_TIME_TOGO)
	CLOCKS_DICT[INTERVAL_COUNT] = f"""{CURRENT_INTERVAL_COUNT:04d}"""
	updateFrameFromDict(CLOCKS_TEXT_DICT)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	def quickRead(self):
		self._RESULT_ = self._MAINFRAME_.Read(timeout=SZ_TIMEOUT_MS)

	def readToDict(self, dictToReadTo_=self._DICTOUT_, setLocalDict_=True):
# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		_dictToRtn_ = {}
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
	APPMODE: APPMODE_NONE,  # default mode is clocks
	EVENT_ENTRIES: {  # holds events
		0: {
			ALARMPOPUP_PROPER: None,  # time of this event
			ALARMPOPUP_TEXT_TEXT: "get up, move around",  # alarm text for this event
			AUTO_CLOSE_DURATION: 10,  # time of this event
			DISMISSED: False,  # is this event dismissed
			ENABLED: True,  # is this event enabled
			EVENT_NAME: "MOVE",  # this entry's name
			EVENTMODE: EVENTMODE_INTERVAL,  # this entry's event_mode
			FIRSTRUN: True,  # are we initializing or not
			FORM_NAME: None,  # time of this event
			INTERVAL_COUNT: 0,  # count of number of times this has alerted since last reset
			KEY_BASE: None,  # count of number of times this has alerted since last reset
			PREDISMISSABLE: True,  # is this event dismissable in advance
			SNOOZABLE: False,  # can this event be snoozed
			SNOOZED: False,  # is this event snoozed
			TIME_ALARM: 0,  # time of this event if it an alarm
			TIME_AT_LAST_RUN: 0,  # time this alarm last ran, now if running
			TIME_AT_NEXT_ALERT: ZERO_CLOCK,  # time next time this alarm goes off
			TIME_AT_ZEROELAPSE: ZERO_CLOCK,  # time next time this alarm goes off
			TIME_ELAPSED: ZERO_CLOCK,  # time next time this alarm goes off
			TIME_INTERVAL: HALFHOURSECS,  # interval of this event
			TIME_INTERVAL__BEGIN: ZERO_CLOCK,  # time of the day this interval is made active
			TIME_INTERVAL__END: ZERO_CLOCK,  # time of the day this interval is no longer active
			TIME_INTERVAL_START: ZERO_CLOCK,  # time of the day this round of interval started
			TIME_LEN_RING: ZERO_CLOCK,  # length of time to alert this event before auto closing it
		},
	},
	INDEX_OF_NEXT_EVENT: 0,  # default to first entry as next until the app can sort through them
}


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed sections of PSG.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


# <<>>
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of unmanaged sections of py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# splitBBoxToRaw
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def splitBBoxToRaw(BBoxToSplit_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return BBoxToSplit_[INDEX_WEST], BBoxToSplit_[INDEX_NORTH], BBoxToSplit_[INDEX_EAST], BBoxToSplit_[INDEX_SOUTH]
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# splitBBoxToRaw
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def splitXYToRaw(XYToSplit_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return XYToSplit_[INDEX_X], XYToSplit_[INDEX_Y]
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# fixTimeAtNext
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def fixTimeAtNext(timeToFix_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

	if timeToFix_ < NOWS:
		timeToFix_ += CF.DAYSECS

	return timeToFix_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# localTimes
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def localTimes(hrs_=None, mins_=None):
	global \
		NOW_NOMS, \
		NOWM, \
		NOWMS, \
		NOWS
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if hrs_ is None:
		hrs_ = TIMEH_ADJUST_HRS

	if mins_ is None:
		mins_ = TIMEM_ADJUST_MINS

	_adjSecs_ = CF.MTSS() - TIME_S_ADJUST_VALUE(hrs_, mins_)
	if _adjSecs_ < 0:
		_adjSecs_ += CF.DAYSECS

	_adjSecs_ = _adjSecs_ % CF.DAYSECS
	NOWS = _adjSecs_
	NOW_NOMS = int(NOWS)
	NOWM = CF.loseTheSecs(_adjSecs_)
	NOWMS = int(NOWS * 1000)
#	print(f"""{CF.getDebugInfo()}
#	{CF.frameItHMS("_adjSecs_", _adjSecs_)}
#	{CF.frameItHMS("TIME_S_ADJUST_VALUE(hrs_, mins_)", TIME_S_ADJUST_VALUE(hrs_, mins_))}""")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# compareXY
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def compareXY(XY1_, XY2_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if (XY1_[INDEX_X] == XY2_[INDEX_X]) and (XY1_[INDEX_Y] == XY2_[INDEX_Y]):
		return True
	else:
		return False
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# compareBBox
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def compareBBox(BBox1_, BBox2_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if ((BBox1_[INDEX_NORTH] == BBox2_[INDEX_NORTH]) and (BBox1_[INDEX_WEST] == BBox2_[INDEX_WEST]) and (BBox1_[INDEX_SOUTH] == BBox2_[INDEX_SOUTH]) and (BBox1_[INDEX_EAST] == BBox2_[INDEX_EAST])):
		return True
	else:
		return False
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# getBBox
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def getBBox(locnToBBox_, sizeToBBox_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_TLcnX_ = locnToBBox_[INDEX_X]
	_TLcnY_ = locnToBBox_[INDEX_Y]
	_TSizeX_ = sizeToBBox_[INDEX_X]
	_TSizeY_ = sizeToBBox_[INDEX_Y]

	return (
		_TLcnX_,
		_TLcnY_,
		(_TLcnX_ + _TSizeX_),
		(_TLcnY_ + _TSizeY_),
	)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# getCloseBBox
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def getCloseBBox(location_, size_, closeEnough_=SZ_CLOSE):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_TLcnX_ = location_[INDEX_X]
	_TLcnY_ = location_[INDEX_Y]
	_TSizeX_ = size_[INDEX_X]
	_TSizeY_ = size_[INDEX_Y]
	return (
		(_TLcnX_ - closeEnough_),
		(_TLcnY_ - closeEnough_),
		(_TLcnX_ + _TSizeX_ + closeEnough_),
		(_TLcnY_ + _TSizeY_ + closeEnough_)
	)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# isInBBox
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def isInBBox(BBoxIn_, pointIn_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if (BBoxIn_[INDEX_NORTH] < pointIn_[INDEX_Y] < BBoxIn_[INDEX_SOUTH]) and (BBoxIn_[INDEX_WEST] < pointIn_[INDEX_X] < BBoxIn_[INDEX_EAST]):
		return True
	else:
		return False
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# findNextAlarmEvent
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def findNextAlarmEvent():
	global \
			INTERVALLING_LIST, \
			APPDS, \
			NAME_NEXT_EVENT_STR, \
			TIME_S_AT_NEXT_EVENT
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_nextEventList_ = []  # (time, index, mode, name)
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	for _index_, _event_ in APPDS[EVENT_ENTRIES].items():

		if _event_ is not None:
			_TEventMode_ = _event_[EVENTMODE]

			if (_TEventMode_ == EVENTMODE_INTERVAL):
				updateInterval(_index_)
				_event_ = APPDS[EVENT_ENTRIES][_index_]

			elif (_TEventMode_ == EVENTMODE_ALARM):
				_event_[TIME_AT_NEXT_ALERT] = _event_[TIME_ALARM]

			if (_event_[DISMISSED] is False) and (_event_[ENABLED] is True) and (_event_[TIME_INTERVAL__BEGIN] <= NOWS < fixTimeAtNext(_event_[TIME_INTERVAL__END])):
				_nextEventList_.append((fixTimeAtNext(_event_[TIME_AT_NEXT_ALERT]), _index_, _event_[EVENTMODE], _event_[NAME]))

	_nextEventList_.sort()

	if _nextEventList_ != []:
		if ALL_THE_FORMS[FORM_CLOCKS] is not None:
			ALL_THE_FORMS[FORM_CLOCKS].easyUpdate(
				TIME_AT_NEXT_=_nextEventList_[0][0],
				NAME_NEXT_EVENT_=_nextEventList_[0][3],
			)
		CLOCKS_DICT[TIME_AT_NEXT_ALERT] = # (time, index, mode, name)
		TIME_S_AT_NEXT_EVENT = CLOCKS_DICT[TIME_AT_NEXT_ALERT]
		NAME_NEXT_EVENT_STR = # (time, index, mode, name)
		CLOCKS_TEXT_DICT[NAME_NEXT_EVENT] = NAME_NEXT_EVENT_STR
		CURRENT_EVENTMODE = _nextEventList_[0][2]# (time, index, mode, name)

		if (CURRENT_EVENTMODE == EVENTMODE_INTERVAL):
			CURRENT_INTERVAL_COUNT = APPDS[EVENT_ENTRIES][_nextEventList_[0][1]]
			updateIntervalCount()

		####updateFrameFromDict(CLOCKS_TEXT_DICT)


	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# doMidnightWork
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def doMidnightWork():
	print("midnight")
	global \
			APPDS_MAIN, \
			TIME_MS_NEXT_MOUSE_CHECK, \
			TIMEMS_NEXT_MOVED, \
			TIMEMS_NEXT_UPDATED, \
			TIME_S_AT_NEXT_EVENT, \
			TIME_S_AT_NEXT_PERIODIC_JOB
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	while NOWMS < 1:
		localTimes()

	TIME_MS_NEXT_MOUSE_CHECK = 0
	TIMEMS_NEXT_MOVED = 0
	TIMEMS_NEXT_UPDATED = 0
	TIME_S_AT_NEXT_EVENT = 0
	TIME_S_AT_NEXT_PERIODIC_JOB = 0

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	for _index_, _event_ in APPDS_MAIN[EVENT_ENTRIES].items():

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (_event_ is not None):  # and (_event_[EVENTMODE] in [EVENTMODE_ALARM]):
			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			APPDS_MAIN[EVENT_ENTRIES][_index_][DISMISSED] = False
			APPDS_MAIN[EVENT_ENTRIES][_index_][IS_ALERTING_NOW] = False

			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			for _index1_ in APPDS_TIMES_LIST:

				# 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥
				if APPDS_MAIN[EVENT_ENTRIES][_index_][_index1_] >= CF.DAYSECS:
					# 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥
					APPDS_MAIN[EVENT_ENTRIES][_index_][_index1_] -= CF.DAYSECS

					# ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥
					if (APPDS_MAIN[EVENT_ENTRIES][_index_][_index1_] < 0):
						# 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥
						APPDS_MAIN[EVENT_ENTRIES][_index_][_index1_] = abs(APPDS_MAIN[EVENT_ENTRIES][_index_][_index1_])

						# ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6
					# ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5
				# ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
	findNextAlarmEvent()
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# outerLoop
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def outerLoop():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	while True:
		window_, _result_, _values_ = SG.read_all_windows(timeout=SZ_TIMEOUT_MS)

		print(f"""_result_ {_result_} _values_ {_values_}""")
		if _result_ != "__TIMEOUT__":
			# do all result processing here

			if (_result_ == BTN_QUIT_ALL):
				return BTN_QUIT_ALL

		localTimes()

		if (NOWMS == 0):
			doMidnightWork()
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# doit
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def doit():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	with CF.withPickles(f"""{CF.CONFIG_DIR}runawayClock/runawayClock.pkl""", APPDS), \
			CLASS_CLOCKS(CF.serializeIt(""), FORM_CLOCKS):

		doMidnightWork()

		while True:
			_result_ = outerLoop()

			if _result_ == BTN_QUIT_ALL:
				break

			elif _result_ == APPMODE_NEW_ALARMPOPUP:
				pass

			else:
				print(f"""I don't know how to handle {CF.frameIt("_result_", _result_)}""")
				break
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# end of PSG_TIME.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#
"""
edit:
	radio: EVENTMODE
	add new events
	delete this event
	TIME_s
CLOCKS_FORMMAIN.__dict__["TKroot"].__str__
CLOCKS_FORMMAIN[TIME_CLOCK].DisplayText
CLOCKS_FORMMAIN.Move(10, 10)

"""
