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
         | [X] | start and stop times for intervals
         | [X] | manage rewrite of the mainframe class to the ALARMPOPUP class
         | []  | length of alarms
         | []  | auto dismiss
         | []  | time until dismissed
         | []  | intervals working
         | []  | alarms working
         | []  | alarm+reminder working
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
