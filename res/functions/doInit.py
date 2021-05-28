def doInit():
	global \
			ALL_THE_FORMS, \
			APPDS
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	localTimes()
	# print(f"""{CF.getDebugInfo()}{CF.NEWLINE}{CF.frameIt("NOWS", NOWS)} {CF.nrmlIntToHMS(NOWS)} {CF.frameIt("NOWS", NOWS)} {CF.nrmlIntToHMS(NOWS)}""")
	for _thisKey_, _theseVals_ in ALL_THE_FORMS.items():
		if _theseVals_ is not None:
			ALL_THE_FORMS[_thisKey_].AlphaChannel = SZ_ALPHA_HIGH
			# FORMMAIN.Maximize()
			# FORMMAIN.BringToFront()
			APPDS[FORM_CURRENT_LCN] = getElementLocation(ALL_THE_FORMS[_thisKey_])
			APPDS[SCREEN_DIMS] = getScreenDims()
			APPDS[FORM_CURRENT_SIZE] = getElementSize(ALL_THE_FORMS[_thisKey_])

	APPDS[ALPHA_CHANNEL] = SZ_ALPHA_HIGH
	APPDS[BBOX] = getBBox(APPDS[FORM_CURRENT_LCN], APPDS[FORM_CURRENT_SIZE])
	APPDS[CLOSE_BBOX] = getCloseBBox(APPDS[FORM_CURRENT_LCN], APPDS[FORM_CURRENT_SIZE])
	CLOCKS_DICT[TIME_CLOCK] = NOWS
	CLOCKS_DICT[TIME_AT_ZEROELAPSE] = NOWS
	TIME_AT_LAST_ZERO_CHECK = NOWS

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	for _index_, _event_ in APPDS[EVENT_ENTRIES].items():
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
#		APPDS[EVENT_ENTRIES][_index_][TIME_AT_LAST_RUN] = None
		for _timeKey_ in APPDS_TIMES_LIST:
			if isinstance(_event_[_timeKey_], str):
				APPDS[EVENT_ENTRIES][_index_][_timeKey_] = CF.HMSToNrmlInt(_event_[_timeKey_])
	doMidnightWork()
	findNextAlarmEvent()

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
