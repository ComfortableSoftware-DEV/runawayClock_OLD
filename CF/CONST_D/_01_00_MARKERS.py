

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of CF.CONST_D.MARKERS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


import ._01_00_MARKERS as M
import ._01_00_NAMES as N
import ._01_00_VALS as V


CMNTLEN = 250
FOLDLEN = 250


FOLD1ENDHERE = f"""# fold here {"⟰1" * (FOLDLEN // 2)}"""
FOLD1ENDHERELN = f"""# fold here {"⟰1" * (FOLDLEN // 2)}{V.NEWLINE}"""
FOLD1STARTHERE = f"""# fold here {"⟱1" * (FOLDLEN // 2)}"""
FOLD1STARTHERELN = f"""# fold here {"⟱1" * (FOLDLEN // 2)}{V.NEWLINE}"""
FOLD2ENDHERE = f"""# fold here {"⟰2" * (FOLDLEN // 2)}"""
FOLD2ENDHERELN = f"""# fold here {"⟰2" * (FOLDLEN // 2)}{V.NEWLINE}"""
FOLD2STARTHERE = f"""# fold here {"⟱2" * (FOLDLEN // 2)}"""
FOLD2STARTHERELN = f"""# fold here {"⟱2" * (FOLDLEN // 2)}{V.NEWLINE}"""
FOLD3ENDHERE = f"""# fold here {"⟰3" * (FOLDLEN // 2)}"""
FOLD3ENDHERELN = f"""# fold here {"⟰3" * (FOLDLEN // 2)}{V.NEWLINE}"""
FOLD3STARTHERE = f"""# fold here {"⟱3" * (FOLDLEN // 2)}"""
FOLD3STARTHERELN = f"""# fold here {"⟱3" * (FOLDLEN // 2)}{V.NEWLINE}"""


CMNTLINE = f"""# * {"#*" * (CMNTLEN // 2)}"""
IMPORTANTSTR = f"""# * {"!-" * (CMNTLEN // 2)}"""  # important line marker
INDENTIN = " -=> "  # display arrow RIGHT
INDENTOUT = " <=- "  # display arrow LEFT
INFOSTR = f"""# * {"%_" * (CMNTLEN // 2)}"""  # INFO _STR_ line


