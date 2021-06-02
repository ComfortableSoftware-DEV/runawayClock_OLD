	def update(self):
# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if (NOWMS < self._TIME_TO_UPDATE_):
			return

		self._TIME_TO_UPDATE_ = NOWMS + SZ_TIMEMS_BETWEEN_UPDATES
		self._LOCATION_ = self._MAINFRAME_.CurrentLocation()
		self._BBOX_ = getBBox(self._LOCATION_, self._SIZE_)
		self._CLOSE_BBOX_ = getCloseBBox(self._LOCATION_, self._SIZE_)
		self._DICTIN_[K_TIME_CLOCK] = NOWS
		self._DICTIN_[K_TIME_TOGO] = (self._DICTIN_[K_TIME_AT_NEXT_ALERT] - NOWS)
		self._DICTIN_[K_TIME_ELAPSED] = (NOWS - self._DICTIN_[K_TIME_AT_ZEROELAPSE])
		self.checkMouse()

		if (self._CHECKBOX_RUNAWAY_ is True):
			self.runaway()

		self.updateFromDict()

		if (self._DPD_[F_UPDATE] is True):
			self.debugPrint(
				title_="update",
				printDictinS_=True,
				message_ = f"""
self._TIME_TO_UPDATE_ {self._TIME_TO_UPDATE_} = NOWMS {NOWMS} + SZ_TIMEMS_BETWEEN_UPDATES {SZ_TIMEMS_BETWEEN_UPDATES}
self._LOCATION_ {self._LOCATION_} = self._MAINFRAME_.CurrentLocation()
self._BBOX_ {self._BBOX_} = getBBox(self._LOCATION_, self._SIZE_ {self._SIZE_})
self._CLOSE_BBOX_ {self._CLOSE_BBOX_} = getCloseBBox(self._LOCATION_, self._SIZE_)
self._DICTIN_[K_TIME_CLOCK] {self._DICTIN_[K_TIME_CLOCK]} = NOWS
self._DICTIN_[K_TIME_TOGO] {self._DICTIN_[K_TIME_TOGO]} = (self._DICTIN_[K_TIME_AT_NEXT_ALERT] {self._DICTIN_[K_TIME_AT_NEXT_ALERT]} - NOWS)
self._DICTIN_[K_TIME_ELAPSED] {self._DICTIN_[K_TIME_ELAPSED]} = (NOWS - self._DICTIN_[K_TIME_AT_ZEROELAPSE] {self._DICTIN_[K_TIME_AT_ZEROELAPSE]})
 self._CURRENT_MOUSE_LOCATION_ {self._CURRENT_MOUSE_LOCATION_}, self._CURRENT_MOUSE_STATUS_ {self._CURRENT_MOUSE_STATUS_} = self.checkMouse()
""",
			)
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
