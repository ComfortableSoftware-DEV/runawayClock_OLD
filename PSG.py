

import PySimpleGUI as SG


import CF


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0900 DEF1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BLACK = "#000000"  # black
CLOCKS_SZ_TIME_CLOCK = 20  # size of the main clock on the clocks only floating widget
CLOCKS_SZ_TIME_ELAPSED = 10  # size of the elapsed clock on the clocks only floating widget
CLOCKS_SZ_TIME_TOGO = 10  # size of the main togo clock on the clocks only floating widget
COLOR_BACKGROUND = "#331122"  # the background of the main frames
COLOR_CLOCK_BACKGROUND = "#221133"  # the background of the main frames
COLOR_TEXT_HIGH = "#CC0088"  # the highlight color used in blinking bits when they are 'lit'
COLOR_TEXT_LOW = "#330022"  # the color the clock digits are
COLOR_TEXT_NORMAL = "#660044"  # the color the clock digits are
COLOR_TIME_CLOCK = "#882299"  # color of the clock on any window/frame/etc.
COLOR_TIME_ELAPSED = "#447733"  # color of the clock on any window/frame/etc.
COLOR_TIME_TOGO = "#AA6600"  # color of the clock on any window/frame/etc.
EDIT_SZ_CLOCK_TOGO = 10  # size of the main togo clock on the clocks only floating widget
EDIT_SZ_TIME_CLOCK = 20  # size of the main clock on the clocks only floating widget
EDIT_SZ_TIME_ELAPSED = 10  # size of the elapsed clock on the clocks only floating widget
FONT_DEFAULT = "Source Code Pro"  # set the main font
GRAY3 = "#333333"  # gray 3
GRAY6 = "#666666"  # gray 6
GRAY9 = "#999999"  # gray 9
GRAYC = "#CCCCCC"  # gray C
JUSTIFICATION_CENTER = "center"  # comment
JUSTIFICATION_LEFT = "left"  # comment
JUSTIFICATION_RIGHT = "right"  # comment
MAIN_SZ_TIME_CLOCK = 60  # size of the main clock on the clocks only floating widget
MAIN_SZ_TIME_ELAPSED = 30  # size of the elapsed clock on the clocks only floating widget
MAIN_SZ_TIME_TOGO = 30  # size of the main togo clock on the clocks only floating widget
WHITE = "#FFFFFF"  # white


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0901 DEF2
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
APPMODE = APPMODE_CLOCKS  # what screen are we showing APPMODE_CLOCKS or APPMODE_CLOCKS+APPMODE_MAIN[+APPMODE_EDIT]
AVOID_MOUSE = "AVOID_MOUSE"  # key for avoiding the mouse bool
CLOCKS_FONTSZ_TIME_CLOCK = (FONT_DEFAULT, CLOCKS_SZ_TIME_CLOCK)  # the font for the clocks only clock
CLOCKS_FONTSZ_TIME_ELAPSED = (FONT_DEFAULT, CLOCKS_SZ_TIME_ELAPSED)  # the font for the clocks only clock
CLOCKS_FONTSZ_TIME_TOGO = (FONT_DEFAULT, CLOCKS_SZ_TIME_TOGO)  # the font for the clocks only clock
COLOR_BTN_BACKGROUND = "#441133"  # background color on buttons by default
COLOR_BTN_TEXT = "#660044"  # text color on buttons by default
COLORS_BTN_NORMAL = (COLOR_TEXT_NORMAL, COLOR_BACKGROUND)  # comment
COLORS_TEXT_HIGH = (COLOR_TEXT_HIGH, COLOR_BACKGROUND)  # combined colors for a clock text element
COLORS_TEXT_LOW = (COLOR_TEXT_LOW, COLOR_BACKGROUND)  # combined colors for a clock text element
COLORS_TEXT_NORMAL = (COLOR_TEXT_NORMAL, COLOR_BACKGROUND)  # combined colors for a clock text element
COLORS_TIME_CLOCK = (COLOR_TIME_CLOCK, COLOR_CLOCK_BACKGROUND)  # combined colors for a clock text element
COLORS_TIME_ELAPSED = (COLOR_TIME_ELAPSED, COLOR_CLOCK_BACKGROUND)  # combined colors for a clock text element
COLORS_TIME_TOGO = (COLOR_TIME_TOGO, COLOR_CLOCK_BACKGROUND)  # combined colors for a clock text element
DISMISSED = "DISMISSED"  # alarm dismissed bool
EVENT_ENTRIES = "EVENT_ENTRIES"  #
EVENT_MODE = "EVENT_MODE"  #
EVENT_MODE_ALARM = "EVENT_MODE_ALARM"  #
EVENT_MODE_ALARMREMIND = "EVENT_MODE_ALARMREMIND"  #
EVENT_MODE_INTERVAL = "EVENT_MODE_INTERVAL"  #
INDEX_OF_NEXT_EVENT = "INDEX_OF_NEXT_EVENT"  #
KEY_TIME_CLOCK = "KEY_TIME_CLOCK"  # key for all clocks time
KEY_TIME_ELAPSED = "KEY_TIME_ELAPSED"  # key for all clocks elapsed
KEY_TIME_TOGO = "KEY_TIME_TOGO"  # key for all clocks togo
NAME = "NAME"  #
PREDISMISSABLE = "PREDISMISSABLE"  #
RUNNING = "RUNNING"  # is this interval running or not
SNOOZABLE = "SNOOZABLE"  #
SNOOZED = "SNOOZED"  # snoozed bool
TIME_ALARM = "TIME_ALARM"  # the alarm time
TIME_CLOCK = "TIME_CLOCK"  # the main clock time
TIME_ELAPSED = "TIME_ELAPSED"  # 24 hour centric elapsed time running, can be reset, may go to 99h
TIME_INTERVAL = "TIME_INTERVAL"  #
TIME_OF_NEXT_EVENT = "TIME_OF_NEXT_EVENT"  # what time is the next alarm, == TIME_ALARM is tomorrow
TIME_REMIND = "TIME_REMIND"  #
TIME_TOGO = "TIME_TOGO"  # down counter to next event on this window/alarm/interval/reminder
TRANSPARENT = "TRANSPARENT"  #
TRANSPARENT_UNDER_MOUSE = "TRANSPARENT_UNDER_MOUSE"  # is the clock transparent under mouse (ineffective if mouse is avoided)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0910 DEF3
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0902 dicts
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
CLOCKS_DICT = {  # holds the values for the clocks frame
	KEY_TIME_CLOCK: "00:00:00",  # holds the values for the clocks frame
	KEY_TIME_ELAPSED: "00:00:00",  # holds the values for the clocks frame
	KEY_TIME_TOGO: "00:00:00",  # holds the values for the clocks frame
}


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
# * start of EMPTY_ALARM structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY_ALARMTUP = (
	(DISMISSED, False),  # bool is this event dismissed already
	(ENABLED, True),  # enabled state of this entry
	(EVENT_MODE, MODE_ALARM),  # set the mode to MODE_ALARM by default of course
	(NAME, ""),  # name of this entry
	(PREDISMISSABLE, True),  # pre-dismissable state of this entry
	(SNOOZABLE, False),  # enabled state of this entry
	(SNOOZED, True),  # enabled state of this entry
	(TIME_ALARM, "00:00:00"),  # time this alarm is set for
	(TIME_OF_NEXT_EVENT, "00:00:00"),  # post snooze or tomorrow
	(TIME_TOGO, "00:00:00"),  # post snooze or tomorrow
)

