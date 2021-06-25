# notes regarding runawayClock


[ ] | item
----|-------------------------------------------------------------------------------------------------------
[]  | auto create res/MARKDOWN/__SCTNS__.md
[]  | auto create res/MARKDOWN/ files
[]  | including functions in main section of all managed files
[]  |
[]  | alarm in time count
[]  | alarms working
[]  | auto dismiss
[]  | auto dismiss, time 0 for no auto dismiss
[]  | check for dict or tdd data in MAPPDS before updating it, translate them back to tuples
[]  | document naming of things such as checkboxes between inside and outside the classes, etc
[]  | edit mode, use combo for selecting which EVENT_ENTRIES entry to use
[]  | flash clocks or theclock instead of popup for intervals
[]  | length of alarms
[]  | lowercase all parm keys to match PySimpleGui conventions
[]  | make event entries work from FM.py on
[]  | make sure doEvent() clears events before each findNextAlarmEvent()
[]  | possiblity of making APPDS a class with it's own support
[]  | see below for clock rearrange
[]  | snoozing times and settings
[]  | time until dismissed timer
[A] | (abandoned) convert all passed about things to a dict (ended up going back to tuples for all of these)
[A] | (abandoned) convert all tupdict here to tupdict_dict -=> the infamous TDD
[A] | (abandoned) main all seeing mode
[A] | clocks mode can be separated
[A] | default intervals to 5 seconds to start
[A] | mv PSG.py PSG_TIME.py to make sure these special modifications to PSG earn their keep
[M] | interval from a start time eg every half hour from 00:01:00
[M] | switch to automatic _DICTIN_, _DICTOUT_, and __CDS__ from a bool in TBGLST
[X] | (alarm+reminder working)
[X] | actually make the bool flags work
[X] | add a counter of intervals, and a reset when counter clicked
[X] | add TIME_AT_ZERO to CLOCKS_MAINFRAME
[X] | all the tupdict and tupdictdict ready
[X] | avoid mouse unless cornered/walled/overrun
[X] | convert APPDS_MAIN\[K_EVENT_ENTRIES\]\[K_ALARMPOPUP_TEXT_TEXT\] from "" to \[""\] (string to list)
[X] | fix elapsed after midnight
[X] | hide clock2/theClock on mouse hover for a set time, so it can be clicked through
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
[X] | update all flipped items to lists

### rearange clocks

* shrink aux times considerably
  * far enough to get Q and Z buttons alongside them
  * move all other buttons to the right click menu
  * shrink _NAME_NEXT_EVENT_  and possibly the count so that both fit under TIME_CLOCK
  * shrink checkboxes more text, shorter, and darken the text a great deal
* darken the frame a great deal
* possibly redden the TIME_CLOCK, and darken
* darken all text
* try text only buttons
* add 3 digit days to elapsed timer
* 
