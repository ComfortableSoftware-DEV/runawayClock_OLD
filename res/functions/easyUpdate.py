	def easyUpdate(self,
			checkboxAlphaDim_=None,
			checkboxRunaway_=None,
			eventMode_=None,
			intervalCount_=None,
			nameNextEvent_=None,
			timeAtNext_=None,
			timeAtZeroelapse_=None,
			timeClock_=None,
			timeElapsed_=None,
			timeTogo_=None,
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if nameNextEvent_ is not None:
			self._DICTIN_[NAME_NEXT_EVENT] = nameNextEvent_

		if checkboxAlphaDim_ is not None:
			self._DICTIN_[CHECKBOX_ALPHA_DIM] = checkboxAlphaDim_

		if checkboxRunaway_ is not None:
			self._DICTIN_[CHECKBOX_RUNAWAY] = checkboxRunaway_

		if eventMode_ is not None:
			self.CURRENT_EVENTMODE = eventMode_

			if intervalCount_ is not None:
				self._DICTIN_[INTERVAL_COUNT] = intervalCount_

			if (eventMode_ == EVENTMODE_INTERVAL):
				self.intervalCountOn()
			else:
				self.intervalCountOff()

		if timeAtNext_ is not None:
			self._DICTIN_[TIME_AT_NEXT] = timeAtNext_

		if timeAtZeroelapse_ is not None:
			self._DICTIN_[TIME_AT_ZEROELAPSE] = timeAtZeroelapse_

		if timeClock_ is not None:
			self._DICTIN_[TIME_CLOCK] = timeClock_

		if timeElapsed_ is not None:
			self._DICTIN_[TIME_ELAPSED] = timeElapsed_

		if timeTogo_ is not None:
			self._DICTIN_[TIME_TOGO] = timeTogo_

		self.enint()
		self.updateFromDict()
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