def EMPTY_ALARMDICT():
	return dict((x, y) for x, y in EMPTY_ALARMTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTY_ALARM_REMIND structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY_ALARM_REMINDTUP = (
	(DISMISSED, False),  # bool is this event dismissed already
	(ENABLED, True),  # enabled state of this entry
	(EVENT_MODE, MODE_ALARMREMIND),  # set the mode to MODE_ALARM by default of course
	(NAME, ""),  # name of this entry
	(PREDISMISSABLE, True),  # pre-dismissable state of this entry
	(SNOOZABLE, False),  # enabled state of this entry
	(SNOOZED, True),  # enabled state of this entry
	(TIME_ALARM, "00:00:00"),  # time this alarm is set for
	(TIME_OF_NEXT_EVENT, "00:00:00"),  # post snooze or tomorrow
	(TIME_REMIND, "00:00:00"),  # time this alarm is set for
	(TIME_TOGO, "00:00:00"),  # post snooze or tomorrow
)

def EMPTY_ALARM_REMINDDICT():
	return dict((x, y) for x, y in EMPTY_ALARM_REMINDTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTY_CLOCKS structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY_CLOCKSTUP = (
	(TIME_CLOCK, "00:00:00"),  # the main clock time
	(TIME_ELAPSED, "00:00:00"),  # the main elapsed time
	(TIME_OF_NEXT_EVENT, "00:00:00"),  # the main count down to the next event time
)

def EMPTY_CLOCKSDICT():
	return dict((x, y) for x, y in EMPTY_CLOCKSTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTY_INTERVAL structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTY_INTERVALTUP = (
	(ENABLED, True),  # enabled state of this entry
	(EVENT_MODE, MODE_INTERVAL),  # set the mode to MODE_ALARM by default of course
	(NAME, ""),  # name of this entry
	(RUNNING, True),  # running state of this entry
	(TIME_INTERVAL, "00:00:00"),  # time this alarm is set for
	(TIME_OF_NEXT_EVENT, "00:00:00"),  # post snooze or tomorrow
	(TIME_TOGO, "00:00:00"),  # post snooze or tomorrow
)

def EMPTY_INTERVALDICT():
	return dict((x, y) for x, y in EMPTY_INTERVALTUP)


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
	(TEXT, ""),  # Text to display next to checkbox
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
	(VERTICAL_SCROLL_ONLY, False),  # if Truen then no horizontal scrollbar will be shown
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
	(AUTO_SIZE_TEXT, None),  # if True size of the Text Element will be sized to fit the string provided in 'text' parm
	(BACKGROUND_COLOR, None),  # color of background
	(BORDER_WIDTH, None),  # number of pixels for the border (if using a relief)
	(CLICK_SUBMITS, False),  # DO NOT USE. Only listed for backwards compat - Use enable_events instead
	(ENABLE_EVENTS, False),  # Turns on the element specific events. Text events happen when the text is clicked
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
	(TEXT, ""),  # Text to display next to checkbox
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
# * SCTN0906 button elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0907 spin box elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0908 checkbox elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0909 text elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090A radio elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090B column elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090C window elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090D frame elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN090E layout elements
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0910 MAIN_DICT_DICT
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
CLOCKS_DICT = {  # holds the values for the clocks frame
	KEY_TIME_CLOCK: "00:00:00",  # holds the values for the clocks frame
	KEY_TIME_ELAPSED: "00:00:00",  # holds the values for the clocks frame
	KEY_TIME_TOGO: "00:00:00",  # holds the values for the clocks frame
}


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed sections of PSG.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of unmanaged sections of PSG.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# updateFromDict
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def updateFromDict(windowToUpdate_, dictToUpdateFrom_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	for key_, val_ in dictToUpdateFrom_.items():
		windowToUpdate_.FindElement(key_)(val_)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# end of PSG.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#
"""
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# class withIndexes
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
class withIndexes(object):
  # fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

  def __init__(self, destDir_):
    self.destDir_ = destDir_

  def __enter__(self):
    getIndexes(self.destDir_)

  def __exit__(self, t1_, t2_, t3_):
    # print(f" " " exiting withIndexes {CF.frameIt("t1_", t1_)} {CF.frameIt("t2_", t2_)} {CF.frameIt("t3_", t3_)}" " ")
    putIndexes(self.destDir_)

  # fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


"""
