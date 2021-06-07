	def update(self):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if (NOWMS < self._TIME_MS_AT_UPDATE_):
			return

		self._TIME_MS_AT_UPDATE_ = NOWMS + SZ_TIME_MS_BETWEEN_UPDATES
		_TLcn_ = self._MAINFRAME_.CurrentLocation()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (_TLcn_ != self._CURRENT_LOCATION_):
			self._CHANGED_LOCATION_ = True
			self._CURRENT_LOCATION_ = _TLcn_
			self._BBOX_ = getBBox(self._CURRENT_LOCATION_, self._SIZE_)
			self._CLOSE_BBOX_ = getCloseBBox(self._CURRENT_LOCATION_, self._SIZE_)
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self._DICTIN_[K_TIME_S_CLOCK] = NOWS
		self._DICTIN_[K_TIME_S_TOGO] = (self._DICTIN_[K_TIME_S_AT_NEXT_ALERT] - NOWS)
		self._DICTIN_[K_TIME_S_ELAPSED] = (NOWS - self._DICTIN_[K_TIME_S_AT_ZEROELAPSE])
		self.checkMouse()
		self.quickRead()
		self.updateFromDict()
		self.updateFlippedItems()

		if (self._DICTIN_[K_CHECKBOX_RUNAWAY] is True) and (self._CURRENT_MOUSE_STATUS_ in LIST_CLOSE):
			self.runaway()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[F_UPDATE] is True):
			self.debugPrint(
				title_="update",
				printDictinS_=False,
				message_=f"""
self._TIME_MS_AT_UPDATE_ {CF.frameItMS("_TIME_MS_AT_UPDATE_", self._TIME_MS_AT_UPDATE_)} = {CF.frameItMS("NOWMS", NOWMS)} + SZ_TIME_MS_BETWEEN_UPDATES {SZ_TIME_MS_BETWEEN_UPDATES / 1000}
self._CURRENT_LOCATION_ {self._CURRENT_LOCATION_} = self._MAINFRAME_.CurrentLocation()
self._BBOX_ {self._BBOX_} = getBBox(self._CURRENT_LOCATION_, self._SIZE_ {self._SIZE_})
self._CLOSE_BBOX_ {self._CLOSE_BBOX_} = getCloseBBox(self._CURRENT_LOCATION_, self._SIZE_)
self._DICTIN_[K_TIME_S_CLOCK] {CF.frameItHMS("K_TIME_S_CLOCK", self._DICTIN_[K_TIME_S_CLOCK])} = {CF.frameItHMS("NOWS", NOWS)}
self._DICTIN_[K_TIME_S_TOGO] {CF.frameItHMS("K_TIME_S_TOGO", self._DICTIN_[K_TIME_S_TOGO])} = (self._DICTIN_[K_TIME_S_AT_NEXT_ALERT] {CF.frameItHMS("K_TIME_S_AT_NEXT_ALERT", self._DICTIN_[K_TIME_S_AT_NEXT_ALERT])} - NOWS  {CF.frameItHMS("NOWS", NOWS)})
self._DICTIN_[K_TIME_S_ELAPSED] {CF.frameItHMS("K_TIME_S_ELAPSED", self._DICTIN_[K_TIME_S_ELAPSED])} = (NOWS - self._DICTIN_[K_TIME_S_AT_ZEROELAPSE] {CF.frameItHMS("K_TIME_S_AT_ZEROELAPSE", self._DICTIN_[K_TIME_S_AT_ZEROELAPSE])})
 self._CURRENT_MOUSE_LOCATION_ {self._CURRENT_MOUSE_LOCATION_}, self._CURRENT_MOUSE_STATUS_ {self._CURRENT_MOUSE_STATUS_} = self.checkMouse()
""",
			)
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
