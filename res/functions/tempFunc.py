# -=>
  def intervalCountOff(self, formToCountOff_):
    global \
        ALL_THE_FORMS
    # fold here ⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3
    _dictToUse_ = {}
    self._MAINFRAME_[INTERVAL_COUNT].update(text_color=COLOR_TEXT_INTERVAL_COUNT_INACTIVE, value=f"""{0:04d}""")
    self._DICTIN_[INTERVAL_COUNT] = 0

    self.updateFromDict(CURRENT_FORM_NAME, CLOCKS_TEXT_DICT)
    # fold here ⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3

  def intervalCountOn(self, formToCountOn_):
    global \
      ALL_THE_FORMS, \
      CLOCKS_DICT
    # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
    ALL_THE_FORMS[formToCountOn_][INTERVAL_COUNT].update(text_color=COLOR_TIME_TOGO)
    CLOCKS_DICT[INTERVAL_COUNT] = f"""{CURRENT_INTERVAL_COUNT:04d}"""
    updateFrameFromDict(CLOCKS_TEXT_DICT)
    # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1

  def updateIntervalCount(self, formNameToUpdate_):
    global \
        ALL_THE_FORMS
    # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
    CLOCKS_TEXT_DICT[INTERVAL_COUNT] = f"""{CURRENT_INTERVAL_COUNT:04d}"""
    updateFrameFromDict(CLOCKS_TEXT_DICT)
    # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1

  def enstring(self, dictToString_=self._DICTIN_):
    # fold here ⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3
    for _thisKey_, _thisVal_ in dictToString_.items():
      if (_thisKey_ in self._TIME_KEY_LIST_)
    # fold here ⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3

  def enint(self, dictToInt_):
    # fold here ⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3⟱3
    # make sure _DICTIN_ is all ints
    # fold here ⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3⟰3

# <=-
