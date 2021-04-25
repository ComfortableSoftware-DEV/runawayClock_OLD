#!/usr/bin/env /usr/bin/python


import inspect


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
		PSG.CLOCKS_DICT_BID[PSG.TIME_ELAPSED] = CF.nrmlIntToHMS(0)
		PSG.updateFromDict(PSG.CLOCKS_MAINFRAME, PSG.CLOCKS_DICT_BID)

	elif event_ == PSG.BTN_XPAND:
		TClocksDict = PSG.readWithDict(PSG.CLOCKS_MAINFRAME, PSG.CLOCKS_DICT_FULL)
		print(f"""{inspect(PSG.CLOCKS_MAINFRAME[PSG.TIME_CLOCK])}""")
#		PSG.CLOCKS_MAINFRAME.Refresh()
#		print(f"""{PSG.CLOCKS_MAINFRAME.Location}""")
#		PSG.CLOCKS_MAINFRAME.Move(10, 10)
#		PSG.CLOCKS_MAINFRAME.Refresh()
#		print(f"""{PSG.CLOCKS_MAINFRAME.Location}""")

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


while True:
	# PSG.CLOCKS_MAINFRAME.bring_to_front()
	event_, values_ = PSG.CLOCKS_MAINFRAME.Read(timeout=100)
	now_ = CF.nowStrHMS(CF.DT.now())
	if now_ != oldClock:
		oldClock = now_
		PSG.CLOCKS_DICT_BID[PSG.TIME_CLOCK] = oldClock
		PSG.CLOCKS_DICT_BID[PSG.TIME_ELAPSED] = CF.incHMS(PSG.CLOCKS_DICT_BID[PSG.TIME_ELAPSED], 0, 0, 1)
		PSG.CLOCKS_DICT_BID[PSG.TIME_TOGO] = CF.incHMS(PSG.CLOCKS_DICT_BID[PSG.TIME_TOGO], 0, 0, -1)
		PSG.updateFromDict(PSG.CLOCKS_MAINFRAME, PSG.CLOCKS_DICT_BID)
	if event_ != "__TIMEOUT__":
		handleEvents(event_)