MARK0END = lambda __TAG__: f"""# {"⟰0 " * (CMNTLEN // 3)} {__TAG__}"""
MARK0ENDLN = lambda __TAG__: f"""# {"⟰0 " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK0MID = lambda __TAG__: f"""# {"⟰0⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK0MIDLN = lambda __TAG__: f"""# {"⟰0⟱ " * (CMNTLEN // 4)} {__TAG__}{V.NEWLINE}"""
MARK0START = lambda __TAG__: f"""# {"0⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK0STARTLN = lambda __TAG__: f"""# {"0⟱ " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK1END = lambda __TAG__: f"""# {"⟰1 " * (CMNTLEN // 3)} {__TAG__}"""
MARK1ENDLN = lambda __TAG__: f"""# {"⟰1 " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK1MID = lambda __TAG__: f"""# {"⟰1⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK1MIDLN = lambda __TAG__: f"""# {"⟰1⟱ " * (CMNTLEN // 4)} {__TAG__}{V.NEWLINE}"""
MARK1START = lambda __TAG__: f"""# {"1⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK1STARTLN = lambda __TAG__: f"""# {"1⟱ " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK2END = lambda __TAG__: f"""# {"⟰2 " * (CMNTLEN // 3)} {__TAG__}"""
MARK2ENDLN = lambda __TAG__: f"""# {"⟰2 " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK2MID = lambda __TAG__: f"""# {"⟰2⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK2MIDLN = lambda __TAG__: f"""# {"⟰2⟱ " * (CMNTLEN // 4)} {__TAG__}{V.NEWLINE}"""
MARK2START = lambda __TAG__: f"""# {"2⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK2STARTLN = lambda __TAG__: f"""# {"2⟱ " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK3END = lambda __TAG__: f"""# {"⟰3 " * (CMNTLEN // 3)} {__TAG__}"""
MARK3ENDLN = lambda __TAG__: f"""# {"⟰3 " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK3MID = lambda __TAG__: f"""# {"⟰3⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK3MIDLN = lambda __TAG__: f"""# {"⟰3⟱ " * (CMNTLEN // 4)} {__TAG__}{V.NEWLINE}"""
MARK3START = lambda __TAG__: f"""# {"3⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK3STARTLN = lambda __TAG__: f"""# {"3⟱ " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK4END = lambda __TAG__: f"""# {"⟰4 " * (CMNTLEN // 3)} {__TAG__}"""
MARK4ENDLN = lambda __TAG__: f"""# {"⟰4 " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK4MID = lambda __TAG__: f"""# {"⟰4⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK4MIDLN = lambda __TAG__: f"""# {"⟰4⟱ " * (CMNTLEN // 4)} {__TAG__}{V.NEWLINE}"""
MARK4START = lambda __TAG__: f"""# {"4⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK4STARTLN = lambda __TAG__: f"""# {"4⟱ " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK5END = lambda __TAG__: f"""# {"⟰5 " * (CMNTLEN // 3)} {__TAG__}"""
MARK5ENDLN = lambda __TAG__: f"""# {"⟰5 " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK5MID = lambda __TAG__: f"""# {"⟰5⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK5MIDLN = lambda __TAG__: f"""# {"⟰5⟱ " * (CMNTLEN // 4)} {__TAG__}{V.NEWLINE}"""
MARK5START = lambda __TAG__: f"""# {"5⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK5STARTLN = lambda __TAG__: f"""# {"5⟱ " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK6END = lambda __TAG__: f"""# {"⟰6 " * (CMNTLEN // 3)} {__TAG__}"""
MARK6ENDLN = lambda __TAG__: f"""# {"⟰6 " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK6MID = lambda __TAG__: f"""# {"⟰6⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK6MIDLN = lambda __TAG__: f"""# {"⟰6⟱ " * (CMNTLEN // 4)} {__TAG__}{V.NEWLINE}"""
MARK6START = lambda __TAG__: f"""# {"6⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK6STARTLN = lambda __TAG__: f"""# {"6⟱ " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK7END = lambda __TAG__: f"""# {"⟰7 " * (CMNTLEN // 3)} {__TAG__}"""
MARK7ENDLN = lambda __TAG__: f"""# {"⟰7 " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK7MID = lambda __TAG__: f"""# {"⟰7⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK7MIDLN = lambda __TAG__: f"""# {"⟰7⟱ " * (CMNTLEN // 4)} {__TAG__}{V.NEWLINE}"""
MARK7START = lambda __TAG__: f"""# {"7⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK7STARTLN = lambda __TAG__: f"""# {"7⟱ " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK8END = lambda __TAG__: f"""# {"⟰8 " * (CMNTLEN // 3)} {__TAG__}"""
MARK8ENDLN = lambda __TAG__: f"""# {"⟰8 " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK8MID = lambda __TAG__: f"""# {"⟰8⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK8MIDLN = lambda __TAG__: f"""# {"⟰8⟱ " * (CMNTLEN // 4)} {__TAG__}{V.NEWLINE}"""
MARK8START = lambda __TAG__: f"""# {"8⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK8STARTLN = lambda __TAG__: f"""# {"8⟱ " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK9END = lambda __TAG__: f"""# {"⟰9 " * (CMNTLEN // 3)} {__TAG__}"""
MARK9ENDLN = lambda __TAG__: f"""# {"⟰9 " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""
MARK9MID = lambda __TAG__: f"""# {"⟰9⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK9MIDLN = lambda __TAG__: f"""# {"⟰9⟱ " * (CMNTLEN // 4)} {__TAG__}{V.NEWLINE}"""
MARK9START = lambda __TAG__: f"""# {"9⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK9STARTLN = lambda __TAG__: f"""# {"9⟱ " * (CMNTLEN // 3)} {__TAG__}{V.NEWLINE}"""


