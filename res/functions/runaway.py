	def runaway(self):
# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if (NOWMS < self._TIME_TO_MOVE_):
			return  # only move at minimum  SZ_TIME_BETWEEN_MOVES apart

		self._TIME_TO_MOVE_ = NOWMS + SZ_TIMEMS_BETWEEN_MOVES
		_screenSZX_, _screenSZY_ = self._SCREEN_DIMS_
		_sizeX_, _sizeY_ = self._SIZE_
		_lcnX_, _lcnY_ = self._LOCATION_
		_moveToX_ = _lcnX_ + (self._MPX_[INDEX_X] * SZ_MOVE_DIST)
		_moveToY_ = _lcnY_ + (self._MPX_[INDEX_Y] * SZ_MOVE_DIST)

		if (_moveToX_ < 0):
			_moveToX_ = 0
		elif (_moveToX_ > (_screenSZX_ - _sizeX_)):
			_moveToX_ = (_screenSZX_ - _sizeX_)

		if (_moveToY_ < 0):
			_moveToY_ = 0
		elif (_moveToY_ > (_screenSZY_ - _sizeY_)):
			_moveToY_ = (_screenSZY_ - _sizeY_)

		if (abs(_moveToX_ - _lcnX_) > SZ_MAX_DELTA) or (abs(_moveToY_ - _lcnY_) > SZ_MAX_DELTA):
			return

		self._MAINFRAME_.Move(_moveToX_, _moveToY_)

		if (self._DEBUG_PRINT_DICT_[F_RUNAWAY] is True):
			self.debugPrint(
				title_="runaway",
				message_=f"""
self._TIME_TO_MOVE_ {self._TIME_TO_MOVE_} = NOWMS {NOWMS} + SZ_TIMEMS_BETWEEN_MOVES {SZ_TIMEMS_BETWEEN_MOVES}
_screenSZX_ {_screenSZX_}, _screenSZY_ {_screenSZY_} = self._SCREEN_DIMS_
_sizeX_ {_sizeX_}, _sizeY_ {_sizeY_} = self._SIZE_
_lcnX_ {_lcnX_}, _lcnY_ {_lcnY_} = self._LOCATION_
_moveToX_ {_moveToX_} = _lcnX_ {_lcnX_} + (self._MPX_[INDEX_X] {self._MPX_[INDEX_X]} * SZ_MOVE_DIST {SZ_MOVE_DIST})
_moveToY_ {_moveToY_} = _lcnY_ {_lcnY_} + (self._MPX_[INDEX_Y] {self._MPX_[INDEX_Y]} * SZ_MOVE_DIST {SZ_MOVE_DIST})
"""
			)
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
