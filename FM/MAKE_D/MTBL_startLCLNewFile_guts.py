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
