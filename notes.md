# notes regarding runawayClock


status   | [ ] | item
---------|-----|-------------------------------------------------------------------------------------------
consider | [ ] | clocks mode can be separated
consider | [ ] | lowercase all parm keys to match PySimpleGui conventions
do       | [X] | avoid mouse unless cornered/walled/overrun
do       | [ ] | edit mode
do       | [ ] | main all seeing mode
do       | [X] | read mouse
do       | [X] | read position
do       | [X] | screen position saved in MAPPDS (added the space, and locator code)
do       | [ ] | alarm in time, with and without reminders
do       | []  | interval from when started
do       | []  | interval from a start time eg every half hour from 00:01:00
do       | []  | make time till next event time work
do       | []  | snoozing times and settings
do       | []  | actually make the bool flags work
do       | []  | make event entries work from FM.py on
do       | []  | make sure empty tupdict works
do       | []  | all the tupdict and tupdictdict ready
do       | []  | convert all passed about things to a dict
         | []  | sizes to dict for sure
         | []  | pos(x, y) to dict
         | []  | convert all tupdict here to tupdict_dict -=> the infamous TDD
         | []  | check for dict or tdd data in MAPPDS before updating it, translate them back to tuples
         | []  | add TIME_AT_ZERO to CLOCKS_MAINFRAME
         | []  | mv PSG.py PSG_TIME.py to make sure these special modifications to PSG earn their keep
         | []  | switch all times to int seconds wallclock from strings
         | []  | only switching to text to display
         |     | also for incrementing, pre cache int for all times, and do everything with raw int seconds
         |     | all times int + HMS, only using HMS when it's time to zero check the main clock
  |   |  convert back to all tuples instead of dicts (x, y) (north, west, south, east)
  |   |  #
  |   |  #
  |   |  #
  |   |  
