	def update():
		if (NOWMS >= self._TIME_TO_UPDATE_):
			return

		self._TIME_TO_UPDATE_ += SZ_TIMEMS_BETWEEN_UPDATES
		self._DICTIN_, _wasUpdated_ = updateClocks(self._DICTIN_)
		if _wasUpdated_ is True:
			self.updateFromDict(setLocalDict_=False)
		if (MAPPDS[CHECKBOX_RUNAWAY] is True):
			_mouseDirection_ = checkMouseLcn(self._THIS_FORM_NAME_, )
			self.runaway()
