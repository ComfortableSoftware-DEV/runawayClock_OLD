	def easyUpdate(self,
			checkboxAlphaDim_=None,
			checkboxRunaway_=None,
			eventMode_=None,
			currentIntervalCount_=None,
			nameNextEvent_=None,
			timeAtNextAlert_=None,
			timeAtZeroelapse_=None,
			timeClock_=None,
			timeElapsed_=None,
			timeTogo_=None,
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if nameNextEvent_ is not None:
			self._DICTIN_[K_NAME_NEXT_EVENT] = nameNextEvent_

		if checkboxAlphaDim_ is not None:
			self._DICTIN_[K_CHECKBOX_ALPHA_DIM] = checkboxAlphaDim_

		if checkboxRunaway_ is not None:
			self._DICTIN_[K_CHECKBOX_RUNAWAY] = checkboxRunaway_

		if eventMode_ is not None:
			self.CURRENT_EVENTMODE = eventMode_

			if currentIntervalCount_ is not None:
				self._DICTIN_[K_INTERVAL_COUNT] = currentIntervalCount_

			if (eventMode_ == EVENTMODE_INTERVAL):
				self.intervalCountOn(currentIntervalCount_)
			else:
				self.intervalCountOff()

		if timeAtNextAlert_ is not None:
			self._DICTIN_[K_TIME_AT_NEXT_ALERT] = timeAtNextAlert_

		if timeAtZeroelapse_ is not None:
			self._DICTIN_[K_TIME_AT_ZEROELAPSE] = timeAtZeroelapse_

		if timeClock_ is not None:
			self._DICTIN_[K_TIME_CLOCK] = timeClock_

		if timeElapsed_ is not None:
			self._DICTIN_[K_TIME_ELAPSED] = timeElapsed_

		if timeTogo_ is not None:
			self._DICTIN_[K_TIME_TOGO] = timeTogo_

		self.enint()
		self.updateFromDict()

		if (self._DEBUG_PRINT_ is True):
			print(f"""easyUpdate
_DICTIN_ {self.dictinRepl()}
_DICTINSTR_ {self.dictinstrRepl()}""")
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
