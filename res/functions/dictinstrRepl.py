
  def dictinstrRepl(self,
      dictToRepl_=None):
    # fold here ⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3
    _dictToRtn_ = {}

      # 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    if (dictToRepl_ is None):
      dictToRepl_ = CF.quickCopyDict(self._DICTINSTR_)
    # ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2

      # 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    if (self._DPD_[F_DICTINREPL] is True):
      self.debugPrint(
        title_="start of dictinstrRepl",
        printDictinS_=True,
        message_=f"""{CF.frameIt("dictToRepl_", dictToRepl_)}"""
      )

    # ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2

    # 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    for _thisKey_, _thisVal_ in dictToRepl_.items():

        # 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
      if (_thisKey_ in self._DICT_KEYS_TIME_):
        _dictToRtn_[_thisKey_] = CF.nrmlIntToHMS(_thisVal_)

        # ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱
      elif (_thisKey_ in self._DICT_KEYS_INT_):

          # 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱
        if (self._DICT_KEYS_INT_[_thisKey_] == "04d"):

            # 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱
          if (isinstance(_thisVal_, list) is True):
            _dictToRtn_[_thisKey_] = []

            # 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱ 6⟱
            for _thisItem_ in _thisVal_:

                # 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱ 7⟱
              if (isinstance(_thisItem_, int) is True):
                _dictToRtn_[_thisKey_].append(f"""{_thisItem_:04d}""")

                # ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱ ⟰7⟱
              else:
                _dictToRtn_[_thisKey_].append(f"""{_thisItem_}""")
            # ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6 ⟰6
          # ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5
        # ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4

        # ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱
      else:
        _dictToRtn_[_thisKey_] = f"""{_thisVal_}"""

      # ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3
    # ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2

      # 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    if (self._DPD_[PSG.F_DICTINREPL] is True):
      self.debugPrint(
        title_="end of dictinstrRepl",
        printDictinS_=True,
        message_=f"""returning:
{CF.frameIt("_dictToRtn_", _dictToRtn_)}"""
      )

    # ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2

    return _dictToRtn_
    # fold here ⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3
