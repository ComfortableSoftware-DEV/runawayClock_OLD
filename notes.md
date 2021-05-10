# notes regarding runawayClock


status   | [ ] | item
---------|-----|--------------------------------------------------------------------------------------------------------------
consider | [ ] | clocks mode can be separated
consider | [ ] | lowercase all parm keys to match PySimpleGui conventions
do       | [X] | avoid mouse unless cornered/walled/overrun
do       | [ ] | edit mode
do       | [ ] | main all seeing mode
do       | [X] | read mouse
do       | [X] | read position
do       | [X] | screen position saved in MAPPDS (added the space, and locator code)
do       | [ ] | alarm in time, with and without reminders
do       | [X] | interval from when started
do       | []  | interval from a start time eg every half hour from 00:01:00
do       | [X] | make time till next event time work
do       | []  | snoozing times and settings
do       | []  | actually make the bool flags work
do       | []  | make event entries work from FM.py on
do       | [X] | make sure empty tupdict works
do       | [X] | all the tupdict and tupdictdict ready
do       | [X] | (abandoned) convert all passed about things to a dict (ended up going back to tuples for all of these)
         | [X] | sizes to dict for sure
         | [X] | pos(x, y) to dict
         | [X] | (abandoned) convert all tupdict here to tupdict_dict -=> the infamous TDD
         | []  | check for dict or tdd data in MAPPDS before updating it, translate them back to tuples
         | [X] | add TIME_AT_ZERO to CLOCKS_MAINFRAME
         | []  | mv PSG.py PSG_TIME.py to make sure these special modifications to PSG earn their keep
         | [X] | switch all times to int seconds MTSS and MTSMS from strings
         | [x] | only switching to text to display
         |     | also for incrementing, pre cache int for all times, and do everything with raw int seconds
         |     | all times int + HMS, only using HMS when it's time to zero check the main clock, ended up with MTSS and MTSMS
         |     | convert back to all tuples instead of dicts (x, y) (west, north, east, south)
         |     | github for android and see how this works on android
         | [X] | fix elapsed after midnight
         | []  | start and stop times for intervals
         | [X] | manage rewrite of the mainframe class to the ALARMPOPUP class
         | []  |
         | []  |




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


file /rcr/0-utils/0-desktop/runawayClock_DEV/PSG.py, line 2499, function updateInterval
                TIntervalBegan_ |1119|00:18:39 =
									(NOWS |63553|17:39:13 // TInterval_ |60|00:01:00) + TInterval_ |60|00:01:00
                TTimeBetween_ |62434|17:20:34 = NOWS |63553|17:39:13 - TIntervalBegan_ |1119|00:18:39
                TTimeRemaining_ |34|00:00:34 = (TTimeBetween_ |62434|17:20:34 % TInterval_ |60|00:01:00)
                TTimeAtStart_ |63480|17:38:00 = ('CF.loseTheSecs(NOWS - TTimeRemaining_)', 63480)
                TTimeAtNext_ |63540|17:39:00 = (TTimeAtStart_ |63480|17:38:00 + TInterval_ |60|00:01:00)
