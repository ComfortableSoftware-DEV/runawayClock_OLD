#!/usr/bin/env /usr/bin/python


import PSG
import CF


oldClock = CF.nowStrHMS(CF.DT.now())
oldElapsed = "00:00:00"
oldTogo = "00:00:00"


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# handleEvents
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def handleEvents(event_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if event_ == "__TIMEOUT__":
		return

	elif event_ == PSG.BTN_QUIT:
		exit()

	elif event_ == PSG.BTN_ZERO:
		PSG.CLOCKS_DICT[PSG.TIME_ELAPSED] = CF.nrmlIntToHMS(0)
		PSG.updateFromDict(PSG.CLOCKS_MAINFRAME, PSG.CLOCKS_DICT)

	# elif event_ == PSG.TIME_CLOCK:

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
while True:
	event_, values_ = PSG.CLOCKS_MAINFRAME.Read(timeout=100)
	now_ = CF.nowStrHMS(CF.DT.now())

	if now_ != oldClock:
		oldClock = now_
		PSG.CLOCKS_DICT[PSG.TIME_CLOCK] = oldClock
		PSG.CLOCKS_DICT[PSG.TIME_ELAPSED] = CF.incHMS(PSG.CLOCKS_DICT[PSG.TIME_ELAPSED], 0, 0, 1)
		PSG.CLOCKS_DICT[PSG.TIME_TOGO] = CF.incHMS(PSG.CLOCKS_DICT[PSG.TIME_TOGO], 0, 0, -1)
		PSG.updateFromDict(PSG.CLOCKS_MAINFRAME, PSG.CLOCKS_DICT)

	if event_ != "__TIMEOUT__":
		handleEvents(event_)

	TMouseStatus_ = PSG.checkMouse(PSG.CLOCKS_MAINFRAME)

	if TMouseStatus_ in PSG.CLOSE_LIST:

		if TMouseStatus_ == PSG.MOUSE_STATUS_CLOSE_N:
			PSG.moveRelFrame(PSG.CLOCKS_MAINFRAME, (0, 1))

		elif TMouseStatus_ == PSG.MOUSE_STATUS_CLOSE_S:
			PSG.moveRelFrame(PSG.CLOCKS_MAINFRAME, (0, -1))

		elif TMouseStatus_ == PSG.MOUSE_STATUS_CLOSE_E:
			PSG.moveRelFrame(PSG.CLOCKS_MAINFRAME, (-1, 0))

		elif TMouseStatus_ == PSG.MOUSE_STATUS_CLOSE_W:
			PSG.moveRelFrame(PSG.CLOCKS_MAINFRAME, (1, 0))

		if TMouseStatus_ == PSG.MOUSE_STATUS_CLOSE_NW:
			PSG.moveRelFrame(PSG.CLOCKS_MAINFRAME, (1, 1))

		elif TMouseStatus_ == PSG.MOUSE_STATUS_CLOSE_SW:
			PSG.moveRelFrame(PSG.CLOCKS_MAINFRAME, (1, -1))

		elif TMouseStatus_ == PSG.MOUSE_STATUS_CLOSE_NE:
			PSG.moveRelFrame(PSG.CLOCKS_MAINFRAME, (-1, 1))

		elif TMouseStatus_ == PSG.MOUSE_STATUS_CLOSE_SE:
			PSG.moveRelFrame(PSG.CLOCKS_MAINFRAME, (-1, -1))


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# end of clocks.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#
