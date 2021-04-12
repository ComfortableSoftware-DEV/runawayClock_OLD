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
SCTNSNAME = f"""{CONFIGDIR}SCTNS.py"""
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
FMAXCF_SCTN0003_LAMBDADEF = "FMAXCF_SCTN0003_LAMBDADEF"  # define a lambda function <NAC><NAME><lambda str>
FMAXCF_SCTN0003_TYPEDEF = "FMAXCF_SCTN0003_TYPEDEF"  # define a fake type used in the translation dict <NAC><NAME><TYPE>
FMAXCF_SCTN0201_STRDEF = "FMAXCF_SCTN0201_STRDEF"  # define a STR in SCTN21 <NAC><NAME><str>
FMAXCF_SCTN0201_VALDEF = "FMAXCF_SCTN0201_VALDEF"  # define a VAL in SCTN21 <NAC><NAME><VAL>
FMAXCF_SCTN0202_OPTIONSADDHELPLINE = "FMAXCF_SCTN0202_OPTIONSADDHELPLINE"  # add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>
FMAXCF_SCTN0202_OPTIONSDICTSTRADD = "FMAXCF_SCTN0202_OPTIONSDICTSTRADD"  # define a OPTNAME: 'str' in SCTN202 <NAC><KEY><PARM><STRDEFAULT>
FMAXCF_SCTN0202_OPTIONSDICTVALADD = "FMAXCF_SCTN0202_OPTIONSDICTVALADD"  # define a OPTNAME: VAL in SCTN202 <NAC><KEY><PARM><VALDEFAULT>
FMAXCF_SCTN0202_OPTIONSSTRADD = "FMAXCF_SCTN0202_OPTIONSSTRADD"  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
FMAXCF_SCTN0202_OPTIONSVALADD = "FMAXCF_SCTN0202_OPTIONSVALADD"  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
FMAXCF_SCTN0203_DICTDEF = "FMAXCF_SCTN0203_DICTDEF"  # define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>
FMAXCF_SCTN0203_DICTSTRADD = "FMAXCF_SCTN0203_DICTSTRADD"  # define a dict STR in SCTN203 <NAC><DICTNAME><STR>
FMAXCF_SCTN0203_DICTVALADD = "FMAXCF_SCTN0203_DICTVALADD"  # define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>
FMAXCF_SCTN0204_LISTDEF = "FMAXCF_SCTN0204_LISTDEF"  # define a list in SCTN204 <NAC><LISTNAME>
FMAXCF_SCTN0204_LISTSTRADD = "FMAXCF_SCTN0204_LISTSTRADD"  # define a list STR in SCTN204 <NAC><LISTNAME><STR>
FMAXCF_SCTN0204_LISTVALADD = "FMAXCF_SCTN0204_LISTVALADD"  # define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>
FMAXFM_SCTN0101_AXDEF = "FMAXFM_SCTN0101_AXDEF"  # define a new FM action <NAC>
FMAXFM_SCTN0102_STRDEF = "FMAXFM_SCTN0102_STRDEF"  # define a FM string <NAC><VALNAME><STR>
FMAXFM_SCTN0102_VALDEF = "FMAXFM_SCTN0102_VALDEF"  # define a FM value_ <NAC><VALNAME><VAL>
FMAXFM_SCTN0103_DICTDEF = "FMAXFM_SCTN0103_DICTDEF"  # define a dict for FM <NAC>
FMAXFM_SCTN0104_LISTDEF = "FMAXFM_SCTN0104_LISTDEF"  # define a list in FM <NAC>
FMAXPSG_SCTN0900_STRDEF = "FMAXPSG_SCTN0900_STRDEF"  # define a string in the first section (colors, etc.) of defines in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0900_VALDEF = "FMAXPSG_SCTN0900_VALDEF"  # define a value in the first define section in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0901_DUBLTSSDEF = "FMAXPSG_SCTN0901_DUBLTSSDEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0901_DUBLTSVDEF = "FMAXPSG_SCTN0901_DUBLTSVDEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0901_DUBLTVSDEF = "FMAXPSG_SCTN0901_DUBLTVSDEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0901_DUBLTVVDEF = "FMAXPSG_SCTN0901_DUBLTVVDEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0901_KEYDEF = "FMAXPSG_SCTN0901_KEYDEF"  # define a key in the second section of defines in PSG.py <NAC><VALNAME>
FMAXPSG_SCTN0901_STRDEF = "FMAXPSG_SCTN0901_STRDEF"  # define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0901_VALDEF = "FMAXPSG_SCTN0901_VALDEF"  # define a value in the second define section in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0902_DICTDEF = "FMAXPSG_SCTN0902_DICTDEF"  # define a dict in PSG <NAC><DICTNAME>
FMAXPSG_SCTN0902_DICTSTRADD = "FMAXPSG_SCTN0902_DICTSTRADD"  # add a str to a dict <NAC><DICTNAME><KEY><VAL>
FMAXPSG_SCTN0902_DICTSTRSTRADD = "FMAXPSG_SCTN0902_DICTSTRSTRADD"  # add a str-str to a dict <NAC><DICTNAME><STR><STR>
FMAXPSG_SCTN0902_DICTSTRVALADD = "FMAXPSG_SCTN0902_DICTSTRVALADD"  # add a str-val to a dict <NAC><DICTNAME><STR><VAL>
FMAXPSG_SCTN0902_DICTVALADD = "FMAXPSG_SCTN0902_DICTVALADD"  # add a val to a dict in PSG <NAC><DICTNAME><KEY><VAL>
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


