

from CF.CONSTANTS import MARKERS as M
from CF.CONSTANTS import NAMES as N
from CF.CONSTANTS import VALS as V
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
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of __init__
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def __init__(self):
		# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
		self.__FILE_DICT__ = {}
		# ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱
		self._DPD_ = {
			F___ENTER__: True,
			F___EXIT__: True,
			F___INIT__: True,
			F_MAKEID: True,
			F_STARTLCLNEWFILE: True,
			F_WRITE: True,
		}
		# ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱
		_moduleName_ = "FM"
		_sub0_ = "TBGLST"
		# ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱
		_IDToRtn_ = N.MAKE_ID(
				__MODULE_NAME__=_moduleName_,
				__SUB0__=_sub0_,
		)
		# ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱
		_TBGLSTEntry_ = (
				"FM_TBGLST",
				"FMAX_NOP",
				"start of all things list",
		)
		# ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱
		_valToRtn_ = (
				_TBGLSTEntry_,
				_IDToRtn_,
		)
		# ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱
		__dummy__ = self.write(_valToRtn_)
		# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# end of __init__
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of makeDictID
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def makeDictID(self,
			ID_
	):
		# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(isinstance(ID_, dict) is True)
		):
			return ID_
		_dictToRtn_ = dict((x, y) for x, y in ID_)
		return _dictToRtn_
		# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# end of makeDictID
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of startLCLNewFile
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def startLCLNewFile(self,
			IDToWrt_
	):
		# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
		_strToRtn_ = ""
		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(isinstance(IDToWrt_, dict))
		):
			_IDIn_ = N.DEFAULT_KWArgs.copy()
			_IDIn_.update(IDToWrt_)
		# ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱
		elif (
				(isinstance(IDToWrt_, tuple))
		):
			_TIDIn_ = self.makeDictID(IDToWrt_)
			_IDIn_ = N.DEFAULT_KWArgs.copy()
			_IDIn_.update(_TIDIn_)
		# ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱
		else:
			return None
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2

		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		for _thisKey_, _thisVal_ in _IDIn_.items():
			# 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
			if (
					(_thisVal_ in V.EMPTYSTRLST)
			):
				_IDIn_[_thisKey_] = "None"
			# ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
		_class_ = _IDIn_.get("__CLASS__")
		_filename_ = _IDIn_.get("__FILENAME__")
		_moduleName_ = _IDIn_.get("__MODULE_NAME__")
		_newFilename_ = _IDIn_.get("__NEW_FILENAME__")
		_subd0_ = _IDIn_.get("__SUBD0__")
		_subd1_ = _IDIn_.get("__SUBD1__")
		_sub0_ = _IDIn_.get("__SUB0__")
		_sub1_ = _IDIn_.get("__SUB1__")
		_sub2_ = _IDIn_.get("__SUB2__")
		_sub3_ = _IDIn_.get("__SUB3__")
		_sub4_ = _IDIn_.get("__SUB4__")
		_sub5_ = _IDIn_.get("__SUB5__")
		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(_filename_ is None)
		):
			_filename_ = N.MAKE_NAME(_IDIn_)
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(_newFilename_ is None)
		):
			_newFilename_ = N.MAKE_NAME(isNew_=True, **IDIn_)
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
		_strToRtn_ = f"""{V.NEWLINE}
{M.makeAComment(f"start of {_filename_}")}
from CF.CONSTANTS import NAMES as NAMES
from FM import FM{V.NEWLINE}
_class_ = "{_class_}"
_filename_ = "{_filename_}"
_moduleName_ = "{_moduleName_}"
_newFilename_ = "{_newFilename_}"
_subd0_ = "{_subd0_}"
_subd1_ = "{_subd1_}"
_sub0_ = "{_sub0_}"
_sub1_ = "{_sub1_}"
_sub2_ = "{_sub2_}"
_sub3_ = "{_sub3_}"
_sub4_ = "{_sub4_}"
_sub5_ = "{_sub5_}"{V.NEWLINE}{V.NEWLINE}
_ID_ = (
{V.NTAB(1)}{V.OPAREN}__CLASS__, _class_,{V.CPAREN},  # {_class_}
{V.NTAB(1)}{V.OPAREN}__FILENAME__, _filename_,{V.CPAREN},  # {_filename_}
{V.NTAB(1)}{V.OPAREN}__MODULE_NAME_, _moduleName_,{V.CPAREN},  # {_moduleName_}
{V.NTAB(1)}{V.OPAREN}__NEWFILENAME__, _newFilename_,{V.CPAREN},  # {_newFilename_}
{V.NTAB(1)}{V.OPAREN}__SUBD0__, _subd0_,{V.CPAREN},  # {_subd0_}
{V.NTAB(1)}{V.OPAREN}__SUBD1__, _subd1_,{V.CPAREN},  # {_subd1_}
{V.NTAB(1)}{V.OPAREN}__SUB0__, _sub0_,{V.CPAREN},  # {_sub0_}
{V.NTAB(1)}{V.OPAREN}__SUB1__, _sub1_,{V.CPAREN},  # {_sub1_}
{V.NTAB(1)}{V.OPAREN}__SUB2__, _sub2_,{V.CPAREN},  # {_sub2_}
{V.NTAB(1)}{V.OPAREN}__SUB3__, _sub3_,{V.CPAREN},  # {_sub3_}
{V.NTAB(1)}{V.OPAREN}__SUB4__, _sub4_,{V.CPAREN},  # {_sub4_}
{V.NTAB(1)}{V.OPAREN}__SUB5__, _sub5_,{V.CPAREN},  # {_sub5_}
){V.NEWLINE}
TBGLST = {V.OBRKT}
"""
		self.__FILE_DICT__[_newFilename_].write(_strToRtn_)
		# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# end of startLCLNewFile
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# start of write
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def write(self,
			itemToExplode_,
	):
		# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (itemToExplode_ is None):
			return None, None
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
		_IDBeingExploded_ = self.makeDictID(itemToExplode_[1])
		_lineToWrt_ = itemToExplode_[0]
		_newFilename_ = _IDBeingExploded_.get("__NEW_FILENAME__")
		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		if (
				(_newFilename_ is not None) and
				(_newFilename_ not in self.__FILE_DICT__)
		):
		# ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱
			self.__FILE_DICT__[_newFilename_] = open(_newFilename_, "tw")
			self.startLCLNewFile(itemToExplode_[1])
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
		_strToWrt_ = f"""{V.NTAB(1)}{V.OPAREN}{V.OPAREN}"""
		_strToWrt1_ = f"""{V.NTAB(1)}{V.OPAREN}{V.OPAREN}"""
		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		for _index_, _itemToWrite_ in enumerate(_lineToWrt_):
			# 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
			if (_index_ != 1):
				_strToWrt_ += f"""{V.DBLQT}{_itemToWrite_}{V.DBLQT}, """
				_strToWrt1_ += f"""{V.DBLQT}{_itemToWrite_}{V.DBLQT}, """
			# ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱ ⟰3⟱
			else:
				_strToWrt_ += f"""FM.{_itemToWrite_}, """
				_strToWrt1_ += f"""FM.{_itemToWrite_}, """
			# ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3
		# ##$# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
		_strToWrt_ = _strToWrt_[:-1]
		_strToWrt_ += f"""{V.CPAREN}, __ID__{V.CPAREN},{V.NEWLINE}"""
		_strToWrt1_ = _strToWrt1_[:-1]
		_strToWrt1_ += f"""{V.CPAREN}, {itemToExplode_[1]}{V.CPAREN},{V.NEWLINE}"""
		self.__FILE_DICT__[_newFilename_].write(_strToWrt_)
		_TID_ = N.MAKE_ID(
				__MODULE_NAME__="FM",
				__SUB0__="TBGLST",
		)
		_newFilename_ = _TID_["__NEW_FILENAME__"]
		self.__FILE_DICT__[N.MAKE_NAME(
				isNew_=True,
				__MODULE_NAME__="FM",
				__SUB0__="TBGLST",
		)].write(_strToWrt1_)
		# ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱ ⟰0⟱
		return itemToExplode_[0], itemToExplode_[1]
	# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# end of write
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# start of __enter__
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	def __enter__(self):
		# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
		return self
		# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
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
		# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
		# 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
		for _thisFilename_, _thisFD_ in self.__FILE_DICT__.items():
			_thisFD_.write(f"""{V.CBRKT}{V.NNL(3)}{M.makeAWideComment(f"end of {_thisFilename_}")}{V.NEWLINE}{V.NEWLINE}#{V.NEWLINE}""")
			_thisFD_.flush()
			_thisFD_.close()
		# ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
		# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
	# end of __exit__
	# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# end of FM_MTBL_C.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*