

import PySimpleGUI as SG


import CF


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0900 DEF1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BACKGROUNDCOLOR = "#331122"  # the background of the main frames
BLACK = "#000000"  # black
GRAY3 = "#333333"  # gray 3
GRAY6 = "#666666"  # gray 6
GRAY9 = "#999999"  # gray 9
GRAYC = "#CCCCCC"  # gray C
NORMALCOLOR = "#660044"  # the color the clock digits are
NORMALHIGH = "#CC0088"  # the highlight color used in blinking bits when they are 'lit'
NORMALLOW = "#330022"  # the color the clock digits are
WHITE = "#FFFFFF"  # white


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0901 DEF2
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
ALPHA_CHANNEL = "alpha_channel"  # 
AUTO_CLOSE = "auto_close"  # 
AUTO_CLOSE_DURATION = "auto_close_duration"  # 
AUTO_SIZE_BUTTON = "auto_size_button"  # 
AUTO_SIZE_BUTTONS = "auto_size_buttons"  # 
AUTO_SIZE_TEXT = "auto_size_text"  # 
AVOIDMOUSE = "AVOIDMOUSE"  # 
BACKGROUND_COLOR = "background_color"  # 
BIND_RETURN_KEY = "bind_return_key"  # 
BORDER_DEPTH = "border_depth"  # 
BORDER_WIDTH = "border_width"  # 
BUTTON_COLOR = "button_color"  # 
BUTTON_TEXT = "button_text"  # 
BUTTON_TYPE = "button_type"  # 
CHANGE_SUBMITS = "change_submits"  # 
CHECKBOX_COLOR = "checkbox_color"  # color of background of the box that has the check mark in it. The checkmark is the same color as the text
CLOCKTIME = "CLOCKTIME"  # holds the clock value (str HH:MM:SS)
DEBUGGER_ENABLED = "debugger_enabled"  # 
DEFAULT = "default"  # 
DEFAULT_BUTTON_ELEMENT_SIZE = "default_button_element_size"  # 
DEFAULT_ELEMENT_SIZE = "default_element_size"  # 
DEFAULT_EXTENSION = "default_extension"  # 
DISABLE_CLOSE = "disable_close"  # 
DISABLE_MINIMIZE = "disable_minimize"  # 
DISABLED = "disabled"  # 
DISABLED_BUTTON_COLOR = "disabled_button_color"  # 
DISMISSED = "DISMISSED"  # alarm dismissed bool
ELAPSEDTIME = "ELAPSEDTIME"  # holds the elapsed time
ELEMENT_JUSTIFICATION = "element_justification"  # 
ELEMENT_PADDING = "element_padding"  # 
ENABLE_CLOSE_ATTEMPTED_EVENT = "enable_close_attempted_event"  # 
ENABLE_EVENTS = "enable_events"  # 
ENABLED = "enabled"  # 
EVENTENTRIES = "EVENTENTRIES"  # 
EVENTMODE = "EVENTMODE"  # 
EXPAND_X = "expand_x"  # 
EXPAND_Y = "expand_y"  # 
FILE_TYPES = "file_types"  # 
FINALIZE = "finalize"  # 
FOCUS = "focus"  # 
FONT = "font"  # 
FORCE_TOPLEVEL = "force_toplevel"  # 
GRAB = "grab"  # 
GRAB_ANYWHERE = "grab_anywhere"  # 
HIGHLIGHT_COLORS = "highlight_colors"  # 
ICON = "icon"  # 
IMAGE_DATA = "image_data"  # 
IMAGE_FILENAME = "image_filename"  # 
IMAGE_SIZE = "image_size"  # 
IMAGE_SUBSAMPLE = "image_subsample"  # 
INDEXNEXTEVENT = "INDEXNEXTEVENT"  # 
INITIAL_FOLDER = "initial_folder"  # 
JUSTIFICATION = "justification"  # 
K = "k"  # 
KEEP_ON_TOP = "keep_on_top"  # 
KEY = "key"  # 
LAYOUT = "layout"  # 
LOCATION = "location"  # 
MARGINS = "margins"  # 
METADATA = "metadata"  # 
MODAL = "modal"  # 
MODE_ALARM = "MODE_ALARM"  # 
MODE_ALARMREMIND = "MODE_ALARMREMIND"  # 
MODE_INTERVAL = "MODE_INTERVAL"  # 
NAME = "NAME"  # 
NEXTTIME = "NEXTTIME"  # holds the next scheduled time countdown
NO_TITLEBAR = "no_titlebar"  # 
PAD = "pad"  # 
PREDISMISSABLE = "PREDISMISSABLE"  # 
PROGRESS_BAR_COLOR = "progress_bar_color"  # 
RESIZABLE = "resizable"  # 
RETURN_KEYBOARD_EVENTS = "return_keyboard_events"  # 
RIGHT_CLICK_MENU = "right_click_menu"  # 
RIGHT_CLICK_MENU_BACKGROUND_COLOR = "right_click_menu_background_color"  # 
RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR = "right_click_menu_disabled_text_color"  # 
RIGHT_CLICK_MENU_FONT = "right_click_menu_font"  # 
RIGHT_CLICK_MENU_SELECTED_COLORS = "right_click_menu_selected_colors"  # 
RIGHT_CLICK_MENU_TEAROFF = "right_click_menu_tearoff"  # 
RIGHT_CLICK_MENU_TEXT_COLOR = "right_click_menu_text_color"  # 
RUNNING = "RUNNING"  # is this interval running or not
S = "s"  # 
SCROLLABLE = "scrollable"  # can this column be scrolled bool
SIZE = "size"  # 
SNOOZABLE = "SNOOZABLE"  # 
SNOOZED = "SNOOZED"  # snoozed bool
TARGET = "target"  # 
TEXT = "text"  # 
TEXT_COLOR = "text_color"  # 
TEXT_JUSTIFICATION = "text_justification"  # 
TIMEALARM = "TIMEALARM"  # 
TIMEELAPSED = "TIMEELAPSED"  # 24 hour centric elapsed time running, can be reset, may go to 99h
TIMEINTERVAL = "TIMEINTERVAL"  # 
TIMEOFNEXTEVENT = "TIMEOFNEXTEVENT"  # what time is the next alarm, == TIMEALARM is tomorrow
TIMEREMIND = "TIMEREMIND"  # 
TIMETONEXTEVENT = "TIMETONEXTEVENT"  # down counter to next event on this window/alarm/interval/reminder
TITLE = "title"  # 
TITLEBAR_BACKGROUND_COLOR = "titlebar_background_color"  # 
TITLEBAR_FONT = "titlebar_font"  # 
TITLEBAR_ICON = "titlebar_icon"  # 
TITLEBAR_TEXT_COLOR = "titlebar_text_color"  # 
TOOLTIP = "tooltip"  # 
TRANSPARENT = "TRANSPARENT"  # 
TRANSPARENT_COLOR = "transparent_color"  # 
TRANSPARENTUNDERMOUSE = "TRANSPARENTUNDERMOUSE"  # is the clock transparent under mouse (ineffective if mouse is avoided)
TTK_THEME = "ttk_theme"  # 
USE_CUSTOM_TITLEBAR = "use_custom_titlebar"  # 
USE_DEFAULT_FOCUS = "use_default_focus"  # 
USE_TTK_BUTTONS = "use_ttk_buttons"  # 
VERTICAL_ALIGNMENT = "vertical_alignment"  # 
VERTICAL_SCROLL_ONLY = "verticale_scroll_only"  # 
VISIBLE = "visible"  # 


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0902 dicts
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0903 lists
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0904 platform equalizers
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0905 tupdict
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTYALARM structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTYALARMTUP = (
	(DISMISSED, False),  # bool is this event dismissed already
	(ENABLED, True),  # enabled state of this entry
	(EVENTMODE, MODE_ALARM),  # set the mode to MODE_ALARM by default of course
	(NAME, ""),  # name of this entry
	(PREDISMISSABLE, True),  # pre-dismissable state of this entry
	(SNOOZABLE, False),  # enabled state of this entry
	(SNOOZED, True),  # enabled state of this entry
	(TIMEALARM, "00:00:00"),  # time this alarm is set for
	(TIMEOFNEXTEVENT, "00:00:00"),  # post snooze or tomorrow
	(TIMETONEXTEVENT, "00:00:00"),  # post snooze or tomorrow
)

