	def easyUpdate(self,
			CHECKBOX_ALPHA_DIM_=None,
			CHECKBOX_RUNAWAY_=None,
			EVENTMODE_=None,
			INTERVAL_COUNT_=None,
			NAME_NEXT_EVENT_=None,
			TIME_AT_NEXT_=None,
			TIME_AT_ZEROELAPSE_=None,
			TIME_CLOCK_=None,
			TIME_ELAPSED_=None,
			TIME_TOGO_=None,
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if NAME_NEXT_EVENT_ is not None:
			self._DICTIN_[NAME_NEXT_EVENT] = NAME_NEXT_EVENT_

		if CHECKBOX_ALPHA_DIM_ is not None:
			self._DICTIN_[CHECKBOX_ALPHA_DIM] = CHECKBOX_ALPHA_DIM_

		if CHECKBOX_RUNAWAY_ is not None:
			self._DICTIN_[CHECKBOX_RUNAWAY] = CHECKBOX_RUNAWAY_

		if INTERVAL_COUNT_ is not None:
			self._DICTIN_[INTERVAL_COUNT] = INTERVAL_COUNT_

		if TIME_AT_NEXT_ is not None:
			self._DICTIN_[TIME_AT_NEXT] = TIME_AT_NEXT_

		if TIME_AT_ZEROELAPSE_ is not None:
			self._DICTIN_[TIME_AT_ZEROELAPSE] = TIME_AT_ZEROELAPSE_

		if TIME_CLOCK_ is not None:
			self._DICTIN_[TIME_CLOCK] = TIME_CLOCK_

		if TIME_ELAPSED_ is not None:
			self._DICTIN_[TIME_ELAPSED] = TIME_ELAPSED_

		if TIME_TOGO_ is not None:
			self._DICTIN_[TIME_TOGO] = TIME_TOGO_

		self.enint()
		self.updateFromDict()
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
