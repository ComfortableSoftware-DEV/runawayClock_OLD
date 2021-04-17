#!/usr/bin/python


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# modules defined in FM.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# FM.py is copied, along with the appropriate FMxxxxxx.py file from CONFIGDIR to local by pythonUnitsLink.py
# make sure if you change the modules, you also update the stored copy FMxxxxxx.py TBGLST file when you update FM.py
# CF.py is always linked, make sure to update CFTOP.py and SCTN0102 when FM.py or CF.py are changed
# all other units are loaded dynamically by pythonUnitsLink.py using the SCTN16 structure, FMSCTNENABLED.py file locally, etc.
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * def doErrorItem(message_, itemToError_):
# * def explodeItem(itemToExplode_):
# * def makeAComment(comment_):
# * def makeADict(dictName_, dictComment_, dictItems_):
# * def makeAList(listName_, listComment_, listItems_):
# * def makeATupDict(tupDictName_, tupDictItems_, tupDictSidecar_):
# * def makeAWideComment(comment_):
# * def makeCF():
# * def makeDBSQLT()
# * def makeDO():
# * def makeDOHBI():
# * def makeFM():
# * def makeFO():
# * def makeSP():
# * def parseTBGLST(FDTBGLST):
# * def readFileToStr(FILENAME_):
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * def __main__():


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0001 _CHR_ _CONST_
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BKQT = "`"  # BACK TICK
BKSLSH = "\\"  # BACKSLASH
CBRCE = "}"  # CLOSEBRACE
CBRKT = "]"  # CLOSEBRACKET
CPAREN = ")"  # CLOSE PARENTHESIS
DBLQT = "\""  # DOUBLE QUOTE
ESC = "\x1b"
NEWLINE = "\n"  # NEWLINE
OBRCE = "{"  # OPENBRACE
OBRKT = "["  # OPENBRACKET
OPAREN = "("  # OPENPAREN
SGLQT = "'"  # simple ' character
SPCSTR = " "  # SPACE character"
TABSTR = "\t"  # TAB

CMNTLEN = 200
CONFIGDIR = "/rcr/0-units/python/"
FOLDLEN = 200
TRIQT = f"""{DBLQT}{DBLQT}{DBLQT}"""


#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0002 value_ constants
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


AO_NAME = "newAO.py"
AOTOP_NAME = f"""{CONFIGDIR}AOTOP.py"""
BIN04 = lambda X: f"""{X:04b}"""
BIN08 = lambda X: f"""{X:08b}"""
BIN16 = lambda X: f"""{X:016b}"""
BIN32 = lambda X: f"""{X:032b}"""
BIN64 = lambda X: f"""{X:064b}"""
CF_NAME = "newCF.py"
CFTOP_NAME = f"""{CONFIGDIR}CFTOP.py"""
CLRALL = f"""{ESC}[2J"""
CLRDOWN = f"""{ESC}[J"""
CLREOL = f"""{ESC}[K"""
CMNTLINE = f"""# * {"#*" * (CMNTLEN // 2)}"""
DBSQLT_NAME = "newDBSQLT.py"
DICTMODE_KEYSTR = "DICTMODE_KEYSTR"  # define dictmode 'key':val
DICTMODE_KEYVAL = "DICTMODE_KEYVAL"  # define dictmode key:val
DOHBIBTM_NAME = f"""{CONFIGDIR}DO_HBIBTM.py"""
DOHBI_NAME = "newDOHBI.py"
DOHBITOP_NAME = f"""{CONFIGDIR}DO_HBITOP.py"""
DO_NAME = "newDO.py"
DOTOP_NAME = f"""{CONFIGDIR}DOTOP.py"""
EEOL = f"""{ESC}[K"""
EMPTY_DICT = {}
EMPTY_LIST = []
EMPTY_STR = ""
EMPTYSTRLST = [None, "", DBLQT, f"""{DBLQT}{DBLQT}""", SGLQT, f"""{SGLQT}{SGLQT}""", BKQT, "None", "\r", NEWLINE, "\r\n", "\n\r", ]
EMPTY_TUPLE = ()
FM_NAME = "newFM.py"
FMTOP_NAME = f"""{CONFIGDIR}FMTOP.py"""
FOLD1ENDHERE = f"""# fold here {"⥣1" * (FOLDLEN // 2)}"""
FOLD1ENDHERELN = f"""# fold here {"⥣1" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD1STARTHERE = f"""# fold here {"⥥1" * (FOLDLEN // 2)}"""
FOLD1STARTHERELN = f"""# fold here {"⥥1" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD2ENDHERE = f"""# fold here {"⥣2" * (FOLDLEN // 2)}"""
FOLD2ENDHERELN = f"""# fold here {"⥣2" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD2STARTHERE = f"""# fold here {"⥥2" * (FOLDLEN // 2)}"""
FOLD2STARTHERELN = f"""# fold here {"⥥2" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD3ENDHERE = f"""# fold here {"⥣3" * (FOLDLEN // 2)}"""
FOLD3ENDHERELN = f"""# fold here {"⥣3" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD3STARTHERE = f"""# fold here {"⥥3" * (FOLDLEN // 2)}"""
FOLD3STARTHERELN = f"""# fold here {"⥥3" * (FOLDLEN // 2)}{NEWLINE}"""
FO_NAME = "newFO.py"
FOTOP_NAME = f"""{CONFIGDIR}FOTOP.py"""
HEX08 = lambda X_: f"""{X_:02H}"""  # {thisComment_}
HEX16 = lambda X_: f"""{X_:04H}"""  # {thisComment_}
HEX32 = lambda X_: f"""{X_:08H}"""  # {thisComment_}
HEX64 = lambda X_: f"""{X_:016H}"""  # {thisComment_}
IMPORTANTSTR = f"""# * {"!-" * (CMNTLEN // 2)}"""  # important line marker
INDENTIN = " -=> "  # display arrow RIGHT
INDENTOUT = " <=- "  # display arrow LEFT
INFOSTR = f"""# * {"%_" * (CMNTLEN // 2)}"""  # INFO _STR_ line
IO_NAME = "newIO.py"
IOTOP_NAME = f"""{CONFIGDIR}IOTOP.py"""
LINESUP = lambda NUM_: f"""{ESC}[{NUM_}A"""
MARK1END = lambda TAG_: f"""# {"⥣1 " * (CMNTLEN // 3)} {TAG_}"""
MARK1ENDLN = lambda TAG_: f"""# {"⥣1 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK1MID = lambda TAG_: f"""# {"⥣1⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK1MIDLN = lambda TAG_: f"""# {"⥣1⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK1START = lambda TAG_: f"""# {"1⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK1STARTLN = lambda TAG_: f"""# {"1⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK2END = lambda TAG_: f"""# {"⥣2 " * (CMNTLEN // 3)} {TAG_}"""
MARK2ENDLN = lambda TAG_: f"""# {"⥣2 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK2MID = lambda TAG_: f"""# {"⥣2⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK2MIDLN = lambda TAG_: f"""# {"⥣2⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK2START = lambda TAG_: f"""# {"2⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK2STARTLN = lambda TAG_: f"""# {"2⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK3END = lambda TAG_: f"""# {"⥣3 " * (CMNTLEN // 3)} {TAG_}"""
MARK3ENDLN = lambda TAG_: f"""# {"⥣3 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK3MID = lambda TAG_: f"""# {"⥣3⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK3MIDLN = lambda TAG_: f"""# {"⥣3⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK3START = lambda TAG_: f"""# {"3⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK3STARTLN = lambda TAG_: f"""# {"3⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK4END = lambda TAG_: f"""# {"⥣4 " * (CMNTLEN // 3)} {TAG_}"""
MARK4ENDLN = lambda TAG_: f"""# {"⥣4 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK4MID = lambda TAG_: f"""# {"⥣4⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK4MIDLN = lambda TAG_: f"""# {"⥣4⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK4START = lambda TAG_: f"""# {"4⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK4STARTLN = lambda TAG_: f"""# {"4⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK5END = lambda TAG_: f"""# {"⥣5 " * (CMNTLEN // 3)} {TAG_}"""
MARK5ENDLN = lambda TAG_: f"""# {"⥣5 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK5MID = lambda TAG_: f"""# {"⥣5⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK5MIDLN = lambda TAG_: f"""# {"⥣5⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK5START = lambda TAG_: f"""# {"5⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK5STARTLN = lambda TAG_: f"""# {"5⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK6END = lambda TAG_: f"""# {"⥣6 " * (CMNTLEN // 3)} {TAG_}"""
MARK6ENDLN = lambda TAG_: f"""# {"⥣6 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK6MID = lambda TAG_: f"""# {"⥣6⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK6MIDLN = lambda TAG_: f"""# {"⥣6⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK6START = lambda TAG_: f"""# {"6⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK6STARTLN = lambda TAG_: f"""# {"6⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK7END = lambda TAG_: f"""# {"⥣7 " * (CMNTLEN // 3)} {TAG_}"""
MARK7ENDLN = lambda TAG_: f"""# {"⥣7 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK7MID = lambda TAG_: f"""# {"⥣7⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK7MIDLN = lambda TAG_: f"""# {"⥣7⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK7START = lambda TAG_: f"""# {"7⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK7STARTLN = lambda TAG_: f"""# {"7⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK8END = lambda TAG_: f"""# {"⥣8 " * (CMNTLEN // 3)} {TAG_}"""
MARK8ENDLN = lambda TAG_: f"""# {"⥣8 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK8MID = lambda TAG_: f"""# {"⥣8⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK8MIDLN = lambda TAG_: f"""# {"⥣8⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK8START = lambda TAG_: f"""# {"8⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK8STARTLN = lambda TAG_: f"""# {"8⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK9END = lambda TAG_: f"""# {"⥣9 " * (CMNTLEN // 3)} {TAG_}"""
MARK9ENDLN = lambda TAG_: f"""# {"⥣9 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK9MID = lambda TAG_: f"""# {"⥣9⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK9MIDLN = lambda TAG_: f"""# {"⥣9⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK9START = lambda TAG_: f"""# {"9⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK9STARTLN = lambda TAG_: f"""# {"9⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARKLINES_NAME = f"""{CONFIGDIR}MARKLINES.py"""
MOVELEFT = lambda NUM_: f"""{ESC}[{NUM_}D"""
MOVETO = lambda LN_, COL_: f"""{ESC}[{LN_};{COL_}H"""
NSPC = lambda NUM_: f"""{SPCSTR * NUM_}"""  # returns a string with NUM_ SPC
NTAB = lambda NUM_: f"""{TABSTR * NUM_}"""  # returns a string with NUM_ TAB
PSG_NAME = f"""newPSG.py"""
PSGTOP_NAME = f"""{CONFIGDIR}PSGTOP.py"""
QTSET = [DBLQT, SGLQT, BKQT]  # set of all quote characters
SCTN0102NAME = f"""{CONFIGDIR}SCTN0102.py"""
SCTNSNAME = f"""{CONFIGDIR}SCTNS.md"""
SP_NAME = "newSP.py"
SPTOP_NAME = f"""{CONFIGDIR}SPTOP.py"""
TBGLST_NAME = "TBGLST.py"
VO_NAME = "newVO.py"
VOTOP_NAME = f"""{CONFIGDIR}VOTOP.py"""
WHIRLSTR = f"""-{BKSLSH}|/*"""
WHIRLCOUNT = 0