MARK_END = lambda __TAG__: f"""# {__TAG__} {"⟰ " * (CMNTLEN // 2)}"""
MARK_ENDLN = lambda __TAG__: f"""# {__TAG__} {"⟰ " * (CMNTLEN // 2)}{V.NEWLINE}"""
MARK_MID = lambda __TAG__: f"""# {__TAG__} {"⟰⟱" * (CMNTLEN // 2)}"""
MARK_MIDLN = lambda __TAG__: f"""# {__TAG__} {"⟰⟱" * (CMNTLEN // 2)}{V.NEWLINE}"""
MARK_START = lambda __TAG__: f"""# {__TAG__} {" ⟱" * (CMNTLEN // 2)}"""
MARK_STARTLN = lambda __TAG__: f"""# {__TAG__} {" ⟱" * (CMNTLEN // 2)}{V.NEWLINE}"""


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeAComment
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeAComment(comment_):
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	_strToRtn_ = ""
	_strToRtn_ += f"""{CMNTLINE}{V.NEWLINE}# * {comment_}{V.NEWLINE}{CMNTLINE}{V.NEWLINE}"""
	return _strToRtn_
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeAComment
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeAWideComment(comment_):
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	_strToRtn_ = ""
	_strToRtn_ += f"""#{V.NEWLINE}#{V.NEWLINE}{CMNTLINE}{V.NEWLINE}# * {comment_}{V.NEWLINE}{CMNTLINE}{V.NEWLINE}#{V.NEWLINE}#{V.NEWLINE}"""
	return _strToRtn_
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