def EMPTYALARMDICT():
	return dict((x, y) for x, y in EMPTYALARMTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTYALARMREMIND structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTYALARMREMINDTUP = (
	(DISMISSED, False),  # bool is this event dismissed already
	(ENABLED, True),  # enabled state of this entry
	(EVENTMODE, MODE_ALARMREMIND),  # set the mode to MODE_ALARM by default of course
	(NAME, ""),  # name of this entry
	(PREDISMISSABLE, True),  # pre-dismissable state of this entry
	(SNOOZABLE, False),  # enabled state of this entry
	(SNOOZED, True),  # enabled state of this entry
	(TIMEALARM, "00:00:00"),  # time this alarm is set for
	(TIMEOFNEXTEVENT, "00:00:00"),  # post snooze or tomorrow
	(TIMEREMIND, "00:00:00"),  # time this alarm is set for
	(TIMETONEXTEVENT, "00:00:00"),  # post snooze or tomorrow
)

def EMPTYALARMREMINDDICT():
	return dict((x, y) for x, y in EMPTYALARMREMINDTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTYINTERVAL structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTYINTERVALTUP = (
	(ENABLED, True),  # enabled state of this entry
	(EVENTMODE, MODE_INTERVAL),  # set the mode to MODE_ALARM by default of course
	(NAME, ""),  # name of this entry
	(RUNNING, True),  # running state of this entry
	(TIMEINTERVAL, "00:00:00"),  # time this alarm is set for
	(TIMEOFNEXTEVENT, "00:00:00"),  # post snooze or tomorrow
	(TIMETONEXTEVENT, "00:00:00"),  # post snooze or tomorrow
)

def EMPTYINTERVALDICT():
	return dict((x, y) for x, y in EMPTYINTERVALTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTYMAIN structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTYMAINTUP = (
	(AVOIDMOUSE, True),  # will the clock avoid the mouse or not bool
	(TIMECLOCK, "00:00:00"),  # the big clock time, updated every time anything is done
	(TIMEELAPSED, "00:00:00"),  # time elapsed since app started 24 hour centric, consider 99h (4 1/8 days)
	(TIMEOFNEXTEVENT, "00:00:00"),  # time of next event
	(TIMETONEXTEVENT, "00:00:00"),  # time to next event counting down
	(TRANSPARENTUNDERMOUSE, True),  # will the clock be transparent under the mouse (ineffective if mouse is avoided)
)

def EMPTYMAINDICT():
	return dict((x, y) for x, y in EMPTYMAINTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FULLBUTTON structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

FULLBUTTONTUP = (
	(AUTO_SIZE_BUTTON, None),  # if True the button size is sized to fit the text
	(BIND_RETURN_KEY, False),  # If True the return key will cause this button to be pressed
	(BORDER_WIDTH, None),  # width of border around button in pixels
	(BUTTON_COLOR, None),  # Color of button. default is from theme or the window. Easy to remember which is which if you say 'ON' between colors. 'red' on 'green'. Normally a tuple, but can be a simplified-button-color-string 'foreground on background'. Can be a single color if want to set only the background.
	(BUTTON_TEXT, ""),  # str text to display on the button
	(BUTTON_TYPE, 7),  # You  should NOT be setting this directly. ONLY the shortcut functions set this
	(CHANGE_SUBMITS, False),  # DO NOT USE. Only listed for backwards compat - Use enable_events instead
	(DEFAULT_EXTENSION, ""),  # If no extension entered by user, add this to filename (only used in saveas dialogs)
	(DISABLED, False),  # If True button will be created disabled. If FULLBUTTON_DISABLED_MEANS_IGNORE then the button will be ignored rather than disabled using tkinter
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

def FULLBUTTONDICT():
	return dict((x, y) for x, y in FULLBUTTONTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FULLCHECKBOX structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

FULLCHECKBOXTUP = (
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
	(TEXT, ""),  # Text to display next to checkbox
	(TEXT_COLOR, None),  # color of the text
	(TOOLTIP, None),  # that will appear when mouse hovers over the element
	(VISIBLE, True),  # set visibility state of the element
)

def FULLCHECKBOXDICT():
	return dict((x, y) for x, y in FULLCHECKBOXTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FULLCOLUMN structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

FULLCOLUMNTUP = (
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
	(VERTICAL_SCROLL_ONLY, False),  # if Truen then no horizontal scrollbar will be shown
	(VERTICAL_ALIGNMENT, None),  # Place the column at the 'top', 'center', 'bottom' of the row (can also use t,c,r). Defaults to no setting (tkinter decides)
	(VISIBLE, True),  # set visibility state of the element
)

def FULLCOLUMNDICT():
	return dict((x, y) for x, y in FULLCOLUMNTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of FULLWINDOW structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

FULLWINDOWTUP = (
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
	(ENABLE_CLOSE_ATTEMPTED_EVENT, False),  # If True then the window will not close when 'X' clicked. Instead an event FULLWINDOW_CLOSE_ATTEMPTED_EVENT if returned from window.read
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
	(RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR, None),  # Text color for disabled right click menu items
	(RIGHT_CLICK_MENU_FONT, None),  # Font for right click menus
	(RIGHT_CLICK_MENU_SELECTED_COLORS, (None, None)),  # Text AND background colors for a selected item. Can be a Tuple OR a color string. simplified-button-color-string 'foreground on background'. Can be a single color if want to set only the background.
	(RIGHT_CLICK_MENU_TEAROFF, False),  # If True then all right click menus can be torn off
	(RIGHT_CLICK_MENU_TEXT_COLOR, None),  # Text color for right click menus
	(SIZE, (None, None)),  # (width, height) size in pixels for this window. Normally the window is autosized to fit contents, not set to an absolute size by the user
	(TEXT_JUSTIFICATION, None),  # Default text justification for all Text Elements in window
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

def FULLWINDOWDICT():
	return dict((x, y) for x, y in FULLWINDOWTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of NORMALBUTTON structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

NORMALBUTTONTUP = (
	(BUTTON_COLOR, None),  # Color of button. default is from theme or the window. Easy to remember which is which if you say 'ON' between colors. 'red' on 'green'. Normally a tuple, but can be a simplified-button-color-string 'foreground on background'. Can be a single color if want to set only the background.
	(BUTTON_TEXT, ""),  # str text to display on the button
	(FOCUS, False),  # if True, initial focus will be put on this button
	(FONT, None),  # specifies the font family, size, etc
	(IMAGE_DATA, None),  # Raw or Base64 representation of the image to put on button. Choose either filename or data
	(IMAGE_FILENAME, None),  # image filename if there is a button image. GIFs and PNGs only.
	(KEY, None),  # Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
)

def NORMALBUTTONDICT():
	return dict((x, y) for x, y in NORMALBUTTONTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of NORMALCHECKBOX structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

NORMALCHECKBOXTUP = (
	(BACKGROUND_COLOR, None),  # color of background
	(CHECKBOX_COLOR, None),  # color of background of the box that has the check mark in it. The checkmark is the same color as the text
	(DEFAULT, False),  # Set to True if you want this checkbox initially checked
	(FONT, None),  # specifies the font family, size, etc
	(KEY, None),  # Used with window.FindElement and with return values to uniquely identify this element
	(TEXT, ""),  # Text to display next to checkbox
	(TEXT_COLOR, None),  # color of the text
)

def NORMALCHECKBOXDICT():
	return dict((x, y) for x, y in NORMALCHECKBOXTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of NORMALWINDOW structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

NORMALWINDOWTUP = (
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

def NORMALWINDOWDICT():
	return dict((x, y) for x, y in NORMALWINDOWTUP)


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed sections of PSG.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


