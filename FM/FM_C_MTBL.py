

from FM import FM


class C_MTBL():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	def __init__(self):
		self.__FILE_DICT__ = {}
		_filename_ = FM.NAME_LCL_SUB_NEW_PY("FM", "TBGLST")
		_tupleToRtn_ = (
			("FM", _filename_),
			"FM_00_ORIGIN",
			FM.FMAX_NOP,
			"start of FM_TBGLST",
		)
		self.write()


	def __enter__(self):
		return self


	def __exit__(self, *args, **KWargs):
		for _thisFilename_, _thisFD_ in self.__FILE_DICT__.items():
			_thisFD_.flush()
			_thisFD_.close()


	def startSubNewFile(self, moduleName_, sub_):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		_strToRtn_ = ""
		_filename_ = FM.NAME_LCL_SUB_NEW_PY(moduleName_, sub_)
		_strToRtn_ += f"""{FM.NEWLINE}{FM.NEWLINE}from FM import FM
__MODULE_NAME__ = {FM.DBLQT}{moduleName_}{FM.DBLQT}
__FILENAME__ = {FM.DBLQT}{_filename_}{FM.DBLQT}
TBGLST = {FM.OBRKT}
{FM.NTAB(1)}{FM.OPAREN}{FM.DBLQT}{moduleName_}{FM.DBLQT}, {FM.DBLQT}{_filename_}{FM.DBLQT}{FM.CPAREN}, {FM.DBLQT}00_{moduleName_}_{sub_}_BEGINS{FM.DBLQT}, FMAX_NOP, {FM.DBLQT}start of {_filename_}{FM.DBLQT},{FM.CPAREN},{FM.NEWLINE}"""
		self.__FILE_DICT__[_filename_].write(_strToRtn_)

		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2


	def write(self, itemToExplode_):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		if (itemToExplode_ is not None):
			_fileData_ = itemToExplode_.pop(0)

			if (_fileData_[1] in self.__FILE_DICT__):
				_strToWrt_ = f"""{NTAB(1)}{FM.OPAREN}{FM.OPAREN}{FM.DBLQT}{_fileData_[0]}, {FM.DBLQT}{_fileData_[1]}{FM.DBLQT}{FM.CPAREN}, {FM.DBLQT}{itemToExplode_[0]}{FM.DBLQT}, {itemToExplode_[1]}, """
				self.__FILE_DICT__[_fileData_[1]].write(_strToWrt_)

			else:
				self.__FILE_DICT__[_fileData_[1]] = open(CF.NAME_LCL_SUB_NEW_PY(_fileData_), "tw")
				self.startSubFile(_fileData_)
				self.__FILE_DICT__[_fileData_[1]].write(f"""{NTAB(1)}{OPAREN}{_fileData_[1]}, {DBLQT}{itemToExplode_[0]}{DBLQT}, {itemToExplode_[1]}, """)

			for _index_ in range(2, len(itemToExplode_)):
				self.__FILE_DICT__[_fileData_[1]].write(f"""{DBLQT}{itemToExplode_[_index_]}{DBLQT}, """)

			self.__FILE_DICT__[_fileData_[1]].write(f"""{_strToRtn_[:-1]}{CPAREN},{NEWLINE}""")
			return itemToExplode_
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2


	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# end of FM_C_MTBL.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#

#