def makeFolds():
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	with (
			(open(N.MAKE_NAME(
					isNew_=True,
					__MODULE_NAME__="CF",
					__SUBD0__="CONSTANTS",
					__SUB0__="MARKERS",
					__SUB1__="FOLDS",
			))) as FD_out
	):
		FD_out.write(f"""{V.NEWLINE}{V.NEWLINE}{makeAWideComment("start of folds ")}{V.NEWLINE}{V.NEWLINE}
FOLD1ENDHERE = {V.DBLQT}{FOLD1ENDHERE}{V.DBLQT}
FOLD1ENDHERELN = {V.DBLQT}{FOLD1ENDHERELN}{V.DBLQT}
FOLD1STARTHERE = {V.DBLQT}{FOLD1STARTHERE}{V.DBLQT}
FOLD1STARTHERELN = {V.DBLQT}{FOLD1STARTHERELN}{V.DBLQT}
FOLD2ENDHERE = {V.DBLQT}{FOLD2ENDHERE}{V.DBLQT}
FOLD2ENDHERELN = {V.DBLQT}{FOLD2ENDHERELN}{V.DBLQT}
FOLD2STARTHERE = {V.DBLQT}{FOLD2STARTHERE}{V.DBLQT}
FOLD2STARTHERELN = {V.DBLQT}{FOLD2STARTHERELN}{V.DBLQT}
FOLD3ENDHERE = {V.DBLQT}{FOLD3ENDHERE}{V.DBLQT}
FOLD3ENDHERELN = {V.DBLQT}{FOLD3ENDHERELN}{V.DBLQT}
FOLD3STARTHERE = {V.DBLQT}{FOLD3STARTHERE}{V.DBLQT}
FOLD3STARTHERELN = {V.DBLQT}{FOLD3STARTHERELN}{V.DBLQT}{V.NEWLINE}{V.NEWLINE}{V.NEWLINE}
FOLD1ENDHERE = {V.FTQ}# fold here {V.OBRCE}"⟰1" * (FOLDLEN // 2){V.CBRCE}{V.TRIQT}
FOLD1ENDHERELN = {V.FTQ}# fold here {V.OBRCE}"⟰1" * (FOLDLEN // 2){V.CBRCE}{V.NEWLINE}{V.TRIQT}
FOLD1STARTHERE = {V.FTQ}# fold here {OBRCE}"1⟱" * (FOLDLEN // 2){CBRCE}{V.TRIQT}
FOLD1STARTHERELN = {V.FTQ}# fold here {OBRCE}"1⟱" * (FOLDLEN // 2){CBRCE}{V.NEWLINE}{V.TRIQT}
FOLD2ENDHERE = {V.FTQ}# fold here {V.OBRCE}"⟰2" * (FOLDLEN // 2){V.CBRCE}{V.TRIQT}
FOLD2ENDHERELN = {V.FTQ}# fold here {V.OBRCE}"⟰2" * (FOLDLEN // 2){V.CBRCE}{V.NEWLINE}{V.TRIQT}
FOLD2STARTHERE = {V.FTQ}# fold here {OBRCE}"2⟱" * (FOLDLEN // 2){CBRCE}{V.TRIQT}
FOLD2STARTHERELN = {V.FTQ}# fold here {OBRCE}"2⟱" * (FOLDLEN // 2){CBRCE}{V.NEWLINE}{V.TRIQT}
FOLD3ENDHERE = {V.FTQ}# fold here {V.OBRCE}"⟰3" * (FOLDLEN // 2){V.CBRCE}{V.TRIQT}
FOLD3ENDHERELN = {V.FTQ}# fold here {V.OBRCE}"⟰3" * (FOLDLEN // 2){V.CBRCE}{V.NEWLINE}{V.TRIQT}
FOLD3STARTHERE = {V.FTQ}# fold here {OBRCE}"3⟱" * (FOLDLEN // 2){CBRCE}{V.TRIQT}
FOLD3STARTHERELN = {V.FTQ}# fold here {OBRCE}"3⟱" * (FOLDLEN // 2){CBRCE}{V.NEWLINE}{V.TRIQT}
{V.NEWLINE}{V.NEWLINE}{makeAWideComment("end of folds ")}{V.NEWLINE}{V.NEWLINE}
""")
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# MAKE_ONELNS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def MAKE_ONELNS():
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	with (
			(open(N.MAKE_NAME(
					isNew_=True,
					__MODULE_NAME__="CF",
					__SUBD0__="CONSTANTS",
					__SUB0__="MARKERS",
					__SUB1__="FOLDS",
			))) as FD_out
	):
		FD_out.write(f"""{V.NEWLINE}{V.NEWLINE}{makeAWideComment("start of folds ")}{V.NEWLINE}{V.NEWLINE}
CMNTLINE = {V.FTQ}{CMNTLINE}{V.TRIQT}
IMPORTANTSTR = {V.FTQ}{IMPORTANTSTR}{V.TRIQT}
INDENTIN = {V.FTQ}{INDENTIN}{V.TRIQT}
INDENTOUT = {V.FTQ}{INDENTOUT}{V.TRIQT}
INFOSTR = {V.FTQ}{INFOSTR}{V.TRIQT}{V.NEWLINE}
CMNTLINE = {V.FTQ}# * {"#*" * (CMNTLEN // 2)}{V.TRIQT}  # my standard # * #*#*… comment line
IMPORTANTSTR = {V.FTQ}# * {"!-" * (CMNTLEN // 2)}{V.TRIQT}  # important line marker
INDENTIN = " -=> "  # display arrow RIGHT
INDENTOUT = " <=- "  # display arrow LEFT
INFOSTR = {V.FTQ}# * {"%_" * (CMNTLEN // 2)}{V.TRIQT}  # INFO _STR_ line""")
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# MAKE_MARKS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def MAKE_MARKS():
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	with (
			(open(N.MAKE_NAME(
					isNew_=True,
					__MODULE_NAME__="CF",
					__SUBD0__="CONSTANTS",
					__SUB0__="MARKERS",
					__SUB1__="FOLDS",
			))) as FD_out
	):
		FD_out.write(f"""{V.NEWLINE}{V.NEWLINE}{makeAWideComment("start of folds ")}{V.NEWLINE}{V.NEWLINE}
""")
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


#


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of CF.CONST_D.MARKERS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#
