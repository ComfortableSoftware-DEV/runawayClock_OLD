#!/usr/bin/env /usr/bin/python


import PSG
import CF


oldClock = CF.nowStrHMS(CF.DT.now())
oldElapsed = "00:00:00"
oldTogo = "00:05:00"


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# handleEvents
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def handleEvents(event_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if event_ == PSG.BTN_QUIT:
		exit()

	elif event_ == PSG.BTN_ZERO:
		PSG.CLOCKS_TIMES_DICT[PSG.TIME_ELAPSED] = CF.nrmlIntToHMS(0)
		PSG.updateFromDict(PSG.CLOCKS_MAINFRAME, PSG.CLOCKS_TIMES_DICT)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


while True:
	event_, values_ = PSG.CLOCKS_MAINFRAME.Read(timeout=100)
	now_ = CF.nowStrHMS(CF.DT.now())
	if now_ != oldClock:
		oldClock = now_
		PSG.CLOCKS_TIMES_DICT[PSG.TIME_CLOCK] = oldClock
		PSG.CLOCKS_TIMES_DICT[PSG.TIME_ELAPSED] = CF.incHMS(PSG.CLOCKS_TIMES_DICT[PSG.TIME_ELAPSED], 0, 0, 1)
		PSG.CLOCKS_TIMES_DICT[PSG.TIME_TOGO] = CF.incHMS(PSG.CLOCKS_TIMES_DICT[PSG.TIME_TOGO], 0, 0, -1)
		PSG.updateFromDict(PSG.CLOCKS_MAINFRAME, PSG.CLOCKS_TIMES_DICT)
	handleEvents(event_)
