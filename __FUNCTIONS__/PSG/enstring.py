# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start on enstring
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def enstring(self,
			dictToUse_=None
	):
		# fold here ⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3
		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(dictToUse_ is None)
		):
			dictToUse_ = CF.quickCopyDict(self._DICTIN_)
			_returnMode_ = False
		# ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱
		else:
			_returnMode_ = True
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2

		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(self._DPD_[PSG.F_ENSTRING])
		):
			self.debugPrint(
				printDictinS_=True,
				title_="start of enstring",
				message_= f"""dictToUse_ {dictToUse_}
{CF.frameIt("_returnMode_", _returnMode_)}"""
			)
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
		_dictToRtn_ = {}
		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		for _thisKey0_, _thisVal0_ in dictToUse_.items():
			# 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
			if (
					(isinstance(_thisVal0_, list) is True)
			):
				# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
				_listToAdd_ = []
				_dictToRtn_[_thisKey0_] = []
				# 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱
				for _thisItem0_ in _thisVal0_:
					_dictToAdd_ = {}
					# 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱
					for _thisKey1_, _thisVal1_ in _thisItem0_.items():
						# 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱
						if (
								(_thisKey1_ in self._DICT_KEYS_TIME_)
						):
							_dictToAdd_[self.makeOutKey(_thisKey1_)] = CF.nrmlIntToHMS(_thisVal1_)
						# ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱
						elif (
								(_thisKey1_ in self._DICT_KEYS_INT_)
						):
							_dictToAdd_[self.makeOutKey(_thisKey1_)] = f"""{_thisVal1_:{self._DICT_KEYS_INT_[_thisKey1_]}}"""
						# ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱ ⟰6⟱
						else:
							_dictToAdd_[self.makeOutKey(_thisKey1_)] = _thisVal1_
						# ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6
					# ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5
					_dictToRtn_[_thisKey0_].append(_dictToAdd_)
				# ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4
				# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
			# ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱
			else:
				# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
				# 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱
				if (
						(_thisKey0_ in self._DICT_KEYS_TIME_)
				):
					_dictToRtn_[self.makeOutKey(_thisKey0_)] = CF.nrmlIntToHMS(_thisVal0_)
				# ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱
				elif (
						(_thisKey0_ in self._DICT_KEYS_INT_)
				):
					_dictToRtn_[self.makeOutKey(_thisKey0_)] = f"""{_thisVal0_:{self._DICT_KEYS_INT_[_thisKey0_]}}"""
				# ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱ ⟰4⟱
				else:
					_dictToRtn_[self.makeOutKey(_thisKey0_)] = _thisVal0_
				# ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4
				# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
			# ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2

		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(_returnMode_ is False) and
				(self._CURRENT_FLIP_INFO_ != [])
		):
		# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
			_newList_ = []
			# 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
			for _thisItem_ in self._CURRENT_FLIP_INFO_:
				_newDict_ = {}
				# 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱
				for _thisKey_, _thisVal_ in _thisItem_.items():
					# 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱
					if (
						(_thisKey_ in self._DICT_KEYS_TIME_) and
						(isinstance(_thisVal_, int) is True)
					):
						_newDict_[_thisKey_] = CF.nrmlIntToHMS(_thisVal_ % self._DICT_KEYS_TIME_[_thisKey_])
					# ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱
					elif (
						(_thisKey_ in self._DICT_KEYS_INT_) and
						(isinstance(_thisVal_, int) is True)
					):
						_newDict_[_thisKey_] = f"""{_thisVal_:{self._DICT_KEYS_INT_[_thisKey_]}}"""
					# ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱ ⟰5⟱
					else:
						_newDict_[_thisKey_] = f"""{_thisVal_}"""
					# ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5
				# ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4
				_newList_.append(_newDict_)
			# ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3
			self._CURRENT_FLIP_INFO_ = _newList_
		# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2


		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(self._DPD_[PSG.F_ENSTRING] is True)
		):
			print(f"""bottom of enstring
dictToUse_ {dictToUse_}
_dictToRtn_ {_dictToRtn_}
""")
		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(_returnMode_ is True)
		):
			return _dictToRtn_
			# ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱
		else:
			self._DICTINSTR_ = CF.quickCopyDict(_dictToRtn_)
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2

		# fold here ⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# end of enstring
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*