CODES2STRIP = [  # {'CODES2STRIP': "dict holding all of the things to strip from 'text' strings like color codes"}
	f"{ESC}[0m",  # entry for ESC-[0m
	f"{ESC}[1m",  # entry for ESC-[1m
	f"{ESC}[32m",  # entry for ESC-[32m
	f"{ESC}[35m",  # entry for ESC-[35m
	f"{ESC}[36m",  # entry for ESC-[36m
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN003 TYPEs and lambda
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN101 FMAX _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMAX_NOP = "FMAX_NOP"  # skip this entry
FMAXCF_SCTN0003_LAMBDA_DEF = "FMAXCF_SCTN0003_LAMBDA_DEF"  # define a lambda function <NAC><NAME><lambda str>
FMAXCF_SCTN0003_TYPE_DEF = "FMAXCF_SCTN0003_TYPE_DEF"  # define a fake type used in the translation dict <NAC><NAME><TYPE>
FMAXCF_SCTN0201_STR_DEF = "FMAXCF_SCTN0201_STR_DEF"  # define a STR in SCTN21 <NAC><NAME><str>
FMAXCF_SCTN0201_VAL_DEF = "FMAXCF_SCTN0201_VAL_DEF"  # define a VAL in SCTN21 <NAC><NAME><VAL>
FMAXCF_SCTN0202_OPTIONS_ADD_HELP_LINE = "FMAXCF_SCTN0202_OPTIONS_ADD_HELP_LINE"  # add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>
FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD = "FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD"  # define a OPTNAME: 'str' in SCTN202 <NAC><KEY><PARM><STRDEFAULT>
FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD = "FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD"  # define a OPTNAME: VAL in SCTN202 <NAC><KEY><PARM><VALDEFAULT>
FMAXCF_SCTN0202_OPTIONS_STR_ADD = "FMAXCF_SCTN0202_OPTIONS_STR_ADD"  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
FMAXCF_SCTN0202_OPTIONS_VAL_ADD = "FMAXCF_SCTN0202_OPTIONS_VAL_ADD"  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
FMAXCF_SCTN0203_DICT_DEF = "FMAXCF_SCTN0203_DICT_DEF"  # define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>
FMAXCF_SCTN0203_DICT_STR_ADD = "FMAXCF_SCTN0203_DICT_STR_ADD"  # define a dict STR in SCTN203 <NAC><DICTNAME><STR>
FMAXCF_SCTN0203_DICT_VAL_ADD = "FMAXCF_SCTN0203_DICT_VAL_ADD"  # define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>
FMAXCF_SCTN0204_LIST_DEF = "FMAXCF_SCTN0204_LIST_DEF"  # define a list in SCTN204 <NAC><LISTNAME>
FMAXCF_SCTN0204_LIST_STR_ADD = "FMAXCF_SCTN0204_LIST_STR_ADD"  # define a list STR in SCTN204 <NAC><LISTNAME><STR>
FMAXCF_SCTN0204_LIST_VAL_ADD = "FMAXCF_SCTN0204_LIST_VAL_ADD"  # define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>
FMAXFM_SCTN0101_AX_DEF = "FMAXFM_SCTN0101_AX_DEF"  # define a new FM action <NAC>
FMAXFM_SCTN0102_STR_DEF = "FMAXFM_SCTN0102_STR_DEF"  # define a FM string <NAC><VALNAME><STR>
FMAXFM_SCTN0102_VAL_DEF = "FMAXFM_SCTN0102_VAL_DEF"  # define a FM value_ <NAC><VALNAME><VAL>
FMAXFM_SCTN0103_DICT_DEF = "FMAXFM_SCTN0103_DICT_DEF"  # define a dict for FM <NAC>
FMAXFM_SCTN0104_LIST_DEF = "FMAXFM_SCTN0104_LIST_DEF"  # define a list in FM <NAC>
FMAXPSG_SCTN0900_STR_DEF = "FMAXPSG_SCTN0900_STR_DEF"  # define a string in the first section (colors, etc.) of defines in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0900_VAL_DEF = "FMAXPSG_SCTN0900_VAL_DEF"  # define a value in the first define section in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0901_DUBLTSSDEF = "FMAXPSG_SCTN0901_DUBLTSSDEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0901_DUBLTSVDEF = "FMAXPSG_SCTN0901_DUBLTSVDEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0901_DUBLTVSDEF = "FMAXPSG_SCTN0901_DUBLTVSDEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0901_DUBLTVVDEF = "FMAXPSG_SCTN0901_DUBLTVVDEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0901_KEY_DEF = "FMAXPSG_SCTN0901_KEY_DEF"  # define a key in the second section of defines in PSG.py <NAC><VALNAME>
FMAXPSG_SCTN0901_STR_DEF = "FMAXPSG_SCTN0901_STR_DEF"  # define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0901_VAL_DEF = "FMAXPSG_SCTN0901_VAL_DEF"  # define a value in the second define section in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0902_DICT_DEF = "FMAXPSG_SCTN0902_DICT_DEF"  # define a dict in PSG <NAC><DICTNAME>
FMAXPSG_SCTN0902_DICT_STR_ADD = "FMAXPSG_SCTN0902_DICT_STR_ADD"  # add a str to a dict <NAC><DICTNAME><KEY><VAL>
FMAXPSG_SCTN0902_DICT_STRSTR_ADD = "FMAXPSG_SCTN0902_DICT_STRSTR_ADD"  # add a str-str to a dict <NAC><DICTNAME><STR><STR>
FMAXPSG_SCTN0902_DICT_STRVAL_ADD = "FMAXPSG_SCTN0902_DICT_STRVAL_ADD"  # add a str-val to a dict <NAC><DICTNAME><STR><VAL>
FMAXPSG_SCTN0902_DICT_VAL_ADD = "FMAXPSG_SCTN0902_DICT_VAL_ADD"  # add a val to a dict in PSG <NAC><DICTNAME><KEY><VAL>
FMAXPSG_SCTN0903_LISTDEF = "FMAXPSG_SCTN0903_LISTDEF"  # define a list in PSG <NAC><LISTNAME>
FMAXPSG_SCTN0903_LISTSTRADD = "FMAXPSG_SCTN0903_LISTSTRADD"  # add a str to a list in PSG <NAC><LISTNAME><STR>
FMAXPSG_SCTN0903_LISTVALADD = "FMAXPSG_SCTN0903_LISTVALADD"  # add a val to a list in PSG <NAC><LISTNAME><VAL>
FMAXPSG_SCTN0904_PLATEQELIFADD = "FMAXPSG_SCTN0904_PLATEQELIFADD"  # platform equalizer define an elif <NAC><STRUCTNAME><CONDITION><VAL>
FMAXPSG_SCTN0904_PLATEQELSEADD = "FMAXPSG_SCTN0904_PLATEQELSEADD"  # platform equalizer define an else <NAC><STRUCTNAME><CONDITION>
FMAXPSG_SCTN0904_PLATEQFUNCSTRADD = "FMAXPSG_SCTN0904_PLATEQFUNCSTRADD"  # add a function string line <NAC><STRUCTNAME><CONDITION>
FMAXPSG_SCTN0904_PLATEQIFADD = "FMAXPSG_SCTN0904_PLATEQIFADD"  # add the 1st if to a platform equalizer <NAC><STRUCTNAME><CONDITION>
FMAXPSG_SCTN0904_PLATEQPLATDEF = "FMAXPSG_SCTN0904_PLATEQPLATDEF"  # define a platform equalizer struct <NAC><STRUCTNAME>
FMAXPSG_SCTN0904_PLATEQSTRADD = "FMAXPSG_SCTN0904_PLATEQSTRADD"  # add a string to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>
FMAXPSG_SCTN0904_PLATEQVALADD = "FMAXPSG_SCTN0904_PLATEQVALADD"  # add a value to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>
FMAXPSG_SCTN0905_TUPDICTDEF = "FMAXPSG_SCTN0905_TUPDICTDEF"  # define a TUPDICT in the second define section in PSG.py <NAC><TUPDICTNAME>
FMAXPSG_SCTN0905_TUPDICTSTRADD = "FMAXPSG_SCTN0905_TUPDICTSTRADD"  # add a str to a tupdict <NAC><TUPDICTNAME><KEY><STR>
FMAXPSG_SCTN0905_TUPDICTSTRSTRADD = "FMAXPSG_SCTN0905_TUPDICTSTRSTRADD"  # add a str to a tupdict <NAC><TUPDICTNAME><STR><STR>
FMAXPSG_SCTN0905_TUPDICTSTRVALADD = "FMAXPSG_SCTN0905_TUPDICTSTRVALADD"  # add a value to a tupdict <NAC><TUPDICTNAME><STR><VAL>
FMAXPSG_SCTN0905_TUPDICTVALADD = "FMAXPSG_SCTN0905_TUPDICTVALADD"  # add a value to a tupdict <NAC><TUPDICTNAME><KEY><VAL>
FMAXPSG_SCTN0906_BTN_STRADD = "FMAXPSG_SCTN0906_BTN_STRADD"  # add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>
FMAXPSG_SCTN0906_BTN_TUPVALVALADD = "FMAXPSG_SCTN0906_BTN_TUPVALVALADD"  # add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL1><VAL2>
FMAXPSG_SCTN0906_BTN_VALADD = "FMAXPSG_SCTN0906_BTN_VALADD"  # add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>
FMAXPSG_SCTN0906_BTNDEF = "FMAXPSG_SCTN0906_BTNDEF"  # define a button <NAC><BTNNAME>
FMAXPSG_SCTN0907_SPIN_DICTSTRADD = "FMAXPSG_SCTN0907_SPIN_DICTSTRADD"  # add a VAL to the SPINDICT <NAC><SPINNAME><KEY><VAL>
FMAXPSG_SCTN0907_SPIN_DICTTUPVALVALADD = "FMAXPSG_SCTN0907_SPIN_DICTTUPVALVALADD"  # add a (VAL1, VAL2) to the SPINDICT <NAC><SPINNAME><KEY><VAL1><VAL2>
FMAXPSG_SCTN0907_SPIN_VALUESSTRADD = "FMAXPSG_SCTN0907_SPIN_VALUESSTRADD"  # add a STR to the values list <NAC><SPINNAME><STR>
FMAXPSG_SCTN0907_SPIN_VALUESVALADD = "FMAXPSG_SCTN0907_SPIN_VALUESVALADD"  # add a VAL to the values list <NAC><SPINNAME><VAL>
FMAXPSG_SCTN0907_SPINDEF = "FMAXPSG_SCTN0907_SPINDEF"  # define a spin box entry <NAC><SPINNAME>
FMAXPSG_SCTN0908_CHECKBOXDEF = "FMAXPSG_SCTN0908_CHECKBOXDEF"  # define a checkbox <NAC><CHECKBOXNAME>
FMAXPSG_SCTN0909_TEXTDEF = "FMAXPSG_SCTN0909_TEXTDEF"  # define a text <NAC><TEXTNAME>
FMAXPSG_SCTN090A_COLUMNDEF = "FMAXPSG_SCTN090A_COLUMNDEF"  # define a column <NAC><COLUMNNAME>
FMAXPSG_SCTN090B_LAYOUTDEF = "FMAXPSG_SCTN090B_LAYOUTDEF"  # define a layout <NAC><LAYOUTNAME>
FMAXPSG_SCTN090C_WINDOWDEF = "FMAXPSG_SCTN090C_WINDOWDEF"  # define a window <NAC><WINDOWNAME>
FMAXPSG_SCTN090D_FRAMEDEF = "FMAXPSG_SCTN090D_FRAMEDEF"  # define a frame <NAC><FRAMENAME>
FMAXPSG_SCTN090E_MAINDICTDEF = "FMAXPSG_SCTN090E_MAINDICTDEF"  # define a main dictdict <NAC><MAINNAME>
FMAXPSG_SCTN090E_MAINDICTDICTDEF = "FMAXPSG_SCTN090E_MAINDICTDICTDEF"  # add a str to the main dictdict
FMAXPSG_SCTN090E_MAINDICTDICTSTRADD = "FMAXPSG_SCTN090E_MAINDICTDICTSTRADD"  # add a str to the main dictdict
FMAXPSG_SCTN090E_MAINDICTDICTVALADD = "FMAXPSG_SCTN090E_MAINDICTDICTVALADD"  # add a str to the main dictdict
FMAXPSG_SCTN090E_MAINDICTSTRADD = "FMAXPSG_SCTN090E_MAINDICTSTRADD"  # add a str to the main dictdict
FMAXPSG_SCTN090E_MAINDICTVALADD = "FMAXPSG_SCTN090E_MAINDICTVALADD"  # add a str to the main dictdict
FMPSG_SCTN0907_SPINCMNTDICT = "FMPSG_SCTN0907_SPINCMNTDICT"  # holds the spin element stufs (TUPDICT)f
FMPSG_SCTN0907_SPINDICT = "FMPSG_SCTN0907_SPINDICT"  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN0907_SPINVALUESLISTDICT = "FMPSG_SCTN0907_SPINVALUESLISTDICT"  # holds the spin element stuffs (TUPDICT)


FMAXFM_AXLST = [
	FMAX_NOP,  # skip this entry
	FMAXCF_SCTN0003_LAMBDA_DEF,  # define a lambda function <NAC><NAME><lambda str>
	FMAXCF_SCTN0003_TYPE_DEF,  # define a fake type used in the translation dict <NAC><NAME><TYPE>
	FMAXCF_SCTN0201_STR_DEF,  # define a STR in SCTN21 <NAC><NAME><str>
	FMAXCF_SCTN0201_VAL_DEF,  # define a VAL in SCTN21 <NAC><NAME><VAL>
	FMAXCF_SCTN0202_OPTIONS_ADD_HELP_LINE,  # add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>
	FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD,  # define a OPTNAME: 'str' in SCTN202 <NAC><KEY><PARM><STRDEFAULT>
	FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD,  # define a OPTNAME: VAL in SCTN202 <NAC><KEY><PARM><VALDEFAULT>
	FMAXCF_SCTN0202_OPTIONS_STR_ADD,  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
	FMAXCF_SCTN0202_OPTIONS_VAL_ADD,  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
	FMAXCF_SCTN0203_DICT_DEF,  # define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>
	FMAXCF_SCTN0203_DICT_STR_ADD,  # define a dict STR in SCTN203 <NAC><DICTNAME><STR>
	FMAXCF_SCTN0203_DICT_VAL_ADD,  # define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>
	FMAXCF_SCTN0204_LIST_DEF,  # define a list in SCTN204 <NAC><LISTNAME>
	FMAXCF_SCTN0204_LIST_STR_ADD,  # define a list STR in SCTN204 <NAC><LISTNAME><STR>
	FMAXCF_SCTN0204_LIST_VAL_ADD,  # define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>
	FMAXFM_SCTN0101_AX_DEF,  # define a new FM action <NAC>
	FMAXFM_SCTN0102_STR_DEF,  # define a FM string <NAC><VALNAME><STR>
	FMAXFM_SCTN0102_VAL_DEF,  # define a FM value_ <NAC><VALNAME><VAL>
	FMAXFM_SCTN0103_DICT_DEF,  # define a dict for FM <NAC>
	FMAXFM_SCTN0104_LIST_DEF,  # define a list in FM <NAC>
	FMAXPSG_SCTN0900_STR_DEF,  # define a string in the first section (colors, etc.) of defines in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0900_VAL_DEF,  # define a value in the first define section in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0901_DUBLTSSDEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0901_DUBLTSVDEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0901_DUBLTVSDEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0901_DUBLTVVDEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0901_KEY_DEF,  # define a key in the second section of defines in PSG.py <NAC><VALNAME>
	FMAXPSG_SCTN0901_STR_DEF,  # define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0901_VAL_DEF,  # define a value in the second define section in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0902_DICT_DEF,  # define a dict in PSG <NAC><DICTNAME>
	FMAXPSG_SCTN0902_DICT_STR_ADD,  # add a str to a dict <NAC><DICTNAME><KEY><VAL>
	FMAXPSG_SCTN0902_DICT_STRSTR_ADD,  # add a str-str to a dict <NAC><DICTNAME><STR><STR>
	FMAXPSG_SCTN0902_DICT_STRVAL_ADD,  # add a str-val to a dict <NAC><DICTNAME><STR><VAL>
	FMAXPSG_SCTN0902_DICT_VAL_ADD,  # add a val to a dict in PSG <NAC><DICTNAME><KEY><VAL>
	FMAXPSG_SCTN0903_LISTDEF,  # define a list in PSG <NAC><LISTNAME>
	FMAXPSG_SCTN0903_LISTSTRADD,  # add a str to a list in PSG <NAC><LISTNAME><STR>
	FMAXPSG_SCTN0903_LISTVALADD,  # add a val to a list in PSG <NAC><LISTNAME><VAL>
	FMAXPSG_SCTN0904_PLATEQELIFADD,  # platform equalizer define an elif <NAC><STRUCTNAME><CONDITION><VAL>
	FMAXPSG_SCTN0904_PLATEQELSEADD,  # platform equalizer define an else <NAC><STRUCTNAME><CONDITION>
	FMAXPSG_SCTN0904_PLATEQFUNCSTRADD,  # add a function string line <NAC><STRUCTNAME><CONDITION>
	FMAXPSG_SCTN0904_PLATEQIFADD,  # add the 1st if to a platform equalizer <NAC><STRUCTNAME><CONDITION>
	FMAXPSG_SCTN0904_PLATEQPLATDEF,  # define a platform equalizer struct <NAC><STRUCTNAME>
	FMAXPSG_SCTN0904_PLATEQSTRADD,  # add a string to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>
	FMAXPSG_SCTN0904_PLATEQVALADD,  # add a value to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>
	FMAXPSG_SCTN0905_TUPDICTDEF,  # define a TUPDICT in the second define section in PSG.py <NAC><TUPDICTNAME>
	FMAXPSG_SCTN0905_TUPDICTSTRADD,  # add a str to a tupdict <NAC><TUPDICTNAME><KEY><STR>
	FMAXPSG_SCTN0905_TUPDICTSTRSTRADD,  # add a str to a tupdict <NAC><TUPDICTNAME><STR><STR>
	FMAXPSG_SCTN0905_TUPDICTSTRVALADD,  # add a value to a tupdict <NAC><TUPDICTNAME><STR><VAL>
	FMAXPSG_SCTN0905_TUPDICTVALADD,  # add a value to a tupdict <NAC><TUPDICTNAME><KEY><VAL>
	FMAXPSG_SCTN0906_BTN_STRADD,  # add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>
	FMAXPSG_SCTN0906_BTN_TUPVALVALADD,  # add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL1><VAL2>
	FMAXPSG_SCTN0906_BTN_VALADD,  # add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>
	FMAXPSG_SCTN0906_BTNDEF,  # define a button <NAC><BTNNAME>
	FMAXPSG_SCTN0907_SPIN_DICTSTRADD,  # add a VAL to the SPINDICT <NAC><SPINNAME><KEY><VAL>
	FMAXPSG_SCTN0907_SPIN_DICTTUPVALVALADD,  # add a (VAL1, VAL2) to the SPINDICT <NAC><SPINNAME><KEY><VAL1><VAL2>
	FMAXPSG_SCTN0907_SPIN_VALUESSTRADD,  # add a STR to the values list <NAC><SPINNAME><STR>
	FMAXPSG_SCTN0907_SPIN_VALUESVALADD,  # add a VAL to the values list <NAC><SPINNAME><VAL>
	FMAXPSG_SCTN0907_SPINDEF,  # define a spin box entry <NAC><SPINNAME>
	FMAXPSG_SCTN0908_CHECKBOXDEF,  # define a checkbox <NAC><CHECKBOXNAME>
	FMAXPSG_SCTN0909_TEXTDEF,  # define a text <NAC><TEXTNAME>
	FMAXPSG_SCTN090A_COLUMNDEF,  # define a column <NAC><COLUMNNAME>
	FMAXPSG_SCTN090B_LAYOUTDEF,  # define a layout <NAC><LAYOUTNAME>
	FMAXPSG_SCTN090C_WINDOWDEF,  # define a window <NAC><WINDOWNAME>
	FMAXPSG_SCTN090D_FRAMEDEF,  # define a frame <NAC><FRAMENAME>
	FMAXPSG_SCTN090E_MAINDICTDEF,  # define a main dictdict <NAC><MAINNAME>
	FMAXPSG_SCTN090E_MAINDICTDICTDEF,  # add a str to the main dictdict
	FMAXPSG_SCTN090E_MAINDICTDICTSTRADD,  # add a str to the main dictdict
	FMAXPSG_SCTN090E_MAINDICTDICTVALADD,  # add a str to the main dictdict
	FMAXPSG_SCTN090E_MAINDICTSTRADD,  # add a str to the main dictdict
	FMAXPSG_SCTN090E_MAINDICTVALADD,  # add a str to the main dictdict
	FMPSG_SCTN0907_SPINCMNTDICT,  # holds the spin element stufs (TUPDICT)f
	FMPSG_SCTN0907_SPINDICT,  # holds the spin element stuffs (TUPDICT)
	FMPSG_SCTN0907_SPINVALUESLISTDICT,  # holds the spin element stuffs (TUPDICT)
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN102 VAL _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN103 _DICT_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMCF_SCTN0003_TYPECMNTDICT = {}  # SCTN009 types comments
FMCF_SCTN0003_TYPEDICT = {}  # SCTN003 types
FMCF_SCTN0201_DEFCMNTDICT = {}  # SCTN201 defines comments dict
FMCF_SCTN0201_DEFDICT = {}  # SCTN201 defines dict
FMCF_SCTN0202_OPTIONSCMNTDICT = {}  # SCTN202 OPTIONS comments dict
FMCF_SCTN0202_OPTIONSDICT = {}  # SCTN202 OPTIONS dict
FMCF_SCTN0202_OPTIONSDICTCMNTDICT = {}  # SCTN202 OPTIONSDICT comments dict
FMCF_SCTN0202_OPTIONSDICTDICT = {}  # SCTN202 OPTIONSDICT
FMCF_SCTN0202_OPTIONSHELPDICT = {}  # SCTN202 OPTIONS HELPDICT
FMCF_SCTN0203_DICTCMNTDICT = {}  # SCTN203 dict comments dict
FMCF_SCTN0203_DICTDICT = {}  # SCTN203 dict dict
FMCF_SCTN0204_LISTCMNTDICT = {}  # SCTN204 list comments dict
FMCF_SCTN0204_LISTDICT = {}  # SCTN204 list dict
FMFM_SCTN0101_AXCMNTDICT = {}  # SCTN101 FMAX defined
FMFM_SCTN0101_AXDICT = {}  # SCTN101 FMAX defined
FMFM_SCTN0102_VALCMNTDICT = {}  # SCTN102 val
FMFM_SCTN0102_VALDICT = {}  # SCTN102 val
FMFM_SCTN0103_DICTCMNTDICT = {}  # SCTN103 dict defined
FMFM_SCTN0103_DICTDICT = {}  # SCTN103 dict defined
FMFM_SCTN0104_LISTCMNTDICT = {}  # SCTN201 device defines
FMFM_SCTN0104_LISTDICT = {}  # SCTN201 device defines
FMPSG_SCTN0900_DEF1CMNTDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0900_DEF1DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0901_DEF2CMNTDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0901_DEF2DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0902_DICTCMNTDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0902_DICTDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0903_LISTCMNTDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0903_LISTDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0904_PLATEQINNERCMNTDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0904_PLATEQINNERDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0904_PLATEQOUTERCMNTDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0904_PLATEQOUTERDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0905_TUPDICTCMNTDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0905_TUPDICTDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0906_BTNSCMNTDICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN0906_BTNSDICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0908_CHECKBOXCMNTDICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0908_CHECKBOXDICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0909_TEXTCMNTDICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN0909_TEXTDICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090A_COLUMNSCMNTDICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN090A_COLUMNSDICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090B_LAYOUTCMNTDICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN090B_LAYOUTDICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090C_WINDOWCMNTDICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN090C_WINDOWDICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090D_FRAMECMNTDICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN090D_FRAMEDICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090E_MAINCMNTDICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN090E_MAINDICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090E_MAINDICTDICT = {}  # holds all of the button entriess (TUPDICT)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN104 _LIST_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed portions of FM.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of not managed portions of FM.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# START OF TBGLST SCTN0105
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!


TBGLST = [
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	("CFVAL", FMAX_NOP, "CFVAL_BEGINS",),
	("CFVAL_____", FMAX_NOP, "CFVAL_ENDS",),
	("FMAXCF", FMAX_NOP, "FMAXCF_BEGINS",),
	("FMAXCF_SCTN0003_LAMBDA_DEF", FMAXFM_SCTN0101_AX_DEF, "define a lambda function <NAC><NAME><lambda str>",),
	("FMAXCF_SCTN0003_TYPE_DEF", FMAXFM_SCTN0101_AX_DEF, "define a fake type used in the translation dict <NAC><NAME><TYPE>",),
	("FMAXCF_SCTN0201_STR_DEF", FMAXFM_SCTN0101_AX_DEF, "define a STR in SCTN21 <NAC><NAME><str>",),
	("FMAXCF_SCTN0201_VAL_DEF", FMAXFM_SCTN0101_AX_DEF, "define a VAL in SCTN21 <NAC><NAME><VAL>",),
	("FMAXCF_SCTN0202_OPTIONS_ADD_HELP_LINE", FMAXFM_SCTN0101_AX_DEF, "add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>",),
	("FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "define a OPTNAME: 'str' in SCTN202 <NAC><KEY><PARM><STRDEFAULT>",),
	("FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a OPTNAME: VAL in SCTN202 <NAC><KEY><PARM><VALDEFAULT>",),
	("FMAXCF_SCTN0202_OPTIONS_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>",),
	("FMAXCF_SCTN0202_OPTIONS_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>",),
	("FMAXCF_SCTN0203_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>",),
	("FMAXCF_SCTN0203_DICT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "define a dict STR in SCTN203 <NAC><DICTNAME><STR>",),
	("FMAXCF_SCTN0203_DICT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>",),
	("FMAXCF_SCTN0204_LIST_DEF", FMAXFM_SCTN0101_AX_DEF, "define a list in SCTN204 <NAC><LISTNAME>",),
	("FMAXCF_SCTN0204_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "define a list STR in SCTN204 <NAC><LISTNAME><STR>",),
	("FMAXCF_SCTN0204_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>",),
	("FMAXCF_____", FMAX_NOP, "FMAXCF_ENDS",),
	("FMAXFM", FMAX_NOP, "FMAXFM_BEGINS",),
	("FMAXFM_SCTN0101_AX_DEF", FMAXFM_SCTN0101_AX_DEF, "define a new FM action <NAC>",),
	("FMAXFM_SCTN0102_STR_DEF", FMAXFM_SCTN0101_AX_DEF, "define a FM string <NAC><VALNAME><STR>",),
	("FMAXFM_SCTN0102_VAL_DEF", FMAXFM_SCTN0101_AX_DEF, "define a FM value_ <NAC><VALNAME><VAL>",),
	("FMAXFM_SCTN0103_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a dict for FM <NAC>",),
	("FMAXFM_SCTN0104_LIST_DEF", FMAXFM_SCTN0101_AX_DEF, "define a list in FM <NAC>",),
	("FMAXFM_____", FMAX_NOP, "FMAXFM_ENDS",),
	("FMAXPSG", FMAX_NOP, "FMAXPSG_BEGINS",),
	("FMAXPSG_SCTN0900_STR_DEF", FMAXFM_SCTN0101_AX_DEF, "define a string in the first section (colors, etc.) of defines in PSG.py <NAC><VALNAME><VAL>",),
	("FMAXPSG_SCTN0900_VAL_DEF", FMAXFM_SCTN0101_AX_DEF, "define a value in the first define section in PSG.py <NAC><VALNAME><VAL>",),
	("FMAXPSG_SCTN0901_DUBLT_SS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>",),
	("FMAXPSG_SCTN0901_DUBLT_SV_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>",),
	("FMAXPSG_SCTN0901_DUBLT_VS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>",),
	("FMAXPSG_SCTN0901_DUBLT_VV_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>",),
	("FMAXPSG_SCTN0901_KEY_DEF", FMAXFM_SCTN0101_AX_DEF, "define a key in the second section of defines in PSG.py <NAC><VALNAME>",),
	("FMAXPSG_SCTN0901_STR_DEF", FMAXFM_SCTN0101_AX_DEF, "define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>",),
	("FMAXPSG_SCTN0901_VAL_DEF", FMAXFM_SCTN0101_AX_DEF, "define a value in the second define section in PSG.py <NAC><VALNAME><VAL>",),
	("FMAXPSG_SCTN0902_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a dict in PSG <NAC><DICTNAME>",),
	("FMAXPSG_SCTN0902_DICT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a dict <NAC><DICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0902_DICT_STRSTR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str-str to a dict <NAC><DICTNAME><STR><STR>",),
	("FMAXPSG_SCTN0902_DICT_STRVAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str-val to a dict <NAC><DICTNAME><STR><VAL>",),
	("FMAXPSG_SCTN0902_DICT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a dict in PSG <NAC><DICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0903_LISTDEF", FMAXFM_SCTN0101_AX_DEF, "define a list in PSG <NAC><LISTNAME>",),
	("FMAXPSG_SCTN0903_LISTSTRADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a list in PSG <NAC><LISTNAME><STR>",),
	("FMAXPSG_SCTN0903_LISTVALADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a list in PSG <NAC><LISTNAME><VAL>",),
	("FMAXPSG_SCTN0904_PLATEQELIFADD", FMAXFM_SCTN0101_AX_DEF, "platform equalizer define an elif <NAC><STRUCTNAME><CONDITION><VAL>",),
	("FMAXPSG_SCTN0904_PLATEQELSEADD", FMAXFM_SCTN0101_AX_DEF, "platform equalizer define an else <NAC><STRUCTNAME><CONDITION>",),
	("FMAXPSG_SCTN0904_PLATEQFUNCSTRADD", FMAXFM_SCTN0101_AX_DEF, "add a function string line <NAC><STRUCTNAME><CONDITION>",),
	("FMAXPSG_SCTN0904_PLATEQIFADD", FMAXFM_SCTN0101_AX_DEF, "add the 1st if to a platform equalizer <NAC><STRUCTNAME><CONDITION>",),
	("FMAXPSG_SCTN0904_PLATEQPLATDEF", FMAXFM_SCTN0101_AX_DEF, "define a platform equalizer struct <NAC><STRUCTNAME>",),
	("FMAXPSG_SCTN0904_PLATEQSTRADD", FMAXFM_SCTN0101_AX_DEF, "add a string to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN0904_PLATEQVALADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN0905_TUPDICTDEF", FMAXFM_SCTN0101_AX_DEF, "define a TUPDICT in the second define section in PSG.py <NAC><TUPDICTNAME>",),
	("FMAXPSG_SCTN0905_TUPDICTSTRADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a tupdict <NAC><TUPDICTNAME><KEY><STR>",),
	("FMAXPSG_SCTN0905_TUPDICTSTRSTRADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a tupdict <NAC><TUPDICTNAME><STR><STR>",),
	("FMAXPSG_SCTN0905_TUPDICTSTRVALADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a tupdict <NAC><TUPDICTNAME><STR><VAL>",),
	("FMAXPSG_SCTN0905_TUPDICTVALADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a tupdict <NAC><TUPDICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0906_BTNDEF", FMAXFM_SCTN0101_AX_DEF, "define a button <NAC><BTNNAME>",),
	("FMAXPSG_SCTN0906_BTN_STRADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0906_BTN_TUPVALVALADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL1><VAL2>",),
	("FMAXPSG_SCTN0906_BTN_VALADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0907_SPINDEF", FMAXFM_SCTN0101_AX_DEF, "define a spin box entry <NAC><SPINNAME>",),
	("FMAXPSG_SCTN0907_SPIN_DICTSTRADD", FMAXFM_SCTN0101_AX_DEF, "add a STR to the SPINDICT <NAC><SPINNAME><KEY><STR>",),
	("FMAXPSG_SCTN0907_SPIN_DICTSTRADD", FMAXFM_SCTN0101_AX_DEF, "add a VAL to the SPINDICT <NAC><SPINNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0907_SPIN_VALUESSTRADD", FMAXFM_SCTN0101_AX_DEF, "add a STR to the values list <NAC><SPINNAME><STR>",),
	("FMAXPSG_SCTN0907_SPIN_VALUESVALADD", FMAXFM_SCTN0101_AX_DEF, "add a VAL to the values list <NAC><SPINNAME><VAL>",),
	("FMAXPSG_SCTN0908_CHECKBOXDEF", FMAXFM_SCTN0101_AX_DEF, "define a checkbox <NAC><CHECKBOXNAME>",),
	("FMAXPSG_SCTN0908_CHECKBOXSTRADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a checkbox <NAC><CHECKBOXNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0908_CHECKBOXVALADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a checkbox <NAC><CHECKBOXNAME><KEY><VAL>",),

	("FMAXPSG_SCTN0909_TEXTDEF", FMAXFM_SCTN0101_AX_DEF, "define a text <NAC><TEXTNAME>",),
	("FMAXPSG_SCTN0909_TEXTSTRADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a text element <NAC><TEXTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0909_TEXTVALADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a text element <NAC><TEXTNAME>",),
	("FMAXPSG_SCTN090A_COLUMNDEF", FMAXFM_SCTN0101_AX_DEF, "define a column <NAC><COLUMNNAME>",),
	("FMAXPSG_SCTN090B_LAYOUTDEF", FMAXFM_SCTN0101_AX_DEF, "define a layout <NAC><LAYOUTNAME>",),
	("FMAXPSG_SCTN090C_WINDOWDEF", FMAXFM_SCTN0101_AX_DEF, "define a window <NAC><WINDOWNAME>",),
	("FMAXPSG_SCTN090D_FRAMEDEF", FMAXFM_SCTN0101_AX_DEF, "define a frame <NAC><FRAMENAME>",),
	("FMAXPSG_SCTN090E_MAINDICTDEF", FMAXFM_SCTN0101_AX_DEF, "define a main dictdict <NAC><MAINNAME>",),
	("FMAXPSG_SCTN090E_MAINDICTDICTDEF", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),
	("FMAXPSG_SCTN090E_MAINDICTDICTSTRADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),
	("FMAXPSG_SCTN090E_MAINDICTDICTVALADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),
	("FMAXPSG_SCTN090E_MAINDICTSTRADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),
	("FMAXPSG_SCTN090E_MAINDICTVALADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),
	("FMAXPSG_____", FMAX_NOP, "FMAXPSG_ENDS",),
	("FMAX_NOP", FMAXFM_SCTN0101_AX_DEF, "skip this entry",),
	("FMCF", FMAX_NOP, "FMCF_BEGINS",),
	("FMCF_SCTN0003_TYPECMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN009 types comments",),
	("FMCF_SCTN0003_TYPEDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN003 types",),
	("FMCF_SCTN0201_DEFCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN201 defines comments dict",),
	("FMCF_SCTN0201_DEFDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN201 defines dict",),
	("FMCF_SCTN0202_OPTIONSCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN202 OPTIONS comments dict",),
	("FMCF_SCTN0202_OPTIONSDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN202 OPTIONS dict",),
	("FMCF_SCTN0202_OPTIONSDICTCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN202 OPTIONSDICT comments dict",),
	("FMCF_SCTN0202_OPTIONSDICTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN202 OPTIONSDICT",),
	("FMCF_SCTN0202_OPTIONSHELPDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN202 OPTIONS HELPDICT",),
	("FMCF_SCTN0203_DICTCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN203 dict comments dict",),
	("FMCF_SCTN0203_DICTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN203 dict dict",),
	("FMCF_SCTN0204_LISTCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN204 list comments dict",),
	("FMCF_SCTN0204_LISTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN204 list dict",),
	("FMCF_____", FMAX_NOP, "FMCF_ENDS",),
	("FMFM", FMAX_NOP, "FMFM_BEGINS",),
	("FMFM_SCTN0101_AXCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN003 types",),
	("FMFM_SCTN0101_AXCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN101 FMAX defined",),
	("FMFM_SCTN0101_AXDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN101 FMAX defined",),
	("FMFM_SCTN0102_VALCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN102 val",),
	("FMFM_SCTN0102_VALDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN102 val",),
	("FMFM_SCTN0103_DICTCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN103 dict defined",),
	("FMFM_SCTN0103_DICTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN103 dict defined",),
	("FMFM_SCTN0104_LISTCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN201 device defines",),
	("FMFM_SCTN0104_LISTDICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN201 device defines",),
	("FMFM_____", FMAX_NOP, "FMFM_ENDS",),
	("FMPSG", FMAX_NOP, "FMPSG_BEGINS",),
	("FMPSG_SCTN0900_DEF1CMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0900_DEF1DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0901_DEF2CMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0901_DEF2DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0902_DICTCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0902_DICTDICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0903_LISTCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0903_LISTDICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0904_PLATEQINNERCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0904_PLATEQINNERDICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0904_PLATEQOUTERCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0904_PLATEQOUTERDICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0905_TUPDICTCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0905_TUPDICTDICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0906_BTNSCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN0906_BTNSDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0907_SPINCMNTDICT", FMAXFM_SCTN0101_AX_DEF, "holds the spin element stufs (TUPDICT)f",),
	("FMPSG_SCTN0907_SPINDICT", FMAXFM_SCTN0101_AX_DEF, "holds the spin element stuffs (TUPDICT)",),
	("FMPSG_SCTN0907_SPINVALUESLISTDICT", FMAXFM_SCTN0101_AX_DEF, "holds the spin element stuffs (TUPDICT)",),
	("FMPSG_SCTN0908_CHECKBOXCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0908_CHECKBOXDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0909_TEXTCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN0909_TEXTDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090A_COLUMNSCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN090A_COLUMNSDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090B_LAYOUTCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN090B_LAYOUTDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090C_WINDOWCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN090C_WINDOWDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090D_FRAMECMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN090D_FRAMEDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090E_MAINCMNTDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN090E_MAINDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090E_MAINDICTDICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_____", FMAX_NOP, "FMPSG_ENDS",),
	("PSGVAL", FMAX_NOP, "FMPSG_BEGINS",),
	("PSGVAL_COLOR_BACKGROUND", FMAXPSG_SCTN0900_STR_DEF, "BACKGROUNDCOLOR", "#331122", "the background of the main frames",),
	("PSGVAL_COLOR_BLACK", FMAXPSG_SCTN0900_STR_DEF, "BLACK", "#000000", "black",),
	("PSGVAL_COLOR_GRAY3", FMAXPSG_SCTN0900_STR_DEF, "GRAY3", "#333333", "gray 3",),
	("PSGVAL_COLOR_GRAY6", FMAXPSG_SCTN0900_STR_DEF, "GRAY6", "#666666", "gray 6",),
	("PSGVAL_COLOR_GRAY9", FMAXPSG_SCTN0900_STR_DEF, "GRAY9", "#999999", "gray 9",),
	("PSGVAL_COLOR_GRAYC", FMAXPSG_SCTN0900_STR_DEF, "GRAYC", "#CCCCCC", "gray C",),
	("PSGVAL_COLOR_NORMAL", FMAXPSG_SCTN0900_STR_DEF, "NORMALCOLOR", "#660044", "the color the clock digits are",),
	("PSGVAL_COLOR_NORMALHIGH", FMAXPSG_SCTN0900_STR_DEF, "NORMALHIGH", "#CC0088", "the highlight color used in blinking bits when they are 'lit'",),
	("PSGVAL_COLOR_NORMALLOW", FMAXPSG_SCTN0900_STR_DEF, "NORMALLOW", "#330022", "the color the clock digits are",),
	("PSGVAL_COLOR_WHITE", FMAXPSG_SCTN0900_STR_DEF, "WHITE", "#FFFFFF", "white",),
	("PSGVAL_EMPTY_ALARM", FMAXPSG_SCTN0905_TUPDICTDEF, "EMPTY_ALARM", "a normal alarm entry",),
	("PSGVAL_EMPTY_ALARM_DISMISSED", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_ALARM", "DISMISSED", "False", "bool is this event dismissed already",),
	("PSGVAL_EMPTY_ALARM_ENABLED", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_ALARM", "ENABLED", "True", "enabled state of this entry",),
	("PSGVAL_EMPTY_ALARM_EVENT_MODE", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_ALARM", "EVENT_MODE", "MODE_ALARM", "set the mode to MODE_ALARM by default of course",),
	("PSGVAL_EMPTY_ALARM_NAME", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_ALARM", "NAME", "", "name of this entry",),
	("PSGVAL_EMPTY_ALARM_PREDISMISSABLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_ALARM", "PREDISMISSABLE", "True", "pre-dismissable state of this entry",),
	("PSGVAL_EMPTY_ALARM_REMIND", FMAXPSG_SCTN0905_TUPDICTDEF, "EMPTY_ALARM_REMIND", "a normal alarm entry",),
	("PSGVAL_EMPTY_ALARM_REMIND_DISMISSED", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_ALARM_REMIND", "DISMISSED", "False", "bool is this event dismissed already",),
	("PSGVAL_EMPTY_ALARM_REMIND_ENABLED", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_ALARM_REMIND", "ENABLED", "True", "enabled state of this entry",),
	("PSGVAL_EMPTY_ALARM_REMIND_EVENT_MODE", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_ALARM_REMIND", "EVENT_MODE", "MODE_ALARMREMIND", "set the mode to MODE_ALARM by default of course",),
	("PSGVAL_EMPTY_ALARM_REMIND_NAME", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_ALARM_REMIND", "NAME", "", "name of this entry",),
	("PSGVAL_EMPTY_ALARM_REMIND_PREDISMISSABLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_ALARM_REMIND", "PREDISMISSABLE", "True", "pre-dismissable state of this entry",),
	("PSGVAL_EMPTY_ALARM_REMIND_SNOOZABLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_ALARM_REMIND", "SNOOZABLE", "False", "enabled state of this entry",),
	("PSGVAL_EMPTY_ALARM_REMIND_SNOOZED", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_ALARM_REMIND", "SNOOZED", "True", "enabled state of this entry",),
	("PSGVAL_EMPTY_ALARM_REMIND_TIME_ALARM", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_ALARM_REMIND", "TIME_ALARM", "00:00:00", "time this alarm is set for",),
	("PSGVAL_EMPTY_ALARM_REMIND_TIME_OF_NEXT_EVENT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_ALARM_REMIND", "TIME_OF_NEXT_EVENT", "00:00:00", "post snooze or tomorrow",),
	("PSGVAL_EMPTY_ALARM_REMIND_TIME_REMIND", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_ALARM_REMIND", "TIME_REMIND", "00:00:00", "time this alarm is set for",),
	("PSGVAL_EMPTY_ALARM_REMIND_TIME_TO_NEXT_EVENT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_ALARM_REMIND", "TIME_TO_NEXT_EVENT", "00:00:00", "post snooze or tomorrow",),
	("PSGVAL_EMPTY_ALARM_SNOOZABLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_ALARM", "SNOOZABLE", "False", "enabled state of this entry",),
	("PSGVAL_EMPTY_ALARM_SNOOZED", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_ALARM", "SNOOZED", "True", "enabled state of this entry",),
	("PSGVAL_EMPTY_ALARM_TIME_ALARM", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_ALARM", "TIME_ALARM", "00:00:00", "time this alarm is set for",),
	("PSGVAL_EMPTY_ALARM_TIME_OF_NEXT_EVENT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_ALARM", "TIME_OF_NEXT_EVENT", "00:00:00", "post snooze or tomorrow",),
	("PSGVAL_EMPTY_ALARM_TIME_TO_NEXT_EVENT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_ALARM", "TIME_TO_NEXT_EVENT", "00:00:00", "post snooze or tomorrow",),
	("PSGVAL_EMPTY_CLOCKS", FMAXPSG_SCTN0905_TUPDICTDEF, "EMPTY_CLOCKS", "just the clocks window",),
	("PSGVAL_EMPTY_CLOCKS_TIME_CLOCK", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_CLOCKS", "TIME_CLOCK", "00:00:00", "the main clock time",),
	("PSGVAL_EMPTY_CLOCKS_TIME_ELAPSED", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_CLOCKS", "TIME_ELAPSED", "00:00:00", "the main elapsed time",),
	("PSGVAL_EMPTY_CLOCKS_TIME_OF_NEXT_EVENT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_CLOCKS", "TIME_OF_NEXT_EVENT", "00:00:00", "the main count down to the next event time",),
	("PSGVAL_EMPTY_INTERVAL", FMAXPSG_SCTN0905_TUPDICTDEF, "EMPTY_INTERVAL", "a normal alarm entry",),
	("PSGVAL_EMPTY_INTERVAL_ENABLED", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_INTERVAL", "ENABLED", "True", "enabled state of this entry",),
	("PSGVAL_EMPTY_INTERVAL_EVENT_MODE", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_INTERVAL", "EVENT_MODE", "MODE_INTERVAL", "set the mode to MODE_ALARM by default of course",),
	("PSGVAL_EMPTY_INTERVAL_NAME", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_INTERVAL", "NAME", "", "name of this entry",),
	("PSGVAL_EMPTY_INTERVAL_RUNNING", FMAXPSG_SCTN0905_TUPDICTVALADD, "EMPTY_INTERVAL", "RUNNING", "True", "running state of this entry",),
	("PSGVAL_EMPTY_INTERVAL_TIME_INTERVAL", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_INTERVAL", "TIME_INTERVAL", "00:00:00", "time this alarm is set for",),
	("PSGVAL_EMPTY_INTERVAL_TIME_OF_NEXT_EVENT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_INTERVAL", "TIME_OF_NEXT_EVENT", "00:00:00", "post snooze or tomorrow",),
	("PSGVAL_EMPTY_INTERVAL_TIME_TO_NEXT_EVENT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "EMPTY_INTERVAL", "TIME_TO_NEXT_EVENT", "00:00:00", "post snooze or tomorrow",),
	("PSGVAL_EMPTY_MAIN", FMAXPSG_SCTN090E_MAINDICTDEF, "EMPTY_MAIN", "empty main form",),
	("PSGVAL_EMPTY_MAIN_AVOID_MOUSE", FMAXPSG_SCTN090E_MAINDICTVALADD, "EMPTY_MAIN", "AVOID_MOUSE", "True", "will the clock avoid the mouse or not bool",),
	("PSGVAL_EMPTY_MAIN_EVENT_ENTRIES", FMAXPSG_SCTN090E_MAINDICTDICTDEF, "EMPTY_MAIN", "EVENT_ENTRIES", "{}", "the events for this structure",),
	("PSGVAL_EMPTY_MAIN_INDEX_OF_NEXT_EVENT", FMAXPSG_SCTN090E_MAINDICTVALADD, "EMPTY_MAIN", "INDEX_OF_NEXT_EVENT", "0", "index of the next event in time",),
	("PSGVAL_EMPTY_MAIN_TIMECLOCK", FMAXPSG_SCTN090E_MAINDICTSTRADD, "EMPTY_MAIN", "TIMECLOCK", "00:00:00", "the big clock time, updated every time anything is done",),
	("PSGVAL_EMPTY_MAIN_TIME_ELAPSED", FMAXPSG_SCTN090E_MAINDICTSTRADD, "EMPTY_MAIN", "TIME_ELAPSED", "00:00:00", "time elapsed since app started 24 hour centric, consider 99h (4 1/8 days)",),
	("PSGVAL_EMPTY_MAIN_TIME_OF_NEXT_EVENT", FMAXPSG_SCTN090E_MAINDICTSTRADD, "EMPTY_MAIN", "TIME_OF_NEXT_EVENT", "00:00:00", "time of next event",),
	("PSGVAL_EMPTY_MAIN_TIME_TO_NEXT_EVENT", FMAXPSG_SCTN090E_MAINDICTSTRADD, "EMPTY_MAIN", "TIME_TO_NEXT_EVENT", "00:00:00", "time to next event counting down",),
	("PSGVAL_EMPTY_MAIN_TRANSPARENT_UNDER_MOUSE", FMAXPSG_SCTN090E_MAINDICTVALADD, "EMPTY_MAIN", "TRANSPARENT_UNDER_MOUSE", "True", "will the clock be transparent under the mouse (ineffective if mouse is avoided)",),
	("PSGVAL_FULL_BUTTON", FMAXPSG_SCTN0905_TUPDICTDEF, "FULL_BUTTON", "define the button empty tupdict",),
	("PSGVAL_FULL_BUTTON_AUTO_SIZE_BUTTON", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "AUTO_SIZE_BUTTON", "None", "if True the button size is sized to fit the text",),
	("PSGVAL_FULL_BUTTON_BIND_RETURN_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "BIND_RETURN_KEY", "False", "If True the return key will cause this button to be pressed",),
	("PSGVAL_FULL_BUTTON_BORDER_WIDTH", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "BORDER_WIDTH", "None", "width of border around button in pixels",),
	("PSGVAL_FULL_BUTTON_BUTTON_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "BUTTON_COLOR", "None", "Color of button. default is from theme or the window. Easy to remember which is which if you say 'ON' between colors. 'red' on 'green'. Normally a tuple, but can be a simplified-button-color-string 'foreground on background'. Can be a single color if want to set only the background.",),
	("PSGVAL_FULL_BUTTON_BUTTON_TEXT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "FULL_BUTTON", "BUTTON_TEXT", "", "str text to display on the button",),
	("PSGVAL_FULL_BUTTON_BUTTON_TYPE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "BUTTON_TYPE", "7", "You  should NOT be setting this directly. ONLY the shortcut functions set this",),
	("PSGVAL_FULL_BUTTON_CHANGE_SUBMITS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "CHANGE_SUBMITS", "False", "DO NOT USE. Only listed for backwards compat - Use enable_events instead",),
	("PSGVAL_FULL_BUTTON_DEFAULT_EXTENSION", FMAXPSG_SCTN0905_TUPDICTSTRADD, "FULL_BUTTON", "DEFAULT_EXTENSION", "", "If no extension entered by user, add this to filename (only used in saveas dialogs)",),
	("PSGVAL_FULL_BUTTON_DISABLED", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "DISABLED", "False", "If True button will be created disabled. If FULL_BUTTON_DISABLED_MEANS_IGNORE then the button will be ignored rather than disabled using tkinter",),
	("PSGVAL_FULL_BUTTON_DISABLED_BUTTON_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "DISABLED_BUTTON_COLOR", "None", "colors to use when button is disabled (text, background). Use None for a color if don't want to change. Only ttk buttons support both text and background colors. tk buttons only support changing text color",),
	("PSGVAL_FULL_BUTTON_ENABLE_EVENTS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "ENABLE_EVENTS", "False", "Turns on the element specific events. If this button is a target, should it generate an event when filled in",),
	("PSGVAL_FULL_BUTTON_FILE_TYPES", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "FILE_TYPES", "(('ALL FILES', '*.*'),)", "the filetypes that will be used to match files. To indicate all files: (('ALL Files', '*.*'),).  Note - NOT SUPPORTED ON MAC",),
	("PSGVAL_FULL_BUTTON_FOCUS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "FOCUS", "False", "if True, initial focus will be put on this button",),
	("PSGVAL_FULL_BUTTON_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_FULL_BUTTON_HIGHLIGHT_COLORS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "HIGHLIGHT_COLORS", "None", "colors to use when button has focus (highlight, background). None will use computed colors. Only used by Linux and only for non-TTK button",),
	("PSGVAL_FULL_BUTTON_IMAGE_DATA", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "IMAGE_DATA", "None", "Raw or Base64 representation of the image to put on button. Choose either filename or data",),
	("PSGVAL_FULL_BUTTON_IMAGE_FILENAME", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "IMAGE_FILENAME", "None", "image filename if there is a button image. GIFs and PNGs only.",),
	("PSGVAL_FULL_BUTTON_IMAGE_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "IMAGE_SIZE", "(None, None)", "Size of the image in pixels (width, height)",),
	("PSGVAL_FULL_BUTTON_IMAGE_SUBSAMPLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "IMAGE_SUBSAMPLE", "None", "amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc",),
	("PSGVAL_FULL_BUTTON_INITIAL_FOLDER", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "INITIAL_FOLDER", "None", "starting path for folders and files",),
	("PSGVAL_FULL_BUTTON_K", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "K", "None", "Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element",),
	("PSGVAL_FULL_BUTTON_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element",),
	("PSGVAL_FULL_BUTTON_METADATA", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_BUTTON_PAD", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "PAD", "None", "Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_BUTTON_RIGHT_CLICK_MENU", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "RIGHT_CLICK_MENU", "None", "A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.",),
	("PSGVAL_FULL_BUTTON_S", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "S", "(None, None)", "(width, height) of the button in characters wide, rows high",),
	("PSGVAL_FULL_BUTTON_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "SIZE", "(None, None)", "(width, height) of the button in characters wide, rows high",),
	("PSGVAL_FULL_BUTTON_TARGET", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "TARGET", "(None, None)", "str | Tuple[int, int] key or (row,col) target for the button. Note that -1 for column means 1 element to the left of this one. The constant ThisRow is used to indicate the current row. The Button itself is a valid target for some types of button",),
	("PSGVAL_FULL_BUTTON_TOOLTIP", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "TOOLTIP", "None", "text, that will appear when mouse hovers over the element",),
	("PSGVAL_FULL_BUTTON_USE_TTK_BUTTONS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "USE_TTK_BUTTONS", "None", "True = use ttk buttons. False = do not use ttk buttons.  None (Default) = use ttk buttons only if on a Mac and not with button images",),
	("PSGVAL_FULL_BUTTON_VISIBLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_BUTTON", "VISIBLE", "True", "set visibility state of the element",),
	("PSGVAL_FULL_CHECKBOX", FMAXPSG_SCTN0905_TUPDICTDEF, "FULL_CHECKBOX", "set a checkbox in motion",),
	("PSGVAL_FULL_CHECKBOX_AUTO_SIZE_TEXT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "AUTO_SIZE_TEXT", "None", "if True will size the element to match the length of the text",),
	("PSGVAL_FULL_CHECKBOX_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_FULL_CHECKBOX_CHANGE_SUBMITS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "CHANGE_SUBMITS", "False", "DO NOT USE. Only listed for backwards compat - Use enable_events instead",),
	("PSGVAL_FULL_CHECKBOX_CHECKBOX_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "CHECKBOX_COLOR", "None", "color of background of the box that has the check mark in it. The checkmark is the same color as the text",),
	("PSGVAL_FULL_CHECKBOX_DEFAULT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "DEFAULT", "False", "Set to True if you want this checkbox initially checked",),
	("PSGVAL_FULL_CHECKBOX_DISABLED", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "DISABLED", "False", "set disable state",),
	("PSGVAL_FULL_CHECKBOX_ENABLE_EVENTS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "ENABLE_EVENTS", "False", "Turns on the element specific events. Checkbox events happen when an item changes",),
	("PSGVAL_FULL_CHECKBOX_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_FULL_CHECKBOX_K", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "K", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_FULL_CHECKBOX_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_FULL_CHECKBOX_METADATA", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_CHECKBOX_PAD", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "PAD", "None", "Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_CHECKBOX_S", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "S", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_FULL_CHECKBOX_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "SIZE", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_FULL_CHECKBOX_TEXT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "FULL_CHECKBOX", "TEXT", "", "Text to display next to checkbox",),
	("PSGVAL_FULL_CHECKBOX_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_FULL_CHECKBOX_TOOLTIP", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "TOOLTIP", "None", "that will appear when mouse hovers over the element",),
	("PSGVAL_FULL_CHECKBOX_VISIBLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_CHECKBOX", "VISIBLE", "True", "set visibility state of the element",),
	("PSGVAL_FULL_COLUMN", FMAXPSG_SCTN0905_TUPDICTDEF, "FULL_COLUMN", "full column entry",),
	("PSGVAL_FULL_COLUMN_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "BACKGROUND_COLOR", "None", "color of background of entire Column",),
	("PSGVAL_FULL_COLUMN_ELEMENT_JUSTIFICATION", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "ELEMENT_JUSTIFICATION", "None", "All elements inside the Column will have this justification 'left', 'right', 'center' are valid values",),
	("PSGVAL_FULL_COLUMN_EXPAND_X", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "EXPAND_X", "None", "If True the column will automatically expand in the X direction to fill available space",),
	("PSGVAL_FULL_COLUMN_EXPAND_Y", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "EXPAND_Y", "None", "If True the column will automatically expand in the X direction to fill available space",),
	("PSGVAL_FULL_COLUMN_GRAB", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "GRAB", "None", "If True can grab this element and move the window around. Default is False",),
	("PSGVAL_FULL_COLUMN_JUSTIFICATION", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "JUSTIFICATION", "None", "set justification for the Column itself. Note entire row containing the Column will be affected",),
	("PSGVAL_FULL_COLUMN_K", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "K", "None", "Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window",),
	("PSGVAL_FULL_COLUMN_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "KEY", "None", "Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window",),
	("PSGVAL_FULL_COLUMN_LAYOUT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "LAYOUT", "[]", "Layout that will be shown in the Column container",),
	("PSGVAL_FULL_COLUMN_METADATA", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_COLUMN_PAD", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "PAD", "None", "Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_COLUMN_RIGHT_CLICK_MENU", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "RIGHT_CLICK_MENU", "None", "A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.",),
	("PSGVAL_FULL_COLUMN_S", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "S", "(None, None)", "(width, height) size in pixels (doesn't work quite right, sometimes only 1 dimension is set by tkinter",),
	("PSGVAL_FULL_COLUMN_SCROLLABLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "SCROLLABLE", "False", "if True then scrollbars will be added to the column",),
	("PSGVAL_FULL_COLUMN_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "SIZE", "(None, None)", "(width, height) size in pixels (doesn't work quite right, sometimes only 1 dimension is set by tkinter",),
	("PSGVAL_FULL_COLUMN_VERTACLE_SCROLL_ONLY", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "VERTICAL_SCROLL_ONLY", "False", "if Truen then no horizontal scrollbar will be shown",),
	("PSGVAL_FULL_COLUMN_VERTICAL_ALIGNMENT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "VERTICAL_ALIGNMENT", "None", "Place the column at the 'top', 'center', 'bottom' of the row (can also use t,c,r). Defaults to no setting (tkinter decides)",),
	("PSGVAL_FULL_COLUMN_VISIBLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COLUMN", "VISIBLE", "True", "set visibility state of the element",),
	("PSGVAL_FULL_COMBO", FMAXPSG_SCTN0905_TUPDICTDEF, "FULL_COMBO", "a full combo tupdict",),
	("PSGVAL_FULL_COMBO_AUTO_SIZE_TEXT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "AUTO_SIZE_TEXT", "None", "True if element should be the same size as the contents",),
	("PSGVAL_FULL_COMBO_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_FULL_COMBO_CHANGE_SUBMITS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "CHANGE_SUBMITS", "False", "DEPRICATED DO NOT USE. Use `enable_events` instead",),
	("PSGVAL_FULL_COMBO_DEFAULT_VALUE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "DEFAULT_VALUE", "None", "Choice to be displayed as initial value. Must match one of values variable contents",),
	("PSGVAL_FULL_COMBO_DISABLED", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "DISABLED", "False", "set disable state for element",),
	("PSGVAL_FULL_COMBO_ENABLE_EVENTS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "ENABLE_EVENTS", "False", "",),
	("PSGVAL_FULL_COMBO_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_FULL_COMBO_K", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "K", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_FULL_COMBO_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_FULL_COMBO_METADATA", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_COMBO_PAD", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "PAD", "None", "Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_COMBO_READONLY", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "READONLY", "False", "make element readonly (user can't change). True means user cannot change",),
	("PSGVAL_FULL_COMBO_S", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "S", "(None, None)", "width, height. Width = characters-wide, height = NOTE it's the number of entries to show in the list",),
	("PSGVAL_FULL_COMBO_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "SIZE", "(None, None)", "width, height. Width = characters-wide, height = NOTE it's the number of entries to show in the list",),
	("PSGVAL_FULL_COMBO_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_FULL_COMBO_TOOLTIP", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "TOOLTIP", "None", "text that will appear when mouse hovers over this element",),
	("PSGVAL_FULL_COMBO_VALUES", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "VALUES", "[]", "values to choose. While displayed as text, the items returned are what the caller supplied, not text",),
	("PSGVAL_FULL_COMBO_VISIBLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_COMBO", "VISIBLE", "True", "set visibility state of the element",),
	("PSGVAL_FULL_RADIO", FMAXPSG_SCTN0905_TUPDICTDEF, "FULL_RADIO", "define a full radio button entity",),
	("PSGVAL_FULL_RADIO_AUTO_SIZE_TEXT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "AUTO_SIZE_TEXT", "None,", "",),
	("PSGVAL_FULL_RADIO_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "BACKGROUND_COLOR", "None,", "",),
	("PSGVAL_FULL_RADIO_CHANGE_SUBMITS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "CHANGE_SUBMITS", "False,", "",),
	("PSGVAL_FULL_RADIO_CIRCLE_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "CIRCLE_COLOR", "None,", "",),
	("PSGVAL_FULL_RADIO_DEFAULT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "DEFAULT", "False,", "",),
	("PSGVAL_FULL_RADIO_DISABLED", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "DISABLED", "False,", "",),
	("PSGVAL_FULL_RADIO_ENABLE_EVENTS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "ENABLE_EVENTS", "False,", "",),
	("PSGVAL_FULL_RADIO_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "FONT", "None,", "",),
	("PSGVAL_FULL_RADIO_GROUP_ID", FMAXPSG_SCTN0905_TUPDICTSTRADD, "FULL_RADIO", "GROUP_ID", "", "Groups together multiple Radio Buttons. Any type works",),
	("PSGVAL_FULL_RADIO_K", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "K", "None,", "",),
	("PSGVAL_FULL_RADIO_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "KEY", "None,", "",),
	("PSGVAL_FULL_RADIO_METADATA", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "METADATA", "None", "",),
	("PSGVAL_FULL_RADIO_PAD", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "PAD", "None,", "",),
	("PSGVAL_FULL_RADIO_S", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "S", "(None, None),", "",),
	("PSGVAL_FULL_RADIO_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "SIZE", "(None, None),", "",),
	("PSGVAL_FULL_RADIO_TEXT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "FULL_RADIO", "TEXT", "", "",),
	("PSGVAL_FULL_RADIO_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "TEXT_COLOR", "None,", "",),
	("PSGVAL_FULL_RADIO_TOOLTIP", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "TOOLTIP", "None,", "",),
	("PSGVAL_FULL_RADIO_VISIBLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_RADIO", "VISIBLE", "True,", "",),
	("PSGVAL_FULL_SPIN", FMAXPSG_SCTN0905_TUPDICTDEF, "FULL_SPIN", "full spin dict",),
	("PSGVAL_FULL_SPIN_AUTO_SIZE_TEXT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "AUTO_SIZE_TEXT", "None", "if True will size the element to match the length of the text",),
	("PSGVAL_FULL_SPIN_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_FULL_SPIN_CHANGE_SUBMITS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "CHANGE_SUBMITS", "False", "DO NOT USE. Only listed for backwards compat - Use enable_events instead",),
	("PSGVAL_FULL_SPIN_DISABLED", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "DISABLED", "False", "set disable state",),
	("PSGVAL_FULL_SPIN_ENABLE_EVENTS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "ENABLE_EVENTS", "False", "Turns on the element specific events. Spin events happen when an item changes",),
	("PSGVAL_FULL_SPIN_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_FULL_SPIN_INITIAL_VALUE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "INITIAL_VALUE", "None", "Initial item to show in window. Choose from list of values supplied",),
	("PSGVAL_FULL_SPIN_K", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "K", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_FULL_SPIN_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_FULL_SPIN_METADATA", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_SPIN_PAD", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "PAD", "None", "Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_SPIN_READONLY", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "READONLY", "False", "readonly bool",),
	("PSGVAL_FULL_SPIN_S", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "S", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_FULL_SPIN_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "SIZE", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_FULL_SPIN_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_FULL_SPIN_TOOLTIP", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "TOOLTIP", "None", "text, that will appear when mouse hovers over the element",),
	("PSGVAL_FULL_SPIN_VALUES", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "VALUES", "[]", "List of valid values",),
	("PSGVAL_FULL_SPIN_VISIBLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_SPIN", "VISIBLE", "True", "set visibility state of the element",),
	("PSGVAL_FULL_TEXT", FMAXPSG_SCTN0905_TUPDICTDEF, "FULL_TEXT", "the full monty for text elements",),
	("PSGVAL_FULL_TEXT_AUTO_SIZE_TEXT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "AUTO_SIZE_TEXT", "None", "if True size of the Text Element will be sized to fit the string provided in 'text' parm",),
	("PSGVAL_FULL_TEXT_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_FULL_TEXT_BORDER_WIDTH", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "BORDER_WIDTH", "None", "number of pixels for the border (if using a relief)",),
	("PSGVAL_FULL_TEXT_CLICK_SUBMITS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "CLICK_SUBMITS", "False", "DO NOT USE. Only listed for backwards compat - Use enable_events instead",),
	("PSGVAL_FULL_TEXT_ENABLE_EVENTS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "ENABLE_EVENTS", "False", "Turns on the element specific events. Text events happen when the text is clicked",),
	("PSGVAL_FULL_TEXT_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_FULL_TEXT_GRAB", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "GRAB", "None", "If True can grab this element and move the window around. Default is False",),
	("PSGVAL_FULL_TEXT_JUSTIFICATION", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "JUSTIFICATION", "None", "how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center`",),
	("PSGVAL_FULL_TEXT_K", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "K", "None", "Same as the Key. You can use either k or key. Which ever is set will be used.",),
	("PSGVAL_FULL_TEXT_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element",),
	("PSGVAL_FULL_TEXT_METADATA", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_TEXT_PAD", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "PAD", "None", "Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_TEXT_RELIEF", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "RELIEF", "None", "relief style around the text. Values are same as progress meter relief values. Should be a constant that is defined at starting with 'RELIEF_' - `RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID`",),
	("PSGVAL_FULL_TEXT_RIGHT_CLICK_MENU", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "RIGHT_CLICK_MENU", "None", "A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.",),
	("PSGVAL_FULL_TEXT_S", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "S", "(None, None)", "Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used",),
	("PSGVAL_FULL_TEXT_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "SIZE", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_FULL_TEXT_TEXT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "TEXT", "", "The text to display. Can include /n to achieve multiple lines.  Will convert (optional) parameter into a string",),
	("PSGVAL_FULL_TEXT_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_FULL_TEXT_TOOLTIP", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "TOOLTIP", "None", "text, that will appear when mouse hovers over the element",),
	("PSGVAL_FULL_TEXT_VISIBLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_TEXT", "VISIBLE", "True", "set visibility state of the element",),
	("PSGVAL_FULL_WINDOW", FMAXPSG_SCTN0905_TUPDICTDEF, "FULL_WINDOW", "define the FULL_WINDOW tupdict",),
	("PSGVAL_FULL_WINDOW_ALPHA_CHANNEL", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "ALPHA_CHANNEL", "1", "Sets the opacity of the window. 0 = invisible 1 = completely visible. Values bewteen 0 & 1 will produce semi-transparent windows in SOME environments (The Raspberry Pi always has this value at 1 and cannot change.",),
	("PSGVAL_FULL_WINDOW_AUTO_CLOSE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "AUTO_CLOSE", "False", "If True, the window will automatically close itself",),
	("PSGVAL_FULL_WINDOW_AUTO_CLOSE_DURATION", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "AUTO_CLOSE_DURATION", "3", "Number of seconds to wait before closing the window",),
	("PSGVAL_FULL_WINDOW_AUTO_SIZE_BUTTONS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "AUTO_SIZE_BUTTONS", "None", "True if Buttons in this Window should be sized to exactly fit the text on this.",),
	("PSGVAL_FULL_WINDOW_AUTO_SIZE_TEXT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "AUTO_SIZE_TEXT", "None", "True if Elements in Window should be sized to exactly fir the length of text",),
	("PSGVAL_FULL_WINDOW_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_FULL_WINDOW_BORDER_DEPTH", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "BORDER_DEPTH", "None", "Default border depth (width) for all elements in the window",),
	("PSGVAL_FULL_WINDOW_BUTTON_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "BUTTON_COLOR", "None", "Default button colors for all buttons in the window",),
	("PSGVAL_FULL_WINDOW_DEBUGGER_ENABLED", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "DEBUGGER_ENABLED", "True", "Default border depth (width) for all elements in the window",),
	("PSGVAL_FULL_WINDOW_DEFAULT_BUTTON_ELEMENT_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "DEFAULT_BUTTON_ELEMENT_SIZE", "(None, None)", "(width, height) size in characters (wide) and rows (high) for all Button elements in this window",),
	("PSGVAL_FULL_WINDOW_DEFAULT_ELEMENT_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "DEFAULT_ELEMENT_SIZE", "(45, 1)", "size in characters (wide) and rows (high) for all elements in this window",),
	("PSGVAL_FULL_WINDOW_DISABLE_CLOSE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "DISABLE_CLOSE", "False", "If True, the X button in the top right corner of the window will no work.  Use with caution and always give a way out toyour users",),
	("PSGVAL_FULL_WINDOW_DISABLE_MINIMIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "DISABLE_MINIMIZE", "False", "if True the user won't be able to minimize window.  Good for taking over entire screen and staying that way.",),
	("PSGVAL_FULL_WINDOW_ELEMENT_JUSTIFICATION", FMAXPSG_SCTN0905_TUPDICTSTRADD, "FULL_WINDOW", "ELEMENT_JUSTIFICATION", "left", "All elements in the Window itself will have this justification 'left', 'right', 'center' are valid values",),
	("PSGVAL_FULL_WINDOW_ELEMENT_PADDING", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "ELEMENT_PADDING", "None", "Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_WINDOW_ENABLE_CLOSE_ATTEMPTED_EVENT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "ENABLE_CLOSE_ATTEMPTED_EVENT", "False", "If True then the window will not close when 'X' clicked. Instead an event FULL_WINDOW_CLOSE_ATTEMPTED_EVENT if returned from window.read",),
	("PSGVAL_FULL_WINDOW_FINALIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "FINALIZE", "False", "If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code",),
	("PSGVAL_FULL_WINDOW_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_FULL_WINDOW_FORCE_TOPLEVEL", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "FORCE_TOPLEVEL", "False", "If True will cause this window to skip the normal use of a hidden master window",),
	("PSGVAL_FULL_WINDOW_GRAB_ANYWHERE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "GRAB_ANYWHERE", "False", "If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems",),
	("PSGVAL_FULL_WINDOW_ICON", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "ICON", "None", "Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO",),
	("PSGVAL_FULL_WINDOW_KEEP_ON_TOP", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "KEEP_ON_TOP", "False", "If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm",),
	("PSGVAL_FULL_WINDOW_LAYOUT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "LAYOUT", "None", "The layout for the window. Can also be specified in the Layout method",),
	("PSGVAL_FULL_WINDOW_LOCATION", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "LOCATION", "(None, None)", "(x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen.",),
	("PSGVAL_FULL_WINDOW_MARGINS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "MARGINS", "(None, None)", "(left/right, top/bottom) Amount of pixels to leave inside the window's frame around the edges before your elements are shown.",),
	("PSGVAL_FULL_WINDOW_METADATA", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_WINDOW_MODAL", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "MODAL", "False", "If True then this window will be the only window a user can interact with until it is closed",),
	("PSGVAL_FULL_WINDOW_NO_TITLEBAR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "NO_TITLEBAR", "False", "If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar",),
	("PSGVAL_FULL_WINDOW_PROGRESS_BAR_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "PROGRESS_BAR_COLOR", "(None, None)", "(bar color, background color) Sets the default colors for all progress bars in the window",),
	("PSGVAL_FULL_WINDOW_RESIZABLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "RESIZABLE", "False", "If True, allows the user to resize the window. Note the not all Elements will change size or location when resizing.",),
	("PSGVAL_FULL_WINDOW_RETURN_KEYBOARD_EVENTS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "RETURN_KEYBOARD_EVENTS", "False", "if True key presses on the keyboard will be returned as Events from Read calls",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "RIGHT_CLICK_MENU", "None", "A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "RIGHT_CLICK_MENU_BACKGROUND_COLOR", "None", "Background color for right click menus",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR", "None", "Text color for disabled right click menu items",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "RIGHT_CLICK_MENU_FONT", "None", "Font for right click menus",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU_SELECTED_COLORS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "RIGHT_CLICK_MENU_SELECTED_COLORS", "(None, None)", "Text AND background colors for a selected item. Can be a Tuple OR a color string. simplified-button-color-string 'foreground on background'. Can be a single color if want to set only the background.",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU_TEAROFF", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "RIGHT_CLICK_MENU_TEAROFF", "False", "If True then all right click menus can be torn off",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "RIGHT_CLICK_MENU_TEXT_COLOR", "None", "Text color for right click menus",),
	("PSGVAL_FULL_WINDOW_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "SIZE", "(None, None)", "(width, height) size in pixels for this window. Normally the window is autosized to fit contents, not set to an absolute size by the user",),
	("PSGVAL_FULL_WINDOW_TEXT_JUSTIFICATION", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "TEXT_JUSTIFICATION", "None", "Default text justification for all Text Elements in window",),
	("PSGVAL_FULL_WINDOW_TITLE", FMAXPSG_SCTN0905_TUPDICTSTRADD, "FULL_WINDOW", "TITLE", "", "The title that will be displayed in the Titlebar and on the Taskbar",),
	("PSGVAL_FULL_WINDOW_TITLEBAR_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "TITLEBAR_BACKGROUND_COLOR", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as background color",),
	("PSGVAL_FULL_WINDOW_TITLEBAR_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "TITLEBAR_FONT", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as title font",),
	("PSGVAL_FULL_WINDOW_TITLEBAR_ICON", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "TITLEBAR_ICON", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as the icon (file or base64 bytes)",),
	("PSGVAL_FULL_WINDOW_TITLEBAR_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "TITLEBAR_TEXT_COLOR", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as text color",),
	("PSGVAL_FULL_WINDOW_TRANSPARENT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "TRANSPARENT_COLOR", "None", "Any portion of the window that has this color will be completely transparent. You can even click through these spots to the window under this window.",),
	("PSGVAL_FULL_WINDOW_TTK_THEME", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "TTK_THEME", "None", "Set the tkinter ttk 'theme' of the window.  Default = DEFAULT_TTK_THEME.  Sets all ttk widgets to this theme as their default",),
	("PSGVAL_FULL_WINDOW_USE_CUSTOM_TITLEBAR", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "USE_CUSTOM_TITLEBAR", "None", "If True, then a custom titlebar will be used instead of the normal titlebar",),
	("PSGVAL_FULL_WINDOW_USE_DEFAULT_FOCUS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "USE_DEFAULT_FOCUS", "True", "If True will use the default focus algorithm to set the focus to the 'Correct' element",),
	("PSGVAL_FULL_WINDOW_USE_TTK_BUTTONS", FMAXPSG_SCTN0905_TUPDICTVALADD, "FULL_WINDOW", "USE_TTK_BUTTONS", "None", "Affects all buttons in window. True = use ttk buttons. False = do not use ttk buttons.  None = use ttk buttons only if on a Mac",),
	("PSGVAL_NORMAL_BUTTON", FMAXPSG_SCTN0905_TUPDICTDEF, "NORMAL_BUTTON", "define the button empty tupdict",),
	("PSGVAL_NORMAL_BUTTON_BUTTON_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_BUTTON", "BUTTON_COLOR", "None", "Color of button. default is from theme or the window. Easy to remember which is which if you say 'ON' between colors. 'red' on 'green'. Normally a tuple, but can be a simplified-button-color-string 'foreground on background'. Can be a single color if want to set only the background.",),
	("PSGVAL_NORMAL_BUTTON_BUTTON_TEXT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "NORMAL_BUTTON", "BUTTON_TEXT", "", "str text to display on the button",),
	("PSGVAL_NORMAL_BUTTON_FOCUS", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_BUTTON", "FOCUS", "False", "if True, initial focus will be put on this button",),
	("PSGVAL_NORMAL_BUTTON_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_BUTTON", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_NORMAL_BUTTON_IMAGE_DATA", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_BUTTON", "IMAGE_DATA", "None", "Raw or Base64 representation of the image to put on button. Choose either filename or data",),
	("PSGVAL_NORMAL_BUTTON_IMAGE_FILENAME", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_BUTTON", "IMAGE_FILENAME", "None", "image filename if there is a button image. GIFs and PNGs only.",),
	("PSGVAL_NORMAL_BUTTON_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_BUTTON", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element",),
	("PSGVAL_NORMAL_CHECKBOX", FMAXPSG_SCTN0905_TUPDICTDEF, "NORMAL_CHECKBOX", "set a checkbox in motion",),
	("PSGVAL_NORMAL_CHECKBOX_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_CHECKBOX", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_NORMAL_CHECKBOX_CHECKBOX_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_CHECKBOX", "CHECKBOX_COLOR", "None", "color of background of the box that has the check mark in it. The checkmark is the same color as the text",),
	("PSGVAL_NORMAL_CHECKBOX_DEFAULT", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_CHECKBOX", "DEFAULT", "False", "Set to True if you want this checkbox initially checked",),
	("PSGVAL_NORMAL_CHECKBOX_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_CHECKBOX", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_NORMAL_CHECKBOX_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_CHECKBOX", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_NORMAL_CHECKBOX_TEXT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "NORMAL_CHECKBOX", "TEXT", "", "Text to display next to checkbox",),
	("PSGVAL_NORMAL_CHECKBOX_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_CHECKBOX", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_NORMAL_COMBO", FMAXPSG_SCTN0905_TUPDICTDEF, "NORMAL_COMBO", "a full combo tupdict",),
	("PSGVAL_NORMAL_COMBO_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_COMBO", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_NORMAL_COMBO_DEFAULT_VALUE", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_COMBO", "DEFAULT_VALUE", "None", "Choice to be displayed as initial value. Must match one of values variable contents",),
	("PSGVAL_NORMAL_COMBO_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_COMBO", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_NORMAL_COMBO_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_COMBO", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_NORMAL_COMBO_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_COMBO", "SIZE", "None", "width, height. Width = characters-wide, height = NOTE it's the number of entries to show in the list",),
	("PSGVAL_NORMAL_COMBO_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_COMBO", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_NORMAL_COMBO_VALUES", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_COMBO", "VALUES", "[]", "values to choose. While displayed as text, the items returned are what the caller supplied, not text",),
	("PSGVAL_NORMAL_RADIO", FMAXPSG_SCTN0905_TUPDICTDEF, "NORMAL_RADIO", "define a full radio button entity",),
	("PSGVAL_NORMAL_RADIO_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_RADIO", "BACKGROUND_COLOR", "None,", "",),
	("PSGVAL_NORMAL_RADIO_CIRCLE_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_RADIO", "CIRCLE_COLOR", "None,", "",),
	("PSGVAL_NORMAL_RADIO_DEFAULT", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_RADIO", "DEFAULT", "False,", "",),
	("PSGVAL_NORMAL_RADIO_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_RADIO", "FONT", "None,", "",),
	("PSGVAL_NORMAL_RADIO_GROUP_ID", FMAXPSG_SCTN0905_TUPDICTSTRADD, "NORMAL_RADIO", "GROUP_ID", "", "Groups together multiple Radio Buttons. Any type works",),
	("PSGVAL_NORMAL_RADIO_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_RADIO", "KEY", "None,", "",),
	("PSGVAL_NORMAL_RADIO_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_RADIO", "SIZE", "(None, None),", "",),
	("PSGVAL_NORMAL_RADIO_TEXT", FMAXPSG_SCTN0905_TUPDICTSTRADD, "NORMAL_RADIO", "TEXT", "", "",),
	("PSGVAL_NORMAL_RADIO_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_RADIO", "TEXT_COLOR", "None,", "",),
	("PSGVAL_NORMAL_SPIN", FMAXPSG_SCTN0905_TUPDICTDEF, "NORMAL_SPIN", "full spin dict",),
	("PSGVAL_NORMAL_SPIN_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_SPIN", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_NORMAL_SPIN_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_SPIN", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_NORMAL_SPIN_INITIAL_VALUE", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_SPIN", "INITIAL_VALUE", "None", "Initial item to show in window. Choose from list of values supplied",),
	("PSGVAL_NORMAL_SPIN_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_SPIN", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_NORMAL_SPIN_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_SPIN", "SIZE", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_NORMAL_SPIN_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_SPIN", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_NORMAL_SPIN_VALUES", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_SPIN", "VALUES", "[]", "List of valid values",),
	("PSGVAL_NORMAL_TEXT", FMAXPSG_SCTN0905_TUPDICTDEF, "NORMAL_TEXT", "the full monty for text elements",),
	("PSGVAL_NORMAL_TEXT_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_TEXT", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_NORMAL_TEXT_BORDER_WIDTH", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_TEXT", "BORDER_WIDTH", "None", "number of pixels for the border (if using a relief)",),
	("PSGVAL_NORMAL_TEXT_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_TEXT", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_NORMAL_TEXT_GRAB", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_TEXT", "GRAB", "None", "If True can grab this element and move the window around. Default is False",),
	("PSGVAL_NORMAL_TEXT_JUSTIFICATION", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_TEXT", "JUSTIFICATION", "None", "how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center`",),
	("PSGVAL_NORMAL_TEXT_KEY", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_TEXT", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element",),
	("PSGVAL_NORMAL_TEXT_RELIEF", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_TEXT", "RELIEF", "None", "relief style around the text. Values are same as progress meter relief values. Should be a constant that is defined at starting with 'RELIEF_' - `RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID`",),
	("PSGVAL_NORMAL_TEXT_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_TEXT", "SIZE", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_NORMAL_TEXT_TEXT", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_TEXT", "TEXT", "", "The text to display. Can include /n to achieve multiple lines.  Will convert (optional) parameter into a string",),
	("PSGVAL_NORMAL_TEXT_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_TEXT", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_NORMAL_WINDOW", FMAXPSG_SCTN0905_TUPDICTDEF, "NORMAL_WINDOW", "define the NORMAL_WINDOW tupdict",),
	("PSGVAL_NORMAL_WINDOW_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_NORMAL_WINDOW_FINALIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "FINALIZE", "False", "If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code",),
	("PSGVAL_NORMAL_WINDOW_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_NORMAL_WINDOW_GRAB_ANYWHERE", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "GRAB_ANYWHERE", "False", "If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems",),
	("PSGVAL_NORMAL_WINDOW_ICON", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "ICON", "None", "Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO",),
	("PSGVAL_NORMAL_WINDOW_KEEP_ON_TOP", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "KEEP_ON_TOP", "False", "If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm",),
	("PSGVAL_NORMAL_WINDOW_LAYOUT", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "LAYOUT", "None", "The layout for the window. Can also be specified in the Layout method",),
	("PSGVAL_NORMAL_WINDOW_LOCATION", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "LOCATION", "(None, None)", "(x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen.",),
	("PSGVAL_NORMAL_WINDOW_MODAL", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "MODAL", "False", "If True then this window will be the only window a user can interact with until it is closed",),
	("PSGVAL_NORMAL_WINDOW_NO_TITLEBAR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "NO_TITLEBAR", "False", "If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar",),
	("PSGVAL_NORMAL_WINDOW_TITLE", FMAXPSG_SCTN0905_TUPDICTSTRADD, "NORMAL_WINDOW", "TITLE", "", "The title that will be displayed in the Titlebar and on the Taskbar",),
	("PSGVAL_NORMAL_WINDOW_TITLEBAR_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "TITLEBAR_BACKGROUND_COLOR", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as background color",),
	("PSGVAL_NORMAL_WINDOW_TITLEBAR_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "TITLEBAR_FONT", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as title font",),
	("PSGVAL_NORMAL_WINDOW_TITLEBAR_ICON", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "TITLEBAR_ICON", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as the icon (file or base64 bytes)",),
	("PSGVAL_NORMAL_WINDOW_TITLEBAR_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "TITLEBAR_TEXT_COLOR", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as text color",),
	("PSGVAL_NORMAL_WINDOW_TRANSPARENT_COLOR", FMAXPSG_SCTN0905_TUPDICTVALADD, "NORMAL_WINDOW", "TRANSPARENT_COLOR", "None", "Any portion of the window that has this color will be completely transparent. You can even click through these spots to the window under this window.",),
	("PSGVAL_UPDATE_COMBO", FMAXPSG_SCTN0905_TUPDICTDEF, "UPDATE_COMBO", "holds the update combo entity",),
	("PSGVAL_UPDATE_COMBO_DISABLED", FMAXPSG_SCTN0905_TUPDICTVALADD, "UPDATE_COMBO", "DISABLED", "None", "set disable state for element",),
	("PSGVAL_UPDATE_COMBO_FONT", FMAXPSG_SCTN0905_TUPDICTVALADD, "UPDATE_COMBO", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_UPDATE_COMBO_READONLY", FMAXPSG_SCTN0905_TUPDICTVALADD, "UPDATE_COMBO", "READONLY", "None", "make element readonly (user can't change). True means user cannot change",),
	("PSGVAL_UPDATE_COMBO_SET_TO_INDEX", FMAXPSG_SCTN0905_TUPDICTVALADD, "UPDATE_COMBO", "SET_TO_INDEX", "None", "",),
	("PSGVAL_UPDATE_COMBO_SIZE", FMAXPSG_SCTN0905_TUPDICTVALADD, "UPDATE_COMBO", "SIZE", "None", "width, height. Width = characters-wide, height = NOTE it's the number of entries to show in the list",),
	("PSGVAL_UPDATE_COMBO_VALUE", FMAXPSG_SCTN0905_TUPDICTVALADD, "UPDATE_COMBO", "VALUE", "None", "change which value is current selected based on new list of previous list of choices",),
	("PSGVAL_UPDATE_COMBO_VALUES", FMAXPSG_SCTN0905_TUPDICTVALADD, "UPDATE_COMBO", "VALUES", "None", "values to choose. While displayed as text, the items returned are what the caller supplied, not text",),
	("PSGVAL_UPDATE_COMBO_VISIBLE", FMAXPSG_SCTN0905_TUPDICTVALADD, "UPDATE_COMBO", "VISIBLE", "None", "set visibility state of the element",),

	("PSGVAL_TEXT_CLOCKS_CLOCKS", FMAXPSG_SCTN0909_TEXTDEF, "CLOCKS_CLOCKS", "text for the clocks on the clocks window/frame",),

	("PSGVAL__AVOID_MOUSE", FMAXPSG_SCTN0901_KEY_DEF, "AVOID_MOUSE", "",),
	("PSGVAL__DISMISSED", FMAXPSG_SCTN0901_KEY_DEF, "DISMISSED", "alarm dismissed bool",),
	("PSGVAL__EVENT_ENTRIES", FMAXPSG_SCTN0901_KEY_DEF, "EVENT_ENTRIES", "",),
	("PSGVAL__EVENT_MODE", FMAXPSG_SCTN0901_KEY_DEF, "EVENT_MODE", "",),
	("PSGVAL__INDEX_OF_NEXT_EVENT", FMAXPSG_SCTN0901_KEY_DEF, "INDEX_OF_NEXT_EVENT", "",),
	("PSGVAL__MAIN_FONT", FMAXPSG_SCTN0901_STR_DEF, "MAIN_FONT", "Source Code Pro", "set the main font",),
	("PSGVAL__MODE_ALARM", FMAXPSG_SCTN0901_KEY_DEF, "MODE_ALARM", "",),
	("PSGVAL__MODE_ALARMREMIND", FMAXPSG_SCTN0901_KEY_DEF, "MODE_ALARMREMIND", "",),
	("PSGVAL__MODE_INTERVAL", FMAXPSG_SCTN0901_KEY_DEF, "MODE_INTERVAL", "",),
	("PSGVAL__NAME", FMAXPSG_SCTN0901_KEY_DEF, "NAME", "",),
	("PSGVAL__PREDISMISSABLE", FMAXPSG_SCTN0901_KEY_DEF, "PREDISMISSABLE", "",),
	("PSGVAL__RUNNING", FMAXPSG_SCTN0901_KEY_DEF, "RUNNING", "is this interval running or not",),
	("PSGVAL__SNOOZABLE", FMAXPSG_SCTN0901_KEY_DEF, "SNOOZABLE", "",),
	("PSGVAL__SNOOZED", FMAXPSG_SCTN0901_KEY_DEF, "SNOOZED", "snoozed bool",),
	("PSGVAL__TIME_ALARM", FMAXPSG_SCTN0901_KEY_DEF, "TIME_ALARM", "the alarm time",),
	("PSGVAL__TIME_CLOCK", FMAXPSG_SCTN0901_KEY_DEF, "TIME_CLOCK", "the main clock time",),
	("PSGVAL__TIME_ELAPSED", FMAXPSG_SCTN0901_KEY_DEF, "TIME_ELAPSED", "24 hour centric elapsed time running, can be reset, may go to 99h",),
	("PSGVAL__TIME_INTERVAL", FMAXPSG_SCTN0901_KEY_DEF, "TIME_INTERVAL", "",),
	("PSGVAL__TIME_OF_NEXT_EVENT", FMAXPSG_SCTN0901_KEY_DEF, "TIME_OF_NEXT_EVENT", "what time is the next alarm, == TIME_ALARM is tomorrow",),
	("PSGVAL__TIME_REMIND", FMAXPSG_SCTN0901_KEY_DEF, "TIME_REMIND", "",),
	("PSGVAL__TIME_TO_NEXT_EVENT", FMAXPSG_SCTN0901_KEY_DEF, "TIME_TO_NEXT_EVENT", "down counter to next event on this window/alarm/interval/reminder",),
	("PSGVAL__TRANSPARENT", FMAXPSG_SCTN0901_KEY_DEF, "TRANSPARENT", "",),
	("PSGVAL__TRANSPARENT_UNDER_MOUSE", FMAXPSG_SCTN0901_KEY_DEF, "TRANSPARENT_UNDER_MOUSE", "is the clock transparent under mouse (ineffective if mouse is avoided)",),
	("PSGVAL___ALPHA_CHANNEL", FMAXPSG_SCTN0901_STR_DEF, "ALPHA_CHANNEL", "alpha_channel", "",),
	("PSGVAL___AUTO_CLOSE", FMAXPSG_SCTN0901_STR_DEF, "AUTO_CLOSE", "auto_close", "",),
	("PSGVAL___AUTO_CLOSE_DURATION", FMAXPSG_SCTN0901_STR_DEF, "AUTO_CLOSE_DURATION", "auto_close_duration", "",),
	("PSGVAL___AUTO_SIZE_BUTTON", FMAXPSG_SCTN0901_STR_DEF, "AUTO_SIZE_BUTTON", "auto_size_button", "",),
	("PSGVAL___AUTO_SIZE_BUTTONS", FMAXPSG_SCTN0901_STR_DEF, "AUTO_SIZE_BUTTONS", "auto_size_buttons", "",),
	("PSGVAL___AUTO_SIZE_TEXT", FMAXPSG_SCTN0901_STR_DEF, "AUTO_SIZE_TEXT", "auto_size_text", "",),
	("PSGVAL___AUTO_SIZE_TEXT", FMAXPSG_SCTN0901_STR_DEF, "AUTO_SIZE_TEXT", "auto_size_text", "",),
	("PSGVAL___BACKGROUND_COLOR", FMAXPSG_SCTN0901_STR_DEF, "BACKGROUND_COLOR", "background_color", "",),
	("PSGVAL___BIND_RETURN_KEY", FMAXPSG_SCTN0901_STR_DEF, "BIND_RETURN_KEY", "bind_return_key", "",),
	("PSGVAL___BORDER_DEPTH", FMAXPSG_SCTN0901_STR_DEF, "BORDER_DEPTH", "border_depth", "",),
	("PSGVAL___BORDER_WIDTH", FMAXPSG_SCTN0901_STR_DEF, "BORDER_WIDTH", "border_width", "",),
	("PSGVAL___BUTTON_COLOR", FMAXPSG_SCTN0901_STR_DEF, "BUTTON_COLOR", "button_color", "",),
	("PSGVAL___BUTTON_TEXT", FMAXPSG_SCTN0901_STR_DEF, "BUTTON_TEXT", "button_text", "",),
	("PSGVAL___BUTTON_TYPE", FMAXPSG_SCTN0901_STR_DEF, "BUTTON_TYPE", "button_type", "",),
	("PSGVAL___CHANGE_SUBMITS", FMAXPSG_SCTN0901_STR_DEF, "CHANGE_SUBMITS", "change_submits", "",),
	("PSGVAL___CHECKBOX_COLOR", FMAXPSG_SCTN0901_STR_DEF, "CHECKBOX_COLOR", "checkbox_color", "color of background of the box that has the check mark in it. The checkmark is the same color as the text",),
	("PSGVAL___CLOCKTIME", FMAXPSG_SCTN0901_KEY_DEF, "CLOCKTIME", "holds the clock value (str HH:MM:SS)",),
	("PSGVAL___DEBUGGER_ENABLED", FMAXPSG_SCTN0901_STR_DEF, "DEBUGGER_ENABLED", "debugger_enabled", "",),
	("PSGVAL___DEFAULT", FMAXPSG_SCTN0901_STR_DEF, "DEFAULT", "default", "",),
	("PSGVAL___DEFAULT_BUTTON_ELEMENT_SIZE", FMAXPSG_SCTN0901_STR_DEF, "DEFAULT_BUTTON_ELEMENT_SIZE", "default_button_element_size", "",),
	("PSGVAL___DEFAULT_ELEMENT_SIZE", FMAXPSG_SCTN0901_STR_DEF, "DEFAULT_ELEMENT_SIZE", "default_element_size", "",),
	("PSGVAL___DEFAULT_EXTENSION", FMAXPSG_SCTN0901_STR_DEF, "DEFAULT_EXTENSION", "default_extension", "",),
	("PSGVAL___DEFAULT_VALUE", FMAXPSG_SCTN0901_STR_DEF, "DEFAULT_VALUE", "default_value", "",),
	("PSGVAL___DISABLED", FMAXPSG_SCTN0901_STR_DEF, "DISABLED", "disabled", "",),
	("PSGVAL___DISABLED_BUTTON_COLOR", FMAXPSG_SCTN0901_STR_DEF, "DISABLED_BUTTON_COLOR", "disabled_button_color", "",),
	("PSGVAL___DISABLE_CLOSE", FMAXPSG_SCTN0901_STR_DEF, "DISABLE_CLOSE", "disable_close", "",),
	("PSGVAL___DISABLE_MINIMIZE", FMAXPSG_SCTN0901_STR_DEF, "DISABLE_MINIMIZE", "disable_minimize", "",),
	("PSGVAL___ELEMENT_JUSTIFICATION", FMAXPSG_SCTN0901_STR_DEF, "ELEMENT_JUSTIFICATION", "element_justification", "",),
	("PSGVAL___ELEMENT_PADDING", FMAXPSG_SCTN0901_STR_DEF, "ELEMENT_PADDING", "element_padding", "",),
	("PSGVAL___ENABLED", FMAXPSG_SCTN0901_STR_DEF, "ENABLED", "enabled", "",),
	("PSGVAL___ENABLE_CLOSE_ATTEMPTED_EVENT", FMAXPSG_SCTN0901_STR_DEF, "ENABLE_CLOSE_ATTEMPTED_EVENT", "enable_close_attempted_event", "",),
	("PSGVAL___ENABLE_EVENTS", FMAXPSG_SCTN0901_STR_DEF, "ENABLE_EVENTS", "enable_events", "",),
	("PSGVAL___ENABLE_EVENTS", FMAXPSG_SCTN0901_STR_DEF, "ENABLE_EVENTS", "enable_events", "",),
	("PSGVAL___EXPAND_X", FMAXPSG_SCTN0901_STR_DEF, "EXPAND_X", "expand_x", "",),
	("PSGVAL___EXPAND_Y", FMAXPSG_SCTN0901_STR_DEF, "EXPAND_Y", "expand_y", "",),
	("PSGVAL___FILE_TYPES", FMAXPSG_SCTN0901_STR_DEF, "FILE_TYPES", "file_types", "",),
	("PSGVAL___FINALIZE", FMAXPSG_SCTN0901_STR_DEF, "FINALIZE", "finalize", "",),
	("PSGVAL___FOCUS", FMAXPSG_SCTN0901_STR_DEF, "FOCUS", "focus", "",),
	("PSGVAL___FONT", FMAXPSG_SCTN0901_STR_DEF, "FONT", "font", "",),
	("PSGVAL___FORCE_TOPLEVEL", FMAXPSG_SCTN0901_STR_DEF, "FORCE_TOPLEVEL", "force_toplevel", "",),
	("PSGVAL___GRAB", FMAXPSG_SCTN0901_STR_DEF, "GRAB", "grab", "",),
	("PSGVAL___GRAB_ANYWHERE", FMAXPSG_SCTN0901_STR_DEF, "GRAB_ANYWHERE", "grab_anywhere", "",),
	("PSGVAL___HIGHLIGHT_COLORS", FMAXPSG_SCTN0901_STR_DEF, "HIGHLIGHT_COLORS", "highlight_colors", "",),
	("PSGVAL___ICON", FMAXPSG_SCTN0901_STR_DEF, "ICON", "icon", "",),
	("PSGVAL___IMAGE_DATA", FMAXPSG_SCTN0901_STR_DEF, "IMAGE_DATA", "image_data", "",),
	("PSGVAL___IMAGE_FILENAME", FMAXPSG_SCTN0901_STR_DEF, "IMAGE_FILENAME", "image_filename", "",),
	("PSGVAL___IMAGE_SIZE", FMAXPSG_SCTN0901_STR_DEF, "IMAGE_SIZE", "image_size", "",),
	("PSGVAL___IMAGE_SUBSAMPLE", FMAXPSG_SCTN0901_STR_DEF, "IMAGE_SUBSAMPLE", "image_subsample", "",),
	("PSGVAL___INITIAL_FOLDER", FMAXPSG_SCTN0901_STR_DEF, "INITIAL_FOLDER", "initial_folder", "",),
	("PSGVAL___JUSTIFICATION", FMAXPSG_SCTN0901_STR_DEF, "JUSTIFICATION", "justification", "",),
	("PSGVAL___K", FMAXPSG_SCTN0901_STR_DEF, "K", "k", "",),
	("PSGVAL___KEEP_ON_TOP", FMAXPSG_SCTN0901_STR_DEF, "KEEP_ON_TOP", "keep_on_top", "",),
	("PSGVAL___KEY", FMAXPSG_SCTN0901_STR_DEF, "KEY", "key", "",),
	("PSGVAL___LAYOUT", FMAXPSG_SCTN0901_STR_DEF, "LAYOUT", "layout", "",),
	("PSGVAL___LOCATION", FMAXPSG_SCTN0901_STR_DEF, "LOCATION", "location", "",),
	("PSGVAL___MARGINS", FMAXPSG_SCTN0901_STR_DEF, "MARGINS", "margins", "",),
	("PSGVAL___METADATA", FMAXPSG_SCTN0901_STR_DEF, "METADATA", "metadata", "",),
	("PSGVAL___MODAL", FMAXPSG_SCTN0901_STR_DEF, "MODAL", "modal", "",),
	("PSGVAL___NO_TITLEBAR", FMAXPSG_SCTN0901_STR_DEF, "NO_TITLEBAR", "no_titlebar", "",),
	("PSGVAL___PAD", FMAXPSG_SCTN0901_STR_DEF, "PAD", "pad", "",),
	("PSGVAL___PROGRESS_BAR_COLOR", FMAXPSG_SCTN0901_STR_DEF, "PROGRESS_BAR_COLOR", "progress_bar_color", "",),
	("PSGVAL___READONLY", FMAXPSG_SCTN0901_STR_DEF, "READONLY", "readonly", "",),
	("PSGVAL___RESIZABLE", FMAXPSG_SCTN0901_STR_DEF, "RESIZABLE", "resizable", "",),
	("PSGVAL___RETURN_KEYBOARD_EVENTS", FMAXPSG_SCTN0901_STR_DEF, "RETURN_KEYBOARD_EVENTS", "return_keyboard_events", "",),
	("PSGVAL___RIGHT_CLICK_MENU", FMAXPSG_SCTN0901_STR_DEF, "RIGHT_CLICK_MENU", "right_click_menu", "",),
	("PSGVAL___RIGHT_CLICK_MENU_BACKGROUND_COLOR", FMAXPSG_SCTN0901_STR_DEF, "RIGHT_CLICK_MENU_BACKGROUND_COLOR", "right_click_menu_background_color", "",),
	("PSGVAL___RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR", FMAXPSG_SCTN0901_STR_DEF, "RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR", "right_click_menu_disabled_text_color", "",),
	("PSGVAL___RIGHT_CLICK_MENU_FONT", FMAXPSG_SCTN0901_STR_DEF, "RIGHT_CLICK_MENU_FONT", "right_click_menu_font", "",),
	("PSGVAL___RIGHT_CLICK_MENU_SELECTED_COLORS", FMAXPSG_SCTN0901_STR_DEF, "RIGHT_CLICK_MENU_SELECTED_COLORS", "right_click_menu_selected_colors", "",),
	("PSGVAL___RIGHT_CLICK_MENU_TEAROFF", FMAXPSG_SCTN0901_STR_DEF, "RIGHT_CLICK_MENU_TEAROFF", "right_click_menu_tearoff", "",),
	("PSGVAL___RIGHT_CLICK_MENU_TEXT_COLOR", FMAXPSG_SCTN0901_STR_DEF, "RIGHT_CLICK_MENU_TEXT_COLOR", "right_click_menu_text_color", "",),
	("PSGVAL___S", FMAXPSG_SCTN0901_STR_DEF, "S", "s", "",),
	("PSGVAL___SCROLLABLE", FMAXPSG_SCTN0901_STR_DEF, "SCROLLABLE", "scrollable", "can this column be scrolled bool",),
	("PSGVAL___SET_TO_INDEX", FMAXPSG_SCTN0901_STR_DEF, "SET_TO_INDEX", "set_to_index", "change selection to a particular choice starting with index = 0",),
	("PSGVAL___SIZE", FMAXPSG_SCTN0901_STR_DEF, "SIZE", "size", "",),
	("PSGVAL___TARGET", FMAXPSG_SCTN0901_STR_DEF, "TARGET", "target", "",),
	("PSGVAL___TEXT", FMAXPSG_SCTN0901_STR_DEF, "TEXT", "text", "",),
	("PSGVAL___TEXT_COLOR", FMAXPSG_SCTN0901_STR_DEF, "TEXT_COLOR", "text_color", "",),
	("PSGVAL___TEXT_JUSTIFICATION", FMAXPSG_SCTN0901_STR_DEF, "TEXT_JUSTIFICATION", "text_justification", "",),
	("PSGVAL___TITLE", FMAXPSG_SCTN0901_STR_DEF, "TITLE", "title", "",),
	("PSGVAL___TITLEBAR_BACKGROUND_COLOR", FMAXPSG_SCTN0901_STR_DEF, "TITLEBAR_BACKGROUND_COLOR", "titlebar_background_color", "",),
	("PSGVAL___TITLEBAR_FONT", FMAXPSG_SCTN0901_STR_DEF, "TITLEBAR_FONT", "titlebar_font", "",),
	("PSGVAL___TITLEBAR_ICON", FMAXPSG_SCTN0901_STR_DEF, "TITLEBAR_ICON", "titlebar_icon", "",),
	("PSGVAL___TITLEBAR_TEXT_COLOR", FMAXPSG_SCTN0901_STR_DEF, "TITLEBAR_TEXT_COLOR", "titlebar_text_color", "",),
	("PSGVAL___TOOLTIP", FMAXPSG_SCTN0901_STR_DEF, "TOOLTIP", "tooltip", "",),
	("PSGVAL___TRANSPARENT_COLOR", FMAXPSG_SCTN0901_STR_DEF, "TRANSPARENT_COLOR", "transparent_color", "",),
	("PSGVAL___TTK_THEME", FMAXPSG_SCTN0901_STR_DEF, "TTK_THEME", "ttk_theme", "",),
	("PSGVAL___USE_CUSTOM_TITLEBAR", FMAXPSG_SCTN0901_STR_DEF, "USE_CUSTOM_TITLEBAR", "use_custom_titlebar", "",),
	("PSGVAL___USE_DEFAULT_FOCUS", FMAXPSG_SCTN0901_STR_DEF, "USE_DEFAULT_FOCUS", "use_default_focus", "",),
	("PSGVAL___USE_TTK_BUTTONS", FMAXPSG_SCTN0901_STR_DEF, "USE_TTK_BUTTONS", "use_ttk_buttons", "",),
	("PSGVAL___VALUE", FMAXPSG_SCTN0901_STR_DEF, "VALUE", "value", "the value of the element",),
	("PSGVAL___VALUES", FMAXPSG_SCTN0901_STR_DEF, "VALUES", "values", "list of values",),
	("PSGVAL___VERTICAL_ALIGNMENT", FMAXPSG_SCTN0901_STR_DEF, "VERTICAL_ALIGNMENT", "vertical_alignment", "",),
	("PSGVAL___VERTICAL_SCROLL_ONLY", FMAXPSG_SCTN0901_STR_DEF, "VERTICAL_SCROLL_ONLY", "verticale_scroll_only", "",),
	("PSGVAL___VISIBLE", FMAXPSG_SCTN0901_STR_DEF, "VISIBLE", "visible", "",),
	("PSGVAL___CIRCLE_COLOR", FMAXPSG_SCTN0901_STR_DEF, "CIRCLE_COLOR", "circle_color", "",),
	("PSGVAL___GROUP_ID", FMAXPSG_SCTN0901_STR_DEF, "GROUP_ID", "group_id", "",),
	("PSGVAL___INITIAL_VALUE", FMAXPSG_SCTN0901_STR_DEF, "INITIAL_VALUE", "INITIAL_VALUE", "",),
	("PSGVAL___CLICK_SUBMITS", FMAXPSG_SCTN0901_STR_DEF, "CLICK_SUBMITS", "click_submits", "",),
	("PSGVAL___RELIEF", FMAXPSG_SCTN0901_STR_DEF, "RELIEF", "relief", "",),
	("PSGVAL_____", FMAX_NOP, "FMPSG_BEGINS",),
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
]
TBGLST.sort()


# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# END OF TBGLST SCTN0105
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeAComment
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeAComment(comment_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""{CMNTLINE}{NEWLINE}# * {comment_}{NEWLINE}{CMNTLINE}{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeAComment
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeAWideComment(comment_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	"""Short summary.

	Parameters
	----------
	comment_ : string
			a string to be inserted in the middle of 7 lines, outer two are attention getters

	Returns
	-------
	string
		contains the comment_ and surrounding lines, plus two # lines above and below

"""
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""#{NEWLINE}#{NEWLINE}{CMNTLINE}{NEWLINE}# * {comment_}{NEWLINE}{CMNTLINE}{NEWLINE}#{NEWLINE}#{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeADict
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeADict(dictName_, dictComment_, dictItems_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""{dictName_} = {OBRCE}  # {dictComment_}
{dictItems_}{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# sortADict
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def sortADict(dictToSort_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	dictToRtn_ = {}
	for thisKey_ in sorted(dictToSort_.keys(), key=lambda KEY_: KEY_.lower()):
		dictToRtn_[thisKey_] = dictToSort_[thisKey_]
	return dictToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeAList
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeAList(listName_, listComment_, listItems_, listItemCmntDict_=None, addQuotes_=False):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""{listName_} = {OBRKT}  # {listComment_}{NEWLINE}"""
	for thisItem_ in listItems_:
		if listItemCmntDict_ is None:
			if addQuotes_ is True:
				strToRtn_ += f"""{NTAB(1)}{DBLQT}{thisItem_}{DBLQT}"""
			else:
				strToRtn_ += f"""{NTAB(1)}{thisItem_}"""
		else:
			if addQuotes_ is True:
				strToRtn_ += f"""{NTAB(1)}{DBLQT}{thisItem_}{DBLQT},  # {listItemCmntDict_[thisItem_]}{NEWLINE}"""
			else:
				strToRtn_ += f"""{NTAB(1)}{thisItem_},  # {listItemCmntDict_[thisItem_]}{NEWLINE}"""
	strToRtn_ += f"""{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeATupDict
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeANormalTupDict(tupDictName_, tupDictItems_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn1_ = ""

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	strToRtn_ += f"""{makeAComment(f"start of {tupDictName_} structures")}
{tupDictName_}TUP = {OPAREN}
{tupDictItems_}{CPAREN}{NEWLINE}{NEWLINE}def {tupDictName_}DICT{OPAREN}{CPAREN}:
{NTAB(1)}return dict{OPAREN}{OPAREN}x, y{CPAREN} for x, y in {tupDictName_}TUP{CPAREN}{NEWLINE}{NEWLINE}{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# makeASidecarTupDic
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def makeASidecarTupDic(tupDictName_, tupDictItems_, tupDictSidecars_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn1_ = ""
	strToRtn_ += f"""{makeAComment(f"start of {tupDictName_} structures")}{NEWLINE}"""
	for key_, items_ in tupDictSidecars_.items():
		strToRtn_ += f"""{tupDictName_}_{key_}TUP = {OPAREN}{NEWLINE}{items_}{CPAREN}{NEWLINE}{NEWLINE}"""
		strToRtn1_ += f"""{NTAB(1)}listToRtn_ = list((x) for x in {tupDictName_}_{key_}TUP){NEWLINE}"""
	strToRtn_ += f"""{tupDictName_}TUP = {OPAREN}
{tupDictItems_}{CPAREN}{NEWLINE}{NEWLINE}def {tupDictName_}DICT{OPAREN}{CPAREN}:
{NTAB(1)}dictToRtn_ = dict{OPAREN}{OPAREN}x, y{CPAREN} for x, y in {tupDictName_}TUP{CPAREN}{NEWLINE}{strToRtn1_}{NTAB(1)}return listToRtn_, dictToRtn_{NEWLINE}{NEWLINE}{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# makeAFullTupDict (sidecar is a single item list, or alist of strings that will be concatenated before substitution)
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def makeAFullTupDict(tupDictName_, tupDictItems_, tupDictSidecars_, tupDictParms_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

	subParmsStr_ = f"""{NTAB(1)}def {tupDictName_}_subParms(listIn_, tupDictParms_):
{NTAB(2)}listToRtn_ = []
{NTAB(2)}for thisStr_ in listIn_:
{NTAB(3)}for subParm_, replaceStr_ in tupDictParms_:
{NTAB(4)}thisStr_ = thisStr_.replace(subParm_, replaceStr_)
{NTAB(3)}listToRtn_.append(thisStr_)
{NTAB(2)}return listToRtn_{NEWLINE}{NEWLINE}"""

	strToRtn1_ = ""
	strToRtn2_ = ""
	sideCarToRtn = {}
	parmsNames_ = ""
	sideCar_ = {}

	for subParm_, replaceStr_ in tupDictParms_:
		parmsNames_ += f"""{replaceStr_}, """
	parmsNames_ = parmsNames_[:-2]

	strToRtn1_ += f"""{makeAComment(f"start of {tupDictName_} structures")}{NEWLINE}"""

	strToRtn3_ = f"""{NTAB(1)}{tupDictName_}_PARMS = {OBRKT}{NEWLINE}"""
	for subParm_, replaceStr_ in tupDictParms_:
		strToRtn3_ += f"""{NTAB(2)}{OPAREN}{DBLQT}{subParm_}{DBLQT}, {replaceStr_}{CPAREN},{NEWLINE}"""
	strToRtn3_ = strToRtn3_[:-1] + f"""{NEWLINE}{NTAB(1)}{CBRKT}{NEWLINE}"""

	for key_, items_ in tupDictSidecars_.items():
		strToRtn1_ += f"""{tupDictName_}_{key_}TUP = {OPAREN}{NEWLINE}{items_}{CPAREN}{NEWLINE}{NEWLINE}"""
		strToRtn2_ += f"""{NTAB(1)}listToRtn_ = list((x) for x in {tupDictName_}_{key_}TUP){NEWLINE}"""
		strToRtn2_ += f"""{NTAB(1)}listToRtn_ = CF.subParms(listToRtn_, {tupDictName_}_PARMS)"""
	strToRtn1_ += f"""{tupDictName_}TUP = {OPAREN}
{tupDictItems_}{CPAREN}{NEWLINE}{NEWLINE}def {tupDictName_}DICT{OPAREN}{parmsNames_}{CPAREN}:{NEWLINE}{strToRtn3_}
{NTAB(1)}dictToRtn_ = dict{OPAREN}{OPAREN}x, y{CPAREN} for x, y in {tupDictName_}TUP{CPAREN}{NEWLINE}"""

	strToRtn1_ += f"""{strToRtn2_}{NEWLINE}{NTAB(1)}return listToRtn_, dictToRtn_{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1
	return strToRtn1_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# readFileToStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def readFileToStr(FILENAME_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	with open(FILENAME_, "tr") as FDIN:
		strToRtn_ += FDIN.read()
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# doErrorItem
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doErrorItem(message_, itemToError_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	print(f"""{NEWLINE}{message_}{NEWLINE}is a tuple {isinstance(itemToError_, tuple)}{NEWLINE}item as parsed{NEWLINE}{repr(itemToError_)}{NEWLINE}""")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# explodeItem
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def explodeItem(itemToExplode_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""{NTAB(1)}{OPAREN}{DBLQT}{itemToExplode_[0]}{DBLQT}, {itemToExplode_[1]}, """
	for TI1_ in range(2, len(itemToExplode_)):
		strToRtn_ += f"""{DBLQT}{itemToExplode_[TI1_]}{DBLQT}, """
	strToRtn_ = f"""{strToRtn_[:-1]}{CPAREN},{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# FMCF_MAKE_BEGINS
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeCF
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeCF():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""{readFileToStr(CFTOP_NAME)}{readFileToStr(SCTN0102NAME)}"""

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	strToRtn_ += f"""{makeAComment("SCTN0201 CF defines")}"""
	dictToUse_ = sortADict(FMCF_SCTN0201_DEFDICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMCF_SCTN0201_DEFCMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	strToRtn_ += f"""{makeAComment("SCTN0202 options structures")}"""
	strToRtn1_ = ""
	strToRtn2_ = ""
	strToRtn1_ += f"""OPTIONS = {OBRCE}{NEWLINE}{FOLD1STARTHERELN}"""
	strToRtn2_ += f"""OPTIONSHELPDICT = {OBRCE}{NEWLINE}{FOLD1STARTHERELN}"""
	dictToUse_ = sortADict(FMCF_SCTN0202_OPTIONSDICT)
	for thisName_, values_ in dictToUse_.items():
		strToRtn1_ += f"""{NTAB(1)}{DBLQT}{thisName_}{DBLQT}: {OBRCE}{NEWLINE}{NTAB(1)}{FOLD2STARTHERELN}{values_}{NTAB(1)}{CBRCE},{NEWLINE}{NTAB(1)}{FOLD2ENDHERELN}"""
		strToRtn2_ += f"""{NTAB(1)}{DBLQT}{thisName_}{DBLQT}: {NEWLINE}{NTAB(1)}{FOLD2STARTHERELN}{TRIQT}{FMCF_SCTN0202_OPTIONSHELPDICT[thisName_]}{NTAB(1)}{TRIQT},{NEWLINE}{NTAB(1)}{FOLD2ENDHERELN}"""
	strToRtn1_ += f"""{CBRCE}{NEWLINE}{FOLD1ENDHERELN}{NEWLINE}"""
	strToRtn2_ += f"""{CBRCE}{NEWLINE}{FOLD1ENDHERELN}{NEWLINE}"""
	strToRtn_ += f"""{strToRtn1_}{strToRtn2_}"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
	strToRtn_ += f"""OPTIONSDICT = {OBRCE}{NEWLINE}"""
	dictToUse_ = sortADict(FMCF_SCTN0202_OPTIONSDICTDICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{value_}"""
	strToRtn_ += f"""{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"""
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	strToRtn_ += f"""{makeAWideComment("end of managed sections of CF.py")}{NEWLINE}{NEWLINE}"""
	return strToRtn_

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
# FMCF_MAKE_ENDS


# FMFM_MAKE_BEGINS
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeFM
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeFM():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	strToRtn_ = ""
	strToRtn_ += f"""{readFileToStr(FMTOP_NAME)}{readFileToStr(SCTN0102NAME)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN003 TYPEs and lambda")}"""
	dictToUse_ = sortADict(FMCF_SCTN0003_TYPEDICT)
	for thisName_, value_ in dictToUse_.items():
		value_ = FMCF_SCTN0003_TYPEDICT[thisName_]
		strToRtn_ += f"""{thisName_} = {value_}  # {FMCF_SCTN0003_TYPECMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += NEWLINE + NEWLINE

	## ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN101 FMAX _DEF_")}"""
	strToRtn01_ = ""
	dictToUse_ = sortADict(FMFM_SCTN0101_AXDICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMFM_SCTN0101_AXCMNTDICT[thisName_]}{NEWLINE}"""
		strToRtn01_ += f"""{NTAB(1)}{thisName_},  # {FMFM_SCTN0101_AXCMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}FMAXFM_AXLST = {OBRKT}{NEWLINE}{strToRtn01_}{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN102 VAL _DEF_")}"""
	strToRtn01_ = ""
	dictToUse_ = sortADict(FMFM_SCTN0102_VALDICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMFM_SCTN0102_VALCMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN103 _DICT_ _DEF_")}"""
	strToRtn01_ = ""
	dictToUse_ = sortADict(FMFM_SCTN0103_DICTDICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {OBRCE}{CBRCE}  # {FMFM_SCTN0103_DICTCMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN104 _LIST_ _DEF_")}"""
	dictToUse_ = sortADict(FMFM_SCTN0104_LISTDICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMFM_SCTN0104_LISTCMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}{makeAWideComment("end of managed portions of FM.py")}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{NTAB(1)}global {BKSLSH}{NEWLINE}"""

	dictToUse_ = sortADict(FMFM_SCTN0102_VALDICT)
	for name_, value_ in dictToUse_.items():
		strToRtn_ += f"""{NTAB(2)}{name_}, {BKSLSH}{NEWLINE}"""

	dictToUse_ = sortADict(FMFM_SCTN0103_DICTDICT)
	for name_, value_ in dictToUse_.items():
		strToRtn_ += f"""{NTAB(2)}{name_}, {BKSLSH}{NEWLINE}"""

	dictToUse_ = sortADict(FMFM_SCTN0104_LISTDICT)
	for name_, value_ in dictToUse_.items():
		strToRtn_ += f"""{NTAB(2)}{name_}, {BKSLSH}{NEWLINE}"""

	strToRtn_ = f"""{strToRtn_[:-4]}{NEWLINE}"""

	return strToRtn_
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
# FMFM_MAKE_ENDS


# FMPSG_MAKE_BEGINS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# makePSG
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def makePSG():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{readFileToStr(f"{PSGTOP_NAME}")}{makeAComment("SCTN0900 DEF1")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0900_DEF1DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMPSG_SCTN0900_DEF1CMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0901 DEF2")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0901_DEF2DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMPSG_SCTN0901_DEF2CMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0902 dicts")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0902_DICTDICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeADict(thisName_, FMPSG_SCTN0902_DICTCMNTDICT[thisName_], value_)}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0903 lists")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0903_LISTDICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeAList(thisName_, FMPSG_SCTN0903_LISTCMNTDICT[thisName_], value_)}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0904 platform equalizers")}"""
	dictToUseOuter_ = sortADict(FMPSG_SCTN0904_PLATEQOUTERDICT)
	dictToUseInner_ = sortADict(FMPSG_SCTN0904_PLATEQINNERDICT)
	for thisouterKey, outerVal_ in dictToUseOuter_.items():
		strToRtn_ += f""""""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0905 tupdict")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0905_TUPDICTDICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeANormalTupDict(thisName_, value_)}"""

	strToRtn_ += f"""{makeAWideComment("end of managed sections of PSG.py")}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# parseTBGLST
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def parseTBGLST(FDTBGLST):
	global \
		FMCF_SCTN0003_TYPECMNTDICT, \
		FMCF_SCTN0003_TYPEDICT, \
		FMCF_SCTN0201_DEFCMNTDICT, \
		FMCF_SCTN0201_DEFDICT, \
		FMCF_SCTN0202_OPTIONSCMNTDICT, \
		FMCF_SCTN0202_OPTIONSDICT, \
		FMCF_SCTN0202_OPTIONSDICTCMNTDICT, \
		FMCF_SCTN0202_OPTIONSDICTDICT, \
		FMCF_SCTN0202_OPTIONSHELPDICT, \
		FMCF_SCTN0203_DICTCMNTDICT, \
		FMCF_SCTN0203_DICTDICT, \
		FMCF_SCTN0204_LISTCMNTDICT, \
		FMCF_SCTN0204_LISTDICT, \
		FMFM_SCTN0101_AXCMNTDICT, \
		FMFM_SCTN0101_AXDICT, \
		FMFM_SCTN0102_VALCMNTDICT, \
		FMFM_SCTN0102_VALDICT, \
		FMFM_SCTN0103_DICTCMNTDICT, \
		FMFM_SCTN0103_DICTDICT, \
		FMFM_SCTN0104_LISTCMNTDICT, \
		FMFM_SCTN0104_LISTDICT, \
		FMPSG_SCTN0900_DEF1CMNTDICT, \
		FMPSG_SCTN0900_DEF1DICT, \
		FMPSG_SCTN0901_DEF2CMNTDICT, \
		FMPSG_SCTN0901_DEF2DICT, \
		FMPSG_SCTN0902_DICTCMNTDICT, \
		FMPSG_SCTN0902_DICTDICT, \
		FMPSG_SCTN0903_LISTCMNTDICT, \
		FMPSG_SCTN0903_LISTDICT, \
		FMPSG_SCTN0904_PLATEQINNERCMNTDICT, \
		FMPSG_SCTN0904_PLATEQINNERDICT, \
		FMPSG_SCTN0904_PLATEQOUTERCMNTDICT, \
		FMPSG_SCTN0904_PLATEQOUTERDICT, \
		FMPSG_SCTN0905_TUPDICTCMNTDICT, \
		FMPSG_SCTN0905_TUPDICTDICT, \
		FMPSG_SCTN0906_BTNSCMNTDICT, \
		FMPSG_SCTN0906_BTNSDICT, \
		FMPSG_SCTN0908_CHECKBOXCMNTDICT, \
		FMPSG_SCTN0908_CHECKBOXDICT, \
		FMPSG_SCTN0909_TEXTCMNTDICT, \
		FMPSG_SCTN0909_TEXTDICT, \
		FMPSG_SCTN090A_COLUMNSCMNTDICT, \
		FMPSG_SCTN090A_COLUMNSDICT, \
		FMPSG_SCTN090B_LAYOUTCMNTDICT, \
		FMPSG_SCTN090B_LAYOUTDICT, \
		FMPSG_SCTN090C_WINDOWCMNTDICT, \
		FMPSG_SCTN090C_WINDOWDICT, \
		FMPSG_SCTN090D_FRAMECMNTDICT, \
		FMPSG_SCTN090D_FRAMEDICT, \
		FMPSG_SCTN090E_MAINCMNTDICT, \
		FMPSG_SCTN090E_MAINDICT, \
		FMPSG_SCTN090E_MAINDICTDICT
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	for thisItem_ in TBGLST:
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ for thisItem_ in TBGLST:

		FDTBGLST.write(f"{explodeItem(thisItem_)}")
		thisItemLen_ = len(thisItem_)
		if thisItemLen_ < 3:
			doErrorItem("fewer than 3 elements", thisItem_)
			continue
		if not isinstance(thisItem_, tuple):
			doErrorItem("not a tuple", thisItem_)
			continue
		thisName_ = thisItem_[0]
		thisAX_ = thisItem_[1]
		thisComment_ = thisItem_[-1]
		if thisAX_ not in FMAXFM_AXLST:
			doErrorItem("not a supported action in FM", thisItem_)
			continue

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		if thisAX_ is None or thisAX_ == FMAX_NOP:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# FMCF_PARSE_BEGINS
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0003_LAMBDA_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisLambdaName_ = thisItem_[2]
			thisLambdaVal_ = thisItem_[3]
			FMCF_SCTN0003_TYPEDICT[thisLambdaName_] = f"lambda {thisLambdaVal_}"
			FMCF_SCTN0003_TYPECMNTDICT[thisLambdaName_] = "{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0003_TYPE_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisTypeName_ = thisItem_[2]
			thisType_ = thisItem_[3]
			FMCF_SCTN0003_TYPEDICT[thisTypeName_] = f"{DBLQT}{thisType_}{DBLQT}"
			FMCF_SCTN0003_TYPECMNTDICT[thisTypeName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0201_STR_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0201_DEFDICT[thisValName_] = f"{DBLQT}{thisVal_}{DBLQT}"
			FMCF_SCTN0201_DEFCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0201_VAL_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0201_DEFDICT[thisValName_] = f"{thisVal_}"
			FMCF_SCTN0201_DEFCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0202_OPTIONS_ADD_HELP_LINE:  # define a '-a[=]' in SCTN22 <NAC><KEY><PARM><VAL>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisParm_ = thisItem_[2]
			if thisParm_ not in FMCF_SCTN0202_OPTIONSHELPDICT:
				FMCF_SCTN0202_OPTIONSHELPDICT[thisParm_] = ""
			FMCF_SCTN0202_OPTIONSHELPDICT[thisParm_] += f"""{thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0202_OPTIONS_STR_ADD:  # define a '-a[=]' in SCTN22 <NAC><KEY><PARM><VAL>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisParm_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisParm_ not in FMCF_SCTN0202_OPTIONSDICT:
				FMCF_SCTN0202_OPTIONSDICT[thisParm_] = ""
			if thisParm_ not in FMCF_SCTN0202_OPTIONSHELPDICT:
				FMCF_SCTN0202_OPTIONSHELPDICT[thisParm_] = ""
			FMCF_SCTN0202_OPTIONSDICT[thisParm_] += f"""{NTAB(2)}{DBLQT}{thisKey_}{DBLQT}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			FMCF_SCTN0202_OPTIONSHELPDICT[thisParm_] += f"""{thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0202_OPTIONS_VAL_ADD:  # define a '-a[=]' in SCTN22 <NAC><KEY><PARM><VAL>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisParm_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisParm_ not in FMCF_SCTN0202_OPTIONSDICT:
				FMCF_SCTN0202_OPTIONSDICT[thisParm_] = ""
			if thisParm_ not in FMCF_SCTN0202_OPTIONSHELPDICT:
				FMCF_SCTN0202_OPTIONSHELPDICT[thisParm_] = ""
			FMCF_SCTN0202_OPTIONSDICT[thisParm_] += f"""{NTAB(2)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			FMCF_SCTN0202_OPTIONSHELPDICT[thisParm_] += f"""{thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD:  # define a OPTNAME: 'str' in SCTN202 <NAC><KEY><STRDEFAULT>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisKey_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0202_OPTIONSDICTDICT[thisName_] = f"{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD:  # define a OPTNAME: VAL in SCTN202 <NAC><KEY><VALDEFAULT>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisKey_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0202_OPTIONSDICTDICT[thisName_] = f"{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0204_LIST_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			FMCF_SCTN0204_LISTDICT[thisListName_] = ""
			FMCF_SCTN0204_LISTCMNTDICT[thisListName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0204_LIST_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0204_LISTDICT[thisListName_] += f"{NTAB(1)}f{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0204_LIST_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0204_LISTDICT[thisListName_] += f"{NTAB(1)}{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0204_LIST_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0204_LISTDICT[thisListName_] += f"{NTAB(1)}{thisVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# FMCF_PARSE_ENDS

	# FMFM_PARSE_BEGINS
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0101_AX_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMFM_SCTN0101_AXDICT[thisName_] = f"{DBLQT}{thisName_}{DBLQT}"
			FMFM_SCTN0101_AXCMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0102_STR_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMFM_SCTN0102_VALDICT[thisValName_] = f"""{DBLQT}{thisVal_}{DBLQT}"""
			FMFM_SCTN0102_VALCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0102_VAL_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMFM_SCTN0102_VALDICT[thisValName_] = thisVal_
			FMFM_SCTN0102_VALCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0103_DICT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMFM_SCTN0103_DICTDICT[thisName_] = f"{OBRCE}{CBRCE}"
			FMFM_SCTN0103_DICTCMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0104_LIST_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMFM_SCTN0104_LISTDICT[thisName_] = f"{OBRKT}{CBRKT}"
			FMFM_SCTN0104_LISTCMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# FMFM_PARSE_ENDS

	# FMAXPSG_PARSE_BEGINS
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0900_STR_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMPSG_SCTN0900_DEF1DICT[thisValName_] = f"""{DBLQT}{thisVal_}{DBLQT}"""
			FMPSG_SCTN0900_DEF1CMNTDICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0900_VAL_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMPSG_SCTN0900_DEF1DICT[thisValName_] = f"""{thisVal_}"""
			FMPSG_SCTN0900_DEF1CMNTDICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0901_DUBLTSSDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal1_ = thisItem_[3]
			thisVal2_ = thisItem_[4]
			FMPSG_SCTN0901_DEF2DICT[thisValName_] = f"""{OPAREN}{DBLQT}{thisVal1_}{DBLQT}, {DBLQT}{thisVal2_}{DBLQT}{CPAREN},"""
			FMPSG_SCTN0901_DEF2CMNTDICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0901_DUBLTSVDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal1_ = thisItem_[3]
			thisVal2_ = thisItem_[4]
			FMPSG_SCTN0901_DEF2DICT[thisValName_] = f"""{OPAREN}{DBLQT}{thisVal1_}{DBLQT}, {thisVal2_}{CPAREN},"""
			FMPSG_SCTN0901_DEF2CMNTDICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0901_DUBLTVSDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal1_ = thisItem_[3]
			thisVal2_ = thisItem_[4]
			FMPSG_SCTN0901_DEF2DICT[thisValName_] = f"""{OPAREN}{thisVal1_}, {DBLQT}{thisVal2_}{DBLQT}{CPAREN},"""
			FMPSG_SCTN0901_DEF2CMNTDICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0901_DUBLTVVDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal1_ = thisItem_[3]
			thisVal2_ = thisItem_[4]
			FMPSG_SCTN0901_DEF2DICT[thisValName_] = f"""{OPAREN}{thisVal1_}, {thisVal2_}{CPAREN}"""
			FMPSG_SCTN0901_DEF2CMNTDICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0901_KEY_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			FMPSG_SCTN0901_DEF2DICT[thisValName_] = f"""{DBLQT}{thisValName_}{DBLQT}"""
			FMPSG_SCTN0901_DEF2CMNTDICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0901_STR_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMPSG_SCTN0901_DEF2DICT[thisValName_] = f"""{DBLQT}{thisVal_}{DBLQT}"""
			FMPSG_SCTN0901_DEF2CMNTDICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0901_VAL_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMPSG_SCTN0901_DEF2DICT[thisValName_] = f"""{thisVal1_}"""
			FMPSG_SCTN0901_DEF2CMNTDICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0902_DICT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			if thisDictName_ not in FMPSG_SCTN0902_DICTDICT:
				FMPSG_SCTN0902_DICTDICT[thisDictName_] = ""
			FMPSG_SCTN0902_DICTCMNTDICT[thisDictName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0902_DICT_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMPSG_SCTN0902_DICTDICT:
				FMPSG_SCTN0902_DICTDICT[thisDictName_] = ""
			FMPSG_SCTN0902_DICTDICT[thisDictName_] += f"""{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0902_DICT_STRSTR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMPSG_SCTN0902_DICTDICT:
				FMPSG_SCTN0902_DICTDICT[thisDictName_] = ""
			FMPSG_SCTN0902_DICTDICT[thisDictName_] += f"""{NTAB(1)}{DBLQT}{thisKey_}{DBLQT}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0902_DICT_STRVAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMPSG_SCTN0902_DICTDICT:
				FMPSG_SCTN0902_DICTDICT[thisDictName_] = ""
			FMPSG_SCTN0902_DICTDICT[thisDictName_] += f"""{NTAB(1)}{DBLQT}{thisKey_}{DBLQT}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0902_DICT_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMPSG_SCTN0902_DICTDICT:
				FMPSG_SCTN0902_DICTDICT[thisDictName_] = ""
			FMPSG_SCTN0902_DICTDICT[thisDictName_] += f"""{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0903_LISTDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			if thisListName_ not in FMPSG_SCTN0903_LISTDICT:
				FMPSG_SCTN0903_LISTDICT[thisListName_] = ""
			FMPSG_SCTN0903_LISTCMNTDICT[thisListName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0903_LISTSTRADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			if thisListName_ not in FMPSG_SCTN0903_LISTDICT:
				FMPSG_SCTN0903_LISTDICT[thisListName_] = ""
			FMPSG_SCTN0903_LISTDICT[thisListName_] += f"""{NTAB(1)}{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0903_LISTVALADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			if thisListName_ not in FMPSG_SCTN0903_LISTDICT:
				FMPSG_SCTN0903_LISTDICT[thisListName_] = ""
			FMPSG_SCTN0903_LISTDICT[thisListName_] += f"""{NTAB(1)}{thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0904_PLATEQPLATDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisPlatEqName_ = thisItem_[2]
			thisPlatEqKey_ = thisItem_[3]
			thisPlatEqCondition_ = thisItem_[4]
			if thisPlatEqName_ not in FMPSG_SCTN0904_PLATEQOUTERDICT:
				FMPSG_SCTN0904_PLATEQOUTERDICT[thisPlatEqName_] = ""
			FMPSG_SCTN0904_PLATEQOUTERDICT[thisPlatEqName_] = f"""{thisPlatEqKey_} = {thisPlatEqCondition_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0905_TUPDICTDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisTupdictName_ = thisItem_[2]
			if thisTupdictName_ not in FMPSG_SCTN0905_TUPDICTDICT:
				FMPSG_SCTN0905_TUPDICTDICT[thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICTCMNTDICT[thisTupdictName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0905_TUPDICTSTRADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisTupdictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisTupdictName_ not in FMPSG_SCTN0905_TUPDICTDICT:
				FMPSG_SCTN0905_TUPDICTDICT[thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICTDICT[thisTupdictName_] += f"""{NTAB(1)}{OPAREN}{thisKey_}, {DBLQT}{thisVal_}{DBLQT}{CPAREN},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0905_TUPDICTSTRSTRADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisTupdictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisTupdictName_ not in FMPSG_SCTN0905_TUPDICTDICT:
				FMPSG_SCTN0905_TUPDICTDICT[thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICTDICT[thisTupdictName_] += f"""{NTAB(1)}{OPAREN}{DBLQT}{thisKey_}{DBLQT}, {DBLQT}{thisVal_}{DBLQT}{CPAREN},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0905_TUPDICTSTRVALADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisTupdictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisTupdictName_ not in FMPSG_SCTN0905_TUPDICTDICT:
				FMPSG_SCTN0905_TUPDICTDICT[thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICTDICT[thisTupdictName_] += f"""{NTAB(1)}{OPAREN}{DBLQT}{thisKey_}{DBLQT}, {thisVal_}{CPAREN},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0905_TUPDICTVALADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisTupdictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisTupdictName_ not in FMPSG_SCTN0905_TUPDICTDICT:
				FMPSG_SCTN0905_TUPDICTDICT[thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICTDICT[thisTupdictName_] += f"""{NTAB(1)}{OPAREN}{thisKey_}, {thisVal_}{CPAREN},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# __main__
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def __main__():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

	# FMFM_MAIN_BEGINS
	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	with open(TBGLST_NAME, "tw") as FDOut:
		FDOut.write(f"TBGLST = {OBRKT}{NEWLINE}{NTAB(1)}{FOLD1STARTHERE}{NEWLINE}")
		parseTBGLST(FDOut)
		FDOut.write(f"{NTAB(1)}{FOLD1ENDHERE}{NEWLINE}{CBRKT}{NEWLINE}")

	with open(FM_NAME, "tw") as FDOut:
		strToWrt_ = makeFM()
		FDOut.writelines(strToWrt_)
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# FMFM_MAIN_ENDS

	# FMCF_MAIN_BEGINS
	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	with open(CF_NAME, "tw") as FDOut:
		strToWrt_ = makeCF()
		FDOut.writelines(strToWrt_)
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# FMCF_MAIN_ENDS

	# FMPSG_MAIN_BEGINS
	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	with open(PSG_NAME, "tw") as FDOut:
		strToWrt_ = makePSG()
		FDOut.writelines(strToWrt_)
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# FMPSG_MAIN_ENDS

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


if __name__ == "__main__":
	__main__()


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# end of FM.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#
