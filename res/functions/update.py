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
		if (self._DEBUG_PRINT_ is True):
			print(f"""update
_DICTIN_ = {self.dictinRepl()}
_DICTINSTR_ = {self.dictinstrRepl()}""")

		if (self._CHECKBOX_RUNAWAY_ is True):
			self.runaway()

		self.updateFromDict()
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
