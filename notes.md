# notes regarding runawayClock


[ ] | item
----|-------------------------------------------------------------------------------------------------------
[]  | actually make the bool flags work
[]  | add a counter of intervals, and a reset when counter clicked
[]  | alarms working
[]  | auto dismiss
[]  | auto dismiss, time 0 for no auto dismiss
[]  | check for dict or tdd data in MAPPDS before updating it, translate them back to tuples
[]  | default intervals to 5 seconds to start
[]  | flash clocks or theclock instead of popup for intervals
[]  | interval from a start time eg every half hour from 00:01:00
[]  | length of alarms
[]  | make event entries work from FM.py on
[]  | make the clocks mode able to invisible all except when over
[]  | mv PSG.py PSG_TIME.py to make sure these special modifications to PSG earn their keep
[]  | snoozing times and settings
[]  | time until dismissed timer
[]  | alarm in time count
[]  | clocks mode can be separated
[]  | edit mode, use combo for selecting which EVENT_ENTRIES entry to use
[]  | lowercase all parm keys to match PySimpleGui conventions
[]  | ** idea ran away before I could get it written **
[X] | (abandoned) convert all passed about things to a dict (ended up going back to tuples for all of these)
[X] | (abandoned) convert all tupdict here to tupdict_dict -=> the infamous TDD
[X] | (abandoned) main all seeing mode
[X] | (alarm+reminder working)
[X] | add TIME_AT_ZERO to CLOCKS_MAINFRAME
[X] | all the tupdict and tupdictdict ready
[X] | avoid mouse unless cornered/walled/overrun
[X] | fix elapsed after midnight
[X] | interval from when started
[X] | intervals working
[X] | make sure empty tupdict works
[X] | make time till next event time work
[X] | manage rewrite of the mainframe class to the ALARMPOPUP class
[x] | only switching to text to display
[X] | pos(x, y) to dict
[X] | read mouse
[X] | read position
[X] | remove reminders
[X] | remove unused structures
[X] | screen position saved in MAPPDS (added the space, and locator code)
[X] | sizes to dict for sure
[X] | start and stop times for intervals
[X] | switch all times to int seconds MTSS and MTSMS from strings
[X] | switching to all classes for the FRAMEs
    |





POPUPFRAME BringToFront bool
POPUPFRAME maximize bool


# execution notes

stopped after 21 hours or so, just like previously, no updating clocks
stopped again, right after 18:00 both times
restarted service at 18:27:45
restarted after upgrades at 19:30:50
stops again at 1800-ish

# eof
#
#
#
#


{
	0:
	{
		'ALARMPOPUP_TEXT_TEXT': 'time to start toward bed',
		'DISMISSED': False,
		'enabled': False,
		'EVENTMODE': 'EVENTMODE_INTERVAL',
		'FIRSTRUN': False,
		'IS_ALERTING_NOW': False,
		'NAME': 'wind it up',
		'PREDISMISSABLE': True,
		'REMIND_DISMISSED': False,
		'SNOOZABLE': False,
		'SNOOZED': False,
		'TIME_ALARM': 12600,
		'TIME_AT_LAST_RUN': 84720,
		'TIME_AT_NEXT': 86400,
		'TIME_INTERVAL': 240,
		'TIME_INTERVAL__BEGIN': 0,
		'TIME_INTERVAL__END': 0,
		'TIME_INTERVAL_START': 84720,
		'TIME_LEN_RING': 0,
		'TIME_REMIND': 0
	},
	1:
	{
		'ALARMPOPUP_TEXT_TEXT': 'MOVE',
		'DISMISSED': False,
		'enabled': True,
		'EVENTMODE': 'EVENTMODE_INTERVAL',
		'FIRSTRUN': False,
		'IS_ALERTING_NOW': False,
		'NAME': 'off you go then',
		'PREDISMISSABLE': True,
		'REMIND_DISMISSED': False,
		'SNOOZABLE': False,
		'SNOOZED': False,
		'TIME_ALARM': 0,
		'TIME_AT_LAST_RUN': 84900,
		'TIME_AT_NEXT': 84960,
		'TIME_INTERVAL': 60,
		'TIME_INTERVAL__BEGIN': 0,
		'TIME_INTERVAL__END': 0,
		'TIME_INTERVAL_START': 84900,
		'TIME_LEN_RING': 0,
		'TIME_REMIND': 0
	}
}

Popup = popup(*args, title=None, button_color=None, background_color=None, text_color=None, button_type=0, auto_close=False, auto_close_duration=None, custom_text=(None, None), non_blocking=False, icon=None, line_width=None, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None), any_key_closes=False, image=None, modal=True)
    Popup - Display a popup Window with as many parms as you wish to include.  This is the GUI equivalent of the
    "print" statement.  It's also great for "pausing" your program's flow until the user can read some error messages.

    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param title: Optional title for the window. If none provided, the first arg will be used instead.
    :type title: (str)
    :param button_color: Color of the buttons shown (text color, button color)
    :type button_color: Tuple[str, str] | None
    :param background_color: Window's background color
    :type background_color: (str)
    :param text_color: text color
    :type text_color: (str)
    :param button_type: NOT USER SET!  Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). There are many Popup functions and they call Popup, changing this parameter to get the desired effect.
    :type button_type: (int)
    :param auto_close: If True the window will automatically close
    :type auto_close: (bool)
    :param auto_close_duration: time in seconds to keep window open before closing it automatically
    :type auto_close_duration: (int)
    :param custom_text: A string or pair of strings that contain the text to display on the buttons
    :type custom_text: Tuple[str, str] | str
    :param non_blocking: If True then will immediately return from the function without waiting for the user's input.
    :type non_blocking: (bool)
    :param icon: icon to display on the window. Same format as a Window call
    :type icon: str | bytes
    :param line_width: Width of lines in characters.  Defaults to MESSAGE_BOX_LINE_WIDTH
    :type line_width: (int)
    :param font: specifies the font family, size, etc
    :type font: str | Tuple[font_name, size, modifiers]
    :param no_titlebar: If True will not show the frame around the window and the titlebar across the top
    :type no_titlebar: (bool)
    :param grab_anywhere: If True can grab anywhere to move the window. If no_titlebar is True, grab_anywhere should likely be enabled too
    :type grab_anywhere: (bool)
    :param location: Location on screen to display the top left corner of window. Defaults to window centered on screen
    :type location: Tuple[int, int]
    :param keep_on_top: If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param any_key_closes: If True then will turn on return_keyboard_events for the window which will cause window to close as soon as any key is pressed.  Normally the return key only will close the window.  Default is false.
    :type any_key_closes: (bool)
    :param image: Image to include at the top of the popup window
    :type image: (str) or (bytes)
    :param modal: If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True
    :type modal: bool
    :return: Returns text of the button that was pressed.  None will be returned if user closed window with X
    :rtype: str | None


PopupAutoClose = popup_auto_close(*args, title=None, button_type=0, button_color=None, background_color=None, text_color=None, auto_close=True, auto_close_duration=None, non_blocking=False, icon=None, line_width=None, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None), image=None, modal=True)
    Popup that closes itself after some time period

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_type: Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK).
    :type button_type: (int)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str] or str
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: int | float
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: bytes | str
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font: specifies the font family, size, etc
    :type font: str | Tuple[str, int]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top: If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param image: Image to include at the top of the popup window
    :type image: (str) or (bytes)
    :param modal: If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True
    :type modal: bool
    :return: Returns text of the button that was pressed.  None will be returned if user closed window with X
    :rtype: str | None | TIMEOUT_KEY
