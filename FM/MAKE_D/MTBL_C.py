

from CF.CONSTANTS import NAMES
from FM import FM


F___ENTER__ = "F___ENTER__"
F___EXIT__ = "F___EXIT__"
F___INIT__ = "F___INIT__"
F_MAKEID = "F_MAKEID"
F_STARTLCLNEWFILE = "F_STARTLCLNEWFILE"
F_WRITE = "F_WRITE"


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of FM_MTBL_C.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
class C_MTBL():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of __init__
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def __init__(self):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		self.__FILE_DICT__ = {}
		# ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥
		self._DPD_ = {
			F___ENTER__: True,
			F___EXIT__: True,
			F___INIT__: True,
			F_MAKEID: True,
			F_STARTLCLNEWFILE: True,
			F_WRITE: True,
		}
		# ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥
		_moduleName_ = "FM"
		_sub0_ = "TBGLST"
		# ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥
		_IDToRtn_ = NAMES.MAKE_ID(
				__MODULE_NAME__=_moduleName_,
				__SUB0__=_sub0_,
		)
		# ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥
		_TBGLSTEntry_ = (
				"FM_TBGLST",
				"FMAX_NOP",
				"start of all things list",
		)
		# ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥
		_valToRtn_ = (
				_TBGLSTEntry_,
				_IDToRtn_,
		)
		# ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥
		__dummy__ = self.write(_valToRtn_)
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# end of __init__
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of makeDictID
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def makeDictID(self,
			ID_
	):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		_dictToRtn_ = dict((x, y) for x, y in ID_)
		return _dictToRtn_
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# end of makeDictID
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of startLCLNewFile
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def startLCLNewFile(self,
			IDToWrt_
	):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		_strToRtn_ = ""
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (
				()
		)
		_IDIn_ = self.makeDictID(IDToWrt_)
		_class_ = _IDIn_.get("__CLASS__")
		_filename_ = _IDIn_.get("__FILENAME__")
		_moduleName_ = _IDIn_.get("__MODULE_NAME__")
		_newFilename_ = _IDIn_.get("__NEW_FILENAME__")
		_subD0_ = _IDIn_.get("__SUBD0__")
		_subD1_ = _IDIn_.get("__SUBD1__")
		_sub0_ = _IDIn_.get("__SUB0__")
		_sub1_ = _IDIn_.get("__SUB1__")
		_sub2_ = _IDIn_.get("__SUB2__")
		_sub3_ = _IDIn_.get("__SUB3__")
		_sub4_ = _IDIn_.get("__SUB4__")
		_sub5_ = _IDIn_.get("__SUB5__")
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (
				(_filename_ is None) or
				(_newFilename_ is None)
		):
			return None

		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# start of __MODULE_NAME__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (
				(_class_ is None) and
				(_moduleName_ is not None) and
				(_sub0_ is None) and
				(_sub1_ is None) and
				(_sub2_ is None) and
				(_sub3_ is None)
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			_strToRtn_ += f"""{FM.NEWLINE}{FM.NEWLINE}from FM import FM{FM.NEWLINE}{FM.NEWLINE}
{FM.makeAComment(f"start of {_moduleName_}.py")}
_moduleName_ = {FM.DBLQT}{_moduleName_}{FM.DBLQT}
{FM.MARK0MID("")}
_filename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_MOD_PY(
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_
){FM.NEWLINE}{FM.CBRCE}{FM.TRIQT}  # {_filename_}
{FM.MARK0MID("")}
_newFilename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_MOD_NEW_PY(
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_
){FM.NEWLINE}{FM.CBRCE}{FM.TRIQT}  # {_newFilename_}
{FM.MARK0MID("")}
__ID__ = {FM.OPAREN}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__FILENAME__{FM.DBLQT}: _filename_,{FM.CPAREN},  # {_filename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__MODULE_NAME__"{FM.DBLQT}, _moduleName_,{FM.CPAREN},  # {_moduleName_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__NEW_FILENAME__{FM.DBLQT}: _newFilename_,{FM.CPAREN},  # {_newFilename_}
{FM.CPAREN}
{FM.MARK0MID("")}
TBGLST = {FM.OBRKT}
"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
			# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# start of __MODULE_NAME__ __SUB0__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (
				(_class_ is None) and
				(_moduleName_ is not None) and
				(_sub0_ is not None) and
				(_sub1_ is None) and
				(_sub2_ is None) and
				(_sub3_ is None)
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		# ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥
			_strToRtn_ += f"""{FM.NEWLINE}{FM.NEWLINE}from FM import FM{FM.NEWLINE}{FM.NEWLINE}
{FM.makeAComment(f"start of {_moduleName_} {_sub0_}")}
_moduleName_ = {FM.DBLQT}{_moduleName_}{FM.DBLQT}
_sub0_ = {FM.DBLQT}{_sub0_}{FM.DBLQT}
{FM.MARK0MID("")}
_filename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_MOD_SUB0_PY(
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
){FM.CBRCE}{FM.TRIQT}  # {_filename_}
{FM.MARK0MID("")}
_newFilename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_MOD_SUB0_NEW_PY(
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
){FM.CBRCE}{FM.TRIQT}  # {_newFilename_}
{FM.MARK0MID("")}
__ID__ = {FM.OPAREN}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__FILENAME__{FM.DBLQT}, _filename_,{FM.CPAREN},  # {_filename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__MODULE_NAME__{FM.DBLQT}, _moduleName_,{FM.CPAREN},  # {_moduleName_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__NEW_FILENAME__{FM.DBLQT}, _newFilename_,{FM.CPAREN},  # {_newFilename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB0__{FM.DBLQT}, _sub0_,{FM.CPAREN},  # {_sub0_}
{FM.CPAREN}
{FM.MARK0MID("")}
TBGLST = {FM.OBRKT}
"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
			# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# end of __MODULE_NAME__ __SUB0__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# start of __MODULE_NAME__ __SUB0__ __SUB1__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (
				(_class_ is None) and
				(_moduleName_ is not None) and
				(_sub0_ is not None) and
				(_sub1_ is not None) and
				(_sub2_ is None) and
				(_sub3_ is None)
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			_strToRtn_ += f"""{FM.NEWLINE}{FM.NEWLINE}from FM import FM{FM.NEWLINE}{FM.NEWLINE}
{FM.makeAComment(f"start of {_moduleName_} {_sub0_} {_sub1_}")}
_moduleName_ = {FM.DBLQT}{_moduleName_}{FM.DBLQT}
_sub0_ = {FM.DBLQT}{_sub0_}{FM.DBLQT}
_sub1_ = {FM.DBLQT}{_sub1_}{FM.DBLQT}
{FM.MARK0MID("")}
_filename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_SUBD0_SUB2_PY(
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
{FM.NTAB(1)}__SUB1__=_sub1_,
){FM.CBRCE}{FM.TRIQT}  # {_filename_}
{FM.MARK0MID("")}
_newFilename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_SUBD0_SUB2_NEW_PY(
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
{FM.NTAB(1)}__SUB1__=_sub1_,
){FM.CBRCE}{FM.TRIQT}  # {_newFilename_}
{FM.MARK0MID("")}
__ID__ = {FM.OPAREN}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__FILENAME__{FM.DBLQT}, _filename_,{FM.CPAREN},  # {_filename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__MODULE_NAME__{FM.DBLQT}, _moduleName_,{FM.CPAREN},  # {_moduleName_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__NEW_FILENAME__{FM.DBLQT}, _newFilename_,{FM.CPAREN},  # {_newFilename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB0__{FM.DBLQT}, _sub0_,{FM.CPAREN},  # {_sub0_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB1__{FM.DBLQT}, _sub1_,{FM.CPAREN},  # {_sub1_}
{FM.CPAREN}
{FM.MARK0MID("")}
TBGLST = {FM.OBRKT}
"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
			# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# end of __MODULE_NAME__ __SUB0__ __SUB1__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# start of __MODULE_NAME__ __SUB0__D __SUB1__ __SUB2__ FM/TBGLST_D/_01_CF_NEW.py
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (
				(_class_ is None) and
				(_moduleName_ is not None) and
				(_sub0_ is not None) and
				(_sub1_ is not None) and
				(_sub2_ is not None) and
				(_sub3_ is None)
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			_strToRtn_ += f"""{FM.NEWLINE}{FM.NEWLINE}from FM import FM{FM.NEWLINE}{FM.NEWLINE}
{FM.makeAComment(f"start of {_moduleName_} {_sub0_} {_sub1_}")}
_moduleName_ = {FM.DBLQT}{_moduleName_}{FM.DBLQT}
_sub0_ = {FM.DBLQT}{_sub0_}{FM.DBLQT}
_sub1_ = {FM.DBLQT}{_sub1_}{FM.DBLQT}
_sub2_ = {FM.DBLQT}{_sub2_}{FM.DBLQT}
{FM.MARK0MID("")}
_filename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_SUBD0_SUB2_PY(
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
{FM.NTAB(1)}__SUB1__=_sub1_,
{FM.NTAB(1)}__SUB2__=_sub2_,
){FM.CBRCE}{FM.TRIQT}  # {_filename_}
{FM.MARK0MID("")}
_newFilename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_SUBD0_SUB2_NEW_PY(
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
{FM.NTAB(1)}__SUB1__=_sub1_,
{FM.NTAB(1)}__SUB2__=_sub2_,
){FM.CBRCE}{FM.TRIQT}  # {_newFilename_}
{FM.MARK0MID("")}
__ID__ = {FM.OPAREN}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__FILENAME__{FM.DBLQT}, _filename_,{FM.CPAREN},  # {_filename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__MODULE_NAME__{FM.DBLQT}, _moduleName_,{FM.CPAREN},  # {_moduleName_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__NEW_FILENAME__{FM.DBLQT}, _newFilename_,{FM.CPAREN},  # {_newFilename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB0__{FM.DBLQT}, _sub0_,{FM.CPAREN},  # {_sub0_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB1__{FM.DBLQT}, _sub1_,{FM.CPAREN},  # {_sub1_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB2__{FM.DBLQT}, _sub2_,{FM.CPAREN},  # {_sub2_}
{FM.CPAREN}
{FM.MARK0MID("")}
TBGLST = {FM.OBRKT}
"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
			# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# end of __MODULE_NAME__ __SUB0__D __SUB1__ __SUB2__ FM/TBGLST_D/_01_CF_NEW.py
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# start of __MODULE_NAME__ __SUB0__ __SUB1__ __CLASS__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (
				(_class_ is not None) and
				(_moduleName_ is not None) and
				(_sub0_ is not None) and
				(_sub1_ is not None) and
				(_sub2_ is None) and
				(_sub3_ is None)
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			_strToRtn_ += f"""{FM.NEWLINE}{FM.NEWLINE}from FM import FM{FM.NEWLINE}{FM.NEWLINE}
{FM.makeAComment(f"start of {_moduleName_} {_sub0_} {_sub1_} {_class_}")}
_class_ = {FM.DBLQT}{_class_}{FM.DBLQT}
_moduleName_ = {FM.DBLQT}{_moduleName_}{FM.DBLQT}
_sub0_ = {FM.DBLQT}{_sub0_}{FM.DBLQT}
_sub1_ = {FM.DBLQT}{_sub1_}{FM.DBLQT}
{FM.MARK0MID("")}
_filename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_SELF_SUB1_CLASS_PY(
{FM.NTAB(1)}__CLASS__=_class_,
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
{FM.NTAB(1)}__SUB1__=_sub1_,
){FM.CBRCE}{FM.TRIQT}  # {_filename_}
{FM.MARK0MID("")}
_newFilename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_SELF_SUB1_CLASS_NEW_PY(
{FM.NTAB(1)}__CLASS__=_class_,
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
{FM.NTAB(1)}__SUB1__=_sub1_,
){FM.CBRCE}{FM.TRIQT}  # {_newFilename_}
{FM.MARK0MID("")}
__ID__ = {FM.OPAREN}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__CLASS__{FM.DBLQT}, _class_,{FM.CPAREN},  # {_class_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__FILENAME__{FM.DBLQT}, _filename_,{FM.CPAREN},  # {_filename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__MODULE_NAME__{FM.DBLQT}, _moduleName_,{FM.CPAREN},  # {_moduleName_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__NEW_FILENAME__{FM.DBLQT}, _newFilename_,{FM.CPAREN},  # {_newFilename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB0__{FM.DBLQT}, _sub0_,{FM.CPAREN},  # {_sub0_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB1__{FM.DBLQT}, _sub1_,{FM.CPAREN},  # {_sub1_}
{FM.CPAREN}
{FM.MARK0MID("")}
TBGLST = {FM.OBRKT}
"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# end of __MODULE_NAME__ __SUB0__ __SUB1__ __CLASS__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# start of __MODULE_NAME__ __SUB0__D __SUB1__ __CLASS__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (
				(_class_ is not None) and
				(_moduleName_ is not None) and
				(_sub0_ is not None) and
				(_sub1_ is not None) and
				(_sub2_ is None) and
				(_sub3_ is None)
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			_strToRtn_ += f"""{FM.NEWLINE}{FM.NEWLINE}from FM import FM{FM.NEWLINE}{FM.NEWLINE}
{FM.makeAComment(f"start of {_moduleName_} {_sub0_} {_sub1_} {_class_}")}
_class_ = {FM.DBLQT}{_class_}{FM.DBLQT}
_moduleName_ = {FM.DBLQT}{_moduleName_}{FM.DBLQT}
_sub0_ = {FM.DBLQT}{_sub0_}{FM.DBLQT}
_sub1_ = {FM.DBLQT}{_sub1_}{FM.DBLQT}
{FM.MARK0MID("")}
_filename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_SELF_SUB1_CLASS_PY(
{FM.NTAB(1)}__CLASS__=_class_,
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
{FM.NTAB(1)}__SUB1__=_sub1_,
){FM.CBRCE}{FM.TRIQT}  # {_filename_}
{FM.MARK0MID("")}
_newFilename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_SELF_SUB1_CLASS_NEW_PY(
{FM.NTAB(1)}__CLASS__=_class_,
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
{FM.NTAB(1)}__SUB1__=_sub1_,
){FM.CBRCE}{FM.TRIQT}  # {_newFilename_}
{FM.MARK0MID("")}
__ID__ = {FM.OPAREN}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__CLASS__{FM.DBLQT}, _class_,{FM.CPAREN},  # {_class_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__FILENAME__{FM.DBLQT}, _filename_,{FM.CPAREN},  # {_filename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__MODULE_NAME__{FM.DBLQT}, _moduleName_,{FM.CPAREN},  # {_moduleName_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__NEW_FILENAME__{FM.DBLQT}, _newFilename_,{FM.CPAREN},  # {_newFilename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB0__{FM.DBLQT}, _sub0_,{FM.CPAREN},  # {_sub0_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB1__{FM.DBLQT}, _sub1_,{FM.CPAREN},  # {_sub1_}
{FM.CPAREN}
{FM.MARK0MID("")}
TBGLST = {FM.OBRKT}
"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# end of __MODULE_NAME__ __SUB0__ __SUB1__ __CLASS__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# start of __MODULE_NAME__ __SUB0__D __SUB1__ __SUB2__ __SUB3__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (
				(_class_ is None) and
				(_moduleName_ is not None) and
				(_sub0_ is not None) and
				(_sub1_ is not None) and
				(_sub2_ is not None) and
				(_sub3_ is not None)
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			_strToRtn_ += f"""{FM.NEWLINE}{FM.NEWLINE}from FM import FM{FM.NEWLINE}{FM.NEWLINE}
{FM.makeAComment(f"start of {_moduleName_} {_sub0_}D {_sub1_} {_sub2_} {_sub3_}")}
_moduleName_ = {FM.DBLQT}{_moduleName_}{FM.DBLQT}
_sub0_ = {FM.DBLQT}{_sub0_}{FM.DBLQT}
_sub1_ = {FM.DBLQT}{_sub1_}{FM.DBLQT}
_sub2_ = {FM.DBLQT}{_sub2_}{FM.DBLQT}
_sub3_ = {FM.DBLQT}{_sub3_}{FM.DBLQT}
{FM.MARK0MID("")}
_filename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_SUBD0_SUB3_PY(
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
{FM.NTAB(1)}__SUB1__=_sub1_,
{FM.NTAB(1)}__SUB2__=_sub2_,
{FM.NTAB(1)}__SUB3__=_sub3_,
){FM.CBRCE}{FM.TRIQT}  # {_filename_}
{FM.MARK0MID("")}
_newFilename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_SUBD0_SUB3_NEW_PY(
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
{FM.NTAB(1)}__SUB1__=_sub1_,
{FM.NTAB(1)}__SUB2__=_sub2_,
{FM.NTAB(1)}__SUB3__=_sub3_,
){FM.CBRCE}{FM.TRIQT}  # {_newFilename_}
{FM.MARK0MID("")}
__ID__ = {FM.OPAREN}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__FILENAME__{FM.DBLQT}, _filename_,{FM.CPAREN},  # {_filename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__MODULE_NAME__{FM.DBLQT}, _moduleName_,{FM.CPAREN},  # {_moduleName_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__NEW_FILENAME__{FM.DBLQT}, _newFilename_,{FM.CPAREN},  # {_newFilename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB0__{FM.DBLQT}, _sub0_,{FM.CPAREN},  # {_sub0_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB1__{FM.DBLQT}, _sub1_,{FM.CPAREN},  # {_sub1_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB2__{FM.DBLQT}, _sub2_,{FM.CPAREN},  # {_sub2_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB3__{FM.DBLQT}, _sub3_,{FM.CPAREN},  # {_sub3_}
{FM.CPAREN}
{FM.MARK0MID("")}
TBGLST = {FM.OBRKT}
"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# end of __MODULE_NAME__ __SUB0__D __SUB1__ __SUB2__ __SUB3__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# start of __MODULE_NAME__ __SUB0__D __SUB1__ __SUB2__ __SUB3__ __CLASS__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (
				(_class_ is not None) and
				(_moduleName_ is not None) and
				(_sub0_ is not None) and
				(_sub1_ is not None) and
				(_sub2_ is not None) and
				(_sub3_ is not None)
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			_strToRtn_ += f"""{FM.NEWLINE}{FM.NEWLINE}from FM import FM{FM.NEWLINE}{FM.NEWLINE}
{FM.makeAComment(f"start of {_moduleName_} {_sub0_} {_sub1_} {_sub2_} {_sub3_} {_class_}")}
_class_ = {FM.DBLQT}{_class_}{FM.DBLQT}
_moduleName_ = {FM.DBLQT}{_moduleName_}{FM.DBLQT}
_sub0_ = {FM.DBLQT}{_sub0_}{FM.DBLQT}
_sub1_ = {FM.DBLQT}{_sub1_}{FM.DBLQT}
_sub2_ = {FM.DBLQT}{_sub2_}{FM.DBLQT}
_sub3_ = {FM.DBLQT}{_sub3_}{FM.DBLQT}
{FM.MARK0MID("")}
_filename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_SUBD0_SUB3_C_PY(
{FM.NTAB(1)}__CLASS__=_class_,
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
{FM.NTAB(1)}__SUB1__=_sub1_,
{FM.NTAB(1)}__SUB2__=_sub2_,
{FM.NTAB(1)}__SUB3__=_sub3_,
){FM.CBRCE}{FM.TRIQT}  # {_filename_}
{FM.MARK0MID("")}
_newFilename_ = f{FM.TRIQT}{FM.OBRCE}FM.NAME_LCL_SUBD0_SUB3_C_NEW_PY(
{FM.NTAB(1)}__CLASS__=_class_,
{FM.NTAB(1)}__MODULE_NAME__=_moduleName_,
{FM.NTAB(1)}__SUB0__=_sub0_,
{FM.NTAB(1)}__SUB1__=_sub1_,
{FM.NTAB(1)}__SUB2__=_sub2_,
{FM.NTAB(1)}__SUB3__=_sub3_,
){FM.CBRCE}{FM.TRIQT}  # {_newFilename_}
{FM.MARK0MID("")}
__ID__ = {FM.OPAREN}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__CLASS__{FM.DBLQT}, _class_,{FM.CPAREN},  # {_class_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__FILENAME__{FM.DBLQT}, _filename_,{FM.CPAREN},  # {_filename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__MODULE_NAME__{FM.DBLQT}, _moduleName_,{FM.CPAREN},  # {_moduleName_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__NEW_FILENAME__{FM.DBLQT}, _newFilename_,{FM.CPAREN},  # {_newFilename_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB0__{FM.DBLQT}, _sub0_,{FM.CPAREN},  # {_sub0_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB1__{FM.DBLQT}, _sub1_,{FM.CPAREN},  # {_sub1_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB2__{FM.DBLQT}, _sub2_,{FM.CPAREN},  # {_sub2_}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}__SUB3__{FM.DBLQT}, _sub3_,{FM.CPAREN},  # {_sub3_}
{FM.CPAREN}
{FM.MARK0MID("")}
TBGLST = {FM.OBRKT}
"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# end of __MODULE_NAME__ __SUB0__D __SUB1__ __SUB2__ __SUB3__ __CLASS__
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

		self.__FILE_DICT__[_newFilename_].write(_strToRtn_)
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# end of startLCLNewFile
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# start of write
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def write(self,
			itemToExplode_,
	):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (itemToExplode_ is None):
			return None, None
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
		_IDBeingExploded_ = self.makeDictID(itemToExplode_[1])
		_lineToWrt_ = itemToExplode_[0]
		_class_ = _IDBeingExploded_.get("__CLASS__")
		_filename_ = _IDBeingExploded_.get("__FILENAME__")
		_moduleName_ = _IDBeingExploded_.get("__MODULE_NAME__")
		_newFilename_ = _IDBeingExploded_.get("__NEW_FILENAME__")
		_sub0_ = _IDBeingExploded_.get("__SUB0__")
		_sub1_ = _IDBeingExploded_.get("__SUB1__")
		_sub2_ = _IDBeingExploded_.get("__SUB2__")
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (
				(_newFilename_ is not None) and
				(_newFilename_ not in self.__FILE_DICT__)
		):
		# ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥
			self.__FILE_DICT__[_newFilename_] = open(_newFilename_, "tw")
			self.startLCLNewFile(itemToExplode_[1])
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
		_strToWrt_ = f"""{FM.NTAB(1)}{FM.OPAREN}{FM.OPAREN}"""
		_strToWrt1_ = f"""{FM.NTAB(1)}{FM.OPAREN}{FM.OPAREN}"""
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _index_, _itemToWrite_ in enumerate(_lineToWrt_):
			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if (_index_ != 1):
				_strToWrt_ += f"""{FM.DBLQT}{_itemToWrite_}{FM.DBLQT}, """
				_strToWrt1_ += f"""{FM.DBLQT}{_itemToWrite_}{FM.DBLQT}, """
			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			else:
				_strToWrt_ += f"""FM.{_itemToWrite_}, """
				_strToWrt1_ += f"""FM.{_itemToWrite_}, """
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
		_strToWrt_ = _strToWrt_[:-1]
		_strToWrt_ += f"""{FM.CPAREN}, __ID__{FM.CPAREN},{FM.NEWLINE}"""
		_strToWrt1_ = _strToWrt1_[:-1]
		_strToWrt1_ += f"""{FM.CPAREN}, {itemToExplode_[1]}{FM.CPAREN},{FM.NEWLINE}"""
		self.__FILE_DICT__[_newFilename_].write(_strToWrt_)
		self.__FILE_DICT__[FM.NAME_LCL_MOD_SUB0_NEW_PY(
				__MODULE_NAME__="FM",
				__SUB0__="TBGLST",
		)].write(_strToWrt1_)
		# ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥ ⥣0⥥
		return itemToExplode_[0], itemToExplode_[1]
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# end of write
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# start of __enter__
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def __enter__(self):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		return self
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# end of __enter__
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# start of __exit__
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def __exit__(self,
			*args,
			**KWargs
	):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisFilename_, _thisFD_ in self.__FILE_DICT__.items():
			_thisFD_.write(f"""{FM.CBRKT}{FM.NNL(3)}{FM.makeAWideComment(f"end of {_thisFilename_}")}{FM.NEWLINE}{FM.NEWLINE}#{FM.NEWLINE}""")
			_thisFD_.flush()
			_thisFD_.close()
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# end of __exit__
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# end of FM_MTBL_C.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