FMAXFM_AXLST = [
	FMAX_NOP,  # skip this entry
	FMAXCF_SCTN0003_LAMBDADEF,  # define a lambda function <NAC><NAME><lambda str>
	FMAXCF_SCTN0003_TYPEDEF,  # define a fake type used in the translation dict <NAC><NAME><TYPE>
	FMAXCF_SCTN0201_STRDEF,  # define a STR in SCTN21 <NAC><NAME><str>
	FMAXCF_SCTN0201_VALDEF,  # define a VAL in SCTN21 <NAC><NAME><VAL>
	FMAXCF_SCTN0202_OPTIONSADDHELPLINE,  # add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>
	FMAXCF_SCTN0202_OPTIONSDICTSTRADD,  # define a OPTNAME: 'str' in SCTN202 <NAC><KEY><PARM><STRDEFAULT>
	FMAXCF_SCTN0202_OPTIONSDICTVALADD,  # define a OPTNAME: VAL in SCTN202 <NAC><KEY><PARM><VALDEFAULT>
	FMAXCF_SCTN0202_OPTIONSSTRADD,  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
	FMAXCF_SCTN0202_OPTIONSVALADD,  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
	FMAXCF_SCTN0203_DICTDEF,  # define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>
	FMAXCF_SCTN0203_DICTSTRADD,  # define a dict STR in SCTN203 <NAC><DICTNAME><STR>
	FMAXCF_SCTN0203_DICTVALADD,  # define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>
	FMAXCF_SCTN0204_LISTDEF,  # define a list in SCTN204 <NAC><LISTNAME>
	FMAXCF_SCTN0204_LISTSTRADD,  # define a list STR in SCTN204 <NAC><LISTNAME><STR>
	FMAXCF_SCTN0204_LISTVALADD,  # define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>
	FMAXFM_SCTN0101_AXDEF,  # define a new FM action <NAC>
	FMAXFM_SCTN0102_STRDEF,  # define a FM string <NAC><VALNAME><STR>
	FMAXFM_SCTN0102_VALDEF,  # define a FM value_ <NAC><VALNAME><VAL>
	FMAXFM_SCTN0103_DICTDEF,  # define a dict for FM <NAC>
	FMAXFM_SCTN0104_LISTDEF,  # define a list in FM <NAC>
	FMAXPSG_SCTN0900_STRDEF,  # define a string in the first section (colors, etc.) of defines in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0900_VALDEF,  # define a value in the first define section in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0901_DUBLTSSDEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0901_DUBLTSVDEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0901_DUBLTVSDEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0901_DUBLTVVDEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0901_KEYDEF,  # define a key in the second section of defines in PSG.py <NAC><VALNAME>
	FMAXPSG_SCTN0901_STRDEF,  # define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0901_VALDEF,  # define a value in the second define section in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0902_DICTDEF,  # define a dict in PSG <NAC><DICTNAME>
	FMAXPSG_SCTN0902_DICTSTRADD,  # add a str to a dict <NAC><DICTNAME><KEY><VAL>
	FMAXPSG_SCTN0902_DICTSTRSTRADD,  # add a str-str to a dict <NAC><DICTNAME><STR><STR>
	FMAXPSG_SCTN0902_DICTSTRVALADD,  # add a str-val to a dict <NAC><DICTNAME><STR><VAL>
	FMAXPSG_SCTN0902_DICTVALADD,  # add a val to a dict in PSG <NAC><DICTNAME><KEY><VAL>
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
FMPSG_SCTN0900_DEFCMNTDICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0900_DEFDICT = {}  # define the dict to hold everything in SCTN0900
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


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN104 _LIST_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMFM_SCTN0004_BTNSHOLDABLELIST = []  # buttons holdable list


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed portions of FM.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


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
		FMPSG_SCTN0900_DEFCMNTDICT, \
		FMPSG_SCTN0900_DEFDICT, \
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
		FMFM_SCTN0004_BTNSHOLDABLELIST
