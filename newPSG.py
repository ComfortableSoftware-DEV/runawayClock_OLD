

from planar import BoundingBox as BB
from Xlib import display as DISP
import gc
import PySimpleGUI as SG


import CF


gc.enable()


#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0900 DEF1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
ALPHA_HIGH = "ALPHA_HIGH"  # alphahigh key
ALPHA_LOW = "ALPHA_LOW"  # alphalow key
ALPHA_MODE = "ALPHA_MODE"  # alpha mode key
APPMODE = "APPMODE"  # app mode key
APPMODE_CLOCKS = "APPMODE_CLOCKS"  # mode clocks only
APPMODE_EDIT = "APPMODE_EDIT"  # edit mode on top of main window
APPMODE_MAIN = "APPMODE_MAIN"  # main mode (xpand from clocks to this)
APPMODE_MOUSE_OVER = "APPMODE_MOUSE_OVER"  # main mode (xpand from clocks to this)
BBOX = "BBOX"  # BOUNDING BOX
BBOX_EAST = "BBOX_EAST"  # BOUNDING BOX_EAST
BBOX_NORTH = "BBOX_NORTH"  # BOUNDING BOX NORTH
BBOX_SOUTH = "BBOX_SOUTH"  # BOUNDING BOX_SOUTH
BBOX_WEST = "BBOX_WEST"  # BOUNDING BOX_WEST
BTN_DOWN = "BTN_DOWN"  # key for all of the button xpand
BTN_EDIT = "BTN_EDIT"  # key for all of the button xpand
BTN_QUIT = "BTN_QUIT"  # key for all of the button xpand
BTN_UP = "BTN_UP"  # key for all of the button xpand
BTN_XPAND = "BTN_XPAND"  # key for all of the button xpand
BTN_ZERO = "BTN_ZERO"  # key for all of the button xpand
CHECKBOX_ALPHA_LOW = "CHECKBOX_ALPHA_LOW"  # is the clock transparent under mouse (ineffective if mouse is avoided)
CHECKBOX_RUNAWAY = "CHECKBOX_RUNAWAY"  # key for avoiding the mouse bool
CLOSE_BBOX = "CLOSE_BBOX"  # CLOSE BOUNDING BOX
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
COLOR_TEXT_LOW = "#330022"  # the color the clock digits are
COLOR_TEXT_NORMAL = "#660044"  # the color the clock digits are
COLOR_TIME_CLOCK = "#9966FF"  # color of the clock on any window/frame/etc.
COLOR_TIME_ELAPSED = "#447733"  # color of the clock on any window/frame/etc.
COLOR_TIME_TOGO = "#AA6600"  # color of the clock on any window/frame/etc.
COLOR_WHITE = "#FFFFFF"  # white
DISMISSED = "DISMISSED"  # alarm dismissed bool
EVENT_ENTRIES = "EVENT_ENTRIES"  # 
EVENT_MODE = "EVENT_MODE"  # what mode is this event
EVENT_MODE_ALARM = "EVENT_MODE_ALARM"  # 
EVENT_MODE_ALARMREMIND = "EVENT_MODE_ALARMREMIND"  # 
EVENT_MODE_INTERVAL = "EVENT_MODE_INTERVAL"  # 
FONT_DEFAULT = "Source Code Pro"  # set the main font
INDEX_OF_NEXT_EVENT = "INDEX_OF_NEXT_EVENT"  # 
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
MOUSE_STATUS_NW = "MOUSE_STATUS_NW"  # mouse is northwest of checked element
MOUSE_STATUS_OVER = "MOUSE_STATUS_OVER"  # mouse is southwest of checked element
MOUSE_STATUS_S = "MOUSE_STATUS_S"  # mouse is south of checked element
MOUSE_STATUS_SE = "MOUSE_STATUS_SE"  # mouse is southeast of checked element
MOUSE_STATUS_SW = "MOUSE_STATUS_SW"  # mouse is southwest of checked element
MOUSE_STATUS_W = "MOUSE_STATUS_W"  # mouse is west of checked element
NAME = "NAME"  # 
PREDISMISSABLE = "PREDISMISSABLE"  # 
RUNNING = "RUNNING"  # is this interval running or not
SCREEN_POS = "SCREEN_POS"  # can this event be snoozed
SCREEN_SIZE = "SCREEN_SIZE"  # dimension of the screen
SNOOZABLE = "SNOOZABLE"  # can this event be snoozed
SNOOZED = "SNOOZED"  # snoozed bool
SZ_ALPHA_HIGH = 1.0  # high alpha
SZ_ALPHA_LOW = 0.1  # low alpha setting
SZ_BORDER_DEPTH = 0  # border depth
SZ_BTNS = 6  # size for button text
SZ_CLOCKS_MOVE = 10  # how far to move each time the mouse approaches
SZ_CLOCKS_TIME_CLOCK = 26  # size of the main clock on the clocks only floating widget
SZ_CLOCKS_TIME_ELAPSED = 13  # size of the elapsed clock on the clocks only floating widget
SZ_CLOCKS_TIME_TOGO = 13  # size of the main togo clock on the clocks only floating widget
SZ_CLOSE = 50  # close enough to move from the mouse
SZ_EDIT_TIME_CLOCK = 20  # size of the main clock on the clocks only floating widget
SZ_EDIT_TIME_ELAPSED = 10  # size of the elapsed clock on the clocks only floating widget
SZ_EDIT_TIME_TOGO = 10  # size of the main togo clock on the clocks only floating widget
SZ_MAIN_TIME_CLOCK = 60  # size of the main clock on the clocks only floating widget
SZ_MAIN_TIME_ELAPSED = 30  # size of the elapsed clock on the clocks only floating widget
SZ_MAIN_TIME_TOGO = 30  # size of the main togo clock on the clocks only floating widget
SZ_MARGINS_ALL = (0, 0)  # all margins default
SZ_MAX_DELTA = 30  # comment
SZ_MOVE_DIST = 15  # comment
SZ_PAD_ALL = ((1, 1), (1, 1))  # add padding to all the things
SZ_TIME_BTWN_MOVES = 100  # comment
TIME_ALARM = "TIME_ALARM"  # the alarm time
TIME_CLOCK = "TIME_CLOCK"  # the main clock time
TIME_ELAPSED = "TIME_ELAPSED"  # key for all clocks elapsed
TIME_INTERVAL = "TIME_INTERVAL"  # interval timer
TIME_OF_NEXT_EVENT = "TIME_OF_NEXT_EVENT"  # what time is the next alarm, == KEY_TIME_ALARM is tomorrow
TIME_REMIND = "TIME_REMIND"  # time yo send reminder
TIME_TOGO = "TIME_TOGO"  # down counter to next event on this window/alarm/interval/reminder
TITLE_CLOCKS = "CLOCKS"  # string with window title for APPMODE_CLOCKS
TITLE_EDIT = "edit an event"  # string with window title for APPMODE_CLOCKS
TITLE_MAIN = "Main window which is xpanded from CLOCKS window and pops up EDIT windows"  # string with window title for APPMODE_CLOCKS
TITLE_THECLOCK = "THECLOCK"  # string with window title for APPMODE_CLOCKS
TRANSPARENT = "TRANSPARENT"  # is the app transparent (only the buttons and text appears, all backgrounds are transparent, can click through transparent)
ZERO_CLOCK = "00:00:00"  # all the zeros


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
FONTSZ_BTNS = (FONT_DEFAULT, SZ_BTNS)  # comment
FONTSZ_CLOCKS_TIME_CLOCK = (FONT_DEFAULT, SZ_CLOCKS_TIME_CLOCK)  # the font for the clocks only clock
FONTSZ_CLOCKS_TIME_ELAPSED = (FONT_DEFAULT, SZ_CLOCKS_TIME_ELAPSED)  # the font for the clocks only clock
FONTSZ_CLOCKS_TIME_TOGO = (FONT_DEFAULT, SZ_CLOCKS_TIME_TOGO)  # the font for the clocks only clock
LAST_MOVED_MTS = CF.MTS() + SZ_TIME_BTWN_MOVES  # to throttle moves


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
CLOCKS_DICT = {  # holds the values for the clocks frame
	TIME_CLOCK: "ZERO_CLOCK",  # holds the values for the clocks frame
	TIME_ELAPSED: "ZERO_CLOCK",  # holds the values for the clocks frame
	TIME_TOGO: "ZERO_CLOCK",  # holds the values for the clocks frame
}


