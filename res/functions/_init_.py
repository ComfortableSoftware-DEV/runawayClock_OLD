		self._THIS_KEY_BASE_ = keyBase_
		self._USE_THIS_KEY_ = lambda __KEY_TEXT__: f"""{__KEY_TEXT__}{self._THIS_KEY_BASE_}"""
		self._THIS_FORM_NAME_ = formName_

		self._ALPHA_CHANNEL_ = SZ_ALPHA_HIGH
		self._ALPHA_HIGH_ = SZ_ALPHA_HIGH
		self._ALPHA_LOW_ = SZ_ALPHA_LOW
		self._BBOX_ = EMPTY_BBOX
		self._CHECKBOX_ALPHA_DIM_ = SZ_ALPHA_DIM
		self._CHECKBOX_RUNAWAY_ = SZ_RUNAWAY
		self._CLOSE_BBOX_ = EMPTY_BBOX
		self._KEY_DICT_ = {}
		self._KEY_DICT_REVERSE_ = {}
		self._LAST_LOCATION_ = EMPTY_XY
		self._LOCATION_ = EMPTY_XY
		self._MAINFRAME_ = None
		self._SCREEN_DIMS_ = EMPTY_XY
		self._SIZE_ = EMPTY_XY
		self._TIME_KEY_LIST_ = []
		self._TIME_TO_CHECK_MOUSE_ = ZERO_CLOCK
		self._TIME_TO_MOVE_ = ZERO_CLOCK
		self._TIME_TO_UPDATE_ = ZERO_CLOCK
