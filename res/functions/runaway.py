		if NOWMS < self._TIME_TO_MOVE_:
			return  # only move at minimum  SZ_TIME_BETWEEN_MOVES apart

		self._TIME_TO_MOVE_ += SZ_TIMEMS_BETWEEN_MOVES
		_screenSZX_, _screenSZY_ = self._MAINFRAME_.GetScreenDimensions()
		_sizeX_, _sizeY_ = self._MAINFRAME_.Size()
		_lcnX_, _lcnY_ = self._MAINFRAME_.CurrentLocation()
		_moveToX_ = _lcnX_ + (moveMpx_[INDEX_X] * SZ_MOVE_DIST)
		_moveToY_ = _lcnY_ + (moveMpx_[INDEX_Y] * SZ_MOVE_DIST)

		if _moveToX_ < 0:
			_moveToX_ = 0
		elif _moveToX_ > (_screenSZX_ - _sizeX_):
			_moveToX_ = (_screenSZX_ - _sizeX_)

		if _moveToY_ < 0:
			_moveToY_ = 0
		elif _moveToY_ > (_screenSZY_ - _sizeY_):
			_moveToY_ = (_screenSZY_ - _sizeY_)

		# print(f"""likely moving abs(_moveToX_ - _lcnX_) {abs(_moveToX_ - _lcnX_)} abs(_moveToY_ - _lcnY_) {abs(_moveToY_ - _lcnY_)} SZ_MAX_DELTA {SZ_MAX_DELTA}""")
			# avoid trouble with spurious moves caused by a process delaying anything here too far
		if (abs(_moveToX_ - _lcnX_) > SZ_MAX_DELTA) or (abs(_moveToY_ - _lcnY_) > SZ_MAX_DELTA):
			# print(f"""(abs(_moveToX_ - _lcnX_) > SZ_MAX_DELTA) (abs({_moveToX_} - {_lcnX_}) > {SZ_MAX_DELTA}) {CF.INDENTIN} {(abs(_moveToX_ - _lcnX_) > SZ_MAX_DELTA)}""")
			# print(f"""(abs(_moveToY_ - _lcnY_) > SZ_MAX_DELTA) (abs({_moveToY_} - {_lcnY_}) > {SZ_MAX_DELTA}) {CF.INDENTIN} {(abs(_moveToY_ - _lcnY_) > SZ_MAX_DELTA)}""")
			return

		self._MAINFRAME_.Move(_moveToX_, _moveToY_)
