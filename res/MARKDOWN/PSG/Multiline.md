class Multiline(Element)
      Multiline(default_text='', enter_submits=False, disabled=False, autoscroll=False, border_width=None, size=(None, None), s=(None, None), auto_size_text=None, background_color=None, text_color=None, change_submits=False, enable_events=False, do_not_clear=True, key=None, k=None, write_only=False, auto_refresh=False, reroute_stdout=False, reroute_stderr=False, reroute_cprint=False, echo_stdout_stderr=False, focus=False, font=None, pad=None, tooltip=None, justification=None, no_scrollbar=False, right_click_menu=None, visible=True, metadata=None)
 
Multiline Element - Display and/or read multiple lines of text.  This is both an input and output element.
Other PySimpleGUI ports have a separate MultilineInput and MultilineOutput elements.  May want to split this
one up in the future too.
 
    

Method resolution order:
    Multiline
    Element
    builtins.object

Methods defined here:

Get = get(self)

Update = update(self, value=None, disabled=None, append=False, font=None, text_color=None, background_color=None, text_color_for_value=None, background_color_for_value=None, visible=None, autoscroll=None, justification=None)

__del__(self)
    If this Widget is deleted, be sure and restore the old stdout, stderr

__init__(self, default_text='', enter_submits=False, disabled=False, autoscroll=False, border_width=None, size=(None, None), s=(None, None), auto_size_text=None, background_color=None, text_color=None, change_submits=False, enable_events=False, do_not_clear=True, key=None, k=None, write_only=False, auto_refresh=False, reroute_stdout=False, reroute_stderr=False, reroute_cprint=False, echo_stdout_stderr=False, focus=False, font=None, pad=None, tooltip=None, justification=None, no_scrollbar=False, right_click_menu=None, visible=True, metadata=None)
    :param default_text: Initial text to show
    :type default_text: (str)
    :param enter_submits: if True, the Window.Read call will return is enter key is pressed in this element
    :type enter_submits: (bool)
    :param disabled: set disable state
    :type disabled: (bool)
    :param autoscroll: If True the contents of the element will automatically scroll as more data added to the end
    :type autoscroll: (bool)
    :param border_width: width of border around element in pixels
    :type border_width: (int)
    :param size: (width, height) width = characters-wide, height = rows-high
    :type size: (int, int) | (None, None)
    :param s: Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
    :type s: (int, int) | (None, None)
    :param auto_size_text: if True will size the element to match the length of the text
    :type auto_size_text: (bool)
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
    :type change_submits: (bool)
    :param enable_events: Turns on the element specific events. Spin events happen when an item changes
    :type enable_events: (bool)
    :param do_not_clear: if False the element will be cleared any time the Window.Read call returns
    :type do_not_clear: (bool)
    :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
    :type key: str | int | tuple | object
    :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k: str | int | tuple | object
    :param write_only: If True then no entry will be added to the values dictionary when the window is read
    :type write_only: bool
    :param auto_refresh: If True then anytime the element is updated, the window will be refreshed so that the change is immediately displayed
    :type auto_refresh: (bool)
    :param reroute_stdout: If True then all output to stdout will be output to this element
    :type reroute_stdout: (bool)
    :param reroute_stderr: If True then all output to stderr will be output to this element
    :type reroute_stderr: (bool)
    :param reroute_cprint: If True your cprint calls will output to this element. It's the same as you calling cprint_set_output_destination
    :type reroute_cprint: (bool)
    :param echo_stdout_stderr: If True then output to stdout and stderr will be output to this element AND also to the normal console location
    :type echo_stdout_stderr: (bool)
    :param focus: if True initial focus will go to this element
    :type focus: (bool)
    :param font: specifies the font family, size, etc
    :type font: str | Tuple[str, int]
    :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param justification: text justification. left, right, center. Can use single characters l, r, c.
    :type justification: (str)
    :param no_scrollbar: If False then a scrollbar will be shown (the default)
    :type no_scrollbar: (bool)
    :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
    :type right_click_menu: List[List[ List[str] | str ]]
    :param visible: set visibility state of the element
    :type visible: (bool)
    :param metadata: User metadata that can be set to ANYTHING
    :type metadata: (Any)

flush(self)
    Flush parameter was passed into a print statement.
    For now doing nothing.  Not sure what action should be taken to ensure a flush happens regardless.

