		_dictToRtn_ = {}
		for _key_ in dictToReadTo_:
			_dictToRtn_[_key_] = self._MAINFRAME_[_key_]
			if (setLocalDict_ is True):
				self._DICTOUT_[_key_] = _dictToRtn_[_key_]
		return _dictToRtn_