THECLOCK_DICT = {  # holds the values for the clocks frame
	TIME_CLOCK: "ZERO_CLOCK",  # holds the values for the clocks frame
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0903 lists
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
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
# * start of EMPTY0_BBOX structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY0_BBOXTUP = (
	(BBOX_EAST, 0),  # bbox east
	(BBOX_NORTH, 0),  # bbox north
	(BBOX_SOUTH, 0),  # bbox south
	(BBOX_WEST, 0),  # bbox west
)

def EMPTY0_BBOXDICT():
	return dict((x, y) for x, y in EMPTY0_BBOXTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTY0_EVENT_ENTRIES structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY0_EVENT_ENTRIESTUP = (
)

def EMPTY0_EVENT_ENTRIESDICT():
	return dict((x, y) for x, y in EMPTY0_EVENT_ENTRIESTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTY0_EVENTS_ENTRIES structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY0_EVENTS_ENTRIESTUP = (
	(DISMISSED, False),  # has the event been dismissed just this once
	(ENABLED, True),  # is the event enabled bool
	(EVENT_MODE, EVENT_MODE_ALARM),  # which event mode is this event
	(NAME, alarm),  # the name of this event
	(PREDISMISSABLE, False),  # can the event be dismissed prior to on time
	(SNOOZABLE, False),  # can the alarm be snoozed
	(SNOOZED, False),  # is the event snoozed
	(TIME_ALARM, ZERO_CLOCK),  # in an alarm mode event, what time is the alarm
	(TIME_INTERVAL, ZERO_CLOCK),  # how much time to add to an interval mode event
	(TIME_REMIND, ZERO_CLOCK),  # wall time at the next alarm
)

def EMPTY0_EVENTS_ENTRIESDICT():
	return dict((x, y) for x, y in EMPTY0_EVENTS_ENTRIESTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTY_ALARM structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY_ALARMTUP = (
	(DISMISSED, False),  # bool is this event dismissed already
	(ENABLED, True),  # enabled state of this entry
	(EVENT_MODE, EVENT_MODE_ALARM),  # set the mode to EVENT_MODE_ALARM by default of course
	(NAME, ),  # name of this entry
	(PREDISMISSABLE, True),  # pre-dismissable state of this entry
	(SNOOZABLE, False),  # enabled state of this entry
	(SNOOZED, True),  # enabled state of this entry
	(TIME_ALARM, ZERO_CLOCK),  # time this alarm is set for
	(TIME_OF_NEXT_EVENT, ZERO_CLOCK),  # post snooze or tomorrow
	(TIME_TOGO, ZERO_CLOCK),  # post snooze or tomorrow
)

def EMPTY_ALARMDICT():
	return dict((x, y) for x, y in EMPTY_ALARMTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTY_ALARM_REMIND structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY_ALARM_REMINDTUP = (
	(DISMISSED, False),  # bool is this event dismissed already
	(ENABLED, True),  # enabled state of this entry
	(EVENT_MODE, EVENT_MODE_ALARMREMIND),  # set the mode to EVENT_MODE_ALARM by default of course
	(NAME, ),  # name of this entry
	(PREDISMISSABLE, True),  # pre-dismissable state of this entry
	(SNOOZABLE, False),  # enabled state of this entry
	(SNOOZED, True),  # enabled state of this entry
	(TIME_ALARM, ZERO_CLOCK),  # time this alarm is set for
	(TIME_OF_NEXT_EVENT, ZERO_CLOCK),  # post snooze or tomorrow
	(TIME_REMIND, ZERO_CLOCK),  # time this alarm is set for
	(TIME_TOGO, ZERO_CLOCK),  # post snooze or tomorrow
)

def EMPTY_ALARM_REMINDDICT():
	return dict((x, y) for x, y in EMPTY_ALARM_REMINDTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTY_CLOCKS structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY_CLOCKSTUP = (
	(TIME_CLOCK, ZERO_CLOCK),  # the main clock time
	(TIME_ELAPSED, ZERO_CLOCK),  # the main elapsed time
	(TIME_OF_NEXT_EVENT, ZERO_CLOCK),  # the main count down to the next event time
)

def EMPTY_CLOCKSDICT():
	return dict((x, y) for x, y in EMPTY_CLOCKSTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTY_INTERVAL structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY_INTERVALTUP = (
	(ENABLED, True),  # enabled state of this entry
	(EVENT_MODE, EVENT_MODE_INTERVAL),  # set the mode to EVENT_MODE_ALARM by default of course
	(NAME, ""),  # name of this entry
	(RUNNING, True),  # running state of this entry
	(TIME_INTERVAL, ZERO_CLOCK),  # time this alarm is set for
	(TIME_OF_NEXT_EVENT, ZERO_CLOCK),  # post snooze or tomorrow
	(TIME_TOGO, ZERO_CLOCK),  # post snooze or tomorrow
)

def EMPTY_INTERVALDICT():
	return dict((x, y) for x, y in EMPTY_INTERVALTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTY_MAPPDS structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY_MAPPDSTUP = (
	(ALPHA_CHANNEL, 1.0),  # fully opaque
	(ALPHA_HIGH, 1.0),  # fully opaque
	(ALPHA_LOW, 0.3),  # almost fully alpha
	(APPMODE, APPMODE_CLOCKS),  # default to clocks mode
	(CHECKBOX_ALPHA_LOW, True),  # the checkbox bool for ALPHA high/low mode
	(CHECKBOX_RUNAWAY, True),  # checkbox bool for RUNAWAY mode
	(INDEX_OF_NEXT_EVENT, 0),  # which event number is upcoming
	(TIME_CLOCK, ZERO_CLOCK),  # time wall clock
	(TIME_ELAPSED, ZERO_CLOCK),  # time elapsed empty
	(TIME_OF_NEXT_EVENT, ZERO_CLOCK),  # time of next event
	(TIME_TOGO, ZERO_CLOCK),  # time till next event empty clock
)

def EMPTY_MAPPDSDICT():
	return dict((x, y) for x, y in EMPTY_MAPPDSTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FULL_BUTTON structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

FULL_BUTTONTUP = (
	(AUTO_SIZE_BUTTON, None),  # if True the button size is sized to fit the text
	(BIND_RETURN_KEY, False),  # If True the return key will cause this button to be pressed
	(BORDER_WIDTH, None),  # width of border around button in pixels
	(BUTTON_COLOR, None),  # Color of button. default is from theme or the window. Easy to remember which is which if you say 'ON' between colors. 'red' on 'green'. Normally a tuple, but can be a simplified-button-color-string 'foreground on background'. Can be a single color if want to set only the background.
	(BUTTON_TEXT, ""),  # str text to display on the button
	(BUTTON_TYPE, 7),  # You  should NOT be setting this directly. ONLY the shortcut functions set this
	(CHANGE_SUBMITS, False),  # DO NOT USE. Only listed for backwards compat - Use enable_events instead
	(DEFAULT_EXTENSION, ""),  # If no extension entered by user, add this to filename (only used in saveas dialogs)
	(DISABLED, False),  # If True button will be created disabled. If FULL_BUTTON_DISABLED_MEANS_IGNORE then the button will be ignored rather than disabled using tkinter
	(DISABLED_BUTTON_COLOR, None),  # colors to use when button is disabled (text, background). Use None for a color if don't want to change. Only ttk buttons support both text and background colors. tk buttons only support changing text color
	(ENABLE_EVENTS, False),  # Turns on the element specific events. If this button is a target, should it generate an event when filled in
	(FILE_TYPES, (('ALL FILES', '*.*'),)),  # the filetypes that will be used to match files. To indicate all files: (('ALL Files', '*.*'),).  Note - NOT SUPPORTED ON MAC
	(FOCUS, False),  # if True, initial focus will be put on this button
	(FONT, None),  # specifies the font family, size, etc
	(HIGHLIGHT_COLORS, None),  # colors to use when button has focus (highlight, background). None will use computed colors. Only used by Linux and only for non-TTK button
	(IMAGE_DATA, None),  # Raw or Base64 representation of the image to put on button. Choose either filename or data
	(IMAGE_FILENAME, None),  # image filename if there is a button image. GIFs and PNGs only.
	(IMAGE_SIZE, (None, None)),  # Size of the image in pixels (width, height)
	(IMAGE_SUBSAMPLE, None),  # amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
	(INITIAL_FOLDER, None),  # starting path for folders and files
	(K, None),  # Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
	(KEY, None),  # Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
	(METADATA, None),  # User metadata that can be set to ANYTHING
	(PAD, None),  # Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
	(RIGHT_CLICK_MENU, None),  # A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
	(S, (None, None)),  # (width, height) of the button in characters wide, rows high
	(SIZE, (None, None)),  # (width, height) of the button in characters wide, rows high
	(TARGET, (None, None)),  # str | Tuple[int, int] key or (row,col) target for the button. Note that -1 for column means 1 element to the left of this one. The constant ThisRow is used to indicate the current row. The Button itself is a valid target for some types of button
	(TOOLTIP, None),  # text, that will appear when mouse hovers over the element
	(USE_TTK_BUTTONS, None),  # True = use ttk buttons. False = do not use ttk buttons.  None (Default) = use ttk buttons only if on a Mac and not with button images
	(VISIBLE, True),  # set visibility state of the element
)

def FULL_BUTTONDICT():
	return dict((x, y) for x, y in FULL_BUTTONTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FULL_CHECKBOX structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

FULL_CHECKBOXTUP = (
	(AUTO_SIZE_TEXT, None),  # if True will size the element to match the length of the text
	(BACKGROUND_COLOR, None),  # color of background
	(CHANGE_SUBMITS, False),  # DO NOT USE. Only listed for backwards compat - Use enable_events instead
	(CHECKBOX_COLOR, None),  # color of background of the box that has the check mark in it. The checkmark is the same color as the text
	(DEFAULT, False),  # Set to True if you want this checkbox initially checked
	(DISABLED, False),  # set disable state
	(ENABLE_EVENTS, False),  # Turns on the element specific events. Checkbox events happen when an item changes
	(FONT, None),  # specifies the font family, size, etc
	(K, None),  # Used with window.FindElement and with return values to uniquely identify this element
	(KEY, None),  # Used with window.FindElement and with return values to uniquely identify this element
	(METADATA, None),  # User metadata that can be set to ANYTHING
	(PAD, None),  # Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
	(S, (None, None)),  # (width, height) width = characters-wide, height = rows-high
	(SIZE, (None, None)),  # (width, height) width = characters-wide, height = rows-high
	(TEXT, ""),  # Window to display next to checkbox
	(TEXT_COLOR, None),  # color of the text
	(TOOLTIP, None),  # that will appear when mouse hovers over the element
	(VISIBLE, True),  # set visibility state of the element
)

def FULL_CHECKBOXDICT():
	return dict((x, y) for x, y in FULL_CHECKBOXTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FULL_COLUMN structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

FULL_COLUMNTUP = (
	(BACKGROUND_COLOR, None),  # color of background of entire Column
	(ELEMENT_JUSTIFICATION, None),  # All elements inside the Column will have this justification 'left', 'right', 'center' are valid values
	(EXPAND_X, None),  # If True the column will automatically expand in the X direction to fill available space
	(EXPAND_Y, None),  # If True the column will automatically expand in the X direction to fill available space
	(GRAB, None),  # If True can grab this element and move the window around. Default is False
	(JUSTIFICATION, None),  # set justification for the Column itself. Note entire row containing the Column will be affected
	(K, None),  # Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
	(KEY, None),  # Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
	(LAYOUT, []),  # Layout that will be shown in the Column container
	(METADATA, None),  # User metadata that can be set to ANYTHING
	(PAD, None),  # Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
	(RIGHT_CLICK_MENU, None),  # A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
	(S, (None, None)),  # (width, height) size in pixels (doesn't work quite right, sometimes only 1 dimension is set by tkinter
	(SCROLLABLE, False),  # if True then scrollbars will be added to the column
	(SIZE, (None, None)),  # (width, height) size in pixels (doesn't work quite right, sometimes only 1 dimension is set by tkinter
	(VERTICAL_SCROLL_ONLY, False),  # if True then no horizontal scrollbar will be shown
	(VERTICAL_ALIGNMENT, None),  # Place the column at the 'top', 'center', 'bottom' of the row (can also use t,c,r). Defaults to no setting (tkinter decides)
	(VISIBLE, True),  # set visibility state of the element
)

def FULL_COLUMNDICT():
	return dict((x, y) for x, y in FULL_COLUMNTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FULL_COMBO structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

FULL_COMBOTUP = (
	(AUTO_SIZE_TEXT, None),  # True if element should be the same size as the contents
	(BACKGROUND_COLOR, None),  # color of background
	(CHANGE_SUBMITS, False),  # DEPRICATED DO NOT USE. Use `enable_events` instead
	(DEFAULT_VALUE, None),  # Choice to be displayed as initial value. Must match one of values variable contents
	(DISABLED, False),  # set disable state for element
	(ENABLE_EVENTS, False),  # 
	(FONT, None),  # specifies the font family, size, etc
	(K, None),  # Used with window.FindElement and with return values to uniquely identify this element
	(KEY, None),  # Used with window.FindElement and with return values to uniquely identify this element
	(METADATA, None),  # User metadata that can be set to ANYTHING
	(PAD, None),  # Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
	(READONLY, False),  # make element readonly (user can't change). True means user cannot change
	(S, (None, None)),  # width, height. Width = characters-wide, height = NOTE it's the number of entries to show in the list
	(SIZE, (None, None)),  # width, height. Width = characters-wide, height = NOTE it's the number of entries to show in the list
	(TEXT_COLOR, None),  # color of the text
	(TOOLTIP, None),  # text that will appear when mouse hovers over this element
	(VALUES, []),  # values to choose. While displayed as text, the items returned are what the caller supplied, not text
	(VISIBLE, True),  # set visibility state of the element
)

def FULL_COMBODICT():
	return dict((x, y) for x, y in FULL_COMBOTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FULL_RADIO structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

FULL_RADIOTUP = (
	(AUTO_SIZE_TEXT, None,),  # 
	(BACKGROUND_COLOR, None,),  # 
	(CHANGE_SUBMITS, False,),  # 
	(CIRCLE_COLOR, None,),  # 
	(DEFAULT, False,),  # 
	(DISABLED, False,),  # 
	(ENABLE_EVENTS, False,),  # 
	(FONT, None,),  # 
	(GROUP_ID, ""),  # Groups together multiple Radio Buttons. Any type works
	(K, None,),  # 
	(KEY, None,),  # 
	(METADATA, None),  # 
	(PAD, None,),  # 
	(S, (None, None),),  # 
	(SIZE, (None, None),),  # 
	(TEXT, ""),  # 
	(TEXT_COLOR, None,),  # 
	(TOOLTIP, None,),  # 
	(VISIBLE, True,),  # 
)

def FULL_RADIODICT():
	return dict((x, y) for x, y in FULL_RADIOTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FULL_SPIN structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

FULL_SPINTUP = (
	(AUTO_SIZE_TEXT, None),  # if True will size the element to match the length of the text
	(BACKGROUND_COLOR, None),  # color of background
	(CHANGE_SUBMITS, False),  # DO NOT USE. Only listed for backwards compat - Use enable_events instead
	(DISABLED, False),  # set disable state
	(ENABLE_EVENTS, False),  # Turns on the element specific events. Spin events happen when an item changes
	(FONT, None),  # specifies the font family, size, etc
	(INITIAL_VALUE, None),  # Initial item to show in window. Choose from list of values supplied
	(K, None),  # Used with window.FindElement and with return values to uniquely identify this element
	(KEY, None),  # Used with window.FindElement and with return values to uniquely identify this element
	(METADATA, None),  # User metadata that can be set to ANYTHING
	(PAD, None),  # Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
	(READONLY, False),  # readonly bool
	(S, (None, None)),  # (width, height) width = characters-wide, height = rows-high
	(SIZE, (None, None)),  # (width, height) width = characters-wide, height = rows-high
	(TEXT_COLOR, None),  # color of the text
	(TOOLTIP, None),  # text, that will appear when mouse hovers over the element
	(VALUES, []),  # List of valid values
	(VISIBLE, True),  # set visibility state of the element
)

def FULL_SPINDICT():
	return dict((x, y) for x, y in FULL_SPINTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FULL_TEXT structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

FULL_TEXTTUP = (
	(AUTO_SIZE_TEXT, None),  # if True size of the Window Element will be sized to fit the string provided in 'text' parm
	(BACKGROUND_COLOR, None),  # color of background
	(BORDER_WIDTH, None),  # number of pixels for the border (if using a relief)
	(CLICK_SUBMITS, False),  # DO NOT USE. Only listed for backwards compat - Use enable_events instead
	(ENABLE_EVENTS, False),  # Turns on the element specific events. Window events happen when the text is clicked
	(FONT, None),  # specifies the font family, size, etc
	(GRAB, None),  # If True can grab this element and move the window around. Default is False
	(JUSTIFICATION, None),  # how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center`
	(K, None),  # Same as the Key. You can use either k or key. Which ever is set will be used.
	(KEY, None),  # Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
	(METADATA, None),  # User metadata that can be set to ANYTHING
	(PAD, None),  # Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
	(RELIEF, None),  # relief style around the text. Values are same as progress meter relief values. Should be a constant that is defined at starting with 'RELIEF_' - `RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID`
	(RIGHT_CLICK_MENU, None),  # A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
	(S, (None, None)),  # Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
	(SIZE, (None, None)),  # (width, height) width = characters-wide, height = rows-high
	(TEXT, ),  # The text to display. Can include /n to achieve multiple lines.  Will convert (optional) parameter into a string
	(TEXT_COLOR, None),  # color of the text
	(TOOLTIP, None),  # text, that will appear when mouse hovers over the element
	(VISIBLE, True),  # set visibility state of the element
)

def FULL_TEXTDICT():
	return dict((x, y) for x, y in FULL_TEXTTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FULL_WINDOW structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

FULL_WINDOWTUP = (
	(ALPHA_CHANNEL, 1),  # Sets the opacity of the window. 0 = invisible 1 = completely visible. Values bewteen 0 & 1 will produce semi-transparent windows in SOME environments (The Raspberry Pi always has this value at 1 and cannot change.
	(AUTO_CLOSE, False),  # If True, the window will automatically close itself
	(AUTO_CLOSE_DURATION, 3),  # Number of seconds to wait before closing the window
	(AUTO_SIZE_BUTTONS, None),  # True if Buttons in this Window should be sized to exactly fit the text on this.
	(AUTO_SIZE_TEXT, None),  # True if Elements in Window should be sized to exactly fir the length of text
	(BACKGROUND_COLOR, None),  # color of background
	(BORDER_DEPTH, None),  # Default border depth (width) for all elements in the window
	(BUTTON_COLOR, None),  # Default button colors for all buttons in the window
	(DEBUGGER_ENABLED, True),  # Default border depth (width) for all elements in the window
	(DEFAULT_BUTTON_ELEMENT_SIZE, (None, None)),  # (width, height) size in characters (wide) and rows (high) for all Button elements in this window
	(DEFAULT_ELEMENT_SIZE, (45, 1)),  # size in characters (wide) and rows (high) for all elements in this window
	(DISABLE_CLOSE, False),  # If True, the X button in the top right corner of the window will no work.  Use with caution and always give a way out toyour users
	(DISABLE_MINIMIZE, False),  # if True the user won't be able to minimize window.  Good for taking over entire screen and staying that way.
	(ELEMENT_JUSTIFICATION, "left"),  # All elements in the Window itself will have this justification 'left', 'right', 'center' are valid values
	(ELEMENT_PADDING, None),  # Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom))
	(ENABLE_CLOSE_ATTEMPTED_EVENT, False),  # If True then the window will not close when 'X' clicked. Instead an event FULL_WINDOW_CLOSE_ATTEMPTED_EVENT if returned from window.read
	(FINALIZE, False),  # If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code
	(FONT, None),  # specifies the font family, size, etc
	(FORCE_TOPLEVEL, False),  # If True will cause this window to skip the normal use of a hidden master window
	(GRAB_ANYWHERE, False),  # If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems
	(ICON, None),  # Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO
	(KEEP_ON_TOP, False),  # If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm
	(LAYOUT, None),  # The layout for the window. Can also be specified in the Layout method
	(LOCATION, (None, None)),  # (x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen.
	(MARGINS, (None, None)),  # (left/right, top/bottom) Amount of pixels to leave inside the window's frame around the edges before your elements are shown.
	(METADATA, None),  # User metadata that can be set to ANYTHING
	(MODAL, False),  # If True then this window will be the only window a user can interact with until it is closed
	(NO_TITLEBAR, False),  # If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar
	(PROGRESS_BAR_COLOR, (None, None)),  # (bar color, background color) Sets the default colors for all progress bars in the window
	(RESIZABLE, False),  # If True, allows the user to resize the window. Note the not all Elements will change size or location when resizing.
	(RETURN_KEYBOARD_EVENTS, False),  # if True key presses on the keyboard will be returned as Events from Read calls
	(RIGHT_CLICK_MENU, None),  # A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
	(RIGHT_CLICK_MENU_BACKGROUND_COLOR, None),  # Background color for right click menus
	(RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR, None),  # Window color for disabled right click menu items
	(RIGHT_CLICK_MENU_FONT, None),  # Font for right click menus
	(RIGHT_CLICK_MENU_SELECTED_COLORS, (None, None)),  # Window AND background colors for a selected item. Can be a Tuple OR a color string. simplified-button-color-string 'foreground on background'. Can be a single color if want to set only the background.
	(RIGHT_CLICK_MENU_TEAROFF, False),  # If True then all right click menus can be torn off
	(RIGHT_CLICK_MENU_TEXT_COLOR, None),  # Window color for right click menus
	(SIZE, (None, None)),  # (width, height) size in pixels for this window. Normally the window is autosized to fit contents, not set to an absolute size by the user
	(TEXT_JUSTIFICATION, None),  # Default text justification for all Window Elements in window
	(TITLE, ""),  # The title that will be displayed in the Titlebar and on the Taskbar
	(TITLEBAR_BACKGROUND_COLOR, None),  # If custom titlebar indicated by use_custom_titlebar, then use this as background color
	(TITLEBAR_FONT, None),  # If custom titlebar indicated by use_custom_titlebar, then use this as title font
	(TITLEBAR_ICON, None),  # If custom titlebar indicated by use_custom_titlebar, then use this as the icon (file or base64 bytes)
	(TITLEBAR_TEXT_COLOR, None),  # If custom titlebar indicated by use_custom_titlebar, then use this as text color
	(TRANSPARENT_COLOR, None),  # Any portion of the window that has this color will be completely transparent. You can even click through these spots to the window under this window.
	(TTK_THEME, None),  # Set the tkinter ttk 'theme' of the window.  Default = DEFAULT_TTK_THEME.  Sets all ttk widgets to this theme as their default
	(USE_CUSTOM_TITLEBAR, None),  # If True, then a custom titlebar will be used instead of the normal titlebar
	(USE_DEFAULT_FOCUS, True),  # If True will use the default focus algorithm to set the focus to the 'Correct' element
	(USE_TTK_BUTTONS, None),  # Affects all buttons in window. True = use ttk buttons. False = do not use ttk buttons.  None = use ttk buttons only if on a Mac
)

def FULL_WINDOWDICT():
	return dict((x, y) for x, y in FULL_WINDOWTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of NORMAL_BUTTON structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

NORMAL_BUTTONTUP = (
	(BUTTON_COLOR, None),  # Color of button. default is from theme or the window. Easy to remember which is which if you say 'ON' between colors. 'red' on 'green'. Normally a tuple, but can be a simplified-button-color-string 'foreground on background'. Can be a single color if want to set only the background.
	(BUTTON_TEXT, ""),  # str text to display on the button
	(FOCUS, False),  # if True, initial focus will be put on this button
	(FONT, None),  # specifies the font family, size, etc
	(IMAGE_DATA, None),  # Raw or Base64 representation of the image to put on button. Choose either filename or data
	(IMAGE_FILENAME, None),  # image filename if there is a button image. GIFs and PNGs only.
	(KEY, None),  # Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
)

def NORMAL_BUTTONDICT():
	return dict((x, y) for x, y in NORMAL_BUTTONTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of NORMAL_CHECKBOX structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

NORMAL_CHECKBOXTUP = (
	(BACKGROUND_COLOR, None),  # color of background
	(CHECKBOX_COLOR, None),  # color of background of the box that has the check mark in it. The checkmark is the same color as the text
	(DEFAULT, False),  # Set to True if you want this checkbox initially checked
	(FONT, None),  # specifies the font family, size, etc
	(KEY, None),  # Used with window.FindElement and with return values to uniquely identify this element
	(TEXT, ""),  # Window to display next to checkbox
	(TEXT_COLOR, None),  # color of the text
)

def NORMAL_CHECKBOXDICT():
	return dict((x, y) for x, y in NORMAL_CHECKBOXTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of NORMAL_COMBO structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

NORMAL_COMBOTUP = (
	(BACKGROUND_COLOR, None),  # color of background
	(DEFAULT_VALUE, None),  # Choice to be displayed as initial value. Must match one of values variable contents
	(FONT, None),  # specifies the font family, size, etc
	(KEY, None),  # Used with window.FindElement and with return values to uniquely identify this element
	(SIZE, None),  # width, height. Width = characters-wide, height = NOTE it's the number of entries to show in the list
	(TEXT_COLOR, None),  # color of the text
	(VALUES, []),  # values to choose. While displayed as text, the items returned are what the caller supplied, not text
)

def NORMAL_COMBODICT():
	return dict((x, y) for x, y in NORMAL_COMBOTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of NORMAL_RADIO structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

NORMAL_RADIOTUP = (
	(BACKGROUND_COLOR, None,),  # 
	(CIRCLE_COLOR, None,),  # 
	(DEFAULT, False,),  # 
	(FONT, None,),  # 
	(GROUP_ID, ""),  # Groups together multiple Radio Buttons. Any type works
	(KEY, None,),  # 
	(SIZE, (None, None),),  # 
	(TEXT, ""),  # 
	(TEXT_COLOR, None,),  # 
)

def NORMAL_RADIODICT():
	return dict((x, y) for x, y in NORMAL_RADIOTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of NORMAL_SPIN structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

NORMAL_SPINTUP = (
	(BACKGROUND_COLOR, None),  # color of background
	(FONT, None),  # specifies the font family, size, etc
	(INITIAL_VALUE, None),  # Initial item to show in window. Choose from list of values supplied
	(KEY, None),  # Used with window.FindElement and with return values to uniquely identify this element
	(SIZE, (None, None)),  # (width, height) width = characters-wide, height = rows-high
	(TEXT_COLOR, None),  # color of the text
	(VALUES, []),  # List of valid values
)

def NORMAL_SPINDICT():
	return dict((x, y) for x, y in NORMAL_SPINTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of NORMAL_TEXT structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

NORMAL_TEXTTUP = (
	(BACKGROUND_COLOR, None),  # color of background
	(BORDER_WIDTH, None),  # number of pixels for the border (if using a relief)
	(FONT, None),  # specifies the font family, size, etc
	(GRAB, None),  # If True can grab this element and move the window around. Default is False
	(JUSTIFICATION, None),  # how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center`
	(KEY, None),  # Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
	(RELIEF, None),  # relief style around the text. Values are same as progress meter relief values. Should be a constant that is defined at starting with 'RELIEF_' - `RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID`
	(SIZE, (None, None)),  # (width, height) width = characters-wide, height = rows-high
	(TEXT, ),  # The text to display. Can include /n to achieve multiple lines.  Will convert (optional) parameter into a string
	(TEXT_COLOR, None),  # color of the text
)

def NORMAL_TEXTDICT():
	return dict((x, y) for x, y in NORMAL_TEXTTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of NORMAL_WINDOW structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

NORMAL_WINDOWTUP = (
	(BACKGROUND_COLOR, None),  # color of background
	(FINALIZE, False),  # If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code
	(FONT, None),  # specifies the font family, size, etc
	(GRAB_ANYWHERE, False),  # If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems
	(ICON, None),  # Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO
	(KEEP_ON_TOP, False),  # If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm
	(LAYOUT, None),  # The layout for the window. Can also be specified in the Layout method
	(LOCATION, (None, None)),  # (x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen.
	(MODAL, False),  # If True then this window will be the only window a user can interact with until it is closed
	(NO_TITLEBAR, False),  # If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar
	(TITLE, ""),  # The title that will be displayed in the Titlebar and on the Taskbar
	(TITLEBAR_BACKGROUND_COLOR, None),  # If custom titlebar indicated by use_custom_titlebar, then use this as background color
	(TITLEBAR_FONT, None),  # If custom titlebar indicated by use_custom_titlebar, then use this as title font
	(TITLEBAR_ICON, None),  # If custom titlebar indicated by use_custom_titlebar, then use this as the icon (file or base64 bytes)
	(TITLEBAR_TEXT_COLOR, None),  # If custom titlebar indicated by use_custom_titlebar, then use this as text color
	(TRANSPARENT_COLOR, None),  # Any portion of the window that has this color will be completely transparent. You can even click through these spots to the window under this window.
)

def NORMAL_WINDOWDICT():
	return dict((x, y) for x, y in NORMAL_WINDOWTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of UPDATE_COMBO structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

UPDATE_COMBOTUP = (
	(DISABLED, None),  # set disable state for element
	(FONT, None),  # specifies the font family, size, etc
	(READONLY, None),  # make element readonly (user can't change). True means user cannot change
	(SET_TO_INDEX, None),  # 
	(SIZE, None),  # width, height. Width = characters-wide, height = NOTE it's the number of entries to show in the list
	(VALUE, None),  # change which value is current selected based on new list of previous list of choices
	(VALUES, None),  # values to choose. While displayed as text, the items returned are what the caller supplied, not text
	(VISIBLE, None),  # set visibility state of the element
)

def UPDATE_COMBODICT():
	return dict((x, y) for x, y in UPDATE_COMBOTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0913 right click menu options
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
THECLOCK_RCMENU01 = [  # right click to do the things
	[],
	[
		BTN_QUIT,  # quit by right click
		CHECKBOX_ALPHA_LOW,  # toggle CHECKBOX_ALPHA_LOW
		CHECKBOX_RUNAWAY,  # toggle CHECKBOX_RUNAWAY
	],
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0906 button elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BTN_DOWN20 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the DOWN button
	IMAGE_FILENAME: "res/down20.png",  # filename for the button icon
	BORDER_WIDTH: 0,  # button xpand key
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_DOWN,  # button xpand key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_DOWN32 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the DOWN button
	IMAGE_FILENAME: "res/down32.png",  # filename for the button icon
	BORDER_WIDTH: 0,  # button xpand key
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_DOWN,  # button xpand key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_EDIT20 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the EDIT button
	IMAGE_FILENAME: "res/edit20.png",  # filename for the button icon
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_EDIT,  # button xpand key
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
	KEY: BTN_QUIT,  # button quit key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_QUIT32 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the QUIT button
	IMAGE_FILENAME: "res/quit32.png",  # filename for the button icon
	TOOLTIP: "quit the app",  # button_text empty for the QUIT button
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_QUIT,  # button quit key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_UP20 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the UP button
	IMAGE_FILENAME: "res/up20.png",  # filename for the button icon
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_UP,  # button xpand key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_UP32 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the UP button
	IMAGE_FILENAME: "res/up32.png",  # filename for the button icon
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_UP,  # button xpand key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_XPAND20 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the XPAND button
	IMAGE_FILENAME: "res/xpand20.png",  # filename for the button icon
	TOOLTIP: "expand to the big window from where you can edit events",  # tooltip
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_XPAND,  # button xpand key
	PAD: SZ_PAD_ALL,  # button xpand key
}


BTN_XPAND32 = {  # 
	BUTTON_TEXT: "",  # button_text empty for the XPAND button
	IMAGE_FILENAME: "res/xpand32.png",  # filename for the button icon
	TOOLTIP: "expand to the big window from where you can edit events",  # tooltip
	BUTTON_COLOR: COLORS_BTN_NORMAL,  # default button color
	FOCUS: True,  # focus on click
	FONT: FONTSZ_BTNS,  # button xpand font
	KEY: BTN_XPAND,  # button xpand key
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
CHECKBOX_ALPHA_LOW01 = {  # checkbox for alpha under mouse
	TEXT: "ALPHA_LOW",  # simple text reminder
	TOOLTIP: "low alpha under mouse",  # comment
	DEFAULT: True,  # leave it on by default
	KEY: CHECKBOX_ALPHA_LOW,  # set the key for the checkbox
}


CHECKBOX_RUNAWAY01 = {  # checkbox for runaway from mouse behavior
	TEXT: "RNAWY",  # text label
	TOOLTIP: "run away from mouse when checked",  # tooltip
	DEFAULT: True,  # leave it on by default
	KEY: CHECKBOX_RUNAWAY,  # set the key for the checkbox
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0909 text elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
CLOCKS_TEXT_TIME_CLOCK = {  # define the text element for CLOCKS_CLOCK_TIME
	TEXT: "ZERO_CLOCK",  # the text color for a clock_time element
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: True,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_CLOCK,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	KEY: TIME_CLOCK,  # comment
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (8, 1),  # characters, lines size line
	TEXT_COLOR: COLOR_TIME_CLOCK,  # the text color for a clock_time element
}


CLOCKS_TEXT_TIME_ELAPSED = {  # define the text element for CLOCKS_CLOCK_TIME
	TEXT: "ZERO_CLOCK",  # the text color for a clock_time element
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	FONT: FONTSZ_CLOCKS_TIME_ELAPSED,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	KEY: TIME_ELAPSED,  # comment
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (8, 1),  # characters, lines size line
	TEXT_COLOR: COLOR_TIME_ELAPSED,  # the text color for a clock_time element
}


CLOCKS_TEXT_TIME_TOGO = {  # define the text element for CLOCKS_CLOCK_TIME
	TEXT: "ZERO_CLOCK",  # the text color for a clock_time element
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	FONT: FONTSZ_CLOCKS_TIME_TOGO,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	KEY: TIME_TOGO,  # comment
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	SIZE: (8, 1),  # characters, lines size line
	TEXT_COLOR: COLOR_TIME_TOGO,  # the text color for a clock_time element
}


THECLOCK_TEXT_TIME_CLOCK = {  # define the text element for THECLOCK_CLOCK_TIME
	TEXT: "ZERO_CLOCK",  # the text color for a clock_time element
	BACKGROUND_COLOR: COLOR_CLOCK_BACKGROUND,  # background color for the clock elements
	ENABLE_EVENTS: False,  # this is clickable
	FONT: FONTSZ_CLOCKS_TIME_CLOCK,  # font+size line
	JUSTIFICATION: JUSTIFICATION_CENTER,  # center everything
	KEY: TIME_CLOCK,  # comment
	PAD: SZ_PAD_ALL,  # the text color for a clock_time element
	RIGHT_CLICK_MENU: THECLOCK_RCMENU01,  # add a right click for quit, runaway, alphalow
	SIZE: (8, 1),  # characters, lines size line
	TEXT_COLOR: COLOR_TIME_CLOCK,  # the text color for a clock_time element
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090A radio elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090B column elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
CLOCKS_COLUMN01 = [  # the column that puts the two smaller clocks below the main one
	[
		SG.Text(  # add a new TEXT element to clocks column
			**CLOCKS_TEXT_TIME_CLOCK,  # add the main clock
		),
	],
	[
		SG.Text(  # add a new text element to row01 clocks column
			**CLOCKS_TEXT_TIME_ELAPSED,  # add elapsed time
		),
		SG.Text(  # add a new row to clocks column
			**CLOCKS_TEXT_TIME_TOGO,  # add time to go
		),
	],
	[
		SG.Checkbox(  # add a new text element to row01 clocks column
			**CHECKBOX_RUNAWAY01,  # add elapsed time
		),
		SG.Checkbox(  # add a new text element to row01 clocks column
			**CHECKBOX_ALPHA_LOW01,  # add elapsed time
		),
	],
]


CLOCKS_COLUMN02 = [  # the column that puts the two smaller clocks below the main one
	[
		SG.Button(  # add a button element to clocks column
			**BTN_QUIT20,  # add the xpand button to clocks
		),
	],
	[
		SG.Button(  # add reset button for elapsed time
			**BTN_ZERO20,  # add the zero button to clocks
		),
	],
	[
		SG.Button(  # add reset button for elapsed time
			**BTN_XPAND20,  # add the zero button to clocks
		),
	],
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090E layout elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
CLOCKS_LAYOUT = [  # layout for APPMODE_CLOCKS
	[
		SG.Col(  # add a column
			layout=CLOCKS_COLUMN01,  # comment
			pad=SZ_PAD_ALL,  # comment
		),
		SG.Col(  # add a column
			layout=CLOCKS_COLUMN02,  # comment
			pad=SZ_PAD_ALL,  # comment
		),
	],
]


THECLOCK_LAYOUT = [  # layout for APPMODE_THECLOCK
	[
		SG.Text(  # add a column
			**THECLOCK_TEXT_TIME_CLOCK,  # comment
		),
	],
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090F window
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
CLOCKS_WINDOW = {  # define the clocks window
	ALPHA_CHANNEL: SZ_ALPHA_HIGH,  # set the high alpha as the default
	BACKGROUND_COLOR: COLOR_BACKGROUND,  # eliminate all not useful on the floating clocks
	BORDER_DEPTH: SZ_BORDER_DEPTH,  # border depth to zero
	ELEMENT_PADDING: SZ_PAD_ALL,  # all padding for elements ((1, 1), (1, 1)) by default
	FORCE_TOPLEVEL: None,  # 
	GRAB_ANYWHERE: True,  # eliminate all not useful on the floating clocks
	KEEP_ON_TOP: True,  # eliminate all not useful on the floating clocks
	LAYOUT: CLOCKS_LAYOUT,  # add the layout for CLOCKS_WINDOW
	MARGINS: SZ_MARGINS_ALL,  # 
	NO_TITLEBAR: True,  # no titlebar on APPMODE_CLOCKS window
	TITLE: TITLE_CLOCKS,  # 
}


THECLOCK_WINDOW = {  # define the clocks window
	ALPHA_CHANNEL: SZ_ALPHA_HIGH,  # set the high alpha as the default
	BACKGROUND_COLOR: COLOR_BACKGROUND,  # eliminate all not useful on the floating clocks
	BORDER_DEPTH: SZ_BORDER_DEPTH,  # border depth to zero
	ELEMENT_PADDING: SZ_PAD_ALL,  # all padding for elements ((1, 1), (1, 1)) by default
	FORCE_TOPLEVEL: None,  # 
	GRAB_ANYWHERE: True,  # eliminate all not useful on the floating clocks
	KEEP_ON_TOP: True,  # eliminate all not useful on the floating clocks
	LAYOUT: THECLOCK_LAYOUT,  # add the layout for THECLOCK_WINDOW
	MARGINS: SZ_MARGINS_ALL,  # 
	NO_TITLEBAR: True,  # no titlebar on APPMODE_THECLOCK window
	TITLE: TITLE_THECLOCK,  # 
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090D frame
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * CLOCKS_MAINFRAME_CLASS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
CLOCKS_MAINFRAME = None
class CLOCKS_MAINFRAME_CLASS():
	global CLOCKS_MAINFRAME

	def __enter__(self):
		global CLOCKS_MAINFRAME
		CLOCKS_MAINFRAME = SG.Window(
			**CLOCKS_WINDOW,
		).finalize()

	def __exit__(self, *args):
		global CLOCKS_MAINFRAME
		CLOCKS_MAINFRAME.close()


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * THECLOCK_MAINFRAME_CLASS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
THECLOCK_MAINFRAME = None
class THECLOCK_MAINFRAME_CLASS():
	global THECLOCK_MAINFRAME

	def __enter__(self):
		global THECLOCK_MAINFRAME
		THECLOCK_MAINFRAME = SG.Window(
			**THECLOCK_WINDOW,
		).finalize()

	def __exit__(self, *args):
		global THECLOCK_MAINFRAME
		THECLOCK_MAINFRAME.close()


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090C MAPPDS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
MAPPDS = {  # the struct holding everything passed betwixt PySimpleGUI and this app
	ALPHA_CHANNEL: 1.0,  # current AlphaChannel setting
	ALPHA_HIGH: 1.0,  # amount of seethrough when mouse is not hovering over CLOCKS or THECLOCK
	ALPHA_LOW: 0.3,  # amount of seethrough when mouse hovers over clocks or THECLOCK
	APPMODE: APPMODE_CLOCKS,  # default mode is clocks
	BBOX: EMPTY_BBOX_DICT,  # FILLED IN BY INIT
	CHECKBOX_ALPHA_LOW: True,  # default transparent under mouse when not cornered to True
	CHECKBOX_RUNAWAY: True,  # default to avoiding mouse
	CLOSE_BBOX: EMPTY_BBOX_DICT,  # FILLED IN BY INIT
	EVENT_ENTRIES: {  # holds events
		0: {
			DISMISSED: False,  # is this event dismissed
			ENABLED: True,  # is this event enabled
			EVENT_MODE: EVENT_MODE_ALARM,  # this entry's event_mode
			NAME: "wind it up",  # this entry's name
			PREDISMISSABLE: True,  # is this event dismissable in advance
			SNOOZABLE: False,  # can this event be snoozed
			SNOOZED: False,  # is this event snoozed
			TIME_ALARM: "ZERO_CLOCK",  # time of this event
			TIME_TOGO: "ZERO_CLOCK",  # updated only when the edit window is open with this event countdown to next event
		},
		1: {
			DISMISSED: False,  # is this event dismissed
			ENABLED: True,  # is this event enabled
			EVENT_MODE: EVENT_MODE_ALARM,  # this entry's event_mode
			NAME: "off you go then",  # this entry's name
			PREDISMISSABLE: True,  # is this event dismissable in advance
			SNOOZABLE: False,  # can this event be snoozed
			SNOOZED: False,  # is this event snoozed
			TIME_ALARM: "ZERO_CLOCK",  # time of this event
			TIME_TOGO: "ZERO_CLOCK",  # updated only when the edit window is open with this event countdown to next event
		},
	},
	INDEX_OF_NEXT_EVENT: 0,  # default to first entry as next until the app can sort through them
	SCREEN_POS: EMPTY_XY,  # current screen position
	SCREEN_SIZE: EMPTY_XY,  # current screen position
	TIME_CLOCK: "ZERO_CLOCK",  # start the clock at midnight
	TIME_ELAPSED: "ZERO_CLOCK",  # start the clock at midnight
	TIME_OF_NEXT_EVENT: "ZERO_CLOCK",  # holds the time of the next coming event for easy maths
	TIME_TOGO: "ZERO_CLOCK",  # start the clock at midnight
}


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed sections of PSG.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


