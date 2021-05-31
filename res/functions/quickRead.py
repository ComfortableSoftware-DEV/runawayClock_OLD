	def quickRead(self, timeout_=1):
		self._CURRENT_EVENT_, self._CURRENT_VALUES_ = self._MAINFRAME_.Read(timeout=timeout_)

		if (self._DEBUG_PRINT_DICT_[F_QUICKREAD]):
			self.debugPrint(
				title_="quickRead",
				message_=f"""set:
_CURRENT_EVENT_ {self._CURRENT_EVENT_}
_CURRENT_VALUES_ {self._CURRENT_VALUES_}"""
			)