get(self)
    Return current contents of the Multiline Element
     
    :return: current contents of the Multiline Element (used as an input type of Multiline
    :rtype: (str)

print(self, *args, end=None, sep=None, text_color=None, background_color=None, justification=None, colors=None, t=None, b=None, c=None)
    Print like Python normally prints except route the output to a multiline element and also add colors if desired
     
    colors -(str, str) or str.  A combined text/background color definition in a single parameter
     
    There are also "aliases" for text_color, background_color and colors (t, b, c)
    t - An alias for color of the text (makes for shorter calls)
    b - An alias for the background_color parameter
    c - Tuple[str, str] - "shorthand" way of specifying color. (foreground, backgrouned)
    c - str - can also be a string of the format "foreground on background"  ("white on red")
     
    With the aliases it's possible to write the same print but in more compact ways:
    cprint('This will print white text on red background', c=('white', 'red'))
    cprint('This will print white text on red background', c='white on red')
    cprint('This will print white text on red background', text_color='white', background_color='red')
    cprint('This will print white text on red background', t='white', b='red')
     
    :param args: The arguments to print
    :type args: (Any)
    :param end: The end char to use just like print uses
    :type end: (str)
    :param sep: The separation character like print uses
    :type sep: (str)
    :param text_color: The color of the text
    :type text_color: (str)
    :param background_color: The background color of the line
    :type background_color: (str)
    :param justification: text justification. left, right, center. Can use single characters l, r, c. Sets only for this value, not entire element
    :type justification: (str)
    :param colors: Either a tuple or a string that has both the text and background colors
    :type colors: (str) or Tuple[str, str]
    :param t: Color of the text
    :type t: (str)
    :param b: The background color of the line
    :type b: (str)
    :param c: Either a tuple or a string that has both the text and background colors
    :type c: (str) or Tuple[str, str]

reroute_stderr_to_here(self)
    Sends stderr to this element

reroute_stdout_to_here(self)
    Sends stdout (prints) to this element

restore_stderr(self)
    Restore a previously re-reouted stderr back to the original destination

restore_stdout(self)
    Restore a previously re-reouted stdout back to the original destination

update(self, value=None, disabled=None, append=False, font=None, text_color=None, background_color=None, text_color_for_value=None, background_color_for_value=None, visible=None, autoscroll=None, justification=None)
    Changes some of the settings for the Multiline Element. Must call `Window.Read` or `Window.Finalize` prior
    :param value: new text to display
    :type value: (str)
    :param disabled: disable or enable state of the element
    :type disabled: (bool)
    :param append: if True then new value will be added onto the end of the current value. if False then contents will be replaced.
    :type append: (bool)
    :param font: specifies the font family, size, etc
    :type font: str | Tuple[str, int]
    :param text_color: color of the text
    :type text_color: (str)
    :param background_color: color of background
    :type background_color: (str)
    :param text_color_for_value: color of the new text being added (the value paramter)
    :type text_color_for_value: (str)
    :param background_color_for_value: color of the new background of the text being added (the value paramter)
    :type background_color_for_value: (str)
    :param visible: set visibility state of the element
    :type visible: (bool)
    :param autoscroll: if True then contents of element are scrolled down when new text is added to the end
    :type autoscroll: (bool)
    :param justification: text justification. left, right, center. Can use single characters l, r, c. Sets only for this value, not entire element
    :type justification: (str)

write(self, txt)
    Called by Python (not tkinter?) when stdout or stderr wants to write
     
    :param txt: text of output
    :type txt: (str)

Methods inherited from Element:

SetFocus = set_focus(self, force=False)

SetTooltip = set_tooltip(self, tooltip_text)

__call__(self, *args, **kwargs)
    Makes it possible to "call" an already existing element.  When you do make the "call", it actually calls
    the Update method for the element.
    Example:    If this text element was in yoiur layout:
                sg.Text('foo', key='T')
                Then you can call the Update method for that element by writing:
                window.FindElement('T')('new text value')

bind(self, bind_string, key_modifier)
    Used to add tkinter events to an Element.
    The tkinter specific data is in the Element's member variable user_bind_event
    :param bind_string: The string tkinter expected in its bind function
    :type bind_string: (str)
    :param key_modifier: Additional data to be added to the element's key when event is returned
    :type key_modifier: (str)

block_focus(self, block=True)
    Enable or disable the element from getting focus by using the keyboard.
    If the block parameter is True, then this element will not be given focus by using
    the keyboard to go from one element to another.
    You CAN click on the element and utilize it.
     
    :param block: if True the element will not get focus via the keyboard
    :type block: bool

expand(self, expand_x=False, expand_y=False, expand_row=True)
    Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions
     
    :param expand_x: If True Element will expand in the Horizontal directions
    :type expand_x: (bool)
    :param expand_y: If True Element will expand in the Vertical directions
    :type expand_y: (bool)
    :param expand_row: If True the row containing the element will also expand. Without this your element is "trapped" within the row
    :type expand_row: (bool)

get_size(self)
    Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.
    :return: width and height of the element
    :rtype: Tuple[int, int]

hide_row(self)
    Hide the entire row an Element is located on.
    Use this if you must have all space removed when you are hiding an element, including the row container

set_cursor(self, cursor=None, cursor_color=None)
    Sets the cursor for the current Element.
    "Cursor" is used in 2 different ways in this call.
    For the parameter "cursor" it's actually the mouse pointer.
    For the parameter "cursor_color" it's the color of the beam used when typing into an input element
     
    :param cursor: The tkinter cursor name
    :type cursor: (str)
    :param cursor_color: color to set the "cursor" to
    :type cursor_color: (str)

set_focus(self, force=False)
    Sets the current focus to be on this element
     
    :param force: if True will call focus_force otherwise calls focus_set
    :type force: bool

set_size(self, size=(None, None))
    Changes the size of an element to a specific size.
    It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.
     
    :param size: The size in characters, rows typically. In some cases they are pixels
    :type size: (int, int)

set_tooltip(self, tooltip_text)
    Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').
     
    :param tooltip_text: the text to show in tooltip.
    :type tooltip_text: (str)

set_vscroll_position(self, percent_from_top)
    Attempts to set the vertical scroll postition for an element's Widget
    :param percent_from_top: From 0 to 1.0, the percentage from the top to move scrollbar to
    :type percent_from_top: (float)

unbind(self, bind_string)
    Removes a previously bound tkinter event from an Element.
    :param bind_string: The string tkinter expected in its bind function
    :type bind_string: (str)

unhide_row(self)
    Unhides (makes visible again) the row container that the Element is located on.
    Note that it will re-appear at the bottom of the window / container, most likely.

Readonly properties inherited from Element:

visible
    Returns visibility state for the element.  This is a READONLY property
    :return: Visibility state for element
    :rtype: (bool)

Data descriptors inherited from Element:

__dict__
    dictionary for instance variables (if defined)

__weakref__
    list of weak references to the object (if defined)

metadata
    Metadata is an Element property that you can use at any time to hold any value
    :return: the current metadata value
    :rtype: (Any)
