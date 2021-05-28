	def updateClocks(dictToUpdate_):
		global \
				TIMEMS_NEXT_UPDATED
		# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	#	print(f"""{CF.getDebugInfo()}
	#	{CF.frameItHMS("NOWS", NOWS)}
	#	{CF.frameIt("NOWMS", NOWMS)}""")
	#	print(f"""{CF.getDebugInfo()}
	#	{CF.frameItMS("NOWMS", NOWMS)}) {CF.frameItMS("TIMEMS_NEXT_UPDATED", TIMEMS_NEXT_UPDATED)}""")
		if (NOWMS >= TIMEMS_NEXT_UPDATED):
			# CF.whirl()

			TIMEMS_NEXT_UPDATED = (NOWMS + SZ_TIMEMS_BETWEEN_UPDATES) % CF.DAYMS
			_dictToRtn_ = {}
			for _key_, _index_ in dictToUpdate_.items():
				_dictToRtn_[_key_] = _val_

			# print(f"""_dictToRtn_ {_dictToRtn_} NOWS {NOWS}""")
			_dictToRtn_[TIME_CLOCK] = NOWS
			_dictToRtn_[TIME_ELAPSED] = NOWS - _dictToRtn_[TIME_AT_ZEROELAPSE]
			_dictToRtn_[TIME_TOGO] = _dictToRtn_[TIME_AT_NEXT] - NOWS

			if _dictToRtn_[TIME_TOGO] < NOWS:
				_dictToRtn_[TIME_TOGO] += CF.DAYSECS

			return _dictToRtn_, True

		return _dictToRtn_, False

		# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
