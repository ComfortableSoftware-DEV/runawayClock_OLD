		self._LAST_LOCATION_ = self._MAINFRAME_.CurrentLocation()
		self._LOCATION_ = self._MAINFRAME_.CurrentLocation()
		self._BBOX_ = getBBox(self._LOCATION_, self._SIZE_)
		self._CHECKBOX_ALPHA_DIM_ = SZ_ALPHA_DIM
		self._CHECKBOX_RUNAWAY_ = SZ_RUNAWAY
		self._CLOSE_BBOX_ = getCloseBBox(self._LOCATION_, self._SIZE_)
		self._SCREEN_DIMS_ = self._MAINFRAME_.GetScreenDimensions()
		self._SIZE_ = self._MAINFRAME_.Size()
