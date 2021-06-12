

class TBGLST():

	def __init__(self):
		__TBGLST__ = []
		import FM_TBGLST_CF
		__TBGLST__.extend(FM_TBGLST_CF.TBGLST)

		self._TBGLST_ = [
			("FM_TBGLST.py", ("FMAX_NOP", FMAXFM_SCTN0101_AX_DEF, "ignore the remainder of the line"))
			("FMVAl_TABLEVEL", FMAXFM_SCTN0102_STR_DEF, "TABLEVEL", "TABLEVEL", "key for tab levels",),
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
		]
		self._TBGLST_.sort()

	def __iter__(self):
		self._RESULT_ = ""
		return self

	def __next__(self):
		self._RESULT_ = self._TBGLST_.pop(0)
		if (self._RESULT_ is not None):
			return self._RESULT_
		else:
			raise StopIteration
