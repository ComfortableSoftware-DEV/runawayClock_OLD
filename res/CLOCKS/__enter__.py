	def __enter__(self):
		global \
			ALL_THE_FORMS, \
			MAPPDS
		#
		self._MAINFRAME_ = SG.Window(**self._WINDOW_).finalize()
		ALL_THE_FORMS[self._THIS_FORM_NAME_] = self._MAINFRAME_
		return self
