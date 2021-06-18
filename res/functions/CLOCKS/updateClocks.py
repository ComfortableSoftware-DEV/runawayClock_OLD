
	def updateClocks(dictToUpdate_):
		global \
				TIMEMS_NEXT_UPDATED
		# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	#	print(f"""{CF.getDebugInfo()}
	#	{CF.frameItHMS("PSG.NOWS", PSG.NOWS)}
	#	{CF.frameIt("PSG.NOWMS", PSG.NOWMS)}""")
	#	print(f"""{CF.getDebugInfo()}
	#	{CF.frameItMS("PSG.NOWMS", PSG.NOWMS)}) {CF.frameItMS("TIMEMS_NEXT_UPDATED", TIMEMS_NEXT_UPDATED)}""")
		if (PSG.NOWMS >= TIMEMS_NEXT_UPDATED):
			# CF.whirl()

			TIMEMS_NEXT_UPDATED = (PSG.NOWMS + SZ_TIMEMS_BETWEEN_UPDATES) % CF.DAYMS
			_dictToRtn_ = {}
			for _key_, _index_ in dictToUpdate_.items():
				_dictToRtn_[_key_] = _val_

			# print(f"""_dictToRtn_ {_dictToRtn_} PSG.NOWS {PSG.NOWS}""")
			_dictToRtn_[PSG.K_TIME_CLOCK] = PSG.NOWS
			_dictToRtn_[PSG.K_TIME_ELAPSED] = PSG.NOWS - _dictToRtn_[PSG.K_TIME_AT_ZEROELAPSE]
			_dictToRtn_[PSG.K_TIME_TOGO] = _dictToRtn_[PSG.K_TIME_AT_NEXT] - PSG.NOWS

			if _dictToRtn_[PSG.K_TIME_TOGO] < PSG.NOWS:
				_dictToRtn_[PSG.K_TIME_TOGO] += CF.DAYSECS

			return _dictToRtn_, True

		return _dictToRtn_, False

		# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
