# notes regarding runawayClock


[ ] | item
----|-------------------------------------------------------------------------------------------------------
[]  | ** idea ran away before I could get it written **
[]  | actually make the bool flags work
[]  | add a counter of intervals, and a reset when counter clicked
[]  | alarm in time count
[]  | alarms working
[]  | auto dismiss
[]  | auto dismiss, time 0 for no auto dismiss
[]  | check for dict or tdd data in MAPPDS before updating it, translate them back to tuples
[]  | clocks mode can be separated
[]  | convert APPDS_MAIN\[K_EVENT_ENTRIES\]\[K_ALARMPOPUP_TEXT_TEXT\] from "" to \[""\]
[]  | default intervals to 5 seconds to start
[]  | document naming of things such as checkboxes between inside and outside the classes, etc
[]  | edit mode, use combo for selecting which EVENT_ENTRIES entry to use
[]  | flash clocks or theclock instead of popup for intervals
[]  | interval from a start time eg every half hour from 00:01:00
[]  | length of alarms
[]  | lowercase all parm keys to match PySimpleGui conventions
[]  | make event entries work from FM.py on
[]  | make sure doEvent() clears events before each findNextAlarmEvent()
[]  | make the clocks mode able to invisible all except when over
[]  | mv PSG.py PSG_TIME.py to make sure these special modifications to PSG earn their keep
[]  | see below for clock rearrange
[]  | snoozing times and settings
[]  | switch to automatic _DICTIN_, _DICTOUT_, and __CDS__ from a bool in TBGLST
[]  | time until dismissed timer
[]  | update all flipped items to lists
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
