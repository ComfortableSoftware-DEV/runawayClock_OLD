	def doReadFrame(timeout_=SZ_TIMEOUT_MS):
		# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
		_eventToRtn_, _valuesToRtn_ = self._MAINFRAME_.Read(timeout=timeout_)

		if (_eventToRtn_ == self._LAST_EVENT_):
			self._EVENT_CHANGED_ = False
			self._CURRENT_EVENT_ = _eventToRtn_

		else:
			self._EVENT_CHANGED_ = True

		if (_valuesToRtn_ == self._LAST_VALUES_):
			self._VALUES_CHANGED_ = False

		else:
			self._VALUES_CHANGED_ = True
			self._CURRENT_VALUES_ = _valuesToRtn_

		if (self._DEBUG_PRINT_DICT_[F_READFRAME]):
			self.debugPrint(
				title_="readFrame",
				message_=f"""set:
_CURRENT_EVENT_ {self._CURRENT_EVENT_}
_CURRENT_VALUES_ {self._CURRENT_VALUES_}
_EVENT_CHANGED_ {self._EVENT_CHANGED_}
_eventToRtn_ {_eventToRtn_}
_LAST_EVENT_ {self._LAST_EVENT_}
_LAST_VALUES_ {self._LAST_VALUES_}
_VALUES_CHANGED_ {self._VALUES_CHANGED_}
_valuesToRtn_ {_valuesToRtn_}
"""
			)
		# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
