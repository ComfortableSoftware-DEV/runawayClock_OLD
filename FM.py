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
CRSTR = "\r"  # carriage return
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
USER_CACHE_DIR = "/home/will/.cache/"
USER_CONFIG_DIR = "/home/will/.config/"


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
DO_NAME = "newDO.py"
DOHBI_NAME = "newDOHBI.py"
DOHBIBTM_NAME = f"""{CONFIGDIR}DO_HBIBTM.py"""
DOHBITOP_NAME = f"""{CONFIGDIR}DO_HBITOP.py"""
DOTOP_NAME = f"""{CONFIGDIR}DOTOP.py"""
EEOL = f"""{ESC}[K"""
EMPTY_DICT = {}
EMPTY_LIST = []
EMPTY_STR = ""
EMPTY_TUPLE = ()
EMPTYSTRLST = [None, "", DBLQT, f"""{DBLQT}{DBLQT}""", SGLQT, f"""{SGLQT}{SGLQT}""", BKQT, "None", "\r", NEWLINE, "\r\n", "\n\r", ]
FM_NAME = "newFM.py"
FMTOP_NAME = f"""{CONFIGDIR}FMTOP.py"""
FO_NAME = "newFO.py"
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
NCR = lambda NUM_: f"""{CRSTR * NUM_}"""
NNL = lambda NUM_: f"""{NEWLINE * NUM_}"""
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
USER_CACHE_URL = lambda FILENAME_: f"""{USER_CACHE_DIR}{FILENAME_}"""
USER_CONFIG_URL = lambda FILENAME_: f"""{USER_CONFIG_DIR}{FILENAME_}"""
VO_NAME = "newVO.py"
VOTOP_NAME = f"""{CONFIGDIR}VOTOP.py"""
WHIRLCOUNT = 0
WHIRLSTR = f"""-{BKSLSH}|/*"""


DAYMS = (60 * 60 * 24 * 1000)  # 86400000
DAYSECS = (60 * 60 * 24)  # 86400
HALFDAY = (60 * 60 * 12)  # 43200
HALFHOUR = (60 * 30)  # 1800
HOURSECONDS = (60 * 60)  # 3600
MINUTESECONDS = 60 # 60
NINETYNINE5959SEC = (60 * 60 * 100)  # 360000
QUARTERDAYSECS = (60 * 60 * 6)
QUARTERHOURSECS = (60 * 15)  # 900


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
FMAXCF_SCTN0202_OPTIONS_STR_ADD = "FMAXCF_SCTN0202_OPTIONS_STR_ADD"  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
FMAXCF_SCTN0202_OPTIONS_VAL_ADD = "FMAXCF_SCTN0202_OPTIONS_VAL_ADD"  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD = "FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD"  # define a OPTNAME: 'str' in SCTN202 <NAC><KEY><PARM><STRDEFAULT>
FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD = "FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD"  # define a OPTNAME: VAL in SCTN202 <NAC><KEY><PARM><VALDEFAULT>
FMAXCF_SCTN0203_DICT_DEF = "FMAXCF_SCTN0203_DICT_DEF"  # define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>
FMAXCF_SCTN0203_DICT_VS_ADD = "FMAXCF_SCTN0203_DICT_VS_ADD"  # define a dict STR in SCTN203 <NAC><DICTNAME><STR>
FMAXCF_SCTN0203_DICT_VV_ADD = "FMAXCF_SCTN0203_DICT_VV_ADD"  # define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>
FMAXCF_SCTN0204_LIST_DEF = "FMAXCF_SCTN0204_LIST_DEF"  # define a list in SCTN204 <NAC><LISTNAME>
FMAXCF_SCTN0204_LIST_STR_ADD = "FMAXCF_SCTN0204_LIST_STR_ADD"  # define a list STR in SCTN204 <NAC><LISTNAME><STR>
FMAXCF_SCTN0204_LIST_VAL_ADD = "FMAXCF_SCTN0204_LIST_VAL_ADD"  # define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>
FMAXFM_SCTN0101_AX_DEF = "FMAXFM_SCTN0101_AX_DEF"  # define a new FM action <NAC>
FMAXFM_SCTN0102_STR_DEF = "FMAXFM_SCTN0102_STR_DEF"  # define a FM string <NAC><VALNAME><STR>
FMAXFM_SCTN0102_VAL_DEF = "FMAXFM_SCTN0102_VAL_DEF"  # define a FM value_ <NAC><VALNAME><VAL>
FMAXFM_SCTN0103_DICT_DEF = "FMAXFM_SCTN0103_DICT_DEF"  # define a dict for FM <NAC>
FMAXFM_SCTN0104_LIST_DEF = "FMAXFM_SCTN0104_LIST_DEF"  # define a list in FM <NAC>
FMAXPSG_SCTN0900_KEY_DEF = "FMAXPSG_SCTN0900_KEY_DEF"  # put a key in def1 of PSG.py
FMAXPSG_SCTN0900_STR_DEF = "FMAXPSG_SCTN0900_STR_DEF"  # define a string in the first section (colors, etc.) of defines in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0900_VAL_DEF = "FMAXPSG_SCTN0900_VAL_DEF"  # define a value in the first define section in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0901_DUBLT_SS_DEF = "FMAXPSG_SCTN0901_DUBLT_SS_DEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0901_DUBLT_SV_DEF = "FMAXPSG_SCTN0901_DUBLT_SV_DEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0901_DUBLT_VS_DEF = "FMAXPSG_SCTN0901_DUBLT_VS_DEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0901_DUBLT_VV_DEF = "FMAXPSG_SCTN0901_DUBLT_VV_DEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0901_KEY_DEF = "FMAXPSG_SCTN0901_KEY_DEF"  # define a key in the second section of defines in PSG.py <NAC><VALNAME>
FMAXPSG_SCTN0901_STR_DEF = "FMAXPSG_SCTN0901_STR_DEF"  # define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0901_VAL_DEF = "FMAXPSG_SCTN0901_VAL_DEF"  # define a value in the second define section in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0902_DICT_DEF = "FMAXPSG_SCTN0902_DICT_DEF"  # define a dict in PSG <NAC><DICTNAME>
FMAXPSG_SCTN0902_DICT_SS_ADD = "FMAXPSG_SCTN0902_DICT_SS_ADD"  # add a str-str to a dict <NAC><DICTNAME><STR><STR>
FMAXPSG_SCTN0902_DICT_SV_ADD = "FMAXPSG_SCTN0902_DICT_SV_ADD"  # add a str-val to a dict <NAC><DICTNAME><STR><VAL>
FMAXPSG_SCTN0902_DICT_VS_ADD = "FMAXPSG_SCTN0902_DICT_VS_ADD"  # add a str to a dict <NAC><DICTNAME><KEY><VAL>
FMAXPSG_SCTN0902_DICT_VV_ADD = "FMAXPSG_SCTN0902_DICT_VV_ADD"  # add a val to a dict in PSG <NAC><DICTNAME><KEY><VAL>
FMAXPSG_SCTN0903_LIST_DEF = "FMAXPSG_SCTN0903_LIST_DEF"  # define a list in PSG <NAC><LISTNAME>
FMAXPSG_SCTN0903_LIST_STR_ADD = "FMAXPSG_SCTN0903_LIST_STR_ADD"  # add a str to a list in PSG <NAC><LISTNAME><STR>
FMAXPSG_SCTN0903_LIST_VAL_ADD = "FMAXPSG_SCTN0903_LIST_VAL_ADD"  # add a val to a list in PSG <NAC><LISTNAME><VAL>
FMAXPSG_SCTN0904_PLATEQ_ELIF_ADD = "FMAXPSG_SCTN0904_PLATEQ_ELIF_ADD"  # platform equalizer define an elif <NAC><STRUCTNAME><CONDITION><VAL>
FMAXPSG_SCTN0904_PLATEQ_ELSE_ADD = "FMAXPSG_SCTN0904_PLATEQ_ELSE_ADD"  # platform equalizer define an else <NAC><STRUCTNAME><CONDITION>
FMAXPSG_SCTN0904_PLATEQ_FUNC_STR_ADD = "FMAXPSG_SCTN0904_PLATEQ_FUNC_STR_ADD"  # add a function string line <NAC><STRUCTNAME><CONDITION>
FMAXPSG_SCTN0904_PLATEQ_IF_ADD = "FMAXPSG_SCTN0904_PLATEQ_IF_ADD"  # add the 1st if to a platform equalizer <NAC><STRUCTNAME><CONDITION>
FMAXPSG_SCTN0904_PLATEQ_PLAT_DEF = "FMAXPSG_SCTN0904_PLATEQ_PLAT_DEF"  # define a platform equalizer struct <NAC><STRUCTNAME>
FMAXPSG_SCTN0904_PLATEQ_STR_ADD = "FMAXPSG_SCTN0904_PLATEQ_STR_ADD"  # add a string to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>
FMAXPSG_SCTN0904_PLATEQ_VAL_ADD = "FMAXPSG_SCTN0904_PLATEQ_VAL_ADD"  # add a value to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>
FMAXPSG_SCTN0905_TDD_VS_ADD = "FMAXPSG_SCTN0905_TDD_VS_ADD"  # define a ddict <NAC><TUPDICTNAME><KEY><VAL><DDICTKEY>
FMAXPSG_SCTN0905_TDD_VV_ADD = "FMAXPSG_SCTN0905_TDD_VV_ADD"  # define a ddict <NAC><TUPDICTNAME><KEY><VAL><DDICTKEY>
FMAXPSG_SCTN0905_TUPDICT_DDICT_DEF = "FMAXPSG_SCTN0905_TUPDICT_DDICT_DEF"  # define a ddict <NAC><TUPDICTNAME><KEY><DDICTKEY>
FMAXPSG_SCTN0905_TUPDICT_DEF = "FMAXPSG_SCTN0905_TUPDICT_DEF"  # define a TUPDICT in the second define section in PSG.py <NAC><TUPDICTNAME>
FMAXPSG_SCTN0905_TUPDICT_DICT_ADD = "FMAXPSG_SCTN0905_TUPDICT_DICT_ADD"  # add a value to a tupdict <NAC><TUPDICTNAME><KEY><VAL>
FMAXPSG_SCTN0905_TUPDICT_SS_ADD = "FMAXPSG_SCTN0905_TUPDICT_SS_ADD"  # add a str to a tupdict <NAC><TUPDICTNAME><STR><STR>
FMAXPSG_SCTN0905_TUPDICT_SV_ADD = "FMAXPSG_SCTN0905_TUPDICT_SV_ADD"  # add a value to a tupdict <NAC><TUPDICTNAME><STR><VAL>
FMAXPSG_SCTN0905_TUPDICT_VS_ADD = "FMAXPSG_SCTN0905_TUPDICT_VS_ADD"  # add a str to a tupdict <NAC><TUPDICTNAME><KEY><STR>
FMAXPSG_SCTN0905_TUPDICT_VV_ADD = "FMAXPSG_SCTN0905_TUPDICT_VV_ADD"  # add a value to a tupdict <NAC><TUPDICTNAME><KEY><VAL>
FMAXPSG_SCTN0906_BTN_DEF = "FMAXPSG_SCTN0906_BTN_DEF"  # define a button <NAC><BTNNAME>
FMAXPSG_SCTN0906_BTN_STR_ADD = "FMAXPSG_SCTN0906_BTN_STR_ADD"  # add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>
FMAXPSG_SCTN0906_BTN_VAL_ADD = "FMAXPSG_SCTN0906_BTN_VAL_ADD"  # add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>
FMAXPSG_SCTN0907_SPIN_DEF = "FMAXPSG_SCTN0907_SPIN_DEF"  # define a spin box entry <NAC><SPINNAME>
FMAXPSG_SCTN0907_SPIN_DICT_STR_ADD = "FMAXPSG_SCTN0907_SPIN_DICT_STR_ADD"  # add a STR to the SPINDICT <NAC><SPINNAME><KEY><STR>
FMAXPSG_SCTN0907_SPIN_DICT_VAL_ADD = "FMAXPSG_SCTN0907_SPIN_DICT_VAL_ADD"  # add a VAL to the SPINDICT <NAC><SPINNAME><KEY><VAL>
FMAXPSG_SCTN0907_SPIN_VALUES_STR_ADD = "FMAXPSG_SCTN0907_SPIN_VALUES_STR_ADD"  # add a STR to the values list <NAC><SPINNAME><STR>
FMAXPSG_SCTN0907_SPIN_VALUES_VAL_ADD = "FMAXPSG_SCTN0907_SPIN_VALUES_VAL_ADD"  # add a VAL to the values list <NAC><SPINNAME><VAL>
FMAXPSG_SCTN0908_CHECKBOX_DEF = "FMAXPSG_SCTN0908_CHECKBOX_DEF"  # define a checkbox <NAC><CHECKBOXNAME>
FMAXPSG_SCTN0908_CHECKBOX_STR_ADD = "FMAXPSG_SCTN0908_CHECKBOX_STR_ADD"  # add a str to a checkbox <NAC><CHECKBOXNAME><KEY><VAL>
FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD = "FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD"  # add a val to a checkbox <NAC><CHECKBOXNAME><KEY><VAL>
FMAXPSG_SCTN0909_TEXT_DEF = "FMAXPSG_SCTN0909_TEXT_DEF"  # define a text <NAC><TEXTNAME>
FMAXPSG_SCTN0909_TEXT_STR_ADD = "FMAXPSG_SCTN0909_TEXT_STR_ADD"  # add a str to a text element <NAC><TEXTNAME><KEY><VAL>
FMAXPSG_SCTN0909_TEXT_VAL_ADD = "FMAXPSG_SCTN0909_TEXT_VAL_ADD"  # add a val to a text element <NAC><TEXTNAME>
FMAXPSG_SCTN090A_RADIO_DEF = "FMAXPSG_SCTN090A_RADIO_DEF"  # define a radio button element
FMAXPSG_SCTN090B_COLUMN_BUTTON_ADD = "FMAXPSG_SCTN090B_COLUMN_BUTTON_ADD"  # add a button to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090B_COLUMN_CHECKBOX_ADD = "FMAXPSG_SCTN090B_COLUMN_CHECKBOX_ADD"  # add a combo to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090B_COLUMN_COLUMN_ADD = "FMAXPSG_SCTN090B_COLUMN_COLUMN_ADD"  # add a column to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090B_COLUMN_COLUMN_PARM_STR_ADD = "FMAXPSG_SCTN090B_COLUMN_COLUMN_PARM_STR_ADD"  # add a column parm to the column to a row <NAC><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>
FMAXPSG_SCTN090B_COLUMN_COLUMN_PARM_VAL_ADD = "FMAXPSG_SCTN090B_COLUMN_COLUMN_PARM_VAL_ADD"  # add a column parm to the column to a row <NAC><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>
FMAXPSG_SCTN090B_COLUMN_COMBO_ADD = "FMAXPSG_SCTN090B_COLUMN_COMBO_ADD"  # add a combo to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090B_COLUMN_DEF = "FMAXPSG_SCTN090B_COLUMN_DEF"  # define a column <NAC><COLUMNNAME>
FMAXPSG_SCTN090B_COLUMN_KEY_ADD = "FMAXPSG_SCTN090B_COLUMN_KEY_ADD"  # add a key to a column element 'key=' will be added automatically <NAC><COLUMNNAME><ROWKEY><ELEMENTKEY><VAL>
FMAXPSG_SCTN090B_COLUMN_PACKEDPARM_ADD = "FMAXPSG_SCTN090B_COLUMN_PACKEDPARM_ADD"  # add packedparms to a column entry <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN090B_COLUMN_PARM_ADD = "FMAXPSG_SCTN090B_COLUMN_PARM_ADD"  # add parms to a column entry <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN090B_COLUMN_RADIO_ADD = "FMAXPSG_SCTN090B_COLUMN_RADIO_ADD"  # add a radio to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090B_COLUMN_ROW_ADD = "FMAXPSG_SCTN090B_COLUMN_ROW_ADD"  # add a row [] to a column <NAC><COLUMNNAME><ROWKEY><LEVEL>
FMAXPSG_SCTN090B_COLUMN_SPIN_ADD = "FMAXPSG_SCTN090B_COLUMN_SPIN_ADD"  # add a spinbox to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090B_COLUMN_TEXT_ADD = "FMAXPSG_SCTN090B_COLUMN_TEXT_ADD"  # add a text element to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090C_MAPPDS_DEF = "FMAXPSG_SCTN090C_MAPPDS_DEF"  # add a nested dict holding all of the variables passed between PySimpleGUI and this app
FMAXPSG_SCTN090C_MAPPDS_DICT_DEF = "FMAXPSG_SCTN090C_MAPPDS_DICT_DEF"  # add a dict to the mainapp dict <NAC><DICTNAME
FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD = "FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD"  # add a string to a dict mainapp dict <NAC><DICTNAME><KEY><STR>
FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD = "FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD"  # add a value to a dict mainapp dict <NAC><DICTNAME><KEY><VAL>
FMAXPSG_SCTN090C_MAPPDS_VS_ADD = "FMAXPSG_SCTN090C_MAPPDS_VS_ADD"  # add a string to the mainapp dict <NAC><KEY><STR>
FMAXPSG_SCTN090C_MAPPDS_VV_ADD = "FMAXPSG_SCTN090C_MAPPDS_VV_ADD"  # add a value to the mainapp dict <NAC><KEY><VAL>
FMAXPSG_SCTN090D_MAINFRAME_DEF = "FMAXPSG_SCTN090D_MAINFRAME_DEF"  # define a frame <NAC><FRAMENAME><WINDOW><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)
FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD = "FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD"  # add a button to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090E_LAYOUT_CHECKBOX_ADD = "FMAXPSG_SCTN090E_LAYOUT_CHECKBOX_ADD"  # add a checkbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD = "FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD"  # add a column to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090E_LAYOUT_COMBO_ADD = "FMAXPSG_SCTN090E_LAYOUT_COMBO_ADD"  # add a combo to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090E_LAYOUT_DEF = "FMAXPSG_SCTN090E_LAYOUT_DEF"  # define layouts
FMAXPSG_SCTN090E_LAYOUT_KEY_ADD = "FMAXPSG_SCTN090E_LAYOUT_KEY_ADD"  # add a key to a layout element 'key=' will be added automatically <NAC><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>
FMAXPSG_SCTN090E_LAYOUT_PACKEDPARM_ADD = "FMAXPSG_SCTN090E_LAYOUT_PACKEDPARM_ADD"  # add packedparms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD = "FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD"  # add parms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN090E_LAYOUT_RADIO_ADD = "FMAXPSG_SCTN090E_LAYOUT_RADIO_ADD"  # add a radio to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090E_LAYOUT_ROW_ADD = "FMAXPSG_SCTN090E_LAYOUT_ROW_ADD"  # add a row [] to a layout <NAC><LAYOUTNAME><ROWKEY><LEVEL>
FMAXPSG_SCTN090E_LAYOUT_SPIN_ADD = "FMAXPSG_SCTN090E_LAYOUT_SPIN_ADD"  # add a spinbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090E_LAYOUT_TEXT_ADD = "FMAXPSG_SCTN090E_LAYOUT_TEXT_ADD"  # add a text element to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090F_WINDOW_DEF = "FMAXPSG_SCTN090F_WINDOW_DEF"  # define a main dictdict <NAC><MAINNAME>
FMAXPSG_SCTN090F_WINDOW_STR_ADD = "FMAXPSG_SCTN090F_WINDOW_STR_ADD"  # add a str to the main dictdict
FMAXPSG_SCTN090F_WINDOW_VAL_ADD = "FMAXPSG_SCTN090F_WINDOW_VAL_ADD"  # add a str to the main dictdict
FMAXPSG_SCTN0910_DUBLT_SS_DEF = "FMAXPSG_SCTN0910_DUBLT_SS_DEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0910_DUBLT_SV_DEF = "FMAXPSG_SCTN0910_DUBLT_SV_DEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0910_DUBLT_VS_DEF = "FMAXPSG_SCTN0910_DUBLT_VS_DEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0910_DUBLT_VV_DEF = "FMAXPSG_SCTN0910_DUBLT_VV_DEF"  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0910_STR_DEF = "FMAXPSG_SCTN0910_STR_DEF"  # define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0910_VAL_DEF = "FMAXPSG_SCTN0910_VAL_DEF"  # define a value in the second define section in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0911_COMBO_DEF = "FMAXPSG_SCTN0911_COMBO_DEF"  # define a combo box
FMAXPSG_SCTN0912_FRAMEELEMENT_DEF = "FMAXPSG_SCTN0912_FRAMEELEMENT_DEF"  # define a frame element
FMAXPSG_SCTN0913_RCMENU_DEF = "FMAXPSG_SCTN0913_RCMENU_DEF"  # define a right click menu
FMAXPSG_SCTN0913_RCMENU_VAL_ADD = "FMAXPSG_SCTN0913_RCMENU_VAL_ADD"  # define a right click menu
FMAXPSG_SCTN0914_POPUPFRAME_DEF = "FMAXPSG_SCTN0914_POPUPFRAME_DEF"  # define a frame <NAC><FRAMENAME><WINDOW><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)
FMAXPSG_SCTN0915_PUDLG_DEF = "FMAXPSG_SCTN0915_PUDLG_DEF"  # define a popup dialog <NAC><POPUPNAME><POPUPTYPE>
FMAXPSG_SCTN0915_PUDLG_DICT_STR_ADD = "FMAXPSG_SCTN0915_PUDLG_DICT_STR_ADD"  # add a str to a text element <NAC><POPUPNAME><KEY><VAL>
FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD = "FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD"  # add a val to a text element <NAC><POPUPNAME><KEY><VAL>
FMAXPSG_SCTN0915_PUDLG_LIST_STR_ADD = "FMAXPSG_SCTN0915_PUDLG_LIST_STR_ADD"  # add a str to a text element <NAC><POPUPNAME><KEY><VAL>
FMAXPSG_SCTN0915_PUDLG_LIST_VAL_ADD = "FMAXPSG_SCTN0915_PUDLG_LIST_VAL_ADD"  # add a val to a text element <NAC><POPUPNAME><KEY><VAL>
FMAXPSG_SCTN0916_CLASS_BTN_DEF = "FMAXPSG_SCTN0916_CLASS_BTN_DEF"  # define a button <NAC><CLASSNAME><BTNNAME>
FMAXPSG_SCTN0916_CLASS_BTN_STR_ADD = "FMAXPSG_SCTN0916_CLASS_BTN_STR_ADD"  # add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>
FMAXPSG_SCTN0916_CLASS_BTN_VAL_ADD = "FMAXPSG_SCTN0916_CLASS_BTN_VAL_ADD"  # add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>
FMAXPSG_SCTN0916_CLASS_CHECKBOX_DEF = "FMAXPSG_SCTN0916_CLASS_CHECKBOX_DEF"  # define a checkbox <NAC><CLASSNAME><CHECKBOXNAME>
FMAXPSG_SCTN0916_CLASS_CHECKBOX_STR_ADD = "FMAXPSG_SCTN0916_CLASS_CHECKBOX_STR_ADD"  # add a str to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>
FMAXPSG_SCTN0916_CLASS_CHECKBOX_VAL_ADD = "FMAXPSG_SCTN0916_CLASS_CHECKBOX_VAL_ADD"  # add a val to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>
FMAXPSG_SCTN0916_CLASS_COLUMN_BUTTON_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_BUTTON_ADD"  # add a button to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_COLUMN_CHECKBOX_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_CHECKBOX_ADD"  # add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_COLUMN_COLUMN_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_COLUMN_ADD"  # add a column to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_COLUMN_COLUMN_PARM_STR_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_COLUMN_PARM_STR_ADD"  # add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>
FMAXPSG_SCTN0916_CLASS_COLUMN_COLUMN_PARM_VAL_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_COLUMN_PARM_VAL_ADD"  # add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>
FMAXPSG_SCTN0916_CLASS_COLUMN_COMBO_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_COMBO_ADD"  # add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_COLUMN_DEF = "FMAXPSG_SCTN0916_CLASS_COLUMN_DEF"  # define a column <NAC><CLASSNAME><COLUMNNAME>
FMAXPSG_SCTN0916_CLASS_COLUMN_KEY_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_KEY_ADD"  # add a key to a column element 'key=' will be added automatically <NAC><CLASSNAME><COLUMNNAME><ROWKEY><ELEMENTKEY><VAL>
FMAXPSG_SCTN0916_CLASS_COLUMN_PACKEDPARM_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_PACKEDPARM_ADD"  # add packedparms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD"  # add parms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN0916_CLASS_COLUMN_RADIO_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_RADIO_ADD"  # add a radio to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD"  # add a row [] to a column <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL>
FMAXPSG_SCTN0916_CLASS_COLUMN_SPIN_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_SPIN_ADD"  # add a spinbox to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_COLUMN_TEXT_ADD = "FMAXPSG_SCTN0916_CLASS_COLUMN_TEXT_ADD"  # add a text element to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_COMBO_DEF = "FMAXPSG_SCTN0916_CLASS_COMBO_DEF"  # define a combo box
FMAXPSG_SCTN0916_CLASS_DEF = "FMAXPSG_SCTN0916_CLASS_DEF"  # define a class <NAC><CLASSNAME>
FMAXPSG_SCTN0916_CLASS_DICT_DEF = "FMAXPSG_SCTN0916_CLASS_DICT_DEF"  # define a dict in PSG <NAC><CLASSNAME><DICTNAME>
FMAXPSG_SCTN0916_CLASS_DICT_SS_ADD = "FMAXPSG_SCTN0916_CLASS_DICT_SS_ADD"  # add a str-str to a dict <NAC><CLASSNAME><DICTNAME><STR><STR>
FMAXPSG_SCTN0916_CLASS_DICT_SV_ADD = "FMAXPSG_SCTN0916_CLASS_DICT_SV_ADD"  # add a str-val to a dict <NAC><CLASSNAME><DICTNAME><STR><VAL>
FMAXPSG_SCTN0916_CLASS_DICT_VS_ADD = "FMAXPSG_SCTN0916_CLASS_DICT_VS_ADD"  # add a str to a dict <NAC><CLASSNAME><DICTNAME><KEY><VAL>
FMAXPSG_SCTN0916_CLASS_DICT_VV_ADD = "FMAXPSG_SCTN0916_CLASS_DICT_VV_ADD"  # add a val to a dict in PSG <NAC><CLASSNAME><DICTNAME><KEY><VAL>
FMAXPSG_SCTN0916_CLASS_FRAMEELEMENT_DEF = "FMAXPSG_SCTN0916_CLASS_FRAMEELEMENT_DEF"  # define a frame element
FMAXPSG_SCTN0916_CLASS_LAYOUT_BUTTON_ADD = "FMAXPSG_SCTN0916_CLASS_LAYOUT_BUTTON_ADD"  # add a button to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_LAYOUT_CHECKBOX_ADD = "FMAXPSG_SCTN0916_CLASS_LAYOUT_CHECKBOX_ADD"  # add a checkbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_LAYOUT_COLUMN_ADD = "FMAXPSG_SCTN0916_CLASS_LAYOUT_COLUMN_ADD"  # add a column to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_LAYOUT_COMBO_ADD = "FMAXPSG_SCTN0916_CLASS_LAYOUT_COMBO_ADD"  # add a combo to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_LAYOUT_DEF = "FMAXPSG_SCTN0916_CLASS_LAYOUT_DEF"  # define layouts
FMAXPSG_SCTN0916_CLASS_LAYOUT_KEY_ADD = "FMAXPSG_SCTN0916_CLASS_LAYOUT_KEY_ADD"  # add a key to a layout element 'key=' will be added automatically <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>
FMAXPSG_SCTN0916_CLASS_LAYOUT_PACKEDPARM_ADD = "FMAXPSG_SCTN0916_CLASS_LAYOUT_PACKEDPARM_ADD"  # add packedparms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN0916_CLASS_LAYOUT_PARM_VAL_ADD = "FMAXPSG_SCTN0916_CLASS_LAYOUT_PARM_VAL_ADD"  # add parms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN0916_CLASS_LAYOUT_RADIO_ADD = "FMAXPSG_SCTN0916_CLASS_LAYOUT_RADIO_ADD"  # add a radio to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_LAYOUT_ROW_ADD = "FMAXPSG_SCTN0916_CLASS_LAYOUT_ROW_ADD"  # add a row [] to a layout <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL>
FMAXPSG_SCTN0916_CLASS_LAYOUT_SPIN_ADD = "FMAXPSG_SCTN0916_CLASS_LAYOUT_SPIN_ADD"  # add a spinbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_LAYOUT_TEXT_ADD = "FMAXPSG_SCTN0916_CLASS_LAYOUT_TEXT_ADD"  # add a text element to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN0916_CLASS_LIST_DEF = "FMAXPSG_SCTN0916_CLASS_LIST_DEF"  # define a list in PSG <NAC><CLASSNAME><LISTNAME>
FMAXPSG_SCTN0916_CLASS_LIST_STR_ADD = "FMAXPSG_SCTN0916_CLASS_LIST_STR_ADD"  # add a str to a list in PSG <NAC><CLASSNAME><LISTNAME><STR>
FMAXPSG_SCTN0916_CLASS_LIST_VAL_ADD = "FMAXPSG_SCTN0916_CLASS_LIST_VAL_ADD"  # add a val to a list in PSG <NAC><CLASSNAME><LISTNAME><VAL>
FMAXPSG_SCTN0916_CLASS_MAINFRAME_DEF = "FMAXPSG_SCTN0916_CLASS_MAINFRAME_DEF"  # define a class mainframe
FMAXPSG_SCTN0916_CLASS_POPUPFRAME_DEF = "FMAXPSG_SCTN0916_CLASS_POPUPFRAME_DEF"  # define a class mainframe
FMAXPSG_SCTN0916_CLASS_RADIO_DEF = "FMAXPSG_SCTN0916_CLASS_RADIO_DEF"  # define a radio button element
FMAXPSG_SCTN0916_CLASS_RCMENU_DEF = "FMAXPSG_SCTN0916_CLASS_RCMENU_DEF"  # define a right click menu
FMAXPSG_SCTN0916_CLASS_RCMENU_VAL_ADD = "FMAXPSG_SCTN0916_CLASS_RCMENU_VAL_ADD"  # define a right click menu
FMAXPSG_SCTN0916_CLASS_SPIN_DEF = "FMAXPSG_SCTN0916_CLASS_SPIN_DEF"  # define a spin box entry <NAC><CLASSNAME><SPINNAME>
FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VS_ADD = "FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VS_ADD"  # add a STR to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><STR>
FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VV_ADD = "FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VV_ADD"  # add a VAL to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><VAL>
FMAXPSG_SCTN0916_CLASS_SPIN_LIST_STR_ADD = "FMAXPSG_SCTN0916_CLASS_SPIN_LIST_STR_ADD"  # add a STR to the values list <NAC><CLASSNAME><SPINNAME><STR>
FMAXPSG_SCTN0916_CLASS_SPIN_LIST_VAL_ADD = "FMAXPSG_SCTN0916_CLASS_SPIN_LIST_VAL_ADD"  # add a VAL to the values list <NAC><CLASSNAME><SPINNAME><VAL>
FMAXPSG_SCTN0916_CLASS_TEXT_DEF = "FMAXPSG_SCTN0916_CLASS_TEXT_DEF"  # define a text <NAC><TEXTNAME>
FMAXPSG_SCTN0916_CLASS_TEXT_STR_ADD = "FMAXPSG_SCTN0916_CLASS_TEXT_STR_ADD"  # add a str to a text element <NAC><CLASSNAME><TEXTNAME><KEY><VAL>
FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD = "FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD"  # add a val to a text element <NAC><CLASSNAME><TEXTNAME>
FMAXPSG_SCTN0916_CLASS_WINDOW_DEF = "FMAXPSG_SCTN0916_CLASS_WINDOW_DEF"  # define a main dictdict <NAC><CLASSNAME><MAINNAME>
FMAXPSG_SCTN0916_CLASS_WINDOW_STR_ADD = "FMAXPSG_SCTN0916_CLASS_WINDOW_STR_ADD"  # add a str to the main dictdict
FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD = "FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD"  # add a str to the main dictdict


FMAXFM_AXLST = [
	FMAX_NOP,  # skip this entry
	FMAXCF_SCTN0003_LAMBDA_DEF,  # define a lambda function <NAC><NAME><lambda str>
	FMAXCF_SCTN0003_TYPE_DEF,  # define a fake type used in the translation dict <NAC><NAME><TYPE>
	FMAXCF_SCTN0201_STR_DEF,  # define a STR in SCTN21 <NAC><NAME><str>
	FMAXCF_SCTN0201_VAL_DEF,  # define a VAL in SCTN21 <NAC><NAME><VAL>
	FMAXCF_SCTN0202_OPTIONS_ADD_HELP_LINE,  # add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>
	FMAXCF_SCTN0202_OPTIONS_STR_ADD,  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
	FMAXCF_SCTN0202_OPTIONS_VAL_ADD,  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
	FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD,  # define a OPTNAME: 'str' in SCTN202 <NAC><KEY><PARM><STRDEFAULT>
	FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD,  # define a OPTNAME: VAL in SCTN202 <NAC><KEY><PARM><VALDEFAULT>
	FMAXCF_SCTN0203_DICT_DEF,  # define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>
	FMAXCF_SCTN0203_DICT_VS_ADD,  # define a dict STR in SCTN203 <NAC><DICTNAME><STR>
	FMAXCF_SCTN0203_DICT_VV_ADD,  # define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>
	FMAXCF_SCTN0204_LIST_DEF,  # define a list in SCTN204 <NAC><LISTNAME>
	FMAXCF_SCTN0204_LIST_STR_ADD,  # define a list STR in SCTN204 <NAC><LISTNAME><STR>
	FMAXCF_SCTN0204_LIST_VAL_ADD,  # define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>
	FMAXFM_SCTN0101_AX_DEF,  # define a new FM action <NAC>
	FMAXFM_SCTN0102_STR_DEF,  # define a FM string <NAC><VALNAME><STR>
	FMAXFM_SCTN0102_VAL_DEF,  # define a FM value_ <NAC><VALNAME><VAL>
	FMAXFM_SCTN0103_DICT_DEF,  # define a dict for FM <NAC>
	FMAXFM_SCTN0104_LIST_DEF,  # define a list in FM <NAC>
	FMAXPSG_SCTN0900_KEY_DEF,  # put a key in def1 of PSG.py
	FMAXPSG_SCTN0900_STR_DEF,  # define a string in the first section (colors, etc.) of defines in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0900_VAL_DEF,  # define a value in the first define section in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0901_DUBLT_SS_DEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0901_DUBLT_SV_DEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0901_DUBLT_VS_DEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0901_DUBLT_VV_DEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0901_KEY_DEF,  # define a key in the second section of defines in PSG.py <NAC><VALNAME>
	FMAXPSG_SCTN0901_STR_DEF,  # define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0901_VAL_DEF,  # define a value in the second define section in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0902_DICT_DEF,  # define a dict in PSG <NAC><DICTNAME>
	FMAXPSG_SCTN0902_DICT_SS_ADD,  # add a str-str to a dict <NAC><DICTNAME><STR><STR>
	FMAXPSG_SCTN0902_DICT_SV_ADD,  # add a str-val to a dict <NAC><DICTNAME><STR><VAL>
	FMAXPSG_SCTN0902_DICT_VS_ADD,  # add a str to a dict <NAC><DICTNAME><KEY><VAL>
	FMAXPSG_SCTN0902_DICT_VV_ADD,  # add a val to a dict in PSG <NAC><DICTNAME><KEY><VAL>
	FMAXPSG_SCTN0903_LIST_DEF,  # define a list in PSG <NAC><LISTNAME>
	FMAXPSG_SCTN0903_LIST_STR_ADD,  # add a str to a list in PSG <NAC><LISTNAME><STR>
	FMAXPSG_SCTN0903_LIST_VAL_ADD,  # add a val to a list in PSG <NAC><LISTNAME><VAL>
	FMAXPSG_SCTN0904_PLATEQ_ELIF_ADD,  # platform equalizer define an elif <NAC><STRUCTNAME><CONDITION><VAL>
	FMAXPSG_SCTN0904_PLATEQ_ELSE_ADD,  # platform equalizer define an else <NAC><STRUCTNAME><CONDITION>
	FMAXPSG_SCTN0904_PLATEQ_FUNC_STR_ADD,  # add a function string line <NAC><STRUCTNAME><CONDITION>
	FMAXPSG_SCTN0904_PLATEQ_IF_ADD,  # add the 1st if to a platform equalizer <NAC><STRUCTNAME><CONDITION>
	FMAXPSG_SCTN0904_PLATEQ_PLAT_DEF,  # define a platform equalizer struct <NAC><STRUCTNAME>
	FMAXPSG_SCTN0904_PLATEQ_STR_ADD,  # add a string to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>
	FMAXPSG_SCTN0904_PLATEQ_VAL_ADD,  # add a value to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>
	FMAXPSG_SCTN0905_TDD_VS_ADD,  # define a ddict <NAC><TUPDICTNAME><KEY><VAL><DDICTKEY>
	FMAXPSG_SCTN0905_TDD_VV_ADD,  # define a ddict <NAC><TUPDICTNAME><KEY><VAL><DDICTKEY>
	FMAXPSG_SCTN0905_TUPDICT_DDICT_DEF,  # define a ddict <NAC><TUPDICTNAME><KEY><DDICTKEY>
	FMAXPSG_SCTN0905_TUPDICT_DEF,  # define a TUPDICT in the second define section in PSG.py <NAC><TUPDICTNAME>
	FMAXPSG_SCTN0905_TUPDICT_DICT_ADD,  # add a value to a tupdict <NAC><TUPDICTNAME><KEY><VAL>
	FMAXPSG_SCTN0905_TUPDICT_SS_ADD,  # add a str to a tupdict <NAC><TUPDICTNAME><STR><STR>
	FMAXPSG_SCTN0905_TUPDICT_SV_ADD,  # add a value to a tupdict <NAC><TUPDICTNAME><STR><VAL>
	FMAXPSG_SCTN0905_TUPDICT_VS_ADD,  # add a str to a tupdict <NAC><TUPDICTNAME><KEY><STR>
	FMAXPSG_SCTN0905_TUPDICT_VV_ADD,  # add a value to a tupdict <NAC><TUPDICTNAME><KEY><VAL>
	FMAXPSG_SCTN0906_BTN_DEF,  # define a button <NAC><BTNNAME>
	FMAXPSG_SCTN0906_BTN_STR_ADD,  # add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>
	FMAXPSG_SCTN0906_BTN_VAL_ADD,  # add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>
	FMAXPSG_SCTN0907_SPIN_DEF,  # define a spin box entry <NAC><SPINNAME>
	FMAXPSG_SCTN0907_SPIN_DICT_STR_ADD,  # add a STR to the SPINDICT <NAC><SPINNAME><KEY><STR>
	FMAXPSG_SCTN0907_SPIN_DICT_VAL_ADD,  # add a VAL to the SPINDICT <NAC><SPINNAME><KEY><VAL>
	FMAXPSG_SCTN0907_SPIN_VALUES_STR_ADD,  # add a STR to the values list <NAC><SPINNAME><STR>
	FMAXPSG_SCTN0907_SPIN_VALUES_VAL_ADD,  # add a VAL to the values list <NAC><SPINNAME><VAL>
	FMAXPSG_SCTN0908_CHECKBOX_DEF,  # define a checkbox <NAC><CHECKBOXNAME>
	FMAXPSG_SCTN0908_CHECKBOX_STR_ADD,  # add a str to a checkbox <NAC><CHECKBOXNAME><KEY><VAL>
	FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD,  # add a val to a checkbox <NAC><CHECKBOXNAME><KEY><VAL>
	FMAXPSG_SCTN0909_TEXT_DEF,  # define a text <NAC><TEXTNAME>
	FMAXPSG_SCTN0909_TEXT_STR_ADD,  # add a str to a text element <NAC><TEXTNAME><KEY><VAL>
	FMAXPSG_SCTN0909_TEXT_VAL_ADD,  # add a val to a text element <NAC><TEXTNAME>
	FMAXPSG_SCTN090A_RADIO_DEF,  # define a radio button element
	FMAXPSG_SCTN090B_COLUMN_BUTTON_ADD,  # add a button to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090B_COLUMN_CHECKBOX_ADD,  # add a combo to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090B_COLUMN_COLUMN_ADD,  # add a column to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090B_COLUMN_COLUMN_PARM_STR_ADD,  # add a column parm to the column to a row <NAC><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>
	FMAXPSG_SCTN090B_COLUMN_COLUMN_PARM_VAL_ADD,  # add a column parm to the column to a row <NAC><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>
	FMAXPSG_SCTN090B_COLUMN_COMBO_ADD,  # add a combo to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090B_COLUMN_DEF,  # define a column <NAC><COLUMNNAME>
	FMAXPSG_SCTN090B_COLUMN_KEY_ADD,  # add a key to a column element 'key=' will be added automatically <NAC><COLUMNNAME><ROWKEY><ELEMENTKEY><VAL>
	FMAXPSG_SCTN090B_COLUMN_PACKEDPARM_ADD,  # add packedparms to a column entry <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN090B_COLUMN_PARM_ADD,  # add parms to a column entry <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN090B_COLUMN_RADIO_ADD,  # add a radio to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090B_COLUMN_ROW_ADD,  # add a row [] to a column <NAC><COLUMNNAME><ROWKEY><LEVEL>
	FMAXPSG_SCTN090B_COLUMN_SPIN_ADD,  # add a spinbox to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090B_COLUMN_TEXT_ADD,  # add a text element to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090C_MAPPDS_DEF,  # add a nested dict holding all of the variables passed between PySimpleGUI and this app
	FMAXPSG_SCTN090C_MAPPDS_DICT_DEF,  # add a dict to the mainapp dict <NAC><DICTNAME
	FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD,  # add a string to a dict mainapp dict <NAC><DICTNAME><KEY><STR>
	FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD,  # add a value to a dict mainapp dict <NAC><DICTNAME><KEY><VAL>
	FMAXPSG_SCTN090C_MAPPDS_VS_ADD,  # add a string to the mainapp dict <NAC><KEY><STR>
	FMAXPSG_SCTN090C_MAPPDS_VV_ADD,  # add a value to the mainapp dict <NAC><KEY><VAL>
	FMAXPSG_SCTN090D_MAINFRAME_DEF,  # define a frame <NAC><FRAMENAME><WINDOW><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)
	FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD,  # add a button to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090E_LAYOUT_CHECKBOX_ADD,  # add a checkbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD,  # add a column to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090E_LAYOUT_COMBO_ADD,  # add a combo to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090E_LAYOUT_DEF,  # define layouts
	FMAXPSG_SCTN090E_LAYOUT_KEY_ADD,  # add a key to a layout element 'key=' will be added automatically <NAC><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>
	FMAXPSG_SCTN090E_LAYOUT_PACKEDPARM_ADD,  # add packedparms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD,  # add parms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN090E_LAYOUT_RADIO_ADD,  # add a radio to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090E_LAYOUT_ROW_ADD,  # add a row [] to a layout <NAC><LAYOUTNAME><ROWKEY><LEVEL>
	FMAXPSG_SCTN090E_LAYOUT_SPIN_ADD,  # add a spinbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090E_LAYOUT_TEXT_ADD,  # add a text element to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090F_WINDOW_DEF,  # define a main dictdict <NAC><MAINNAME>
	FMAXPSG_SCTN090F_WINDOW_STR_ADD,  # add a str to the main dictdict
	FMAXPSG_SCTN090F_WINDOW_VAL_ADD,  # add a str to the main dictdict
	FMAXPSG_SCTN0910_DUBLT_SS_DEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0910_DUBLT_SV_DEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0910_DUBLT_VS_DEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0910_DUBLT_VV_DEF,  # define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0910_STR_DEF,  # define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0910_VAL_DEF,  # define a value in the second define section in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0911_COMBO_DEF,  # define a combo box
	FMAXPSG_SCTN0912_FRAMEELEMENT_DEF,  # define a frame element
	FMAXPSG_SCTN0913_RCMENU_DEF,  # define a right click menu
	FMAXPSG_SCTN0913_RCMENU_VAL_ADD,  # define a right click menu
	FMAXPSG_SCTN0914_POPUPFRAME_DEF,  # define a frame <NAC><FRAMENAME><WINDOW><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)
	FMAXPSG_SCTN0915_PUDLG_DEF,  # define a popup dialog <NAC><POPUPNAME><POPUPTYPE>
	FMAXPSG_SCTN0915_PUDLG_DICT_STR_ADD,  # add a str to a text element <NAC><POPUPNAME><KEY><VAL>
	FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD,  # add a val to a text element <NAC><POPUPNAME><KEY><VAL>
	FMAXPSG_SCTN0915_PUDLG_LIST_STR_ADD,  # add a str to a text element <NAC><POPUPNAME><KEY><VAL>
	FMAXPSG_SCTN0915_PUDLG_LIST_VAL_ADD,  # add a val to a text element <NAC><POPUPNAME><KEY><VAL>
	FMAXPSG_SCTN0916_CLASS_BTN_DEF,  # define a button <NAC><CLASSNAME><BTNNAME>
	FMAXPSG_SCTN0916_CLASS_BTN_STR_ADD,  # add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>
	FMAXPSG_SCTN0916_CLASS_BTN_VAL_ADD,  # add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>
	FMAXPSG_SCTN0916_CLASS_CHECKBOX_DEF,  # define a checkbox <NAC><CLASSNAME><CHECKBOXNAME>
	FMAXPSG_SCTN0916_CLASS_CHECKBOX_STR_ADD,  # add a str to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>
	FMAXPSG_SCTN0916_CLASS_CHECKBOX_VAL_ADD,  # add a val to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>
	FMAXPSG_SCTN0916_CLASS_COLUMN_BUTTON_ADD,  # add a button to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_COLUMN_CHECKBOX_ADD,  # add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_COLUMN_COLUMN_ADD,  # add a column to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_COLUMN_COLUMN_PARM_STR_ADD,  # add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>
	FMAXPSG_SCTN0916_CLASS_COLUMN_COLUMN_PARM_VAL_ADD,  # add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>
	FMAXPSG_SCTN0916_CLASS_COLUMN_COMBO_ADD,  # add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_COLUMN_DEF,  # define a column <NAC><CLASSNAME><COLUMNNAME>
	FMAXPSG_SCTN0916_CLASS_COLUMN_KEY_ADD,  # add a key to a column element 'key=' will be added automatically <NAC><CLASSNAME><COLUMNNAME><ROWKEY><ELEMENTKEY><VAL>
	FMAXPSG_SCTN0916_CLASS_COLUMN_PACKEDPARM_ADD,  # add packedparms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD,  # add parms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN0916_CLASS_COLUMN_RADIO_ADD,  # add a radio to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD,  # add a row [] to a column <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL>
	FMAXPSG_SCTN0916_CLASS_COLUMN_SPIN_ADD,  # add a spinbox to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_COLUMN_TEXT_ADD,  # add a text element to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_COMBO_DEF,  # define a combo box
	FMAXPSG_SCTN0916_CLASS_DEF,  # define a class <NAC><CLASSNAME>
	FMAXPSG_SCTN0916_CLASS_DICT_DEF,  # define a dict in PSG <NAC><CLASSNAME><DICTNAME>
	FMAXPSG_SCTN0916_CLASS_DICT_SS_ADD,  # add a str-str to a dict <NAC><CLASSNAME><DICTNAME><STR><STR>
	FMAXPSG_SCTN0916_CLASS_DICT_SV_ADD,  # add a str-val to a dict <NAC><CLASSNAME><DICTNAME><STR><VAL>
	FMAXPSG_SCTN0916_CLASS_DICT_VS_ADD,  # add a str to a dict <NAC><CLASSNAME><DICTNAME><KEY><VAL>
	FMAXPSG_SCTN0916_CLASS_DICT_VV_ADD,  # add a val to a dict in PSG <NAC><CLASSNAME><DICTNAME><KEY><VAL>
	FMAXPSG_SCTN0916_CLASS_FRAMEELEMENT_DEF,  # define a frame element
	FMAXPSG_SCTN0916_CLASS_LAYOUT_BUTTON_ADD,  # add a button to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_LAYOUT_CHECKBOX_ADD,  # add a checkbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_LAYOUT_COLUMN_ADD,  # add a column to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_LAYOUT_COMBO_ADD,  # add a combo to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_LAYOUT_DEF,  # define layouts
	FMAXPSG_SCTN0916_CLASS_LAYOUT_KEY_ADD,  # add a key to a layout element 'key=' will be added automatically <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>
	FMAXPSG_SCTN0916_CLASS_LAYOUT_PACKEDPARM_ADD,  # add packedparms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN0916_CLASS_LAYOUT_PARM_VAL_ADD,  # add parms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN0916_CLASS_LAYOUT_RADIO_ADD,  # add a radio to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_LAYOUT_ROW_ADD,  # add a row [] to a layout <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL>
	FMAXPSG_SCTN0916_CLASS_LAYOUT_SPIN_ADD,  # add a spinbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_LAYOUT_TEXT_ADD,  # add a text element to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN0916_CLASS_LIST_DEF,  # define a list in PSG <NAC><CLASSNAME><LISTNAME>
	FMAXPSG_SCTN0916_CLASS_LIST_STR_ADD,  # add a str to a list in PSG <NAC><CLASSNAME><LISTNAME><STR>
	FMAXPSG_SCTN0916_CLASS_LIST_VAL_ADD,  # add a val to a list in PSG <NAC><CLASSNAME><LISTNAME><VAL>
	FMAXPSG_SCTN0916_CLASS_MAINFRAME_DEF,  # define a class mainframe
	FMAXPSG_SCTN0916_CLASS_POPUPFRAME_DEF,  # define a class mainframe
	FMAXPSG_SCTN0916_CLASS_RADIO_DEF,  # define a radio button element
	FMAXPSG_SCTN0916_CLASS_RCMENU_DEF,  # define a right click menu
	FMAXPSG_SCTN0916_CLASS_RCMENU_VAL_ADD,  # define a right click menu
	FMAXPSG_SCTN0916_CLASS_SPIN_DEF,  # define a spin box entry <NAC><CLASSNAME><SPINNAME>
	FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VS_ADD,  # add a STR to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><STR>
	FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VV_ADD,  # add a VAL to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><VAL>
	FMAXPSG_SCTN0916_CLASS_SPIN_LIST_STR_ADD,  # add a STR to the values list <NAC><CLASSNAME><SPINNAME><STR>
	FMAXPSG_SCTN0916_CLASS_SPIN_LIST_VAL_ADD,  # add a VAL to the values list <NAC><CLASSNAME><SPINNAME><VAL>
	FMAXPSG_SCTN0916_CLASS_TEXT_DEF,  # define a text <NAC><TEXTNAME>
	FMAXPSG_SCTN0916_CLASS_TEXT_STR_ADD,  # add a str to a text element <NAC><CLASSNAME><TEXTNAME><KEY><VAL>
	FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD,  # add a val to a text element <NAC><CLASSNAME><TEXTNAME>
	FMAXPSG_SCTN0916_CLASS_WINDOW_DEF,  # define a main dictdict <NAC><CLASSNAME><MAINNAME>
	FMAXPSG_SCTN0916_CLASS_WINDOW_STR_ADD,  # add a str to the main dictdict
	FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD,  # add a str to the main dictdict
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN102 VAL _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
TABLEVEL = "TABLEVEL"  # key for tab levels


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN103 _DICT_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMCF_SCTN0003_TYPE_CMNT_DICT = {}  # SCTN009 types comments
FMCF_SCTN0003_TYPE_DICT = {}  # SCTN003 types
FMCF_SCTN0201_DEF_CMNT_DICT = {}  # SCTN201 defines comments dict
FMCF_SCTN0201_DEF_DICT = {}  # SCTN201 defines dict
FMCF_SCTN0202_OPTIONS_CMNT_DICT = {}  # SCTN202 OPTIONS comments dict
FMCF_SCTN0202_OPTIONS_DICT = {}  # SCTN202 OPTIONS dict
FMCF_SCTN0202_OPTIONSDICT_CMNT_DICT = {}  # SCTN202 OPTIONSDICT comments dict
FMCF_SCTN0202_OPTIONSDICT_DICT = {}  # SCTN202 OPTIONSDICT
FMCF_SCTN0202_OPTIONSHELPDICT_DICT = {}  # SCTN202 OPTIONS HELPDICT
FMCF_SCTN0203_DICT_CMNT_DICT = {}  # SCTN203 dict comments dict
FMCF_SCTN0203_DICT_DICT = {}  # SCTN203 dict dict
FMCF_SCTN0204_LIST_CMNT_DICT = {}  # SCTN204 list comments dict
FMCF_SCTN0204_LIST_DICT = {}  # SCTN204 list dict
FMFM_SCTN0101_AX_CMNT_DICT = {}  # SCTN101 FMAX defined
FMFM_SCTN0101_AX_DICT = {}  # SCTN101 FMAX defined
FMFM_SCTN0102_VAL_CMNT_DICT = {}  # SCTN102 val
FMFM_SCTN0102_VAL_DICT = {}  # SCTN102 val
FMFM_SCTN0103_DICT_CMNT_DICT = {}  # SCTN103 dict defined
FMFM_SCTN0103_DICT_DICT = {}  # SCTN103 dict defined
FMFM_SCTN0104_LIST_CMNT_DICT = {}  # SCTN201 device defines
FMFM_SCTN0104_LIST_DICT = {}  # SCTN201 device defines
FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN0900_DEF1_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0900_DEF1_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0901_DEF2_CMNT_DICT = {}  # define the dict to hold everything in SCTN0901
FMPSG_SCTN0901_DEF2_DICT = {}  # define the dict to hold everything in SCTN0901
FMPSG_SCTN0902_DICT_CMNT_DICT = {}  # define the dict to hold everything in SCTN0902
FMPSG_SCTN0902_DICT_DICT = {}  # define the dict to hold everything in SCTN0902
FMPSG_SCTN0903_LIST_CMNT_DICT = {}  # define the dict to hold everything in SCTN0903
FMPSG_SCTN0903_LIST_DICT = {}  # define the dict to hold everything in SCTN0903
FMPSG_SCTN0904_PLATEQ_INNER_CMNT_DICT = {}  # define the dict to hold everything in SCTN0904
FMPSG_SCTN0904_PLATEQ_INNER_DICT = {}  # define the dict to hold everything in SCTN0904
FMPSG_SCTN0904_PLATEQ_OUTER_CMNT_DICT = {}  # define the dict to hold everything in SCTN0904
FMPSG_SCTN0904_PLATEQ_OUTER_DICT = {}  # define the dict to hold everything in SCTN0904
FMPSG_SCTN0905_TUPDICT_CMNT_DICT = {}  # define the dict to hold everything in SCTN0905
FMPSG_SCTN0905_TUPDICT_DICT = {}  # define the dict to hold everything in SCTN0905
FMPSG_SCTN0905_TUPDICT_TDD_DICT = {}  # define the dict to hold everything in SCTN0905
FMPSG_SCTN0906_BTNS_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN0906_BTNS_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0907_SPIN_CMNT_DICT = {}  # holds the spin element stuffs (TUPDICT)f
FMPSG_SCTN0907_SPIN_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN0908_CHECKBOX_CMNT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0908_CHECKBOX_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0909_TEXT_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN0909_TEXT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090A_RADIO_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN090A_RADIO_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090B_COLUMN_CMNT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090B_COLUMN_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090B_COLUMN_PARMS_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090C_MAPPDS_CMNT_DICT = {}  # the main app dict for this app
FMPSG_SCTN090C_MAPPDS_DICT = {}  # the main app dict for this app
FMPSG_SCTN090C_MAPPDSDICT_DICT = {}  # the main app dict+dict for this app
FMPSG_SCTN090D_MAINFRAME_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN090D_MAINFRAME_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090E_LAYOUT_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN090E_LAYOUT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN090F_WINDOW_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN090F_WINDOW_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0910_DEF3_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0910_DEF3_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0911_COMBO_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0911_COMBO_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0912_FRAME_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0912_FRAME_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0913_RCMENU_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0913_RCMENU_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0914_POPUPFRAME_CMNT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0914_POPUPFRAME_DICT = {}  # holds all of the DIALOG DIALOG (TUPDICT)
FMPSG_SCTN0915_PUDLG_CMNT_DICT = {}  # holds all of the DIALOG DIALOG (TUPDICT)
FMPSG_SCTN0915_PUDLG_DICT_DICT = {}  # holds all of the DIALOG DIALOG (TUPDICT)
FMPSG_SCTN0915_PUDLG_LIST_DICT = {}  # holds all of the DIALOG DIALOG (TUPDICT)
FMPSG_SCTN0915_PUDLG_TYPE_DICT = {}  # holds all of the DIALOG DIALOG (TUPDICT)
FMPSG_SCTN0916_CLASS_BTNS_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN0916_CLASS_BTNS_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0916_CLASS_CHECKBOX_CMNT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0916_CLASS_CHECKBOX_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0916_CLASS_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0916_CLASS_COLUMN_CMNT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0916_CLASS_COLUMN_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0916_CLASS_COLUMN_PARMS_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0916_CLASS_COMBO_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0916_CLASS_COMBO_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0916_CLASS_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0916_CLASS_DICT_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0916_CLASS_DICT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0916_CLASS_FRAME_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0916_CLASS_FRAME_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0916_CLASS_LAYOUT_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN0916_CLASS_LAYOUT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0916_CLASS_LIST_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0916_CLASS_LIST_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0916_CLASS_RADIO_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN0916_CLASS_RADIO_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0916_CLASS_RCMENU_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0916_CLASS_RCMENU_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN0916_CLASS_SPIN_CMNT_DICT = {}  # holds the spin element stuffs (TUPDICT)f
FMPSG_SCTN0916_CLASS_SPIN_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN0916_CLASS_TEXT_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN0916_CLASS_TEXT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0916_CLASS_WINDOW_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN0916_CLASS_WINDOW_DICT = {}  # holds all of the button entriess (TUPDICT)


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


# <<>>
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of unmanaged sections of FM.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
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
	("FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "define a OPTNAME: 'str' in SCTN202 <NAC><KEY><PARM><STRDEFAULT>",),
	("FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a OPTNAME: VAL in SCTN202 <NAC><KEY><PARM><VALDEFAULT>",),
	("FMAXCF_SCTN0202_OPTIONS_ADD_HELP_LINE", FMAXFM_SCTN0101_AX_DEF, "add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>",),
	("FMAXCF_SCTN0202_OPTIONS_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>",),
	("FMAXCF_SCTN0202_OPTIONS_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>",),
	("FMAXCF_SCTN0203_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>",),
	("FMAXCF_SCTN0203_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "define a dict STR in SCTN203 <NAC><DICTNAME><STR>",),
	("FMAXCF_SCTN0203_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>",),
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
	("FMAXPSG_SCTN0900_KEY_DEF", FMAXFM_SCTN0101_AX_DEF, "put a key in def1 of PSG.py",),
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
	("FMAXPSG_SCTN0902_DICT_SS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str-str to a dict <NAC><DICTNAME><STR><STR>",),
	("FMAXPSG_SCTN0902_DICT_SV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str-val to a dict <NAC><DICTNAME><STR><VAL>",),
	("FMAXPSG_SCTN0902_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a dict <NAC><DICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0902_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a dict in PSG <NAC><DICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0903_LIST_DEF", FMAXFM_SCTN0101_AX_DEF, "define a list in PSG <NAC><LISTNAME>",),
	("FMAXPSG_SCTN0903_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a list in PSG <NAC><LISTNAME><STR>",),
	("FMAXPSG_SCTN0903_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a list in PSG <NAC><LISTNAME><VAL>",),
	("FMAXPSG_SCTN0904_PLATEQ_ELIF_ADD", FMAXFM_SCTN0101_AX_DEF, "platform equalizer define an elif <NAC><STRUCTNAME><CONDITION><VAL>",),
	("FMAXPSG_SCTN0904_PLATEQ_ELSE_ADD", FMAXFM_SCTN0101_AX_DEF, "platform equalizer define an else <NAC><STRUCTNAME><CONDITION>",),
	("FMAXPSG_SCTN0904_PLATEQ_FUNC_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a function string line <NAC><STRUCTNAME><CONDITION>",),
	("FMAXPSG_SCTN0904_PLATEQ_IF_ADD", FMAXFM_SCTN0101_AX_DEF, "add the 1st if to a platform equalizer <NAC><STRUCTNAME><CONDITION>",),
	("FMAXPSG_SCTN0904_PLATEQ_PLAT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a platform equalizer struct <NAC><STRUCTNAME>",),
	("FMAXPSG_SCTN0904_PLATEQ_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a string to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN0904_PLATEQ_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a PLATEQ <NAC><STRUCTNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN0905_TDD_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "define a ddict <NAC><TUPDICTNAME><KEY><VAL><DDICTKEY>",),
	("FMAXPSG_SCTN0905_TDD_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "define a ddict <NAC><TUPDICTNAME><KEY><VAL><DDICTKEY>",),
	("FMAXPSG_SCTN0905_TUPDICT_DDICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a ddict <NAC><TUPDICTNAME><KEY><DDICTKEY>",),
	("FMAXPSG_SCTN0905_TUPDICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a TUPDICT in the second define section in PSG.py <NAC><TUPDICTNAME>",),
	("FMAXPSG_SCTN0905_TUPDICT_DICT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a tupdict <NAC><TUPDICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0905_TUPDICT_SS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a tupdict <NAC><TUPDICTNAME><STR><STR>",),
	("FMAXPSG_SCTN0905_TUPDICT_SV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a tupdict <NAC><TUPDICTNAME><STR><VAL>",),
	("FMAXPSG_SCTN0905_TUPDICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a tupdict <NAC><TUPDICTNAME><KEY><STR>",),
	("FMAXPSG_SCTN0905_TUPDICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a tupdict <NAC><TUPDICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0906_BTN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a button <NAC><BTNNAME>",),
	("FMAXPSG_SCTN0906_BTN_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0906_BTN_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><BTNNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0907_SPIN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a spin box entry <NAC><SPINNAME>",),
	("FMAXPSG_SCTN0907_SPIN_DICT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a STR to the SPINDICT <NAC><SPINNAME><KEY><STR>",),
	("FMAXPSG_SCTN0907_SPIN_DICT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a VAL to the SPINDICT <NAC><SPINNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0907_SPIN_VALUES_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a STR to the values list <NAC><SPINNAME><STR>",),
	("FMAXPSG_SCTN0907_SPIN_VALUES_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a VAL to the values list <NAC><SPINNAME><VAL>",),
	("FMAXPSG_SCTN0908_CHECKBOX_DEF", FMAXFM_SCTN0101_AX_DEF, "define a checkbox <NAC><CHECKBOXNAME>",),
	("FMAXPSG_SCTN0908_CHECKBOX_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a checkbox <NAC><CHECKBOXNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a checkbox <NAC><CHECKBOXNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0909_TEXT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a text <NAC><TEXTNAME>",),
	("FMAXPSG_SCTN0909_TEXT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a text element <NAC><TEXTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0909_TEXT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a text element <NAC><TEXTNAME>",),
	("FMAXPSG_SCTN090A_RADIO_DEF", FMAXFM_SCTN0101_AX_DEF, "define a radio button element",),
	("FMAXPSG_SCTN090B_COLUMN_BUTTON_ADD", FMAXFM_SCTN0101_AX_DEF, "add a button to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090B_COLUMN_CHECKBOX_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090B_COLUMN_COLUMN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090B_COLUMN_COLUMN_PARM_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column parm to the column to a row <NAC><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>",),
	("FMAXPSG_SCTN090B_COLUMN_COLUMN_PARM_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column parm to the column to a row <NAC><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>",),
	("FMAXPSG_SCTN090B_COLUMN_COMBO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090B_COLUMN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a column <NAC><COLUMNNAME>",),
	("FMAXPSG_SCTN090B_COLUMN_KEY_ADD", FMAXFM_SCTN0101_AX_DEF, "add a key to a column element 'key=' will be added automatically <NAC><COLUMNNAME><ROWKEY><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN090B_COLUMN_PACKEDPARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add packedparms to a column entry <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN090B_COLUMN_PARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add parms to a column entry <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN090B_COLUMN_RADIO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a radio to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090B_COLUMN_ROW_ADD", FMAXFM_SCTN0101_AX_DEF, "add a row [] to a column <NAC><COLUMNNAME><ROWKEY><LEVEL>",),
	("FMAXPSG_SCTN090B_COLUMN_SPIN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a spinbox to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090B_COLUMN_TEXT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a text element to a row <NAC><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090C_MAPPDS_DEF", FMAXFM_SCTN0101_AX_DEF, "add a nested dict holding all of the variables passed between PySimpleGUI and this app",),
	("FMAXPSG_SCTN090C_MAPPDS_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "add a dict to the mainapp dict <NAC><DICTNAME",),
	("FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a string to a dict mainapp dict <NAC><DICTNAME><KEY><STR>",),
	("FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a dict mainapp dict <NAC><DICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN090C_MAPPDS_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a string to the mainapp dict <NAC><KEY><STR>",),
	("FMAXPSG_SCTN090C_MAPPDS_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to the mainapp dict <NAC><KEY><VAL>",),
	("FMAXPSG_SCTN090D_MAINFRAME_DEF", FMAXFM_SCTN0101_AX_DEF, "define a frame <NAC><FRAMENAME><WINDOW><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)",),
	("FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD", FMAXFM_SCTN0101_AX_DEF, "add a button to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090E_LAYOUT_CHECKBOX_ADD", FMAXFM_SCTN0101_AX_DEF, "add a checkbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090E_LAYOUT_COMBO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090E_LAYOUT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a layout <NAC><LAYOUTNAME>",),
	("FMAXPSG_SCTN090E_LAYOUT_DEF", FMAXFM_SCTN0101_AX_DEF, "define layouts",),
	("FMAXPSG_SCTN090E_LAYOUT_KEY_ADD", FMAXFM_SCTN0101_AX_DEF, "add a key to a layout element 'key=' will be added automatically <NAC><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN090E_LAYOUT_PACKEDPARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add packedparms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add parms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN090E_LAYOUT_RADIO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a radio to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090E_LAYOUT_ROW_ADD", FMAXFM_SCTN0101_AX_DEF, "add a row [] to a layout <NAC><LAYOUTNAME><ROWKEY><LEVEL>",),
	("FMAXPSG_SCTN090E_LAYOUT_SPIN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a spinbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090E_LAYOUT_TEXT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a text element to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090F_WINDOW_DEF", FMAXFM_SCTN0101_AX_DEF, "define a main dictdict <NAC><MAINNAME>",),
	("FMAXPSG_SCTN090F_WINDOW_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),
	("FMAXPSG_SCTN090F_WINDOW_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),
	("FMAXPSG_SCTN0910_DUBLT_SS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>",),
	("FMAXPSG_SCTN0910_DUBLT_SV_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>",),
	("FMAXPSG_SCTN0910_DUBLT_VS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>",),
	("FMAXPSG_SCTN0910_DUBLT_VV_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple used to hold URL pairs <NAC><DUBTUPNAME><VAL1><VAL2>",),
	("FMAXPSG_SCTN0910_STR_DEF", FMAXFM_SCTN0101_AX_DEF, "define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>",),
	("FMAXPSG_SCTN0910_VAL_DEF", FMAXFM_SCTN0101_AX_DEF, "define a value in the second define section in PSG.py <NAC><VALNAME><VAL>",),
	("FMAXPSG_SCTN0911_COMBO_DEF", FMAXFM_SCTN0101_AX_DEF, "define a combo box",),
	("FMAXPSG_SCTN0912_FRAMEELEMENT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a frame element",),
	("FMAXPSG_SCTN0913_RCMENU_DEF", FMAXFM_SCTN0101_AX_DEF, "define a right click menu",),
	("FMAXPSG_SCTN0913_RCMENU_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a right click menu",),
	("FMAXPSG_SCTN0914_POPUPFRAME_DEF", FMAXFM_SCTN0101_AX_DEF, "define a frame <NAC><FRAMENAME><WINDOW><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)",),
	("FMAXPSG_SCTN0915_PUDLG_DEF", FMAXFM_SCTN0101_AX_DEF, "define a popup dialog <NAC><POPUPNAME><POPUPTYPE>",),
	("FMAXPSG_SCTN0915_PUDLG_DICT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a text element <NAC><POPUPNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a text element <NAC><POPUPNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0915_PUDLG_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a text element <NAC><POPUPNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0915_PUDLG_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a text element <NAC><POPUPNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_BTN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a button <NAC><CLASSNAME><BTNNAME>",),
	("FMAXPSG_SCTN0916_CLASS_BTN_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_BTN_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_CHECKBOX_DEF", FMAXFM_SCTN0101_AX_DEF, "define a checkbox <NAC><CLASSNAME><CHECKBOXNAME>",),
	("FMAXPSG_SCTN0916_CLASS_CHECKBOX_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_CHECKBOX_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_BUTTON_ADD", FMAXFM_SCTN0101_AX_DEF, "add a button to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_CHECKBOX_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_COLUMN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_COLUMN_PARM_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_COLUMN_PARM_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_COMBO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a column <NAC><CLASSNAME><COLUMNNAME>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_KEY_ADD", FMAXFM_SCTN0101_AX_DEF, "add a key to a column element 'key=' will be added automatically <NAC><CLASSNAME><COLUMNNAME><ROWKEY><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_PACKEDPARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add packedparms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add parms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_RADIO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a radio to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD", FMAXFM_SCTN0101_AX_DEF, "add a row [] to a column <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_SPIN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a spinbox to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_COLUMN_TEXT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a text element to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_COMBO_DEF", FMAXFM_SCTN0101_AX_DEF, "define a combo box",),
	("FMAXPSG_SCTN0916_CLASS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME>",),
	("FMAXPSG_SCTN0916_CLASS_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a dict in PSG <NAC><CLASSNAME><DICTNAME>",),
	("FMAXPSG_SCTN0916_CLASS_DICT_SS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str-str to a dict <NAC><CLASSNAME><DICTNAME><STR><STR>",),
	("FMAXPSG_SCTN0916_CLASS_DICT_SV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str-val to a dict <NAC><CLASSNAME><DICTNAME><STR><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a dict <NAC><CLASSNAME><DICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a dict in PSG <NAC><CLASSNAME><DICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_FRAMEELEMENT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a frame element",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_BUTTON_ADD", FMAXFM_SCTN0101_AX_DEF, "add a button to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_CHECKBOX_ADD", FMAXFM_SCTN0101_AX_DEF, "add a checkbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_COLUMN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_COMBO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a layout <NAC><CLASSNAME><LAYOUTNAME>",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_DEF", FMAXFM_SCTN0101_AX_DEF, "define layouts",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_KEY_ADD", FMAXFM_SCTN0101_AX_DEF, "add a key to a layout element 'key=' will be added automatically <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_PACKEDPARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add packedparms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_PARM_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add parms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_RADIO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a radio to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_ROW_ADD", FMAXFM_SCTN0101_AX_DEF, "add a row [] to a layout <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL>",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_SPIN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a spinbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_LAYOUT_TEXT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a text element to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN0916_CLASS_LIST_DEF", FMAXFM_SCTN0101_AX_DEF, "define a list in PSG <NAC><CLASSNAME><LISTNAME>",),
	("FMAXPSG_SCTN0916_CLASS_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a list in PSG <NAC><CLASSNAME><LISTNAME><STR>",),
	("FMAXPSG_SCTN0916_CLASS_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a list in PSG <NAC><CLASSNAME><LISTNAME><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_MAINFRAME_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class mainframe",),
	("FMAXPSG_SCTN0916_CLASS_POPUPFRAME_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class mainframe",),
	("FMAXPSG_SCTN0916_CLASS_RADIO_DEF", FMAXFM_SCTN0101_AX_DEF, "define a radio button element",),
	("FMAXPSG_SCTN0916_CLASS_RCMENU_DEF", FMAXFM_SCTN0101_AX_DEF, "define a right click menu",),
	("FMAXPSG_SCTN0916_CLASS_RCMENU_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a right click menu",),
	("FMAXPSG_SCTN0916_CLASS_SPIN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a spin box entry <NAC><CLASSNAME><SPINNAME>",),
	("FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a STR to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><STR>",),
	("FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a VAL to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_SPIN_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a STR to the values list <NAC><CLASSNAME><SPINNAME><STR>",),
	("FMAXPSG_SCTN0916_CLASS_SPIN_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a VAL to the values list <NAC><CLASSNAME><SPINNAME><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_TEXT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a text <NAC><TEXTNAME>",),
	("FMAXPSG_SCTN0916_CLASS_TEXT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a text element <NAC><CLASSNAME><TEXTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a text element <NAC><CLASSNAME><TEXTNAME>",),
	("FMAXPSG_SCTN0916_CLASS_WINDOW_DEF", FMAXFM_SCTN0101_AX_DEF, "define a main dictdict <NAC><CLASSNAME><MAINNAME>",),
	("FMAXPSG_SCTN0916_CLASS_WINDOW_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),
	("FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),
	("FMAXPSG_____", FMAX_NOP, "FMAXPSG_ENDS",),
	("FMAX_NOP", FMAXFM_SCTN0101_AX_DEF, "skip this entry",),
	("FMCF", FMAX_NOP, "FMCF_BEGINS",),
	("FMCF_SCTN0003_TYPE_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN009 types comments",),
	("FMCF_SCTN0003_TYPE_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN003 types",),
	("FMCF_SCTN0201_DEF_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN201 defines comments dict",),
	("FMCF_SCTN0201_DEF_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN201 defines dict",),
	("FMCF_SCTN0202_OPTIONSDICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN202 OPTIONSDICT comments dict",),
	("FMCF_SCTN0202_OPTIONSDICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN202 OPTIONSDICT",),
	("FMCF_SCTN0202_OPTIONSHELPDICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN202 OPTIONS HELPDICT",),
	("FMCF_SCTN0202_OPTIONS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN202 OPTIONS comments dict",),
	("FMCF_SCTN0202_OPTIONS_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN202 OPTIONS dict",),
	("FMCF_SCTN0203_DICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN203 dict comments dict",),
	("FMCF_SCTN0203_DICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN203 dict dict",),
	("FMCF_SCTN0204_LIST_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN204 list comments dict",),
	("FMCF_SCTN0204_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN204 list dict",),
	("FMCF_____", FMAX_NOP, "FMCF_ENDS",),
	("FMFM", FMAX_NOP, "FMFM_BEGINS",),
	("FMFMVAl_TABLEVEL", FMAXFM_SCTN0102_STR_DEF, "TABLEVEL", "TABLEVEL", "key for tab levels",),
	("FMFM_SCTN0101_AX_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN101 FMAX defined",),
	("FMFM_SCTN0101_AX_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN101 FMAX defined",),
	("FMFM_SCTN0102_VAL_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN102 val",),
	("FMFM_SCTN0102_VAL_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN102 val",),
	("FMFM_SCTN0103_DICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN103 dict defined",),
	("FMFM_SCTN0103_DICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN103 dict defined",),
	("FMFM_SCTN0104_LIST_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN201 device defines",),
	("FMFM_SCTN0104_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN201 device defines",),
	("FMFM_____", FMAX_NOP, "FMFM_ENDS",),
	("FMPSG", FMAX_NOP, "FMPSG_BEGINS",),
	("FMPSG_SCTN0900_DEF1_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0900_DEF1_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0901_DEF2_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0901",),
	("FMPSG_SCTN0901_DEF2_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0901",),
	("FMPSG_SCTN0902_DICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0902",),
	("FMPSG_SCTN0902_DICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0902",),
	("FMPSG_SCTN0903_LIST_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0903",),
	("FMPSG_SCTN0903_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0903",),
	("FMPSG_SCTN0904_PLATEQ_INNER_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0904",),
	("FMPSG_SCTN0904_PLATEQ_INNER_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0904",),
	("FMPSG_SCTN0904_PLATEQ_OUTER_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0904",),
	("FMPSG_SCTN0904_PLATEQ_OUTER_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0904",),
	("FMPSG_SCTN0905_TUPDICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0905",),
	("FMPSG_SCTN0905_TUPDICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0905",),
	("FMPSG_SCTN0905_TUPDICT_TDD_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0905",),
	("FMPSG_SCTN0906_BTNS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN0906_BTNS_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0907_SPIN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)f",),
	("FMPSG_SCTN0907_SPIN_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)",),
	("FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)",),
	("FMPSG_SCTN0908_CHECKBOX_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0908_CHECKBOX_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0909_TEXT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN0909_TEXT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090A_RADIO_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN090A_RADIO_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090B_COLUMN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090B_COLUMN_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090B_COLUMN_PARMS_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090C_MAPPDSDICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "the main app dict+dict for this app",),
	("FMPSG_SCTN090C_MAPPDS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "the main app dict for this app",),
	("FMPSG_SCTN090C_MAPPDS_DICT", FMAXFM_SCTN0103_DICT_DEF, "the main app dict for this app",),
	("FMPSG_SCTN090D_MAINFRAME_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN090D_MAINFRAME_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090E_LAYOUT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN090E_LAYOUT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN090F_WINDOW_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN090F_WINDOW_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0910_DEF3_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0910_DEF3_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0911_COMBO_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0911_COMBO_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0912_FRAME_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0912_FRAME_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0913_RCMENU_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0913_RCMENU_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0914_POPUPFRAME_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0914_POPUPFRAME_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the DIALOG DIALOG (TUPDICT)",),
	("FMPSG_SCTN0915_PUDLG_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the DIALOG DIALOG (TUPDICT)",),
	("FMPSG_SCTN0915_PUDLG_DICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the DIALOG DIALOG (TUPDICT)",),
	("FMPSG_SCTN0915_PUDLG_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the DIALOG DIALOG (TUPDICT)",),
	("FMPSG_SCTN0915_PUDLG_TYPE_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the DIALOG DIALOG (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_BTNS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_BTNS_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_CHECKBOX_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_CHECKBOX_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0916_CLASS_COLUMN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_COLUMN_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_COLUMN_PARMS_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_COMBO_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0916_CLASS_COMBO_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0916_CLASS_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0916_CLASS_DICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0916_CLASS_DICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0916_CLASS_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0916_CLASS_LIST_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0916_CLASS_FRAME_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0916_CLASS_FRAME_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0916_CLASS_LAYOUT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_LAYOUT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_RADIO_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_RADIO_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_RCMENU_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0916_CLASS_RCMENU_DICT", FMAXFM_SCTN0103_DICT_DEF, "define the dict to hold everything in SCTN0900",),
	("FMPSG_SCTN0916_CLASS_SPIN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)f",),
	("FMPSG_SCTN0916_CLASS_SPIN_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)",),
	("FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_TEXT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_TEXT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_WINDOW_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entries (TUPDICT)",),
	("FMPSG_SCTN0916_CLASS_WINDOW_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds all of the button entriess (TUPDICT)",),
	("FMPSG_____", FMAX_NOP, "FMPSG_ENDS",),
	("PSGVAL", FMAX_NOP, "FMPSG_BEGINS",),
	("PSGVAL_ALERTING_LIST", FMAXPSG_SCTN0903_LIST_DEF, "ALERTING_LIST", "list that holds all currently alarming events",),
	("PSGVAL_CLOSE_LIST", FMAXPSG_SCTN0903_LIST_DEF, "CLOSE_LIST", "list with close statuses",),
	("PSGVAL_CLOSE_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "CLOSE_LIST", "MOUSE_STATUS_CLOSE_E", "easet close entry",),
	("PSGVAL_CLOSE_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "CLOSE_LIST", "MOUSE_STATUS_CLOSE_N", "easet close entry",),
	("PSGVAL_CLOSE_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "CLOSE_LIST", "MOUSE_STATUS_CLOSE_NE", "easet close entry",),
	("PSGVAL_CLOSE_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "CLOSE_LIST", "MOUSE_STATUS_CLOSE_NW", "easet close entry",),
	("PSGVAL_CLOSE_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "CLOSE_LIST", "MOUSE_STATUS_CLOSE_S", "easet close entry",),
	("PSGVAL_CLOSE_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "CLOSE_LIST", "MOUSE_STATUS_CLOSE_SE", "easet close entry",),
	("PSGVAL_CLOSE_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "CLOSE_LIST", "MOUSE_STATUS_CLOSE_SW", "easet close entry",),
	("PSGVAL_CLOSE_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "CLOSE_LIST", "MOUSE_STATUS_CLOSE_W", "easet close entry",),
	("PSGVAL_COLOR", FMAX_NOP, "colors defined",),
	("PSGVAL_COLOR_ALERT_BACKGROUND", FMAXPSG_SCTN0900_STR_DEF, "COLOR_ALERT_BACKGROUND", "#662244", "alert background color",),
	("PSGVAL_COLOR_ALERT_TEXT", FMAXPSG_SCTN0900_STR_DEF, "COLOR_ALERT_TEXT", "#CC4466", "color of text on alert popup",),
	("PSGVAL_COLOR_BACKGROUND", FMAXPSG_SCTN0900_STR_DEF, "COLOR_BACKGROUND", "#331122", "the background of the main frames",),
	("PSGVAL_COLOR_BLACK", FMAXPSG_SCTN0900_STR_DEF, "COLOR_BLACK", "#000000", "black",),
	("PSGVAL_COLOR_BTN_BACKGROUND", FMAXPSG_SCTN0900_STR_DEF, "COLOR_BTN_BACKGROUND", "#441133", "background color on buttons by default",),
	("PSGVAL_COLOR_BTN_TEXT", FMAXPSG_SCTN0900_STR_DEF, "COLOR_BTN_TEXT", "#660044", "text color on buttons by default",),
	("PSGVAL_COLOR_CLOCK_BACKGROUND", FMAXPSG_SCTN0900_STR_DEF, "COLOR_CLOCK_BACKGROUND", "#221133", "the background of the main frames",),
	("PSGVAL_COLOR_GRAY3", FMAXPSG_SCTN0900_STR_DEF, "COLOR_GRAY3", "#333333", "gray 3",),
	("PSGVAL_COLOR_GRAY6", FMAXPSG_SCTN0900_STR_DEF, "COLOR_GRAY6", "#666666", "gray 6",),
	("PSGVAL_COLOR_GRAY9", FMAXPSG_SCTN0900_STR_DEF, "COLOR_GRAY9", "#999999", "gray 9",),
	("PSGVAL_COLOR_GRAYC", FMAXPSG_SCTN0900_STR_DEF, "COLOR_GRAYC", "#CCCCCC", "gray C",),
	("PSGVAL_COLOR_TEXT_HIGH", FMAXPSG_SCTN0900_STR_DEF, "COLOR_TEXT_HIGH", "#9900FF", "the highlight color used in blinking bits when they are 'lit'",),
	("PSGVAL_COLOR_TEXT_INTERVAL_COUNT_INACTIVE", FMAXPSG_SCTN0900_STR_DEF, "COLOR_TEXT_INTERVAL_COUNT_INACTIVE", "#999988", "the GRAY color used when the next event is not an interval",),
	("PSGVAL_COLOR_TEXT_LOW", FMAXPSG_SCTN0900_STR_DEF, "COLOR_TEXT_LOW", "#330022", "the color the clock digits are",),
	("PSGVAL_COLOR_TEXT_NORMAL", FMAXPSG_SCTN0900_STR_DEF, "COLOR_TEXT_NORMAL", "#660044", "the color the clock digits are",),
	("PSGVAL_COLOR_TIME_CLOCK", FMAXPSG_SCTN0900_STR_DEF, "COLOR_TIME_CLOCK", "#CC66FF", "color of the clock on any window/frame/etc.",),
	("PSGVAL_COLOR_TIME_ELAPSED", FMAXPSG_SCTN0900_STR_DEF, "COLOR_TIME_ELAPSED", "#447733", "color of the clock on any window/frame/etc.",),
	("PSGVAL_COLOR_TIME_TOGO", FMAXPSG_SCTN0900_STR_DEF, "COLOR_TIME_TOGO", "#AA6600", "color of the clock on any window/frame/etc.",),
	("PSGVAL_COLOR_WHITE", FMAXPSG_SCTN0900_STR_DEF, "COLOR_WHITE", "#FFFFFF", "white",),
	("PSGVAL_EMPTY0_EVENT_ENTRY", FMAXPSG_SCTN0905_TUPDICT_DEF, "EMPTY0_EVENT_ENTRY", "define the empty event entries for MAPPDS",),
	("PSGVAL_EMPTY0_EVENT_ENTRY_DISMISSED", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY0_EVENT_ENTRY", "DISMISSED", "False", "has the event been dismissed just this once",),
	("PSGVAL_EMPTY0_EVENT_ENTRY_ENABLED", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY0_EVENT_ENTRY", "ENABLED", "True", "is the event enabled bool",),
	("PSGVAL_EMPTY0_EVENT_ENTRY_EVENTMODE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY0_EVENT_ENTRY", "EVENTMODE", "EVENTMODE_ALARM", "which event mode is this event",),
	("PSGVAL_EMPTY0_EVENT_ENTRY_NAME", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "EMPTY0_EVENT_ENTRY", "NAME", "alarm", "the name of this event",),
	("PSGVAL_EMPTY0_EVENT_ENTRY_PREDISMISSABLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY0_EVENT_ENTRY", "PREDISMISSABLE", "False", "can the event be dismissed prior to on time",),
	("PSGVAL_EMPTY0_EVENT_ENTRY_SNOOZABLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY0_EVENT_ENTRY", "SNOOZABLE", "False", "can the alarm be snoozed",),
	("PSGVAL_EMPTY0_EVENT_ENTRY_SNOOZED", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY0_EVENT_ENTRY", "SNOOZED", "False", "is the event snoozed",),
	("PSGVAL_EMPTY0_EVENT_ENTRY_TIME_ALARM", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY0_EVENT_ENTRY", "TIME_ALARM", "ZERO_CLOCK", "in an alarm mode event, what time is the alarm",),
	("PSGVAL_EMPTY0_EVENT_ENTRY_TIME_AT_LAST_RUN", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY0_EVENT_ENTRY", "TIME_AT_LAST_RUN", "0", "has the event been dismissed just this once",),
	("PSGVAL_EMPTY0_EVENT_ENTRY_TIME_INTERVAL", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY0_EVENT_ENTRY", "TIME_INTERVAL", "ZERO_CLOCK", "how much time to add to an interval mode event",),
	("PSGVAL_EMPTY_BBOX", FMAXPSG_SCTN0901_VAL_DEF, "EMPTY_BBOX", "(0, 0, 0, 0)", "create as needed dict for values passed around as dict",),
	("PSGVAL_EMPTY_CLOCKS", FMAXPSG_SCTN0905_TUPDICT_DEF, "EMPTY_CLOCKS", "just the clocks window",),
	("PSGVAL_EMPTY_CLOCKS_TIME_AT_NEXT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_CLOCKS", "TIME_AT_NEXT", "ZERO_CLOCK", "the main count down to the next event time",),
	("PSGVAL_EMPTY_CLOCKS_TIME_AT_ZEROELAPSE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_CLOCKS", "TIME_AT_ZEROELAPSE", "ZERO_CLOCK", "the main clock time",),
	("PSGVAL_EMPTY_CLOCKS_TIME_CLOCK", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_CLOCKS", "TIME_CLOCK", "ZERO_CLOCK", "the main clock time",),
	("PSGVAL_EMPTY_CLOCKS_TIME_ELAPSED", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_CLOCKS", "TIME_ELAPSED", "ZERO_CLOCK", "the main elapsed time",),
	("PSGVAL_EMPTY_CLOCKS_TIME_TOGO", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_CLOCKS", "TIME_TOGO", "ZERO_CLOCK", "the main count down to the next event time",),
	("PSGVAL_EMPTY_MAPPDS", FMAXPSG_SCTN0905_TUPDICT_DEF, "EMPTY_MAPPDS", "holds the empty tupt dict for the root MAPPDS",),
	("PSGVAL_EMPTY_MAPPDS01_ALPHA_CHANNEL", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "ALPHA_CHANNEL", "1.0", "fully opaque",),
	("PSGVAL_EMPTY_MAPPDS01_ALPHA_HIGH", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "ALPHA_HIGH", "1.0", "fully opaque",),
	("PSGVAL_EMPTY_MAPPDS01_ALPHA_LOW", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "ALPHA_LOW", "0.3", "almost fully alpha",),
	("PSGVAL_EMPTY_MAPPDS01_APPMODE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "APPMODE", "APPMODE_CLOCKS", "default to clocks mode",),
	("PSGVAL_EMPTY_MAPPDS01_BBOX", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "BBOX", "EMPTY_BBOX", "empty bbox entry",),
	("PSGVAL_EMPTY_MAPPDS01_CHECKBOX_ALPHA_LOW", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "CHECKBOX_ALPHA_LOW", "True", "the checkbox bool for ALPHA high/low mode",),
	("PSGVAL_EMPTY_MAPPDS01_CHECKBOX_RUNAWAY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "CHECKBOX_RUNAWAY", "True", "checkbox bool for RUNAWAY mode",),
	("PSGVAL_EMPTY_MAPPDS01_CLOSE_BBOX", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "CLOSE_BBOX", "EMPTY_BBOX", "empty BBOX dict",),
	("PSGVAL_EMPTY_MAPPDS01_EVENT_ENTRIES", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "EVENT_ENTRIES", "EMPTY0_EVENT_ENTRY_TDD", "an empty event",),
	("PSGVAL_EMPTY_MAPPDS01_INDEX_OF_NEXT_EVENT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "INDEX_OF_NEXT_EVENT", "0", "which event number is upcoming",),
	("PSGVAL_EMPTY_MAPPDS01_MAINFRAME_LCN", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "MAINFRAME_LCN", "EMPTY_XY", "holds the screen position",),
	("PSGVAL_EMPTY_MAPPDS01_MAINFRAME_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "MAINFRAME_SIZE", "EMPTY_XY", "which event number is upcoming",),
	("PSGVAL_EMPTY_MAPPDS01_SCREEN_DIMS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "EMPTY_MAPPDS", "SCREEN_DIMS", "EMPTY_XY", "",),
	("PSGVAL_EMPTY_XY", FMAXPSG_SCTN0901_VAL_DEF, "EMPTY_XY", "(0, 0)", "empty XY dict",),
	("PSGVAL_FONT_DEFAULT", FMAXPSG_SCTN0900_STR_DEF, "FONT_DEFAULT", "Source Code Pro", "set the main font",),
	("PSGVAL_FULL_BUTTON", FMAXPSG_SCTN0905_TUPDICT_DEF, "FULL_BUTTON", "define the button empty tupdict",),
	("PSGVAL_FULL_BUTTON_AUTO_SIZE_BUTTON", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "AUTO_SIZE_BUTTON", "None", "if True the button size is sized to fit the text",),
	("PSGVAL_FULL_BUTTON_BIND_RETURN_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "BIND_RETURN_KEY", "False", "If True the return key will cause this button to be pressed",),
	("PSGVAL_FULL_BUTTON_BORDER_WIDTH", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "BORDER_WIDTH", "None", "width of border around button in pixels",),
	("PSGVAL_FULL_BUTTON_BUTTON_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "BUTTON_COLOR", "None", "Color of button. default is from theme or the window. Easy to remember which is which if you say 'ON' between colors. 'red' on 'green'. Normally a tuple, but can be a simplified-button-color-string 'foreground on background'. Can be a single color if want to set only the background.",),
	("PSGVAL_FULL_BUTTON_BUTTON_TEXT", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "FULL_BUTTON", "BUTTON_TEXT", "", "str text to display on the button",),
	("PSGVAL_FULL_BUTTON_BUTTON_TYPE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "BUTTON_TYPE", "7", "You  should NOT be setting this directly. ONLY the shortcut functions set this",),
	("PSGVAL_FULL_BUTTON_CHANGE_SUBMITS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "CHANGE_SUBMITS", "False", "DO NOT USE. Only listed for backwards compat - Use enable_events instead",),
	("PSGVAL_FULL_BUTTON_DEFAULT_EXTENSION", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "FULL_BUTTON", "DEFAULT_EXTENSION", "", "If no extension entered by user, add this to filename (only used in saveas dialogs)",),
	("PSGVAL_FULL_BUTTON_DISABLED", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "DISABLED", "False", "If True button will be created disabled. If FULL_BUTTON_DISABLED_MEANS_IGNORE then the button will be ignored rather than disabled using tkinter",),
	("PSGVAL_FULL_BUTTON_DISABLED_BUTTON_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "DISABLED_BUTTON_COLOR", "None", "colors to use when button is disabled (text, background). Use None for a color if don't want to change. Only ttk buttons support both text and background colors. tk buttons only support changing text color",),
	("PSGVAL_FULL_BUTTON_ENABLE_EVENTS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "ENABLE_EVENTS", "False", "Turns on the element specific events. If this button is a target, should it generate an event when filled in",),
	("PSGVAL_FULL_BUTTON_FILE_TYPES", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "FILE_TYPES", "(('ALL FILES', '*.*'),)", "the filetypes that will be used to match files. To indicate all files: (('ALL Files', '*.*'),).  Note - NOT SUPPORTED ON MAC",),
	("PSGVAL_FULL_BUTTON_FOCUS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "FOCUS", "False", "if True, initial focus will be put on this button",),
	("PSGVAL_FULL_BUTTON_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_FULL_BUTTON_HIGHLIGHT_COLORS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "HIGHLIGHT_COLORS", "None", "colors to use when button has focus (highlight, background). None will use computed colors. Only used by Linux and only for non-TTK button",),
	("PSGVAL_FULL_BUTTON_IMAGE_DATA", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "IMAGE_DATA", "None", "Raw or Base64 representation of the image to put on button. Choose either filename or data",),
	("PSGVAL_FULL_BUTTON_IMAGE_FILENAME", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "IMAGE_FILENAME", "None", "image filename if there is a button image. GIFs and PNGs only.",),
	("PSGVAL_FULL_BUTTON_IMAGE_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "IMAGE_SIZE", "(None, None)", "Size of the image in pixels (width, height)",),
	("PSGVAL_FULL_BUTTON_IMAGE_SUBSAMPLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "IMAGE_SUBSAMPLE", "None", "amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc",),
	("PSGVAL_FULL_BUTTON_INITIAL_FOLDER", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "INITIAL_FOLDER", "None", "starting path for folders and files",),
	("PSGVAL_FULL_BUTTON_K", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "K", "None", "Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element",),
	("PSGVAL_FULL_BUTTON_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element",),
	("PSGVAL_FULL_BUTTON_METADATA", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_BUTTON_PAD", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "PAD", "None", "Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_BUTTON_RIGHT_CLICK_MENU", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "RIGHT_CLICK_MENU", "None", "A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.",),
	("PSGVAL_FULL_BUTTON_S", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "S", "(None, None)", "(width, height) of the button in characters wide, rows high",),
	("PSGVAL_FULL_BUTTON_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "SIZE", "(None, None)", "(width, height) of the button in characters wide, rows high",),
	("PSGVAL_FULL_BUTTON_TARGET", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "TARGET", "(None, None)", "str | Tuple[int, int] key or (row,col) target for the button. Note that -1 for column means 1 element to the left of this one. The constant ThisRow is used to indicate the current row. The Button itself is a valid target for some types of button",),
	("PSGVAL_FULL_BUTTON_TOOLTIP", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "TOOLTIP", "None", "text, that will appear when mouse hovers over the element",),
	("PSGVAL_FULL_BUTTON_USE_TTK_BUTTONS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "USE_TTK_BUTTONS", "None", "True = use ttk buttons. False = do not use ttk buttons.  None (Default) = use ttk buttons only if on a Mac and not with button images",),
	("PSGVAL_FULL_BUTTON_VISIBLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_BUTTON", "VISIBLE", "True", "set visibility state of the element",),
	("PSGVAL_FULL_CHECKBOX", FMAXPSG_SCTN0905_TUPDICT_DEF, "FULL_CHECKBOX", "set a checkbox in motion",),
	("PSGVAL_FULL_CHECKBOX_AUTO_SIZE_TEXT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "AUTO_SIZE_TEXT", "None", "if True will size the element to match the length of the text",),
	("PSGVAL_FULL_CHECKBOX_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_FULL_CHECKBOX_CHANGE_SUBMITS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "CHANGE_SUBMITS", "False", "DO NOT USE. Only listed for backwards compat - Use enable_events instead",),
	("PSGVAL_FULL_CHECKBOX_CHECKBOX_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "CHECKBOX_COLOR", "None", "color of background of the box that has the check mark in it. The checkmark is the same color as the text",),
	("PSGVAL_FULL_CHECKBOX_DEFAULT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "DEFAULT", "False", "Set to True if you want this checkbox initially checked",),
	("PSGVAL_FULL_CHECKBOX_DISABLED", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "DISABLED", "False", "set disable state",),
	("PSGVAL_FULL_CHECKBOX_ENABLE_EVENTS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "ENABLE_EVENTS", "False", "Turns on the element specific events. Checkbox events happen when an item changes",),
	("PSGVAL_FULL_CHECKBOX_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_FULL_CHECKBOX_K", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "K", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_FULL_CHECKBOX_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_FULL_CHECKBOX_METADATA", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_CHECKBOX_PAD", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "PAD", "None", "Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_CHECKBOX_S", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "S", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_FULL_CHECKBOX_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "SIZE", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_FULL_CHECKBOX_TEXT", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "FULL_CHECKBOX", "TEXT", "", "Window to display next to checkbox",),
	("PSGVAL_FULL_CHECKBOX_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_FULL_CHECKBOX_TOOLTIP", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "TOOLTIP", "None", "that will appear when mouse hovers over the element",),
	("PSGVAL_FULL_CHECKBOX_VISIBLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_CHECKBOX", "VISIBLE", "True", "set visibility state of the element",),
	("PSGVAL_FULL_COLUMN", FMAXPSG_SCTN0905_TUPDICT_DEF, "FULL_COLUMN", "full column entry",),
	("PSGVAL_FULL_COLUMN_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "BACKGROUND_COLOR", "None", "color of background of entire Column",),
	("PSGVAL_FULL_COLUMN_ELEMENT_JUSTIFICATION", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "ELEMENT_JUSTIFICATION", "None", "All elements inside the Column will have this justification 'left', 'right', 'center' are valid values",),
	("PSGVAL_FULL_COLUMN_EXPAND_X", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "EXPAND_X", "None", "If True the column will automatically expand in the X direction to fill available space",),
	("PSGVAL_FULL_COLUMN_EXPAND_Y", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "EXPAND_Y", "None", "If True the column will automatically expand in the X direction to fill available space",),
	("PSGVAL_FULL_COLUMN_GRAB", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "GRAB", "None", "If True can grab this element and move the window around. Default is False",),
	("PSGVAL_FULL_COLUMN_JUSTIFICATION", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "JUSTIFICATION", "None", "set justification for the Column itself. Note entire row containing the Column will be affected",),
	("PSGVAL_FULL_COLUMN_K", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "K", "None", "Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window",),
	("PSGVAL_FULL_COLUMN_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "KEY", "None", "Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window",),
	("PSGVAL_FULL_COLUMN_LAYOUT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "LAYOUT", "[]", "Layout that will be shown in the Column container",),
	("PSGVAL_FULL_COLUMN_METADATA", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_COLUMN_PAD", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "PAD", "None", "Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_COLUMN_RIGHT_CLICK_MENU", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "RIGHT_CLICK_MENU", "None", "A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.",),
	("PSGVAL_FULL_COLUMN_S", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "S", "(None, None)", "(width, height) size in pixels (doesn't work quite right, sometimes only 1 dimension is set by tkinter",),
	("PSGVAL_FULL_COLUMN_SCROLLABLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "SCROLLABLE", "False", "if True then scrollbars will be added to the column",),
	("PSGVAL_FULL_COLUMN_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "SIZE", "(None, None)", "(width, height) size in pixels (doesn't work quite right, sometimes only 1 dimension is set by tkinter",),
	("PSGVAL_FULL_COLUMN_VERTACLE_SCROLL_ONLY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "VERTICAL_SCROLL_ONLY", "False", "if True then no horizontal scrollbar will be shown",),
	("PSGVAL_FULL_COLUMN_VERTICAL_ALIGNMENT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "VERTICAL_ALIGNMENT", "None", "Place the column at the 'top', 'center', 'bottom' of the row (can also use t,c,r). Defaults to no setting (tkinter decides)",),
	("PSGVAL_FULL_COLUMN_VISIBLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COLUMN", "VISIBLE", "True", "set visibility state of the element",),
	("PSGVAL_FULL_COMBO", FMAXPSG_SCTN0905_TUPDICT_DEF, "FULL_COMBO", "a full combo tupdict",),
	("PSGVAL_FULL_COMBO_AUTO_SIZE_TEXT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "AUTO_SIZE_TEXT", "None", "True if element should be the same size as the contents",),
	("PSGVAL_FULL_COMBO_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_FULL_COMBO_CHANGE_SUBMITS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "CHANGE_SUBMITS", "False", "DEPRICATED DO NOT USE. Use `enable_events` instead",),
	("PSGVAL_FULL_COMBO_DEFAULT_VALUE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "DEFAULT_VALUE", "None", "Choice to be displayed as initial value. Must match one of values variable contents",),
	("PSGVAL_FULL_COMBO_DISABLED", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "DISABLED", "False", "set disable state for element",),
	("PSGVAL_FULL_COMBO_ENABLE_EVENTS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "ENABLE_EVENTS", "False", "",),
	("PSGVAL_FULL_COMBO_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_FULL_COMBO_K", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "K", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_FULL_COMBO_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_FULL_COMBO_METADATA", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_COMBO_PAD", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "PAD", "None", "Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_COMBO_READONLY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "READONLY", "False", "make element readonly (user can't change). True means user cannot change",),
	("PSGVAL_FULL_COMBO_S", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "S", "(None, None)", "width, height. Width = characters-wide, height = NOTE it's the number of entries to show in the list",),
	("PSGVAL_FULL_COMBO_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "SIZE", "(None, None)", "width, height. Width = characters-wide, height = NOTE it's the number of entries to show in the list",),
	("PSGVAL_FULL_COMBO_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_FULL_COMBO_TOOLTIP", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "TOOLTIP", "None", "text that will appear when mouse hovers over this element",),
	("PSGVAL_FULL_COMBO_VALUES", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "VALUES", "[]", "values to choose. While displayed as text, the items returned are what the caller supplied, not text",),
	("PSGVAL_FULL_COMBO_VISIBLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_COMBO", "VISIBLE", "True", "set visibility state of the element",),
	("PSGVAL_FULL_RADIO", FMAXPSG_SCTN0905_TUPDICT_DEF, "FULL_RADIO", "define a full radio button entity",),
	("PSGVAL_FULL_RADIO_AUTO_SIZE_TEXT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "AUTO_SIZE_TEXT", "None", "",),
	("PSGVAL_FULL_RADIO_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "BACKGROUND_COLOR", "None", "",),
	("PSGVAL_FULL_RADIO_CHANGE_SUBMITS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "CHANGE_SUBMITS", "False", "",),
	("PSGVAL_FULL_RADIO_CIRCLE_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "CIRCLE_COLOR", "None", "",),
	("PSGVAL_FULL_RADIO_DEFAULT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "DEFAULT", "False", "",),
	("PSGVAL_FULL_RADIO_DISABLED", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "DISABLED", "False", "",),
	("PSGVAL_FULL_RADIO_ENABLE_EVENTS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "ENABLE_EVENTS", "False", "",),
	("PSGVAL_FULL_RADIO_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "FONT", "None", "",),
	("PSGVAL_FULL_RADIO_GROUP_ID", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "FULL_RADIO", "GROUP_ID", "", "Groups together multiple Radio Buttons. Any type works",),
	("PSGVAL_FULL_RADIO_K", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "K", "None", "",),
	("PSGVAL_FULL_RADIO_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "KEY", "None", "",),
	("PSGVAL_FULL_RADIO_METADATA", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "METADATA", "None", "",),
	("PSGVAL_FULL_RADIO_PAD", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "PAD", "None", "",),
	("PSGVAL_FULL_RADIO_S", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "S", "(None, None)", "",),
	("PSGVAL_FULL_RADIO_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "SIZE", "(None, None)", "",),
	("PSGVAL_FULL_RADIO_TEXT", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "FULL_RADIO", "TEXT", "", "",),
	("PSGVAL_FULL_RADIO_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "TEXT_COLOR", "None", "",),
	("PSGVAL_FULL_RADIO_TOOLTIP", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "TOOLTIP", "None", "",),
	("PSGVAL_FULL_RADIO_VISIBLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_RADIO", "VISIBLE", "True", "",),
	("PSGVAL_FULL_SPIN", FMAXPSG_SCTN0905_TUPDICT_DEF, "FULL_SPIN", "full spin dict",),
	("PSGVAL_FULL_SPIN_AUTO_SIZE_TEXT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "AUTO_SIZE_TEXT", "None", "if True will size the element to match the length of the text",),
	("PSGVAL_FULL_SPIN_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_FULL_SPIN_CHANGE_SUBMITS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "CHANGE_SUBMITS", "False", "DO NOT USE. Only listed for backwards compat - Use enable_events instead",),
	("PSGVAL_FULL_SPIN_DISABLED", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "DISABLED", "False", "set disable state",),
	("PSGVAL_FULL_SPIN_ENABLE_EVENTS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "ENABLE_EVENTS", "False", "Turns on the element specific events. Spin events happen when an item changes",),
	("PSGVAL_FULL_SPIN_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_FULL_SPIN_INITIAL_VALUE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "INITIAL_VALUE", "None", "Initial item to show in window. Choose from list of values supplied",),
	("PSGVAL_FULL_SPIN_K", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "K", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_FULL_SPIN_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_FULL_SPIN_METADATA", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_SPIN_PAD", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "PAD", "None", "Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_SPIN_READONLY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "READONLY", "False", "readonly bool",),
	("PSGVAL_FULL_SPIN_S", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "S", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_FULL_SPIN_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "SIZE", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_FULL_SPIN_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_FULL_SPIN_TOOLTIP", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "TOOLTIP", "None", "text, that will appear when mouse hovers over the element",),
	("PSGVAL_FULL_SPIN_VALUES", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "VALUES", "[]", "List of valid values",),
	("PSGVAL_FULL_SPIN_VISIBLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_SPIN", "VISIBLE", "True", "set visibility state of the element",),
	("PSGVAL_FULL_TEXT", FMAXPSG_SCTN0905_TUPDICT_DEF, "FULL_TEXT", "the full monty for text elements",),
	("PSGVAL_FULL_TEXT_AUTO_SIZE_TEXT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "AUTO_SIZE_TEXT", "None", "if True size of the Window Element will be sized to fit the string provided in 'text' parm",),
	("PSGVAL_FULL_TEXT_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_FULL_TEXT_BORDER_WIDTH", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "BORDER_WIDTH", "None", "number of pixels for the border (if using a relief)",),
	("PSGVAL_FULL_TEXT_CLICK_SUBMITS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "CLICK_SUBMITS", "False", "DO NOT USE. Only listed for backwards compat - Use enable_events instead",),
	("PSGVAL_FULL_TEXT_ENABLE_EVENTS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "ENABLE_EVENTS", "False", "Turns on the element specific events. Window events happen when the text is clicked",),
	("PSGVAL_FULL_TEXT_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_FULL_TEXT_GRAB", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "GRAB", "None", "If True can grab this element and move the window around. Default is False",),
	("PSGVAL_FULL_TEXT_JUSTIFICATION", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "JUSTIFICATION", "None", "how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center`",),
	("PSGVAL_FULL_TEXT_K", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "K", "None", "Same as the Key. You can use either k or key. Which ever is set will be used.",),
	("PSGVAL_FULL_TEXT_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element",),
	("PSGVAL_FULL_TEXT_METADATA", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_TEXT_PAD", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "PAD", "None", "Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_TEXT_RELIEF", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "RELIEF", "None", "relief style around the text. Values are same as progress meter relief values. Should be a constant that is defined at starting with 'RELIEF_' - `RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID`",),
	("PSGVAL_FULL_TEXT_RIGHT_CLICK_MENU", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "RIGHT_CLICK_MENU", "None", "A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.",),
	("PSGVAL_FULL_TEXT_S", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "S", "(None, None)", "Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used",),
	("PSGVAL_FULL_TEXT_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "SIZE", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_FULL_TEXT_TEXT", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "FULL_TEXT", "TEXT", "", "The text to display. Can include /n to achieve multiple lines.  Will convert (optional) parameter into a string",),
	("PSGVAL_FULL_TEXT_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_FULL_TEXT_TOOLTIP", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "TOOLTIP", "None", "text, that will appear when mouse hovers over the element",),
	("PSGVAL_FULL_TEXT_VISIBLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_TEXT", "VISIBLE", "True", "set visibility state of the element",),
	("PSGVAL_FULL_WINDOW", FMAXPSG_SCTN0905_TUPDICT_DEF, "FULL_WINDOW", "define the FULL_WINDOW tupdict",),
	("PSGVAL_FULL_WINDOW_ALPHA_CHANNEL", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "ALPHA_CHANNEL", "1", "Sets the opacity of the window. 0 = invisible 1 = completely visible. Values bewteen 0 & 1 will produce semi-transparent windows in SOME environments (The Raspberry Pi always has this value at 1 and cannot change.",),
	("PSGVAL_FULL_WINDOW_AUTO_CLOSE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "AUTO_CLOSE", "False", "If True, the window will automatically close itself",),
	("PSGVAL_FULL_WINDOW_AUTO_CLOSE_DURATION", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "AUTO_CLOSE_DURATION", "3", "Number of seconds to wait before closing the window",),
	("PSGVAL_FULL_WINDOW_AUTO_SIZE_BUTTONS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "AUTO_SIZE_BUTTONS", "None", "True if Buttons in this Window should be sized to exactly fit the text on this.",),
	("PSGVAL_FULL_WINDOW_AUTO_SIZE_TEXT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "AUTO_SIZE_TEXT", "None", "True if Elements in Window should be sized to exactly fir the length of text",),
	("PSGVAL_FULL_WINDOW_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_FULL_WINDOW_BORDER_DEPTH", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "BORDER_DEPTH", "None", "Default border depth (width) for all elements in the window",),
	("PSGVAL_FULL_WINDOW_BUTTON_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "BUTTON_COLOR", "None", "Default button colors for all buttons in the window",),
	("PSGVAL_FULL_WINDOW_DEBUGGER_ENABLED", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "DEBUGGER_ENABLED", "True", "Default border depth (width) for all elements in the window",),
	("PSGVAL_FULL_WINDOW_DEFAULT_BUTTON_ELEMENT_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "DEFAULT_BUTTON_ELEMENT_SIZE", "(None, None)", "(width, height) size in characters (wide) and rows (high) for all Button elements in this window",),
	("PSGVAL_FULL_WINDOW_DEFAULT_ELEMENT_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "DEFAULT_ELEMENT_SIZE", "(45, 1)", "size in characters (wide) and rows (high) for all elements in this window",),
	("PSGVAL_FULL_WINDOW_DISABLE_CLOSE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "DISABLE_CLOSE", "False", "If True, the X button in the top right corner of the window will no work.  Use with caution and always give a way out toyour users",),
	("PSGVAL_FULL_WINDOW_DISABLE_MINIMIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "DISABLE_MINIMIZE", "False", "if True the user won't be able to minimize window.  Good for taking over entire screen and staying that way.",),
	("PSGVAL_FULL_WINDOW_ELEMENT_JUSTIFICATION", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "FULL_WINDOW", "ELEMENT_JUSTIFICATION", "left", "All elements in the Window itself will have this justification 'left', 'right', 'center' are valid values",),
	("PSGVAL_FULL_WINDOW_ELEMENT_PADDING", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "ELEMENT_PADDING", "None", "Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom))",),
	("PSGVAL_FULL_WINDOW_ENABLE_CLOSE_ATTEMPTED_EVENT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "ENABLE_CLOSE_ATTEMPTED_EVENT", "False", "If True then the window will not close when 'X' clicked. Instead an event FULL_WINDOW_CLOSE_ATTEMPTED_EVENT if returned from window.read",),
	("PSGVAL_FULL_WINDOW_FINALIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "FINALIZE", "False", "If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code",),
	("PSGVAL_FULL_WINDOW_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_FULL_WINDOW_FORCE_TOPLEVEL", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "FORCE_TOPLEVEL", "False", "If True will cause this window to skip the normal use of a hidden master window",),
	("PSGVAL_FULL_WINDOW_GRAB_ANYWHERE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "GRAB_ANYWHERE", "False", "If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems",),
	("PSGVAL_FULL_WINDOW_ICON", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "ICON", "None", "Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO",),
	("PSGVAL_FULL_WINDOW_KEEP_ON_TOP", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "KEEP_ON_TOP", "False", "If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm",),
	("PSGVAL_FULL_WINDOW_LAYOUT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "LAYOUT", "None", "The layout for the window. Can also be specified in the Layout method",),
	("PSGVAL_FULL_WINDOW_LOCATION", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "LOCATION", "(None, None)", "(x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen.",),
	("PSGVAL_FULL_WINDOW_MARGINS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "MARGINS", "(None, None)", "(left/right, top/bottom) Amount of pixels to leave inside the window's frame around the edges before your elements are shown.",),
	("PSGVAL_FULL_WINDOW_METADATA", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "METADATA", "None", "User metadata that can be set to ANYTHING",),
	("PSGVAL_FULL_WINDOW_MODAL", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "MODAL", "False", "If True then this window will be the only window a user can interact with until it is closed",),
	("PSGVAL_FULL_WINDOW_NO_TITLEBAR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "NO_TITLEBAR", "False", "If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar",),
	("PSGVAL_FULL_WINDOW_PROGRESS_BAR_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "PROGRESS_BAR_COLOR", "(None, None)", "(bar color, background color) Sets the default colors for all progress bars in the window",),
	("PSGVAL_FULL_WINDOW_RESIZABLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "RESIZABLE", "False", "If True, allows the user to resize the window. Note the not all Elements will change size or location when resizing.",),
	("PSGVAL_FULL_WINDOW_RETURN_KEYBOARD_EVENTS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "RETURN_KEYBOARD_EVENTS", "False", "if True key presses on the keyboard will be returned as Events from Read calls",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "RIGHT_CLICK_MENU", "None", "A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "RIGHT_CLICK_MENU_BACKGROUND_COLOR", "None", "Background color for right click menus",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR", "None", "Window color for disabled right click menu items",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "RIGHT_CLICK_MENU_FONT", "None", "Font for right click menus",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU_SELECTED_COLORS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "RIGHT_CLICK_MENU_SELECTED_COLORS", "(None, None)", "Window AND background colors for a selected item. Can be a Tuple OR a color string. simplified-button-color-string 'foreground on background'. Can be a single color if want to set only the background.",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU_TEAROFF", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "RIGHT_CLICK_MENU_TEAROFF", "False", "If True then all right click menus can be torn off",),
	("PSGVAL_FULL_WINDOW_RIGHT_CLICK_MENU_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "RIGHT_CLICK_MENU_TEXT_COLOR", "None", "Window color for right click menus",),
	("PSGVAL_FULL_WINDOW_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "SIZE", "(None, None)", "(width, height) size in pixels for this window. Normally the window is autosized to fit contents, not set to an absolute size by the user",),
	("PSGVAL_FULL_WINDOW_TEXT_JUSTIFICATION", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "TEXT_JUSTIFICATION", "None", "Default text justification for all Window Elements in window",),
	("PSGVAL_FULL_WINDOW_TITLE", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "FULL_WINDOW", "TITLE", "", "The title that will be displayed in the Titlebar and on the Taskbar",),
	("PSGVAL_FULL_WINDOW_TITLEBAR_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "TITLEBAR_BACKGROUND_COLOR", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as background color",),
	("PSGVAL_FULL_WINDOW_TITLEBAR_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "TITLEBAR_FONT", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as title font",),
	("PSGVAL_FULL_WINDOW_TITLEBAR_ICON", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "TITLEBAR_ICON", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as the icon (file or base64 bytes)",),
	("PSGVAL_FULL_WINDOW_TITLEBAR_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "TITLEBAR_TEXT_COLOR", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as text color",),
	("PSGVAL_FULL_WINDOW_TRANSPARENT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "TRANSPARENT_COLOR", "None", "Any portion of the window that has this color will be completely transparent. You can even click through these spots to the window under this window.",),
	("PSGVAL_FULL_WINDOW_TTK_THEME", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "TTK_THEME", "None", "Set the tkinter ttk 'theme' of the window.  Default = DEFAULT_TTK_THEME.  Sets all ttk widgets to this theme as their default",),
	("PSGVAL_FULL_WINDOW_USE_CUSTOM_TITLEBAR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "USE_CUSTOM_TITLEBAR", "None", "If True, then a custom titlebar will be used instead of the normal titlebar",),
	("PSGVAL_FULL_WINDOW_USE_DEFAULT_FOCUS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "USE_DEFAULT_FOCUS", "True", "If True will use the default focus algorithm to set the focus to the 'Correct' element",),
	("PSGVAL_FULL_WINDOW_USE_TTK_BUTTONS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "FULL_WINDOW", "USE_TTK_BUTTONS", "None", "Affects all buttons in window. True = use ttk buttons. False = do not use ttk buttons.  None = use ttk buttons only if on a Mac",),
	("PSGVAL_INDEX_EAST", FMAXPSG_SCTN0900_VAL_DEF, "INDEX_EAST", "2", "EAST",),
	("PSGVAL_INDEX_NORTH", FMAXPSG_SCTN0900_VAL_DEF, "INDEX_NORTH", "1", "NORTH",),
	("PSGVAL_INDEX_SOUTH", FMAXPSG_SCTN0900_VAL_DEF, "INDEX_SOUTH", "3", "SOUTH",),
	("PSGVAL_INDEX_WEST", FMAXPSG_SCTN0900_VAL_DEF, "INDEX_WEST", "0", "WEST",),
	("PSGVAL_INDEX_X", FMAXPSG_SCTN0900_VAL_DEF, "INDEX_X", "0", "X",),
	("PSGVAL_INDEX_Y", FMAXPSG_SCTN0900_VAL_DEF, "INDEX_Y", "1", "Y",),
	("PSGVAL_INTERVALLING_LIST", FMAXPSG_SCTN0903_LIST_DEF, "INTERVALLING_LIST", "list that holds all currently alarming events",),
	("PSGVAL_KEY", FMAX_NOP, "keys defined",),
	("PSGVAL_KEY_ALARMPOPUP_PROPER", FMAXPSG_SCTN0900_KEY_DEF, "ALARMPOPUP_PROPER", "key for the button return for the popup",),
	("PSGVAL_KEY_ALARMPOPUP_TEXT_TEXT", FMAXPSG_SCTN0900_KEY_DEF, "ALARMPOPUP_TEXT_TEXT", "key for the text on a popup",),
	("PSGVAL_KEY_ALPHA_HIGH", FMAXPSG_SCTN0900_KEY_DEF, "ALPHA_HIGH", "alphahigh key",),
	("PSGVAL_KEY_ALPHA_LOW", FMAXPSG_SCTN0900_KEY_DEF, "ALPHA_LOW", "alphalow key",),
	("PSGVAL_KEY_ALPHA_MODE", FMAXPSG_SCTN0900_KEY_DEF, "ALPHA_MODE", "alpha mode key",),
	("PSGVAL_KEY_APPMODE", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE", "app mode key",),
	("PSGVAL_KEY_APPMODE_ALARMPOPUP", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_ALARMPOPUP", "main mode (xpand from clocks to this)",),
	("PSGVAL_KEY_APPMODE_CLOCKS", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_CLOCKS", "mode clocks only",),
	("PSGVAL_KEY_APPMODE_EDIT", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_EDIT", "edit mode on top of main window",),
	("PSGVAL_KEY_APPMODE_MAIN", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_MAIN", "main mode (xpand from clocks to this)",),
	("PSGVAL_KEY_APPMODE_MOUSE_OVER", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_MOUSE_OVER", "mouseOver mode (xpand from clocks to this)",),
	("PSGVAL_KEY_APPMODE_NONE", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_NONE", "NONE mode",),
	("PSGVAL_KEY_APPMODE_THECLOCK", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_THECLOCK", "theClock mode (xpand from clocks to this)",),
	("PSGVAL_KEY_BBOX", FMAXPSG_SCTN0900_KEY_DEF, "BBOX", "BOUNDING BOX",),
	("PSGVAL_KEY_BTN_DISMISS", FMAXPSG_SCTN0900_KEY_DEF, "BTN_DISMISS", "key for all of the button xpand",),
	("PSGVAL_KEY_BTN_DOWN", FMAXPSG_SCTN0900_KEY_DEF, "BTN_DOWN", "key for all of the button xpand",),
	("PSGVAL_KEY_BTN_EDIT", FMAXPSG_SCTN0900_KEY_DEF, "BTN_EDIT", "key for all of the button xpand",),
	("PSGVAL_KEY_BTN_QUIT", FMAXPSG_SCTN0900_KEY_DEF, "BTN_QUIT", "key for all of the button xpand",),
	("PSGVAL_KEY_BTN_UP", FMAXPSG_SCTN0900_KEY_DEF, "BTN_UP", "key for all of the button xpand",),
	("PSGVAL_KEY_BTN_XPAND", FMAXPSG_SCTN0900_KEY_DEF, "BTN_XPAND", "key for all of the button xpand",),
	("PSGVAL_KEY_BTN_ZERO", FMAXPSG_SCTN0900_KEY_DEF, "BTN_ZERO", "key for all of the button xpand",),
	("PSGVAL_KEY_CHECKBOX_ALPHA_LOW", FMAXPSG_SCTN0900_KEY_DEF, "CHECKBOX_ALPHA_LOW", "is the clock transparent under mouse (ineffective if mouse is avoided)",),
	("PSGVAL_KEY_CHECKBOX_RUNAWAY", FMAXPSG_SCTN0900_KEY_DEF, "CHECKBOX_RUNAWAY", "key for avoiding the mouse bool",),
	("PSGVAL_KEY_CLOSE_BBOX", FMAXPSG_SCTN0900_KEY_DEF, "CLOSE_BBOX", "CLOSE BOUNDING BOX",),
	("PSGVAL_KEY_DISMISSED", FMAXPSG_SCTN0900_KEY_DEF, "DISMISSED", "alarm dismissed bool",),
	("PSGVAL_KEY_EVENTMODE", FMAXPSG_SCTN0900_KEY_DEF, "EVENTMODE", "what mode is this event",),
	("PSGVAL_KEY_EVENTMODE_ALARM", FMAXPSG_SCTN0900_KEY_DEF, "EVENTMODE_ALARM", "",),
	("PSGVAL_KEY_EVENTMODE_INTERVAL", FMAXPSG_SCTN0900_KEY_DEF, "EVENTMODE_INTERVAL", "",),
	("PSGVAL_KEY_EVENTMODE_NONE", FMAXPSG_SCTN0900_KEY_DEF, "EVENTMODE_NONE", "what mode is this event",),
	("PSGVAL_KEY_EVENT_ENTRIES", FMAXPSG_SCTN0900_KEY_DEF, "EVENT_ENTRIES", "",),
	("PSGVAL_KEY_FIRSTRUN", FMAXPSG_SCTN0900_KEY_DEF, "FIRSTRUN", "True if just started, false after init1()",),
	("PSGVAL_KEY_INDEX_OF_NEXT_EVENT", FMAXPSG_SCTN0900_KEY_DEF, "INDEX_OF_NEXT_EVENT", "",),
	("PSGVAL_KEY_INTERVAL_COUNT", FMAXPSG_SCTN0900_KEY_DEF, "INTERVAL_COUNT", "count of the number of times since last reset this interval has triggered an alert",),
	("PSGVAL_KEY_IS_ALERTING_NOW", FMAXPSG_SCTN0900_KEY_DEF, "IS_ALERTING_NOW", "is the event currently alerting",),
	("PSGVAL_KEY_MAINFRAME_LCN", FMAXPSG_SCTN0900_KEY_DEF, "MAINFRAME_LCN", "screen position of the mainframe",),
	("PSGVAL_KEY_MAINFRAME_SIZE", FMAXPSG_SCTN0900_KEY_DEF, "MAINFRAME_SIZE", "make life easier by remembering mainframe size, and why currently resizable is always False",),
	("PSGVAL_KEY_MOUSE_LCN", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_LCN", "track mouse location to ease load a bit",),
	("PSGVAL_KEY_MOUSE_STATUS_CLOSE_E", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_CLOSE_E", "mouse is east of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_CLOSE_N", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_CLOSE_N", "mouse is north of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_CLOSE_NE", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_CLOSE_NE", "mouse is northeast of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_CLOSE_NW", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_CLOSE_NW", "mouse is northwest of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_CLOSE_S", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_CLOSE_S", "mouse is south of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_CLOSE_SE", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_CLOSE_SE", "mouse is southeast of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_CLOSE_SW", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_CLOSE_SW", "mouse is southwest of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_CLOSE_W", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_CLOSE_W", "mouse is west of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_E", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_E", "mouse is east of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_N", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_N", "mouse is north of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_NE", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_NE", "mouse is northeast of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_NONE", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_NONE", "mouse is northeast of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_NW", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_NW", "mouse is northwest of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_OVER", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_OVER", "mouse is southwest of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_S", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_S", "mouse is south of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_SE", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_SE", "mouse is southeast of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_SW", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_SW", "mouse is southwest of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_W", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_W", "mouse is west of checked element",),
	("PSGVAL_KEY_NAME", FMAXPSG_SCTN0900_KEY_DEF, "NAME", "name of the event",),
	("PSGVAL_KEY_NAME_NEXT_EVENT", FMAXPSG_SCTN0900_KEY_DEF, "NAME_NEXT_EVENT", "name of the next event up",),
	("PSGVAL_KEY_POPUPTYPE", FMAXPSG_SCTN0900_KEY_DEF, "POPUPTYPE", "which type of popup are we defining",),
	("PSGVAL_KEY_POPUPTYPE_AUTO_CLOSE", FMAXPSG_SCTN0900_KEY_DEF, "POPUPTYPE_AUTO_CLOSE", "for intervals auto close",),
	("PSGVAL_KEY_PREDISMISSABLE", FMAXPSG_SCTN0900_KEY_DEF, "PREDISMISSABLE", "",),
	("PSGVAL_KEY_SCREEN_DIMS", FMAXPSG_SCTN0900_KEY_DEF, "SCREEN_DIMS", "dimension of the screen",),
	("PSGVAL_KEY_SNOOZABLE", FMAXPSG_SCTN0900_KEY_DEF, "SNOOZABLE", "can this event be snoozed",),
	("PSGVAL_KEY_SNOOZED", FMAXPSG_SCTN0900_KEY_DEF, "SNOOZED", "snoozed bool",),
	("PSGVAL_KEY_TIME_ALARM", FMAXPSG_SCTN0900_KEY_DEF, "TIME_ALARM", "the alarm time",),
	("PSGVAL_KEY_TIME_AT_LAST_RUN", FMAXPSG_SCTN0900_KEY_DEF, "TIME_AT_LAST_RUN", "timeS of last alarm ",),
	("PSGVAL_KEY_TIME_AT_NEXT", FMAXPSG_SCTN0900_KEY_DEF, "TIME_AT_NEXT", "what time is the next alarm, == KEY_TIME_ALARM is tomorrow",),
	("PSGVAL_KEY_TIME_AT_ZEROELAPSE", FMAXPSG_SCTN0900_KEY_DEF, "TIME_AT_ZEROELAPSE", "the time at last zero to keep elapsed time accurate despite other things hogging CPU time",),
	("PSGVAL_KEY_TIME_CLOCK", FMAXPSG_SCTN0900_KEY_DEF, "TIME_CLOCK", "the main clock time",),
	("PSGVAL_KEY_TIME_ELAPSED", FMAXPSG_SCTN0900_KEY_DEF, "TIME_ELAPSED", "key for all clocks elapsed",),
	("PSGVAL_KEY_TIME_INTERVAL", FMAXPSG_SCTN0900_KEY_DEF, "TIME_INTERVAL", "interval timer starting time, reset each time the interval goes off",),
	("PSGVAL_KEY_TIME_INTERVAL_START", FMAXPSG_SCTN0900_KEY_DEF, "TIME_INTERVAL_START", "interval timer starting time, reset each time the interval goes off",),
	("PSGVAL_KEY_TIME_INTERVAL__BEGIN", FMAXPSG_SCTN0900_KEY_DEF, "TIME_INTERVAL__BEGIN", "key for time interval starts alerting",),
	("PSGVAL_KEY_TIME_INTERVAL__END", FMAXPSG_SCTN0900_KEY_DEF, "TIME_INTERVAL__END", "key for time an interval goes to leep and stops alerting",),
	("PSGVAL_KEY_TIME_LEN_RING", FMAXPSG_SCTN0900_KEY_DEF, "TIME_LEN_RING", "length of ringing",),
	("PSGVAL_KEY_TIME_TOGO", FMAXPSG_SCTN0900_KEY_DEF, "TIME_TOGO", "down counter to next event on this window/alarm/interval/reminder",),
	("PSGVAL_KEY_TRANSPARENT", FMAXPSG_SCTN0900_KEY_DEF, "TRANSPARENT", "is the app transparent (only the buttons and text appears, all backgrounds are transparent, can click through transparent)",),
	("PSGVAL_NORMAL_BUTTON", FMAXPSG_SCTN0905_TUPDICT_DEF, "NORMAL_BUTTON", "define the button empty tupdict",),
	("PSGVAL_NORMAL_BUTTON_BUTTON_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_BUTTON", "BUTTON_COLOR", "None", "Color of button. default is from theme or the window. Easy to remember which is which if you say 'ON' between colors. 'red' on 'green'. Normally a tuple, but can be a simplified-button-color-string 'foreground on background'. Can be a single color if want to set only the background.",),
	("PSGVAL_NORMAL_BUTTON_BUTTON_TEXT", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "NORMAL_BUTTON", "BUTTON_TEXT", "", "str text to display on the button",),
	("PSGVAL_NORMAL_BUTTON_FOCUS", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_BUTTON", "FOCUS", "False", "if True, initial focus will be put on this button",),
	("PSGVAL_NORMAL_BUTTON_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_BUTTON", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_NORMAL_BUTTON_IMAGE_DATA", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_BUTTON", "IMAGE_DATA", "None", "Raw or Base64 representation of the image to put on button. Choose either filename or data",),
	("PSGVAL_NORMAL_BUTTON_IMAGE_FILENAME", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_BUTTON", "IMAGE_FILENAME", "None", "image filename if there is a button image. GIFs and PNGs only.",),
	("PSGVAL_NORMAL_BUTTON_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_BUTTON", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element",),
	("PSGVAL_NORMAL_CHECKBOX", FMAXPSG_SCTN0905_TUPDICT_DEF, "NORMAL_CHECKBOX", "set a checkbox in motion",),
	("PSGVAL_NORMAL_CHECKBOX_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_CHECKBOX", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_NORMAL_CHECKBOX_CHECKBOX_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_CHECKBOX", "CHECKBOX_COLOR", "None", "color of background of the box that has the check mark in it. The checkmark is the same color as the text",),
	("PSGVAL_NORMAL_CHECKBOX_DEFAULT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_CHECKBOX", "DEFAULT", "False", "Set to True if you want this checkbox initially checked",),
	("PSGVAL_NORMAL_CHECKBOX_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_CHECKBOX", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_NORMAL_CHECKBOX_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_CHECKBOX", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_NORMAL_CHECKBOX_TEXT", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "NORMAL_CHECKBOX", "TEXT", "", "Window to display next to checkbox",),
	("PSGVAL_NORMAL_CHECKBOX_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_CHECKBOX", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_NORMAL_COMBO", FMAXPSG_SCTN0905_TUPDICT_DEF, "NORMAL_COMBO", "a full combo tupdict",),
	("PSGVAL_NORMAL_COMBO_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_COMBO", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_NORMAL_COMBO_DEFAULT_VALUE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_COMBO", "DEFAULT_VALUE", "None", "Choice to be displayed as initial value. Must match one of values variable contents",),
	("PSGVAL_NORMAL_COMBO_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_COMBO", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_NORMAL_COMBO_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_COMBO", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_NORMAL_COMBO_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_COMBO", "SIZE", "None", "width, height. Width = characters-wide, height = NOTE it's the number of entries to show in the list",),
	("PSGVAL_NORMAL_COMBO_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_COMBO", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_NORMAL_COMBO_VALUES", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_COMBO", "VALUES", "[]", "values to choose. While displayed as text, the items returned are what the caller supplied, not text",),
	("PSGVAL_NORMAL_RADIO", FMAXPSG_SCTN0905_TUPDICT_DEF, "NORMAL_RADIO", "define a full radio button entity",),
	("PSGVAL_NORMAL_RADIO_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_RADIO", "BACKGROUND_COLOR", "None", "",),
	("PSGVAL_NORMAL_RADIO_CIRCLE_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_RADIO", "CIRCLE_COLOR", "None", "",),
	("PSGVAL_NORMAL_RADIO_DEFAULT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_RADIO", "DEFAULT", "False", "",),
	("PSGVAL_NORMAL_RADIO_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_RADIO", "FONT", "None", "",),
	("PSGVAL_NORMAL_RADIO_GROUP_ID", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "NORMAL_RADIO", "GROUP_ID", "", "Groups together multiple Radio Buttons. Any type works",),
	("PSGVAL_NORMAL_RADIO_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_RADIO", "KEY", "None", "",),
	("PSGVAL_NORMAL_RADIO_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_RADIO", "SIZE", "(None, None)", "",),
	("PSGVAL_NORMAL_RADIO_TEXT", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "NORMAL_RADIO", "TEXT", "", "",),
	("PSGVAL_NORMAL_RADIO_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_RADIO", "TEXT_COLOR", "None", "",),
	("PSGVAL_NORMAL_SPIN", FMAXPSG_SCTN0905_TUPDICT_DEF, "NORMAL_SPIN", "full spin dict",),
	("PSGVAL_NORMAL_SPIN_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_SPIN", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_NORMAL_SPIN_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_SPIN", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_NORMAL_SPIN_INITIAL_VALUE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_SPIN", "INITIAL_VALUE", "None", "Initial item to show in window. Choose from list of values supplied",),
	("PSGVAL_NORMAL_SPIN_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_SPIN", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element",),
	("PSGVAL_NORMAL_SPIN_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_SPIN", "SIZE", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_NORMAL_SPIN_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_SPIN", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_NORMAL_SPIN_VALUES", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_SPIN", "VALUES", "[]", "List of valid values",),
	("PSGVAL_NORMAL_TEXT", FMAXPSG_SCTN0905_TUPDICT_DEF, "NORMAL_TEXT", "the full monty for text elements",),
	("PSGVAL_NORMAL_TEXT_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_TEXT", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_NORMAL_TEXT_BORDER_WIDTH", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_TEXT", "BORDER_WIDTH", "None", "number of pixels for the border (if using a relief)",),
	("PSGVAL_NORMAL_TEXT_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_TEXT", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_NORMAL_TEXT_GRAB", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_TEXT", "GRAB", "None", "If True can grab this element and move the window around. Default is False",),
	("PSGVAL_NORMAL_TEXT_JUSTIFICATION", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_TEXT", "JUSTIFICATION", "None", "how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center`",),
	("PSGVAL_NORMAL_TEXT_KEY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_TEXT", "KEY", "None", "Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element",),
	("PSGVAL_NORMAL_TEXT_RELIEF", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_TEXT", "RELIEF", "None", "relief style around the text. Values are same as progress meter relief values. Should be a constant that is defined at starting with 'RELIEF_' - `RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID`",),
	("PSGVAL_NORMAL_TEXT_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_TEXT", "SIZE", "(None, None)", "(width, height) width = characters-wide, height = rows-high",),
	("PSGVAL_NORMAL_TEXT_TEXT", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "NORMAL_TEXT", "TEXT", "", "The text to display. Can include /n to achieve multiple lines.  Will convert (optional) parameter into a string",),
	("PSGVAL_NORMAL_TEXT_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_TEXT", "TEXT_COLOR", "None", "color of the text",),
	("PSGVAL_NORMAL_WINDOW", FMAXPSG_SCTN0905_TUPDICT_DEF, "NORMAL_WINDOW", "define the NORMAL_WINDOW tupdict",),
	("PSGVAL_NORMAL_WINDOW_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "BACKGROUND_COLOR", "None", "color of background",),
	("PSGVAL_NORMAL_WINDOW_FINALIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "FINALIZE", "False", "If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code",),
	("PSGVAL_NORMAL_WINDOW_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_NORMAL_WINDOW_GRAB_ANYWHERE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "GRAB_ANYWHERE", "False", "If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems",),
	("PSGVAL_NORMAL_WINDOW_ICON", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "ICON", "None", "Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO",),
	("PSGVAL_NORMAL_WINDOW_KEEP_ON_TOP", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "KEEP_ON_TOP", "False", "If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm",),
	("PSGVAL_NORMAL_WINDOW_LAYOUT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "LAYOUT", "None", "The layout for the window. Can also be specified in the Layout method",),
	("PSGVAL_NORMAL_WINDOW_LOCATION", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "LOCATION", "(None, None)", "(x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen.",),
	("PSGVAL_NORMAL_WINDOW_MODAL", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "MODAL", "False", "If True then this window will be the only window a user can interact with until it is closed",),
	("PSGVAL_NORMAL_WINDOW_NO_TITLEBAR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "NO_TITLEBAR", "False", "If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar",),
	("PSGVAL_NORMAL_WINDOW_TITLE", FMAXPSG_SCTN0905_TUPDICT_VS_ADD, "NORMAL_WINDOW", "TITLE", "", "The title that will be displayed in the Titlebar and on the Taskbar",),
	("PSGVAL_NORMAL_WINDOW_TITLEBAR_BACKGROUND_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "TITLEBAR_BACKGROUND_COLOR", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as background color",),
	("PSGVAL_NORMAL_WINDOW_TITLEBAR_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "TITLEBAR_FONT", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as title font",),
	("PSGVAL_NORMAL_WINDOW_TITLEBAR_ICON", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "TITLEBAR_ICON", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as the icon (file or base64 bytes)",),
	("PSGVAL_NORMAL_WINDOW_TITLEBAR_TEXT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "TITLEBAR_TEXT_COLOR", "None", "If custom titlebar indicated by use_custom_titlebar, then use this as text color",),
	("PSGVAL_NORMAL_WINDOW_TRANSPARENT_COLOR", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "NORMAL_WINDOW", "TRANSPARENT_COLOR", "None", "Any portion of the window that has this color will be completely transparent. You can even click through these spots to the window under this window.",),
	("PSGVAL_POPUP_INTERVAL", FMAX_NOP, "FMAXPSG_SCTN0915_PUDLG_DEF", "POPUP_INTERVAL", "POPUPTYPE_AUTO_CLOSE", "the dialog when an interval goes off",),
	("PSGVAL_POPUP_INTERVAL01", FMAX_NOP, "FMAXPSG_SCTN0915_PUDLG_DICT_STR_ADD", "POPUP_INTERVAL", "TITLE", "", "title of the alert window",),
	("PSGVAL_POPUP_INTERVAL01", FMAX_NOP, "FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD", "POPUP_INTERVAL", "AUTO_CLOSE", "True", "interval timers get auto dismiss by default",),
	("PSGVAL_POPUP_INTERVAL01", FMAX_NOP, "FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD", "POPUP_INTERVAL", "AUTO_CLOSE_DURATION", "5", "5 seconds before auto closing an interval alert",),
	("PSGVAL_POPUP_INTERVAL01", FMAX_NOP, "FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD", "POPUP_INTERVAL", "FONT", "FONTSZ_ALERT_TEXT", "no title bar on our popup",),
	("PSGVAL_POPUP_INTERVAL01", FMAX_NOP, "FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD", "POPUP_INTERVAL", "GRAB_ANYWHERE", "True", "grab anywhere on our popup",),
	("PSGVAL_POPUP_INTERVAL01", FMAX_NOP, "FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD", "POPUP_INTERVAL", "KEEP_ON_TOP", "True", "keep our popup on top",),
	("PSGVAL_POPUP_INTERVAL01", FMAX_NOP, "FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD", "POPUP_INTERVAL", "MODAL", "True", "grab anywhere on our popup",),
	("PSGVAL_POPUP_INTERVAL01", FMAX_NOP, "FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD", "POPUP_INTERVAL", "NON_BLOCKING", "True", "carry on with everything else",),
	("PSGVAL_POPUP_INTERVAL01", FMAX_NOP, "FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD", "POPUP_INTERVAL", "NO_TITLEBAR", "True", "no title bar on our popup",),
	("PSGVAL_POPUP_INTERVAL01", FMAX_NOP, "FMAXPSG_SCTN0915_PUDLG_LIST_STR_ADD", "POPUP_INTERVAL", "INTERVAL %title_% has expired %count_% times", "line of text",),
	("PSGVAL_POPUP_INTERVAL01", FMAX_NOP, "FMAXPSG_SCTN0915_PUDLG_LIST_STR_ADD", "POPUP_INTERVAL", "click OK to dismiss or wait %self.POPUP_INTERVAL_DICT[auto_close_duration]% seconds or so", "line of text",),
	("PSGVAL_SZ_ALERT_TEXT", FMAXPSG_SCTN0900_VAL_DEF, "SZ_ALERT_TEXT", "20", "high alpha",),
	("PSGVAL_SZ_ALPHA_HIGH", FMAXPSG_SCTN0900_VAL_DEF, "SZ_ALPHA_HIGH", "1.0", "high alpha",),
	("PSGVAL_SZ_ALPHA_LOW", FMAXPSG_SCTN0900_VAL_DEF, "SZ_ALPHA_LOW", "0.1", "low alpha setting",),
	("PSGVAL_SZ_BORDER_DEPTH", FMAXPSG_SCTN0900_VAL_DEF, "SZ_BORDER_DEPTH", "0", "border depth",),
	("PSGVAL_SZ_BTNS", FMAXPSG_SCTN0900_VAL_DEF, "SZ_BTNS", "6", "size for button text",),
	("PSGVAL_SZ_CLOCKS_MOVE", FMAXPSG_SCTN0900_VAL_DEF, "SZ_CLOCKS_MOVE", "15", "how far to move each time the mouse approaches",),
	("PSGVAL_SZ_CLOCKS_TIME_CLOCK", FMAXPSG_SCTN0900_VAL_DEF, "SZ_CLOCKS_TIME_CLOCK", "26", "size of the main clock on the clocks only floating widget",),
	("PSGVAL_SZ_CLOCKS_TIME_ELAPSED", FMAXPSG_SCTN0900_VAL_DEF, "SZ_CLOCKS_TIME_ELAPSED", "13", "size of the elapsed clock on the clocks only floating widget",),
	("PSGVAL_SZ_CLOCKS_TIME_TOGO", FMAXPSG_SCTN0900_VAL_DEF, "SZ_CLOCKS_TIME_TOGO", "13", "size of the main togo clock on the clocks only floating widget",),
	("PSGVAL_SZ_CLOSE", FMAXPSG_SCTN0900_VAL_DEF, "SZ_CLOSE", "80", "close enough to move from the mouse",),
	("PSGVAL_SZ_EDIT_TIME_CLOCK", FMAXPSG_SCTN0900_VAL_DEF, "SZ_EDIT_TIME_CLOCK", "20", "size of the main clock on the clocks only floating widget",),
	("PSGVAL_SZ_EDIT_TIME_ELAPSED", FMAXPSG_SCTN0900_VAL_DEF, "SZ_EDIT_TIME_ELAPSED", "10", "size of the elapsed clock on the clocks only floating widget",),
	("PSGVAL_SZ_EDIT_TIME_TOGO", FMAXPSG_SCTN0900_VAL_DEF, "SZ_EDIT_TIME_TOGO", "10", "size of the main togo clock on the clocks only floating widget",),
	("PSGVAL_SZ_INTERVAL_COUNT", FMAXPSG_SCTN0900_VAL_DEF, "SZ_INTERVAL_COUNT", "10", "size of the main togo clock on the clocks only floating widget",),
	("PSGVAL_SZ_MAIN_TIME_CLOCK", FMAXPSG_SCTN0900_VAL_DEF, "SZ_MAIN_TIME_CLOCK", "60", "size of the main clock on the clocks only floating widget",),
	("PSGVAL_SZ_MAIN_TIME_ELAPSED", FMAXPSG_SCTN0900_VAL_DEF, "SZ_MAIN_TIME_ELAPSED", "30", "size of the elapsed clock on the clocks only floating widget",),
	("PSGVAL_SZ_MAIN_TIME_TOGO", FMAXPSG_SCTN0900_VAL_DEF, "SZ_MAIN_TIME_TOGO", "30", "size of the main togo clock on the clocks only floating widget",),
	("PSGVAL_SZ_MARGINS_ALL", FMAXPSG_SCTN0900_VAL_DEF, "SZ_MARGINS_ALL", "(0, 0)", "all margins default",),
	("PSGVAL_SZ_MAX_DELTA", FMAXPSG_SCTN0900_VAL_DEF, "SZ_MAX_DELTA", "100", "comment",),
	("PSGVAL_SZ_MOVE_DIST", FMAXPSG_SCTN0900_VAL_DEF, "SZ_MOVE_DIST", "50", "comment",),
	("PSGVAL_SZ_PAD_ALL", FMAXPSG_SCTN0900_VAL_DEF, "SZ_PAD_ALL", "((1, 1), (1, 1))", "add padding to all the things",),
	("PSGVAL_SZ_TIMEMS_BETWEEN_MOUSE_CHECKS", FMAXPSG_SCTN0900_VAL_DEF, "SZ_TIMEMS_BETWEEN_MOUSE_CHECKS", "300", "throttle mouse checking",),
	("PSGVAL_SZ_TIMEMS_BETWEEN_MOVES", FMAXPSG_SCTN0900_VAL_DEF, "SZ_TIMEMS_BETWEEN_MOVES", "500", "comment",),
	("PSGVAL_SZ_TIMEMS_BETWEEN_UPDATES", FMAXPSG_SCTN0900_VAL_DEF, "SZ_TIMEMS_BETWEEN_UPDATES", "500", "comment",),
	("PSGVAL_SZ_TIMEOUT_MS", FMAXPSG_SCTN0900_VAL_DEF, "SZ_TIMEOUT_MS", "100", "timeout for PSG",),
	("PSGVAL_SZ_TIMES_BETWEEN_PERIODIC_JOB", FMAXPSG_SCTN0901_VAL_DEF, "SZ_TIMES_BTWN_PERIODIC_JOB", "900", "time between periodic job runnings",),
	("PSGVAL_TIMEH_ADJUST_HRS", FMAXPSG_SCTN0900_VAL_DEF, "TIMEH_ADJUST_HRS", "0", "comment",),
	("PSGVAL_TIMEM_ADJUST_MINS", FMAXPSG_SCTN0900_VAL_DEF, "TIMEM_ADJUST_MINS", "0", "comment",),
	("PSGVAL_TIMES_LIST", FMAXPSG_SCTN0903_LIST_DEF, "TIMES_LIST", "list of all keys to times for midnight etc. processing",),
	("PSGVAL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "TIMES_LIST", "TIME_AT_LAST_RUN", "time at last run entry in TIMES_LIST",),
	("PSGVAL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "TIMES_LIST", "TIME_AT_NEXT", "time at next event entry in TIMES_LIST",),
	("PSGVAL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "TIMES_LIST", "TIME_AT_ZEROELAPSE", "time the elapsed timer was reset in TIMES_LIST",),
	("PSGVAL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "TIMES_LIST", "TIME_ALARM", "alarm time entry in TIMES_LIST",),
	("PSGVAL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "TIMES_LIST", "TIME_CLOCK", "alarm time entry in TIMES_LIST",),
	("PSGVAL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "TIMES_LIST", "TIME_ELAPSED", "alarm time entry in TIMES_LIST",),
	("PSGVAL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "TIMES_LIST", "TIME_TOGO", "alarm time entry in TIMES_LIST",),
	("PSGVAL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "TIMES_LIST", "TIME_INTERVAL__BEGIN", "alarm time entry in TIMES_LIST",),
	("PSGVAL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "TIMES_LIST", "TIME_INTERVAL__END", "alarm time entry in TIMES_LIST",),
	("PSGVAL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "TIMES_LIST", "TIME_INTERVAL_START", "alarm time entry in TIMES_LIST",),
	("PSGVAL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "TIMES_LIST", "TIME_INTERVAL", "alarm time entry in TIMES_LIST",),
	("PSGVAL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "TIMES_LIST", "TIME_LEN_RING", "alarm time entry in TIMES_LIST",),
	("PSGVAL_TITLE", FMAX_NOP, "titles start here",),
	("PSGVAL_TITLE_ALARMPOPUP", FMAXPSG_SCTN0900_STR_DEF, "TITLE_ALARMPOPUP", "ALERT", "string with window title for APPMODE_CLOCKS",),
	("PSGVAL_TITLE_CLOCKS", FMAXPSG_SCTN0900_STR_DEF, "TITLE_CLOCKS", "CLOCKS", "string with window title for APPMODE_CLOCKS",),
	("PSGVAL_TITLE_EDIT", FMAXPSG_SCTN0900_STR_DEF, "TITLE_EDIT", "edit an event", "string with window title for APPMODE_CLOCKS",),
	("PSGVAL_TITLE_MAIN", FMAXPSG_SCTN0900_STR_DEF, "TITLE_MAIN", "Main window which is xpanded from CLOCKS window and pops up EDIT windows", "string with window title for APPMODE_CLOCKS",),
	("PSGVAL_TITLE_THECLOCK", FMAXPSG_SCTN0900_STR_DEF, "TITLE_THECLOCK", "THECLOCK", "string with window title for APPMODE_CLOCKS",),
	("PSGVAL_UPDATE_COMBO", FMAXPSG_SCTN0905_TUPDICT_DEF, "UPDATE_COMBO", "holds the update combo entity",),
	("PSGVAL_UPDATE_COMBO_DISABLED", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "UPDATE_COMBO", "DISABLED", "None", "set disable state for element",),
	("PSGVAL_UPDATE_COMBO_FONT", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "UPDATE_COMBO", "FONT", "None", "specifies the font family, size, etc",),
	("PSGVAL_UPDATE_COMBO_READONLY", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "UPDATE_COMBO", "READONLY", "None", "make element readonly (user can't change). True means user cannot change",),
	("PSGVAL_UPDATE_COMBO_SET_TO_INDEX", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "UPDATE_COMBO", "SET_TO_INDEX", "None", "",),
	("PSGVAL_UPDATE_COMBO_SIZE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "UPDATE_COMBO", "SIZE", "None", "width, height. Width = characters-wide, height = NOTE it's the number of entries to show in the list",),
	("PSGVAL_UPDATE_COMBO_VALUE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "UPDATE_COMBO", "VALUE", "None", "change which value is current selected based on new list of previous list of choices",),
	("PSGVAL_UPDATE_COMBO_VALUES", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "UPDATE_COMBO", "VALUES", "None", "values to choose. While displayed as text, the items returned are what the caller supplied, not text",),
	("PSGVAL_UPDATE_COMBO_VISIBLE", FMAXPSG_SCTN0905_TUPDICT_VV_ADD, "UPDATE_COMBO", "VISIBLE", "None", "set visibility state of the element",),
	("PSGVAL_ZERO_CLOCK", FMAXPSG_SCTN0900_VAL_DEF, "ZERO_CLOCK", "0", "all the zeros",),
	("PSGVAL__BTN_DISMISS20", FMAX_NOP, "start of the dismiss button for alarms",),
	("PSGVAL__BTN_DISMISS2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_DISMISS20", "",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_DISMISS20", "BUTTON_TEXT", "", "button_text empty for the DOWN button",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_DISMISS20", "IMAGE_FILENAME", "res/dismiss20.png", "filename for the button icon",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DISMISS20", "BORDER_WIDTH", "0", "button xpand key",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DISMISS20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DISMISS20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DISMISS20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DISMISS20", "KEY", "BTN_DISMISS", "button xpand key",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DISMISS20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_DOWN20", FMAX_NOP, "clocks down20 button",),
	("PSGVAL__BTN_DOWN2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_DOWN20", "",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_DOWN20", "BUTTON_TEXT", "", "button_text empty for the DOWN button",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_DOWN20", "IMAGE_FILENAME", "res/down20.png", "filename for the button icon",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN20", "BORDER_WIDTH", "0", "button xpand key",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN20", "KEY", "BTN_DOWN", "button xpand key",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_DOWN32", FMAX_NOP, "clocks down32 button",),
	("PSGVAL__BTN_DOWN3200", FMAXPSG_SCTN0906_BTN_DEF, "BTN_DOWN32", "",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_DOWN32", "BUTTON_TEXT", "", "button_text empty for the DOWN button",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_DOWN32", "IMAGE_FILENAME", "res/down32.png", "filename for the button icon",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN32", "BORDER_WIDTH", "0", "button xpand key",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN32", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN32", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN32", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN32", "KEY", "BTN_DOWN", "button xpand key",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN32", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_EDIT20", FMAX_NOP, "clocks edit20 button",),
	("PSGVAL__BTN_EDIT2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_EDIT20", "",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_EDIT20", "BUTTON_TEXT", "", "button_text empty for the EDIT button",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_EDIT20", "IMAGE_FILENAME", "res/edit20.png", "filename for the button icon",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT20", "KEY", "BTN_EDIT", "button xpand key",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_EDIT32", FMAX_NOP, "clocks edit32 button",),
	("PSGVAL__BTN_EDIT3200", FMAXPSG_SCTN0906_BTN_DEF, "BTN_EDIT32", "",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_EDIT32", "BUTTON_TEXT", "", "button_text empty for the EDIT button",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_EDIT32", "IMAGE_FILENAME", "res/edit32.png", "filename for the button icon",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT32", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT32", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT32", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT32", "KEY", "BTN_EDIT", "button xpand key",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT32", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_QUIT20", FMAX_NOP, "clocks quit20 button",),
	("PSGVAL__BTN_QUIT2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_QUIT20", "",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_QUIT20", "BUTTON_TEXT", "", "button_text empty for the QUIT button",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_QUIT20", "IMAGE_FILENAME", "res/quit20.png", "filename for the button icon",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_QUIT20", "TOOLTIP", "quit the app", "button_text empty for the QUIT button",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT20", "KEY", "BTN_QUIT", "button quit key",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_QUIT32", FMAX_NOP, "clocks quit32 button",),
	("PSGVAL__BTN_QUIT3200", FMAXPSG_SCTN0906_BTN_DEF, "BTN_QUIT32", "",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_QUIT32", "BUTTON_TEXT", "", "button_text empty for the QUIT button",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_QUIT32", "IMAGE_FILENAME", "res/quit32.png", "filename for the button icon",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_QUIT32", "TOOLTIP", "quit the app", "button_text empty for the QUIT button",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT32", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT32", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT32", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT32", "KEY", "BTN_QUIT", "button quit key",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT32", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_UP20", FMAX_NOP, "clocks up20 button",),
	("PSGVAL__BTN_UP2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_UP20", "",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_UP20", "BUTTON_TEXT", "", "button_text empty for the UP button",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_UP20", "IMAGE_FILENAME", "res/up20.png", "filename for the button icon",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP20", "KEY", "BTN_UP", "button xpand key",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_UP32", FMAX_NOP, "clocks up32 button",),
	("PSGVAL__BTN_UP3200", FMAXPSG_SCTN0906_BTN_DEF, "BTN_UP32", "",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_UP32", "BUTTON_TEXT", "", "button_text empty for the UP button",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_UP32", "IMAGE_FILENAME", "res/up32.png", "filename for the button icon",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP32", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP32", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP32", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP32", "KEY", "BTN_UP", "button xpand key",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP32", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_XPAND20", FMAX_NOP, "clocks xpand20 button",),
	("PSGVAL__BTN_XPAND2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_XPAND20", "",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_XPAND20", "BUTTON_TEXT", "", "button_text empty for the XPAND button",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_XPAND20", "IMAGE_FILENAME", "res/xpand20.png", "filename for the button icon",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_XPAND20", "TOOLTIP", "expand to the big window from where you can edit events", "tooltip",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND20", "KEY", "BTN_XPAND", "button xpand key",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_XPAND32", FMAX_NOP, "clocks xpand32 button",),
	("PSGVAL__BTN_XPAND3200", FMAXPSG_SCTN0906_BTN_DEF, "BTN_XPAND32", "",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_XPAND32", "BUTTON_TEXT", "", "button_text empty for the XPAND button",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_XPAND32", "IMAGE_FILENAME", "res/xpand32.png", "filename for the button icon",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_XPAND32", "TOOLTIP", "expand to the big window from where you can edit events", "tooltip",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND32", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND32", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND32", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND32", "KEY", "BTN_XPAND", "button xpand key",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND32", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_ZERO20", FMAX_NOP, "clocks zero20 button",),
	("PSGVAL__BTN_ZERO2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_ZERO20", "",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_ZERO20", "BUTTON_TEXT", "", "button_text empty for the ZERO button",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_ZERO20", "IMAGE_FILENAME", "res/zero20.png", "filename for the button icon",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_ZERO20", "TOOLTIP", "zero the elapsed timer", "tooltip",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO20", "KEY", "BTN_ZERO", "button zero key",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_ZERO32", FMAX_NOP, "clocks zero32 button",),
	("PSGVAL__BTN_ZERO3200", FMAXPSG_SCTN0906_BTN_DEF, "BTN_ZERO32", "",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_ZERO32", "BUTTON_TEXT", "", "button_text empty for the ZERO button",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_ZERO32", "IMAGE_FILENAME", "res/zero32.png", "filename for the button icon",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_ZERO32", "TOOLTIP", "zero the elapsed timer", "tooltip",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO32", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO32", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO32", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO32", "KEY", "BTN_ZERO", "button zero key",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO32", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__CHECKBOX_ALPHA_LOW01", FMAX_NOP, "alpha=0 under mouse",),
	("PSGVAL__CHECKBOX_ALPHA_LOW0100", FMAXPSG_SCTN0908_CHECKBOX_DEF, "CHECKBOX_ALPHA_LOW01", "checkbox for alpha under mouse",),
	("PSGVAL__CHECKBOX_ALPHA_LOW0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_ALPHA_LOW01", "TEXT", "ALPHA_LOW", "simple text reminder",),
	("PSGVAL__CHECKBOX_ALPHA_LOW0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_ALPHA_LOW01", "TOOLTIP", "low alpha under mouse", "comment",),
	("PSGVAL__CHECKBOX_ALPHA_LOW0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_ALPHA_LOW01", "DEFAULT", "True", "leave it on by default",),
	("PSGVAL__CHECKBOX_ALPHA_LOW0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_ALPHA_LOW01", "KEY", "CHECKBOX_ALPHA_LOW", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_RUNAWAY01", FMAX_NOP, "run away or not checkbox",),
	("PSGVAL__CHECKBOX_RUNAWAY0100", FMAXPSG_SCTN0908_CHECKBOX_DEF, "CHECKBOX_RUNAWAY01", "checkbox for runaway from mouse behavior",),
	("PSGVAL__CHECKBOX_RUNAWAY0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_RUNAWAY01", "TEXT", "RNAWY", "text label",),
	("PSGVAL__CHECKBOX_RUNAWAY0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_RUNAWAY01", "TOOLTIP", "run away from mouse when checked", "tooltip",),
	("PSGVAL__CHECKBOX_RUNAWAY0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_RUNAWAY01", "DEFAULT", "False", "leave it on by default",),
	("PSGVAL__CHECKBOX_RUNAWAY0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_RUNAWAY01", "KEY", "CHECKBOX_RUNAWAY", "set the key for the checkbox",),
	("PSGVAL__CLOCKS_COLUMN01", FMAX_NOP, "the column for APPMODE_CLOCKS",),
	("PSGVAL__CLOCKS_COLUMN0100", FMAXPSG_SCTN090B_COLUMN_DEF, "CLOCKS_COLUMN01", "the column that puts the two smaller clocks below the main one",),
	("PSGVAL__CLOCKS_COLUMN0101", FMAXPSG_SCTN090B_COLUMN_ROW_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_00", "L01", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0102", FMAXPSG_SCTN090B_COLUMN_TEXT_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_00", "L02", "CLOCKS_COLUMN01_E01", "add a new TEXT element to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0103", FMAXPSG_SCTN090B_COLUMN_PARM_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_00", "L03", "CLOCKS_COLUMN01_E01", "**CLOCKS_TEXT_TIME_CLOCK", "add the main clock",),
	("PSGVAL__CLOCKS_COLUMN0104", FMAXPSG_SCTN090B_COLUMN_ROW_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_01", "L01", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0105", FMAXPSG_SCTN090B_COLUMN_TEXT_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_01", "L02", "CLOCKS_COLUMN01_E02", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0106", FMAXPSG_SCTN090B_COLUMN_PARM_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_01", "L03", "CLOCKS_COLUMN01_E02", "**CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "add time to go",),
	("PSGVAL__CLOCKS_COLUMN0107", FMAXPSG_SCTN090B_COLUMN_TEXT_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_01", "L02", "CLOCKS_COLUMN01_E03", "add a new text element to row01 clocks column",),
	("PSGVAL__CLOCKS_COLUMN0108", FMAXPSG_SCTN090B_COLUMN_PARM_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_01", "L03", "CLOCKS_COLUMN01_E03", "**CLOCKS_TEXT_TIME_ELAPSED", "add elapsed time",),
	("PSGVAL__CLOCKS_COLUMN0109", FMAXPSG_SCTN090B_COLUMN_ROW_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_02", "L01", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN010A", FMAXPSG_SCTN090B_COLUMN_TEXT_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_02", "L02", "CLOCKS_COLUMN01_E04", "add a new text element to row01 clocks column",),
	("PSGVAL__CLOCKS_COLUMN010B", FMAXPSG_SCTN090B_COLUMN_PARM_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_02", "L03", "CLOCKS_COLUMN01_E04", "**CLOCKS_TEXT_TIME_TOGO", "add elapsed time",),
	("PSGVAL__CLOCKS_COLUMN010C", FMAXPSG_SCTN090B_COLUMN_TEXT_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_02", "L02", "CLOCKS_COLUMN01_E05", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN010D", FMAXPSG_SCTN090B_COLUMN_PARM_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_02", "L03", "CLOCKS_COLUMN01_E05", "**CLOCKS_TEXT_TIME_AT_NEXT", "add time to go",),
	("PSGVAL__CLOCKS_COLUMN010E", FMAXPSG_SCTN090B_COLUMN_ROW_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_03", "L01", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN010F", FMAXPSG_SCTN090B_COLUMN_TEXT_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_03", "L02", "CLOCKS_COLUMN01_E08", "add a new text element to row01 clocks column",),
	("PSGVAL__CLOCKS_COLUMN0110", FMAXPSG_SCTN090B_COLUMN_PARM_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_03", "L03", "CLOCKS_COLUMN01_E08", "**CLOCKS_TEXT_NAME_NEXT_EVENT", "add the main clock",),
	("PSGVAL__CLOCKS_COLUMN0111", FMAXPSG_SCTN090B_COLUMN_ROW_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_04", "L01", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0112", FMAXPSG_SCTN090B_COLUMN_CHECKBOX_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_04", "L02", "CLOCKS_COLUMN01_E06", "add a new text element to row01 clocks column",),
	("PSGVAL__CLOCKS_COLUMN0113", FMAXPSG_SCTN090B_COLUMN_PARM_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_04", "L03", "CLOCKS_COLUMN01_E06", "**CHECKBOX_RUNAWAY01", "add elapsed time",),
	("PSGVAL__CLOCKS_COLUMN0114", FMAXPSG_SCTN090B_COLUMN_CHECKBOX_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_04", "L02", "CLOCKS_COLUMN01_E07", "add a new text element to row01 clocks column",),
	("PSGVAL__CLOCKS_COLUMN0115", FMAXPSG_SCTN090B_COLUMN_PARM_ADD, "CLOCKS_COLUMN01", "CLOCKS_COLUMN01_ROW_04", "L03", "CLOCKS_COLUMN01_E07", "**CHECKBOX_ALPHA_LOW01", "add elapsed time",),
	("PSGVAL__CLOCKS_COLUMN02", FMAX_NOP, "the column for APPMODE_CLOCKS",),
	("PSGVAL__CLOCKS_COLUMN0200", FMAXPSG_SCTN090B_COLUMN_DEF, "CLOCKS_COLUMN02", "the column that puts the two smaller clocks below the main one",),
	("PSGVAL__CLOCKS_COLUMN0201", FMAXPSG_SCTN090B_COLUMN_ROW_ADD, "CLOCKS_COLUMN02", "CLOCKS_COLUMN02_ROW_01", "L01", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0202", FMAXPSG_SCTN090B_COLUMN_BUTTON_ADD, "CLOCKS_COLUMN02", "CLOCKS_COLUMN02_ROW_01", "L02", "CLOCKS_COLUMN02_E01", "add a button element to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0203", FMAXPSG_SCTN090B_COLUMN_PARM_ADD, "CLOCKS_COLUMN02", "CLOCKS_COLUMN02_ROW_01", "L03", "CLOCKS_COLUMN02_E01", "**BTN_QUIT20", "add the xpand button to clocks",),
	("PSGVAL__CLOCKS_COLUMN0204", FMAXPSG_SCTN090B_COLUMN_ROW_ADD, "CLOCKS_COLUMN02", "CLOCKS_COLUMN02_ROW_02", "L01", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0205", FMAXPSG_SCTN090B_COLUMN_BUTTON_ADD, "CLOCKS_COLUMN02", "CLOCKS_COLUMN02_ROW_02", "L02", "CLOCKS_COLUMN02_E02", "add reset button for elapsed time",),
	("PSGVAL__CLOCKS_COLUMN0206", FMAXPSG_SCTN090B_COLUMN_PARM_ADD, "CLOCKS_COLUMN02", "CLOCKS_COLUMN02_ROW_02", "L03", "CLOCKS_COLUMN02_E02", "**BTN_ZERO20", "add the zero button to clocks",),
	("PSGVAL__CLOCKS_COLUMN0207", FMAXPSG_SCTN090B_COLUMN_ROW_ADD, "CLOCKS_COLUMN02", "CLOCKS_COLUMN02_ROW_03", "L01", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0208", FMAXPSG_SCTN090B_COLUMN_BUTTON_ADD, "CLOCKS_COLUMN02", "CLOCKS_COLUMN02_ROW_03", "L02", "CLOCKS_COLUMN02_E03", "add reset button for elapsed time",),
	("PSGVAL__CLOCKS_COLUMN0209", FMAXPSG_SCTN090B_COLUMN_PARM_ADD, "CLOCKS_COLUMN02", "CLOCKS_COLUMN02_ROW_03", "L03", "CLOCKS_COLUMN02_E03", "**BTN_XPAND20", "add the zero button to clocks",),
	("PSGVAL__CLOCKS_COLUMN020A", FMAXPSG_SCTN090B_COLUMN_ROW_ADD, "CLOCKS_COLUMN02", "CLOCKS_COLUMN02_ROW_04", "L01", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN020B", FMAXPSG_SCTN090B_COLUMN_TEXT_ADD, "CLOCKS_COLUMN02", "CLOCKS_COLUMN02_ROW_04", "L02", "CLOCKS_COLUMN02_E04", "add reset button for elapsed time",),
	("PSGVAL__CLOCKS_COLUMN020C", FMAXPSG_SCTN090B_COLUMN_PARM_ADD, "CLOCKS_COLUMN02", "CLOCKS_COLUMN02_ROW_04", "L03", "CLOCKS_COLUMN02_E04", "**CLOCKS_TEXT_INTERVAL_COUNT", "add the zero button to clocks",),
	("PSGVAL__CLOCKS_DICT", FMAX_NOP, "dict with the root source for clocks values, updated both directions as appropriate",),
	("PSGVAL__CLOCKS_DICT00", FMAXPSG_SCTN0902_DICT_DEF, "CLOCKS_DICT", "holds the values for the clocks frame",),
	("PSGVAL__CLOCKS_DICT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "CLOCKS_DICT", "TIME_AT_NEXT", "ZERO_CLOCK", "holds the values for the clocks frame",),
	("PSGVAL__CLOCKS_DICT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "CLOCKS_DICT", "TIME_AT_ZEROELAPSE", "ZERO_CLOCK", "holds the values for the clocks frame",),
	("PSGVAL__CLOCKS_DICT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "CLOCKS_DICT", "TIME_CLOCK", "ZERO_CLOCK", "holds the values for the clocks frame",),
	("PSGVAL__CLOCKS_DICT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "CLOCKS_DICT", "TIME_ELAPSED", "ZERO_CLOCK", "holds the values for the clocks frame",),
	("PSGVAL__CLOCKS_DICT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "CLOCKS_DICT", "TIME_TOGO", "ZERO_CLOCK", "holds the values for the clocks frame",),
	("PSGVAL__CLOCKS_LAYOUT", FMAX_NOP, "layout for APPMODE_CLOCKS",),
	("PSGVAL__CLOCKS_LAYOUT00", FMAXPSG_SCTN090E_LAYOUT_DEF, "CLOCKS_LAYOUT", "layout for APPMODE_CLOCKS",),
	("PSGVAL__CLOCKS_LAYOUT01", FMAXPSG_SCTN090E_LAYOUT_ROW_ADD, "CLOCKS_LAYOUT", "CLOCKS_LAYOUT_ROW_00", "L01", "add a row to the layout",),
	("PSGVAL__CLOCKS_LAYOUT02", FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD, "CLOCKS_LAYOUT", "CLOCKS_LAYOUT_ROW_00", "L02", "CLOCKS_LAYOUT_E01", "add a column",),
	("PSGVAL__CLOCKS_LAYOUT03", FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD, "CLOCKS_LAYOUT", "CLOCKS_LAYOUT_ROW_00", "L03", "CLOCKS_LAYOUT_E01", "layout", "CLOCKS_COLUMN01", "comment",),
	("PSGVAL__CLOCKS_LAYOUT04", FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD, "CLOCKS_LAYOUT", "CLOCKS_LAYOUT_ROW_00", "L03", "CLOCKS_LAYOUT_E01", "pad", "SZ_PAD_ALL", "comment",),
	("PSGVAL__CLOCKS_LAYOUT05", FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD, "CLOCKS_LAYOUT", "CLOCKS_LAYOUT_ROW_00", "L02", "CLOCKS_LAYOUT_E02", "add a column",),
	("PSGVAL__CLOCKS_LAYOUT06", FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD, "CLOCKS_LAYOUT", "CLOCKS_LAYOUT_ROW_00", "L03", "CLOCKS_LAYOUT_E02", "layout", "CLOCKS_COLUMN02", "comment",),
	("PSGVAL__CLOCKS_LAYOUT07", FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD, "CLOCKS_LAYOUT", "CLOCKS_LAYOUT_ROW_00", "L03", "CLOCKS_LAYOUT_E02", "pad", "SZ_PAD_ALL", "comment",),
	("PSGVAL__CLOCKS_MAINFRAME", FMAX_NOP, "the frame for clocks",),
	("PSGVAL__CLOCKS_MAINFRAME00", FMAXPSG_SCTN090D_MAINFRAME_DEF, "CLOCKS", "CLOCKS_WINDOW", "True", "the clocks frame defined and done",),
	("PSGVAL__CLOCKS_TEXT_DICT", FMAX_NOP, "dict with the root source for clocks values, updated both directions as appropriate",),
	("PSGVAL__CLOCKS_TEXT_DICT00", FMAXPSG_SCTN0902_DICT_DEF, "CLOCKS_TEXT_DICT", "holds the values for the text elements",),
	("PSGVAL__CLOCKS_TEXT_DICT01", FMAXPSG_SCTN0902_DICT_VS_ADD, "CLOCKS_TEXT_DICT", "NAME_NEXT_EVENT", "", "name of next event",),
	("PSGVAL__CLOCKS_TEXT_DICT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "CLOCKS_TEXT_DICT", "INTERVAL_COUNT", "0", "interval count",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT", FMAX_NOP, "CLOCKS text interval count",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT00", FMAXPSG_SCTN0909_TEXT_DEF, "CLOCKS_TEXT_INTERVAL_COUNT", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_STR_ADD, "CLOCKS_TEXT_INTERVAL_COUNT", "TEXT", "0000", "the text to fill in",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_INTERVAL_COUNT", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_INTERVAL_COUNT", "ENABLE_EVENTS", "False", "this is clickable",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_INTERVAL_COUNT", "FONT", "FONTSZ_CLOCKS_INTERVAL_COUNT", "font+size line",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_INTERVAL_COUNT", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_INTERVAL_COUNT", "KEY", "INTERVAL_COUNT", "comment",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_INTERVAL_COUNT", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_INTERVAL_COUNT", "SIZE", "(4, 1)", "characters, lines size line",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_INTERVAL_COUNT", "TEXT_COLOR", "COLOR_TIME_TOGO", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT", FMAX_NOP, "CLOCKS text TIME_AT_NEXT",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT00", FMAXPSG_SCTN0909_TEXT_DEF, "CLOCKS_TEXT_NAME_NEXT_EVENT", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_STR_ADD, "CLOCKS_TEXT_NAME_NEXT_EVENT", "TEXT", "", "the text to fill in",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_NAME_NEXT_EVENT", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_NAME_NEXT_EVENT", "ENABLE_EVENTS", "False", "this is clickable",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_NAME_NEXT_EVENT", "FONT", "FONTSZ_CLOCKS_TIME_TOGO", "font+size line",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_NAME_NEXT_EVENT", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_NAME_NEXT_EVENT", "KEY", "NAME_NEXT_EVENT", "comment",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_NAME_NEXT_EVENT", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_NAME_NEXT_EVENT", "SIZE", "(16, 1)", "characters, lines size line",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_NAME_NEXT_EVENT", "TEXT_COLOR", "COLOR_TIME_TOGO", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT", FMAX_NOP, "CLOCKS text NAME_NEXT_EVENT_STR",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT00", FMAXPSG_SCTN0909_TEXT_DEF, "CLOCKS_TEXT_TIME_AT_NEXT", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_NEXT", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_NEXT", "ENABLE_EVENTS", "False", "this is clickable",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_NEXT", "FONT", "FONTSZ_CLOCKS_TIME_TOGO", "font+size line",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_NEXT", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_NEXT", "KEY", "TIME_AT_NEXT", "comment",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_NEXT", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_NEXT", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_NEXT", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_NEXT", "TEXT_COLOR", "COLOR_TIME_TOGO", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZEROELAPSE", FMAX_NOP, "CLOCKS text TIME_AT_ZEROELAPSE",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZEROELAPSE00", FMAXPSG_SCTN0909_TEXT_DEF, "CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "ENABLE_EVENTS", "False", "this is clickable",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "FONT", "FONTSZ_CLOCKS_TIME_ELAPSED", "font+size line",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "KEY", "TIME_AT_ZEROELAPSE", "comment",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "TEXT_COLOR", "COLOR_TIME_ELAPSED", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK", FMAX_NOP, "CLOCKS text TIME_CLOCK",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK00", FMAXPSG_SCTN0909_TEXT_DEF, "CLOCKS_TEXT_TIME_CLOCK", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_CLOCK", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_CLOCK", "ENABLE_EVENTS", "True", "this is clickable",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_CLOCK", "FONT", "FONTSZ_CLOCKS_TIME_CLOCK", "font+size line",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_CLOCK", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_CLOCK", "KEY", "TIME_CLOCK", "comment",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_CLOCK", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_CLOCK", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_CLOCK", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_CLOCK", "TEXT_COLOR", "COLOR_TIME_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED", FMAX_NOP, "CLOCKS text TIME_ELAPSED",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED00", FMAXPSG_SCTN0909_TEXT_DEF, "CLOCKS_TEXT_TIME_ELAPSED", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_ELAPSED", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_ELAPSED", "FONT", "FONTSZ_CLOCKS_TIME_ELAPSED", "font+size line",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_ELAPSED", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_ELAPSED", "KEY", "TIME_ELAPSED", "comment",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_ELAPSED", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_ELAPSED", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_ELAPSED", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_ELAPSED", "TEXT_COLOR", "COLOR_TIME_ELAPSED", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO", FMAX_NOP, "CLOCKS text TIME_TOGO",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO00", FMAXPSG_SCTN0909_TEXT_DEF, "CLOCKS_TEXT_TIME_TOGO", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_TOGO", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_TOGO", "FONT", "FONTSZ_CLOCKS_TIME_TOGO", "font+size line",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_TOGO", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_TOGO", "KEY", "TIME_TOGO", "comment",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_TOGO", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_TOGO", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_TOGO", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "CLOCKS_TEXT_TIME_TOGO", "TEXT_COLOR", "COLOR_TIME_TOGO", "the text color for a clock_time element",),
	("PSGVAL__CLOCKS_WINDOW", FMAX_NOP, "the window for APPMODE_CLOCKS",),
	("PSGVAL__CLOCKS_WINDOW00", FMAXPSG_SCTN090F_WINDOW_DEF, "CLOCKS_WINDOW", "define the clocks window",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "CLOCKS_WINDOW", "ALPHA_CHANNEL", "SZ_ALPHA_HIGH", "set the high alpha as the default",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "CLOCKS_WINDOW", "BACKGROUND_COLOR", "COLOR_BACKGROUND", "eliminate all not useful on the floating clocks",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "CLOCKS_WINDOW", "BORDER_DEPTH", "SZ_BORDER_DEPTH", "border depth to zero",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "CLOCKS_WINDOW", "ELEMENT_PADDING", "SZ_PAD_ALL", "all padding for elements ((1, 1), (1, 1)) by default",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "CLOCKS_WINDOW", "FORCE_TOPLEVEL", "None", "",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "CLOCKS_WINDOW", "GRAB_ANYWHERE", "True", "eliminate all not useful on the floating clocks",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "CLOCKS_WINDOW", "KEEP_ON_TOP", "True", "eliminate all not useful on the floating clocks",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "CLOCKS_WINDOW", "LAYOUT", "CLOCKS_LAYOUT", "add the layout for CLOCKS_WINDOW",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "CLOCKS_WINDOW", "MARGINS", "SZ_MARGINS_ALL", "",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "CLOCKS_WINDOW", "NO_TITLEBAR", "True", "no titlebar on APPMODE_CLOCKS window",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "CLOCKS_WINDOW", "TITLE", "TITLE_CLOCKS", "",),
	("PSGVAL__COLORS", FMAX_NOP, "colors defines",),
	("PSGVAL__COLORS_BTN_NORMAL", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_BTN_NORMAL", "(COLOR_TEXT_NORMAL, COLOR_BACKGROUND)", "comment",),
	("PSGVAL__COLORS_TEXT_HIGH", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_TEXT_HIGH", "(COLOR_TEXT_HIGH, COLOR_BACKGROUND)", "combined colors for a clock text element",),
	("PSGVAL__COLORS_TEXT_LOW", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_TEXT_LOW", "(COLOR_TEXT_LOW, COLOR_BACKGROUND)", "combined colors for a clock text element",),
	("PSGVAL__COLORS_TEXT_NORMAL", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_TEXT_NORMAL", "(COLOR_TEXT_NORMAL, COLOR_BACKGROUND)", "combined colors for a clock text element",),
	("PSGVAL__COLORS_TIME_CLOCK", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_TIME_CLOCK", "(COLOR_TIME_CLOCK, COLOR_CLOCK_BACKGROUND)", "combined colors for a clock text element",),
	("PSGVAL__COLORS_TIME_ELAPSED", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_TIME_ELAPSED", "(COLOR_TIME_ELAPSED, COLOR_CLOCK_BACKGROUND)", "combined colors for a clock text element",),
	("PSGVAL__COLORS_TIME_TOGO", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_TIME_TOGO", "(COLOR_TIME_TOGO, COLOR_CLOCK_BACKGROUND)", "combined colors for a clock text element",),
	("PSGVAL__C_CLOCKS_BTN_DISMISS20", FMAX_NOP, "start of the dismiss button for alarms",),
	("PSGVAL__C_CLOCKS_BTN_DISMISS2000", FMAXPSG_SCTN0916_CLASS_BTN_DEF, "C_CLOCKS", "C_BTN_DISMISS20", "",),
	("PSGVAL__C_CLOCKS_BTN_DISMISS2001", FMAXPSG_SCTN0916_CLASS_BTN_STR_ADD, "C_CLOCKS", "C_BTN_DISMISS20", "BUTTON_TEXT", "", "button_text empty for the DOWN button",),
	("PSGVAL__C_CLOCKS_BTN_DISMISS2001", FMAXPSG_SCTN0916_CLASS_BTN_STR_ADD, "C_CLOCKS", "C_BTN_DISMISS20", "IMAGE_FILENAME", "res/dismiss20.png", "filename for the button icon",),
	("PSGVAL__C_CLOCKS_BTN_DISMISS2001", FMAXPSG_SCTN0916_CLASS_BTN_VAL_ADD, "C_CLOCKS", "C_BTN_DISMISS20", "BORDER_WIDTH", "0", "button xpand key",),
	("PSGVAL__C_CLOCKS_BTN_DISMISS2001", FMAXPSG_SCTN0916_CLASS_BTN_VAL_ADD, "C_CLOCKS", "C_BTN_DISMISS20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__C_CLOCKS_BTN_DISMISS2001", FMAXPSG_SCTN0916_CLASS_BTN_VAL_ADD, "C_CLOCKS", "C_BTN_DISMISS20", "FOCUS", "True", "focus on click",),
	("PSGVAL__C_CLOCKS_BTN_DISMISS2001", FMAXPSG_SCTN0916_CLASS_BTN_VAL_ADD, "C_CLOCKS", "C_BTN_DISMISS20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__C_CLOCKS_BTN_DISMISS2001", FMAXPSG_SCTN0916_CLASS_BTN_VAL_ADD, "C_CLOCKS", "C_BTN_DISMISS20", "KEY", "BTN_DISMISS%KEY%", "button xpand key",),
	("PSGVAL__C_CLOCKS_BTN_DISMISS2001", FMAXPSG_SCTN0916_CLASS_BTN_VAL_ADD, "C_CLOCKS", "C_BTN_DISMISS20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__C_CLOCKS", FMAXPSG_SCTN0916_CLASS_DEF, "C_CLOCKS", "comment",),
	("PSGVAL__C_CLOCKS_COLUMN01", FMAX_NOP, "the column for APPMODE_CLOCKS",),
	("PSGVAL__C_CLOCKS_COLUMN0100", FMAXPSG_SCTN0916_CLASS_COLUMN_DEF, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_the column that puts the two smaller clocks below the main one",),
	("PSGVAL__C_CLOCKS_COLUMN0101", FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_00", "L01", "add a new row to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0102", FMAXPSG_SCTN0916_CLASS_COLUMN_TEXT_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_00", "L02", "C_CLOCKS_COLUMN01_E01", "add a new TEXT element to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0103", FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_00", "L03", "C_CLOCKS_COLUMN01_E01", "**CLOCKS_TEXT_TIME_CLOCK", "add the main clock",),
	("PSGVAL__C_CLOCKS_COLUMN0104", FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_01", "L01", "add a new row to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0105", FMAXPSG_SCTN0916_CLASS_COLUMN_TEXT_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_01", "L02", "C_CLOCKS_COLUMN01_E02", "add a new row to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0106", FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_01", "L03", "C_CLOCKS_COLUMN01_E02", "**self.C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "add time to go",),
	("PSGVAL__C_CLOCKS_COLUMN0107", FMAXPSG_SCTN0916_CLASS_COLUMN_TEXT_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_01", "L02", "C_CLOCKS_COLUMN01_E03", "add a new text element to row01 clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0108", FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_01", "L03", "C_CLOCKS_COLUMN01_E03", "**self.C_CLOCKS_TEXT_TIME_ELAPSED", "add elapsed time",),
	("PSGVAL__C_CLOCKS_COLUMN0109", FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_02", "L01", "add a new row to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN010A", FMAXPSG_SCTN0916_CLASS_COLUMN_TEXT_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_02", "L02", "C_CLOCKS_COLUMN01_E04", "add a new text element to row01 clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN010B", FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_02", "L03", "C_CLOCKS_COLUMN01_E04", "**self.C_CLOCKS_TEXT_TIME_TOGO", "add elapsed time",),
	("PSGVAL__C_CLOCKS_COLUMN010C", FMAXPSG_SCTN0916_CLASS_COLUMN_TEXT_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_02", "L02", "C_CLOCKS_COLUMN01_E05", "add a new row to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN010D", FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_02", "L03", "C_CLOCKS_COLUMN01_E05", "**self.C_CLOCKS_TEXT_TIME_AT_NEXT", "add time to go",),
	("PSGVAL__C_CLOCKS_COLUMN010E", FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_03", "L01", "add a new row to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN010F", FMAXPSG_SCTN0916_CLASS_COLUMN_TEXT_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_03", "L02", "C_CLOCKS_COLUMN01_E08", "add a new text element to row01 clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0110", FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_03", "L03", "C_CLOCKS_COLUMN01_E08", "**self.C_CLOCKS_TEXT_NAME_NEXT_EVENT", "add the main clock",),
	("PSGVAL__C_CLOCKS_COLUMN0111", FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_04", "L01", "add a new row to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0112", FMAXPSG_SCTN0916_CLASS_COLUMN_CHECKBOX_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_04", "L02", "C_CLOCKS_COLUMN01_E06", "add a new text element to row01 clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0113", FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_04", "L03", "C_CLOCKS_COLUMN01_E06", "**self.C_CHECKBOX_RUNAWAY01", "add elapsed time",),
	("PSGVAL__C_CLOCKS_COLUMN0114", FMAXPSG_SCTN0916_CLASS_COLUMN_CHECKBOX_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_04", "L02", "C_CLOCKS_COLUMN01_E07", "add a new text element to row01 clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0115", FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN01", "C_CLOCKS_COLUMN01_ROW_04", "L03", "C_CLOCKS_COLUMN01_E07", "**CHECKBOX_ALPHA_LOW01", "add elapsed time",),
	("PSGVAL__C_CLOCKS_COLUMN02", FMAX_NOP, "the column for APPMODE_CLOCKS",),
	("PSGVAL__C_CLOCKS_COLUMN0200", FMAXPSG_SCTN0916_CLASS_COLUMN_DEF, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_the column that puts the two smaller clocks below the main one",),
	("PSGVAL__C_CLOCKS_COLUMN0201", FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_CLOCKS_COLUMN02_ROW_01", "L01", "add a new row to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0202", FMAXPSG_SCTN0916_CLASS_COLUMN_BUTTON_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_CLOCKS_COLUMN02_ROW_01", "L02", "C_CLOCKS_COLUMN02_E01", "add a button element to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0203", FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_CLOCKS_COLUMN02_ROW_01", "L03", "C_CLOCKS_COLUMN02_E01", "**BTN_QUIT20", "add the xpand button to clocks",),
	("PSGVAL__C_CLOCKS_COLUMN0204", FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_CLOCKS_COLUMN02_ROW_02", "L01", "add a new row to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0205", FMAXPSG_SCTN0916_CLASS_COLUMN_BUTTON_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_CLOCKS_COLUMN02_ROW_02", "L02", "C_CLOCKS_COLUMN02_E02", "add reset button for elapsed time",),
	("PSGVAL__C_CLOCKS_COLUMN0206", FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_CLOCKS_COLUMN02_ROW_02", "L03", "C_CLOCKS_COLUMN02_E02", "**BTN_ZERO20", "add the zero button to clocks",),
	("PSGVAL__C_CLOCKS_COLUMN0207", FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_CLOCKS_COLUMN02_ROW_03", "L01", "add a new row to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN0208", FMAXPSG_SCTN0916_CLASS_COLUMN_BUTTON_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_CLOCKS_COLUMN02_ROW_03", "L02", "C_CLOCKS_COLUMN02_E03", "add reset button for elapsed time",),
	("PSGVAL__C_CLOCKS_COLUMN0209", FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_CLOCKS_COLUMN02_ROW_03", "L03", "C_CLOCKS_COLUMN02_E03", "**BTN_XPAND20", "add the zero button to clocks",),
	("PSGVAL__C_CLOCKS_COLUMN020A", FMAXPSG_SCTN0916_CLASS_COLUMN_ROW_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_CLOCKS_COLUMN02_ROW_04", "L01", "add a new row to clocks column",),
	("PSGVAL__C_CLOCKS_COLUMN020B", FMAXPSG_SCTN0916_CLASS_COLUMN_TEXT_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_CLOCKS_COLUMN02_ROW_04", "L02", "C_CLOCKS_COLUMN02_E04", "add reset button for elapsed time",),
	("PSGVAL__C_CLOCKS_COLUMN020C", FMAXPSG_SCTN0916_CLASS_COLUMN_PARM_ADD, "C_CLOCKS", "C_CLOCKS_COLUMN02", "C_CLOCKS_COLUMN02_ROW_04", "L03", "C_CLOCKS_COLUMN02_E04", "**self.C_CLOCKS_TEXT_INTERVAL_COUNT", "add the zero button to clocks",),
	("PSGVAL__C_CLOCKS_LAYOUT", FMAX_NOP, "layout for APPMODE_CLOCKS",),
	("PSGVAL__C_CLOCKS_LAYOUT00", FMAXPSG_SCTN0916_CLASS_LAYOUT_DEF, "C_CLOCKS", "C_CLOCKS_LAYOUT", "C_layout for APPMODE_CLOCKS",),
	("PSGVAL__C_CLOCKS_LAYOUT01", FMAXPSG_SCTN0916_CLASS_LAYOUT_ROW_ADD, "C_CLOCKS", "C_CLOCKS_LAYOUT", "C_CLOCKS_LAYOUT_ROW_00", "L01", "add a row to the layout",),
	("PSGVAL__C_CLOCKS_LAYOUT02", FMAXPSG_SCTN0916_CLASS_LAYOUT_COLUMN_ADD, "C_CLOCKS", "C_CLOCKS_LAYOUT", "C_CLOCKS_LAYOUT_ROW_00", "L02", "CLOCKS_LAYOUT_E01", "add a column",),
	("PSGVAL__C_CLOCKS_LAYOUT03", FMAXPSG_SCTN0916_CLASS_LAYOUT_PARM_VAL_ADD, "C_CLOCKS", "C_CLOCKS_LAYOUT", "C_CLOCKS_LAYOUT_ROW_00", "L03", "CLOCKS_LAYOUT_E01", "layout", "C_CLOCKS_COLUMN01", "comment",),
	("PSGVAL__C_CLOCKS_LAYOUT04", FMAXPSG_SCTN0916_CLASS_LAYOUT_PARM_VAL_ADD, "C_CLOCKS", "C_CLOCKS_LAYOUT", "C_CLOCKS_LAYOUT_ROW_00", "L03", "CLOCKS_LAYOUT_E01", "pad", "SZ_PAD_ALL", "comment",),
	("PSGVAL__C_CLOCKS_LAYOUT05", FMAXPSG_SCTN0916_CLASS_LAYOUT_COLUMN_ADD, "C_CLOCKS", "C_CLOCKS_LAYOUT", "C_CLOCKS_LAYOUT_ROW_00", "L02", "CLOCKS_LAYOUT_E02", "add a column",),
	("PSGVAL__C_CLOCKS_LAYOUT06", FMAXPSG_SCTN0916_CLASS_LAYOUT_PARM_VAL_ADD, "C_CLOCKS", "C_CLOCKS_LAYOUT", "C_CLOCKS_LAYOUT_ROW_00", "L03", "CLOCKS_LAYOUT_E02", "layout", "C_CLOCKS_COLUMN02", "comment",),
	("PSGVAL__C_CLOCKS_LAYOUT07", FMAXPSG_SCTN0916_CLASS_LAYOUT_PARM_VAL_ADD, "C_CLOCKS", "C_CLOCKS_LAYOUT", "C_CLOCKS_LAYOUT_ROW_00", "L03", "CLOCKS_LAYOUT_E02", "pad", "SZ_PAD_ALL", "comment",),
	("PSGVAL__C_CLOCKS_MAINFRAME", FMAX_NOP, "the frame for clocks",),
	("PSGVAL__C_CLOCKS_MAINFRAME00", FMAXPSG_SCTN0916_CLASS_MAINFRAME_DEF, "C_CLOCKS", "C_CLOCKS_WINDOW", "True", "the clocks frame defined and done",),
	("PSGVAL__C_CLOCKS_SPIN01_00", FMAXPSG_SCTN0916_CLASS_SPIN_DEF, "C_CLOCKS", "C_CLOCKS_SPIN01", "define the alarm en/dis/able spinbox",),
	("PSGVAL__C_CLOCKS_SPIN01_01", FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VV_ADD, "C_CLOCKS", "C_CLOCKS_SPIN01", "VALUES", "%LIST%", "comment",),
	("PSGVAL__C_CLOCKS_SPIN01_01", FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VV_ADD, "C_CLOCKS", "C_CLOCKS_SPIN01", "BACKGROUND_COLOR", "COLOR_ALERT_BACKGROUND", "comment",),
	("PSGVAL__C_CLOCKS_SPIN01_01", FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VV_ADD, "C_CLOCKS", "C_CLOCKS_SPIN01", "FONT", "FONTSZ_ALERT_TEXT", "comment",),
	("PSGVAL__C_CLOCKS_SPIN01_01", FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VV_ADD, "C_CLOCKS", "C_CLOCKS_SPIN01", "SIZE", "(16, 1)", "comment",),
	("PSGVAL__C_CLOCKS_SPIN01_01", FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VV_ADD, "C_CLOCKS", "C_CLOCKS_SPIN01", "TEXT", "SPIN_TEXT", "comment",),
	("PSGVAL__C_CLOCKS_SPIN01_01", FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VV_ADD, "C_CLOCKS", "C_CLOCKS_SPIN01", "TEXT_COLOR", "COLOR_ALERT_TEXT", "comment",),
	("PSGVAL__C_CLOCKS_SPIN01_02", FMAXPSG_SCTN0916_CLASS_SPIN_LIST_VAL_ADD, "C_CLOCKS", "C_CLOCKS_SPIN01", "0", "index 0",),
	("PSGVAL__C_CLOCKS_SPIN01_02", FMAXPSG_SCTN0916_CLASS_SPIN_LIST_VAL_ADD, "C_CLOCKS", "C_CLOCKS_SPIN01", "1", "index 1",),
	("PSGVAL__C_CLOCKS_SPIN01_02", FMAXPSG_SCTN0916_CLASS_SPIN_LIST_VAL_ADD, "C_CLOCKS", "C_CLOCKS_SPIN01", "2", "index 2",),
	("PSGVAL__C_CLOCKS_TEXT_DICT", FMAX_NOP, "dict with the root source for clocks values, updated both directions as appropriate",),
	("PSGVAL__C_CLOCKS_TEXT_DICT00", FMAXPSG_SCTN0916_CLASS_DICT_DEF, "C_CLOCKS", "C_CLOCKS_TEXT_DICT", "C_holds the values for the text elements",),
	("PSGVAL__C_CLOCKS_TEXT_DICT01", FMAXPSG_SCTN0916_CLASS_DICT_VS_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_DICT", "C_NAME_NEXT_EVENT", "", "name of next event",),
	("PSGVAL__C_CLOCKS_TEXT_DICT01", FMAXPSG_SCTN0916_CLASS_DICT_VV_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_DICT", "C_INTERVAL_COUNT", "0", "interval count",),
	("PSGVAL__C_CLOCKS_TEXT_INTERVAL_COUNT", FMAX_NOP, "CLOCKS text interval count",),
	("PSGVAL__C_CLOCKS_TEXT_INTERVAL_COUNT00", FMAXPSG_SCTN0916_CLASS_TEXT_DEF, "C_CLOCKS", "C_CLOCKS_TEXT_INTERVAL_COUNT", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__C_CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0916_CLASS_TEXT_STR_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_INTERVAL_COUNT", "TEXT", "0000", "the text to fill in",),
	("PSGVAL__C_CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_INTERVAL_COUNT", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__C_CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_INTERVAL_COUNT", "ENABLE_EVENTS", "False", "this is clickable",),
	("PSGVAL__C_CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_INTERVAL_COUNT", "FONT", "FONTSZ_CLOCKS_INTERVAL_COUNT", "font+size line",),
	("PSGVAL__C_CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_INTERVAL_COUNT", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__C_CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_INTERVAL_COUNT", "KEY", "INTERVAL_COUNT%KEY%", "comment",),
	("PSGVAL__C_CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_INTERVAL_COUNT", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_INTERVAL_COUNT", "SIZE", "(4, 1)", "characters, lines size line",),
	("PSGVAL__C_CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_INTERVAL_COUNT", "TEXT_COLOR", "COLOR_TIME_TOGO", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_NAME_NEXT_EVENT", FMAX_NOP, "CLOCKS text TIME_AT_NEXT",),
	("PSGVAL__C_CLOCKS_TEXT_NAME_NEXT_EVENT00", FMAXPSG_SCTN0916_CLASS_TEXT_DEF, "C_CLOCKS", "C_CLOCKS_TEXT_NAME_NEXT_EVENT", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__C_CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0916_CLASS_TEXT_STR_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_NAME_NEXT_EVENT", "TEXT", "", "the text to fill in",),
	("PSGVAL__C_CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_NAME_NEXT_EVENT", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__C_CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_NAME_NEXT_EVENT", "ENABLE_EVENTS", "False", "this is clickable",),
	("PSGVAL__C_CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_NAME_NEXT_EVENT", "FONT", "FONTSZ_CLOCKS_TIME_TOGO", "font+size line",),
	("PSGVAL__C_CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_NAME_NEXT_EVENT", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__C_CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_NAME_NEXT_EVENT", "KEY", "NAME_NEXT_EVENT%KEY%", "comment",),
	("PSGVAL__C_CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_NAME_NEXT_EVENT", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_NAME_NEXT_EVENT", "SIZE", "(16, 1)", "characters, lines size line",),
	("PSGVAL__C_CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_NAME_NEXT_EVENT", "TEXT_COLOR", "COLOR_TIME_TOGO", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_NEXT", FMAX_NOP, "CLOCKS text NAME_NEXT_EVENT_STR",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_NEXT00", FMAXPSG_SCTN0916_CLASS_TEXT_DEF, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_NEXT", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_NEXT", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_NEXT", "ENABLE_EVENTS", "False", "this is clickable",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_NEXT", "FONT", "FONTSZ_CLOCKS_TIME_TOGO", "font+size line",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_NEXT", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_NEXT", "KEY", "TIME_AT_NEXT%KEY%", "comment",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_NEXT", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_NEXT", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_NEXT", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_NEXT01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_NEXT", "TEXT_COLOR", "COLOR_TIME_TOGO", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE", FMAX_NOP, "CLOCKS text TIME_AT_ZEROELAPSE",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE00", FMAXPSG_SCTN0916_CLASS_TEXT_DEF, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "ENABLE_EVENTS", "False", "this is clickable",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "FONT", "FONTSZ_CLOCKS_TIME_ELAPSED", "font+size line",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "KEY", "TIME_AT_ZEROELAPSE%KEY%", "comment",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_AT_ZEROELAPSE", "TEXT_COLOR", "COLOR_TIME_ELAPSED", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_CLOCK", FMAX_NOP, "CLOCKS text TIME_CLOCK",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_CLOCK00", FMAXPSG_SCTN0916_CLASS_TEXT_DEF, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_CLOCK", "C_define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_CLOCK", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_CLOCK", "ENABLE_EVENTS", "True", "this is clickable",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_CLOCK", "FONT", "FONTSZ_CLOCKS_TIME_CLOCK", "font+size line",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_CLOCK", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_CLOCK", "KEY", "TIME_CLOCK%KEY%", "comment",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_CLOCK", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_CLOCK", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_CLOCK", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_CLOCK", "TEXT_COLOR", "COLOR_TIME_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_ELAPSED", FMAX_NOP, "CLOCKS text TIME_ELAPSED",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_ELAPSED00", FMAXPSG_SCTN0916_CLASS_TEXT_DEF, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_ELAPSED", "C_define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_ELAPSED", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_ELAPSED", "FONT", "FONTSZ_CLOCKS_TIME_ELAPSED", "font+size line",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_ELAPSED", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_ELAPSED", "KEY", "TIME_ELAPSED%KEY%", "comment",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_ELAPSED", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_ELAPSED", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_ELAPSED", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_ELAPSED", "TEXT_COLOR", "COLOR_TIME_ELAPSED", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_TOGO", FMAX_NOP, "CLOCKS text TIME_TOGO",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_TOGO00", FMAXPSG_SCTN0916_CLASS_TEXT_DEF, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_TOGO", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_TOGO", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_TOGO", "FONT", "FONTSZ_CLOCKS_TIME_TOGO", "font+size line",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_TOGO", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_TOGO", "KEY", "TIME_TOGO%KEY%", "comment",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_TOGO", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_TOGO", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_TOGO", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD, "C_CLOCKS", "C_CLOCKS_TEXT_TIME_TOGO", "TEXT_COLOR", "COLOR_TIME_TOGO", "the text color for a clock_time element",),
	("PSGVAL__C_CLOCKS_WINDOW", FMAX_NOP, "the window for APPMODE_CLOCKS",),
	("PSGVAL__C_CLOCKS_WINDOW00", FMAXPSG_SCTN0916_CLASS_WINDOW_DEF, "C_CLOCKS", "C_CLOCKS_WINDOW", "define the clocks window",),
	("PSGVAL__C_CLOCKS_WINDOW01", FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD, "C_CLOCKS", "C_CLOCKS_WINDOW", "ALPHA_CHANNEL", "SZ_ALPHA_HIGH", "set the high alpha as the default",),
	("PSGVAL__C_CLOCKS_WINDOW01", FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD, "C_CLOCKS", "C_CLOCKS_WINDOW", "BACKGROUND_COLOR", "COLOR_BACKGROUND", "eliminate all not useful on the floating clocks",),
	("PSGVAL__C_CLOCKS_WINDOW01", FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD, "C_CLOCKS", "C_CLOCKS_WINDOW", "BORDER_DEPTH", "SZ_BORDER_DEPTH", "border depth to zero",),
	("PSGVAL__C_CLOCKS_WINDOW01", FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD, "C_CLOCKS", "C_CLOCKS_WINDOW", "ELEMENT_PADDING", "SZ_PAD_ALL", "all padding for elements ((1, 1), (1, 1)) by default",),
	("PSGVAL__C_CLOCKS_WINDOW01", FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD, "C_CLOCKS", "C_CLOCKS_WINDOW", "FORCE_TOPLEVEL", "None", "",),
	("PSGVAL__C_CLOCKS_WINDOW01", FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD, "C_CLOCKS", "C_CLOCKS_WINDOW", "GRAB_ANYWHERE", "True", "eliminate all not useful on the floating clocks",),
	("PSGVAL__C_CLOCKS_WINDOW01", FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD, "C_CLOCKS", "C_CLOCKS_WINDOW", "KEEP_ON_TOP", "True", "eliminate all not useful on the floating clocks",),
	("PSGVAL__C_CLOCKS_WINDOW01", FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD, "C_CLOCKS", "C_CLOCKS_WINDOW", "LAYOUT", "self.C_CLOCKS_LAYOUT", "add the layout for CLOCKS_WINDOW",),
	("PSGVAL__C_CLOCKS_WINDOW01", FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD, "C_CLOCKS", "C_CLOCKS_WINDOW", "MARGINS", "SZ_MARGINS_ALL", "",),
	("PSGVAL__C_CLOCKS_WINDOW01", FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD, "C_CLOCKS", "C_CLOCKS_WINDOW", "NO_TITLEBAR", "True", "no titlebar on APPMODE_CLOCKS window",),
	("PSGVAL__C_CLOCKS_WINDOW01", FMAXPSG_SCTN0916_CLASS_WINDOW_VAL_ADD, "C_CLOCKS", "C_CLOCKS_WINDOW", "TITLE", "TITLE_C_CLOCKS", "",),
	("PSGVAL__C_CLOCKS_TIMES_LIST", FMAXPSG_SCTN0916_CLASS_LIST_DEF, "C_CLOCKS", "TIMES_LIST", "list of all keys to times for midnight etc. processing",),
	("PSGVAL__C_CLOCKS_TIMES_LIST01", FMAXPSG_SCTN0916_CLASS_LIST_VAL_ADD, "C_CLOCKS", "TIMES_LIST", "TIME_ALARM%KEY%", "alarm time entry in TIMES_LIST",),
	("PSGVAL__C_CLOCKS_TIMES_LIST01", FMAXPSG_SCTN0916_CLASS_LIST_VAL_ADD, "C_CLOCKS", "TIMES_LIST", "TIME_AT_LAST_RUN%KEY%", "alarm time entry in TIMES_LIST",),
	("PSGVAL__C_CLOCKS_TIMES_LIST01", FMAXPSG_SCTN0916_CLASS_LIST_VAL_ADD, "C_CLOCKS", "TIMES_LIST", "TIME_AT_NEXT%KEY%", "alarm time entry in TIMES_LIST",),
	("PSGVAL__C_CLOCKS_TIMES_LIST01", FMAXPSG_SCTN0916_CLASS_LIST_VAL_ADD, "C_CLOCKS", "TIMES_LIST", "TIME_INTERVAL%KEY%", "alarm time entry in TIMES_LIST",),
	("PSGVAL__C_CLOCKS_TIMES_LIST01", FMAXPSG_SCTN0916_CLASS_LIST_VAL_ADD, "C_CLOCKS", "TIMES_LIST", "TIME_INTERVAL_START%KEY%", "alarm time entry in TIMES_LIST",),
	("PSGVAL__C_CLOCKS_TIMES_LIST01", FMAXPSG_SCTN0916_CLASS_LIST_VAL_ADD, "C_CLOCKS", "TIMES_LIST", "TIME_INTERVAL__BEGIN%KEY%", "alarm time entry in TIMES_LIST",),
	("PSGVAL__C_CLOCKS_TIMES_LIST01", FMAXPSG_SCTN0916_CLASS_LIST_VAL_ADD, "C_CLOCKS", "TIMES_LIST", "TIME_INTERVAL__END%KEY%", "alarm time entry in TIMES_LIST",),
	("PSGVAL__C_CLOCKS_TIMES_LIST01", FMAXPSG_SCTN0916_CLASS_LIST_VAL_ADD, "C_CLOCKS", "TIMES_LIST", "TIME_LEN_RING%KEY%", "alarm time entry in TIMES_LIST",),
	("PSGVAL__FONTSZ_ALERT_TEXT", FMAXPSG_SCTN0901_VAL_DEF, "FONTSZ_ALERT_TEXT", "(FONT_DEFAULT, SZ_ALERT_TEXT)", "the font for the clocks only clock",),
	("PSGVAL__FONTSZ_BTNS", FMAXPSG_SCTN0901_VAL_DEF, "FONTSZ_BTNS", "(FONT_DEFAULT, SZ_BTNS)", "comment",),
	("PSGVAL__FONTSZ_CLOCKS_INTERVAL_COUNT", FMAXPSG_SCTN0901_VAL_DEF, "FONTSZ_CLOCKS_INTERVAL_COUNT", "(FONT_DEFAULT, SZ_INTERVAL_COUNT)", "the font for the clocks only clock",),
	("PSGVAL__FONTSZ_CLOCKS_TIME_CLOCK", FMAXPSG_SCTN0901_VAL_DEF, "FONTSZ_CLOCKS_TIME_CLOCK", "(FONT_DEFAULT, SZ_CLOCKS_TIME_CLOCK)", "the font for the clocks only clock",),
	("PSGVAL__FONTSZ_CLOCKS_TIME_ELAPSED", FMAXPSG_SCTN0901_VAL_DEF, "FONTSZ_CLOCKS_TIME_ELAPSED", "(FONT_DEFAULT, SZ_CLOCKS_TIME_ELAPSED)", "the font for the clocks only clock",),
	("PSGVAL__FONTSZ_CLOCKS_TIME_TOGO", FMAXPSG_SCTN0901_VAL_DEF, "FONTSZ_CLOCKS_TIME_TOGO", "(FONT_DEFAULT, SZ_CLOCKS_TIME_TOGO)", "the font for the clocks only clock",),
	("PSGVAL__MAPPDS", FMAX_NOP, "the dict that holds all of the structure of the variables, read from and written to PySimpleGUI bits and un/pickled",),
	("PSGVAL__MAPPDS00", FMAXPSG_SCTN090C_MAPPDS_DEF, "MAPPDS", "the struct holding everything passed betwixt PySimpleGUI and this app",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "ALPHA_CHANNEL", "1.0", "current AlphaChannel setting",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "ALPHA_HIGH", "1.0", "amount of seethrough when mouse is not hovering over CLOCKS or THECLOCK",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "ALPHA_LOW", "0.3", "amount of seethrough when mouse hovers over clocks or THECLOCK",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "APPMODE", "APPMODE_NONE", "default mode is clocks",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "BBOX", "EMPTY_BBOX", "FILLED IN BY INIT",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "CHECKBOX_ALPHA_LOW", "True", "default transparent under mouse when not cornered to True",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "CHECKBOX_RUNAWAY", "True", "default to avoiding mouse",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "CLOSE_BBOX", "EMPTY_BBOX", "FILLED IN BY INIT",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "INDEX_OF_NEXT_EVENT", "0", "default to first entry as next until the app can sort through them",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "MAINFRAME", "None", "current screen position",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "MAINFRAME_LCN", "EMPTY_XY", "current screen position",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "MAINFRAME_SIZE", "EMPTY_XY", "current screen position",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "MOUSE_LCN", "(0, 0)", "track mouse location",),
	("PSGVAL__MAPPDS01", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "SCREEN_DIMS", "EMPTY_XY", "current screen position",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_DEF, "MAPPDS", "EVENT_ENTRIES", "0", "holds events",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "ALARMPOPUP_TEXT_TEXT", "get up, move around", "alarm text for this event",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "NAME", "MOVE", "this entry's name",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "TIME_ALARM", "03:30:00", "time of this event if it an alarm",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "TIME_INTERVAL", "00:30:00", "interval of this event",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "ALARMPOPUP_PROPER", "None", "time of this event",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "AUTO_CLOSE_DURATION", "10", "time of this event",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "DISMISSED", "False", "is this event dismissed",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "ENABLED", "True", "is this event enabled",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "EVENTMODE", "EVENTMODE_INTERVAL", "this entry's event_mode",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "FIRSTRUN", "True", "are we initializing or not",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "INTERVAL_COUNT", "0", "count of number of times this has alerted since last reset",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "PREDISMISSABLE", "True", "is this event dismissable in advance",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "SNOOZABLE", "False", "can this event be snoozed",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "SNOOZED", "False", "is this event snoozed",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "TIME_AT_LAST_RUN", "0", "time this alarm last ran, now if running",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "TIME_AT_NEXT", "ZERO_CLOCK", "time next time this alarm goes off",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "TIME_INTERVAL_START", "ZERO_CLOCK", "time of the day this round of interval started",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "TIME_INTERVAL__BEGIN", "ZERO_CLOCK", "time of the day this interval is made active",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "TIME_INTERVAL__END", "ZERO_CLOCK", "time of the day this interval is no longer active",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "0", "TIME_LEN_RING", "ZERO_CLOCK", "length of time to alert this event before auto closing it",),
	("PSGVAL__MAPPDS02", FMAXPSG_SCTN090C_MAPPDS_VV_ADD, "MAPPDS", "IS_ALERTING_NOW", "False", "is any event alerting right now",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_DEF, "MAPPDS", "EVENT_ENTRIES", "1", "holds events",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "ALARMPOPUP_TEXT_TEXT", "start winding down", "time of this event",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "NAME", "wind down", "this entry's name",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "TIME_ALARM", "03:30:00", "time of this event",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "TIME_INTERVAL", "00:00:00", "time of this event",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "ALARMPOPUP_PROPER", "None", "time of this event",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "AUTO_CLOSE_DURATION", "10", "time of this event",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "DISMISSED", "False", "is this event dismissed",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "ENABLED", "True", "is this event enabled",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "EVENTMODE", "EVENTMODE_ALARM", "this entry's event_mode",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "FIRSTRUN", "True", "are we initializing or not",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "INTERVAL_COUNT", "0", "count of number of times this has alerted since last reset",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "IS_ALERTING_NOW", "False", "is this event dismissed",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "PREDISMISSABLE", "True", "is this event dismissable in advance",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "SNOOZABLE", "False", "can this event be snoozed",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "SNOOZED", "False", "is this event snoozed",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "TIME_AT_LAST_RUN", "0", "is this event dismissed",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "TIME_AT_NEXT", "ZERO_CLOCK", "time of this event",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "TIME_INTERVAL_START", "ZERO_CLOCK", "time of this event",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "TIME_INTERVAL__BEGIN", "ZERO_CLOCK", "time of this event",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "TIME_INTERVAL__END", "ZERO_CLOCK", "time of this event",),
	("PSGVAL__MAPPDS03", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "1", "TIME_LEN_RING", "ZERO_CLOCK", "time of this event",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_DEF, "MAPPDS", "EVENT_ENTRIES", "2", "holds events",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "ALARMPOPUP_TEXT_TEXT", "next interval", "alarm text for this event",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "NAME", "test interval", "this entry's name",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "TIME_ALARM", "00:00:00", "time of this event if it an alarm",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "TIME_INTERVAL", "00:00:30", "interval of this event",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "ALARMPOPUP_PROPER", "None", "time of this event",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "AUTO_CLOSE_DURATION", "10", "time of this event",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "DISMISSED", "False", "is this event dismissed",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "ENABLED", "True", "is this event enabled",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "EVENTMODE", "EVENTMODE_INTERVAL", "this entry's event_mode",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "FIRSTRUN", "True", "are we initializing or not",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "INTERVAL_COUNT", "0", "count of number of times this has alerted since last reset",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "IS_ALERTING_NOW", "False", "is this event alerting right now",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "PREDISMISSABLE", "True", "is this event dismissable in advance",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "SNOOZABLE", "False", "can this event be snoozed",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "SNOOZED", "False", "is this event snoozed",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "TIME_AT_LAST_RUN", "0", "time this alarm last ran, now if running",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "TIME_AT_NEXT", "ZERO_CLOCK", "time next time this alarm goes off",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "TIME_INTERVAL_START", "ZERO_CLOCK", "time of the day this round of interval started",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "TIME_INTERVAL__BEGIN", "ZERO_CLOCK", "time of the day this interval is made active",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "TIME_INTERVAL__END", "ZERO_CLOCK", "time of the day this interval is no longer active",),
	("PSGVAL__MAPPDS04", FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD, "MAPPDS", "EVENT_ENTRIES", "2", "TIME_LEN_RING", "ZERO_CLOCK", "length of time to alert this event before auto closing it",),
	("PSGVAL__THECLOCK_DICT", FMAXPSG_SCTN0902_DICT_DEF, "THECLOCK_DICT", "set up the mainframe update dict for theclock mode",),
	("PSGVAL__THECLOCK_DICT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "THECLOCK_DICT", "TIME_CLOCK", "ZERO_CLOCK", "comment",),
	("PSGVAL__THECLOCK_LAYOUT00", FMAXPSG_SCTN090E_LAYOUT_DEF, "THECLOCK_LAYOUT", "layout for APPMODE_THECLOCK",),
	("PSGVAL__THECLOCK_LAYOUT01", FMAXPSG_SCTN090E_LAYOUT_ROW_ADD, "THECLOCK_LAYOUT", "THECLOCK_LAYOUT_ROW_00", "L01", "add a row to the layout",),
	("PSGVAL__THECLOCK_LAYOUT02", FMAXPSG_SCTN090E_LAYOUT_TEXT_ADD, "THECLOCK_LAYOUT", "THECLOCK_LAYOUT_ROW_00", "L02", "THECLOCK_LAYOUT_E01", "add a column",),
	("PSGVAL__THECLOCK_LAYOUT03", FMAXPSG_SCTN090E_LAYOUT_PACKEDPARM_ADD, "THECLOCK_LAYOUT", "THECLOCK_LAYOUT_ROW_00", "L03", "THECLOCK_LAYOUT_E01", "THECLOCK_TEXT_TIME_CLOCK", "comment",),
	("PSGVAL__THECLOCK_MAINFRAME", FMAX_NOP, "the frame for clocks",),
	("PSGVAL__THECLOCK_MAINFRAME00", FMAXPSG_SCTN090D_MAINFRAME_DEF, "THECLOCK", "THECLOCK_WINDOW", "True", "the clocks frame defined and done",),
	("PSGVAL__THECLOCK_RCMENU01", FMAXPSG_SCTN0913_RCMENU_DEF, "THECLOCK_RCMENU01", "right click to do the things",),
	("PSGVAL__THECLOCK_RCMENU0101", FMAXPSG_SCTN0913_RCMENU_VAL_ADD, "THECLOCK_RCMENU01", "BTN_QUIT", "quit by right click",),
	("PSGVAL__THECLOCK_RCMENU0101", FMAXPSG_SCTN0913_RCMENU_VAL_ADD, "THECLOCK_RCMENU01", "CHECKBOX_ALPHA_LOW", "toggle CHECKBOX_ALPHA_LOW",),
	("PSGVAL__THECLOCK_RCMENU0101", FMAXPSG_SCTN0913_RCMENU_VAL_ADD, "THECLOCK_RCMENU01", "CHECKBOX_RUNAWAY", "toggle CHECKBOX_RUNAWAY",),
	("PSGVAL__THECLOCK_TEXT_TIME_CLOCK", FMAX_NOP, "CLOCKS text TIME_CLOCK",),
	("PSGVAL__THECLOCK_TEXT_TIME_CLOCK00", FMAXPSG_SCTN0909_TEXT_DEF, "THECLOCK_TEXT_TIME_CLOCK", "define the text element for THECLOCK_CLOCK_TIME",),
	("PSGVAL__THECLOCK_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "THECLOCK_TEXT_TIME_CLOCK", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__THECLOCK_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "THECLOCK_TEXT_TIME_CLOCK", "ENABLE_EVENTS", "True", "this is clickable",),
	("PSGVAL__THECLOCK_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "THECLOCK_TEXT_TIME_CLOCK", "FONT", "FONTSZ_CLOCKS_TIME_CLOCK", "font+size line",),
	("PSGVAL__THECLOCK_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "THECLOCK_TEXT_TIME_CLOCK", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__THECLOCK_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "THECLOCK_TEXT_TIME_CLOCK", "KEY", "TIME_CLOCK", "comment",),
	("PSGVAL__THECLOCK_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "THECLOCK_TEXT_TIME_CLOCK", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__THECLOCK_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "THECLOCK_TEXT_TIME_CLOCK", "RIGHT_CLICK_MENU", "THECLOCK_RCMENU01", "set up the right click menu",),
	("PSGVAL__THECLOCK_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "THECLOCK_TEXT_TIME_CLOCK", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__THECLOCK_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "THECLOCK_TEXT_TIME_CLOCK", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__THECLOCK_TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "THECLOCK_TEXT_TIME_CLOCK", "TEXT_COLOR", "COLOR_TIME_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__THECLOCK_WINDOW", FMAX_NOP, "the window for APPMODE_THECLOCK",),
	("PSGVAL__THECLOCK_WINDOW00", FMAXPSG_SCTN090F_WINDOW_DEF, "THECLOCK_WINDOW", "define the clocks window",),
	("PSGVAL__THECLOCK_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "THECLOCK_WINDOW", "ALPHA_CHANNEL", "SZ_ALPHA_HIGH", "set the high alpha as the default",),
	("PSGVAL__THECLOCK_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "THECLOCK_WINDOW", "BACKGROUND_COLOR", "COLOR_BACKGROUND", "eliminate all not useful on the floating clocks",),
	("PSGVAL__THECLOCK_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "THECLOCK_WINDOW", "BORDER_DEPTH", "SZ_BORDER_DEPTH", "border depth to zero",),
	("PSGVAL__THECLOCK_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "THECLOCK_WINDOW", "ELEMENT_PADDING", "SZ_PAD_ALL", "all padding for elements ((1, 1), (1, 1)) by default",),
	("PSGVAL__THECLOCK_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "THECLOCK_WINDOW", "FORCE_TOPLEVEL", "None", "",),
	("PSGVAL__THECLOCK_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "THECLOCK_WINDOW", "GRAB_ANYWHERE", "True", "eliminate all not useful on the floating clocks",),
	("PSGVAL__THECLOCK_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "THECLOCK_WINDOW", "KEEP_ON_TOP", "True", "eliminate all not useful on the floating clocks",),
	("PSGVAL__THECLOCK_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "THECLOCK_WINDOW", "LAYOUT", "THECLOCK_LAYOUT", "add the layout for THECLOCK_WINDOW",),
	("PSGVAL__THECLOCK_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "THECLOCK_WINDOW", "MARGINS", "SZ_MARGINS_ALL", "",),
	("PSGVAL__THECLOCK_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "THECLOCK_WINDOW", "NO_TITLEBAR", "True", "no titlebar on APPMODE_THECLOCK window",),
	("PSGVAL__THECLOCK_WINDOW01", FMAXPSG_SCTN090F_WINDOW_VAL_ADD, "THECLOCK_WINDOW", "TITLE", "TITLE_THECLOCK", "",),
	("PSGVAL__VCURRENT_ALARM_NAME", FMAXPSG_SCTN0901_VAL_DEF, "CURRENT_ALARM_NAME", "None", "last returned mouse status to deal with hover events",),
	("PSGVAL__VCURRENT_EVENTMODE", FMAXPSG_SCTN0901_VAL_DEF, "CURRENT_EVENTMODE", "EVENTMODE_NONE", "last returned mouse status to deal with hover events",),
	("PSGVAL__VCURRENT_INTERVAL_COUNT", FMAXPSG_SCTN0901_VAL_DEF, "CURRENT_INTERVAL_COUNT", "0", "comment",),
	("PSGVAL__VIS_ALERTING_NOWV", FMAXPSG_SCTN0901_VAL_DEF, "IS_ALERTING_NOWV", "False", "comment",),
	("PSGVAL__VLAST_MOUSE_STATUS", FMAXPSG_SCTN0901_VAL_DEF, "LAST_MOUSE_STATUS", "None", "last returned mouse status to deal with hover events",),
	("PSGVAL__VMAINFRAME", FMAXPSG_SCTN0901_VAL_DEF, "MAINFRAME", "None", "mainframe so everything passes together always",),
	("PSGVAL__VMLCN", FMAXPSG_SCTN0901_VAL_DEF, "MLCN", "DISP.Display().screen().root.query_pointer", "short cut to get mouse position",),
	("PSGVAL__VNAME_NEXT_EVENT_STR", FMAXPSG_SCTN0901_STR_DEF, "NAME_NEXT_EVENT_STR", "", "name of the next event",),
	("PSGVAL__VNOWM", FMAXPSG_SCTN0901_VAL_DEF, "NOWM", "0", "comment",),
	("PSGVAL__VNOWMS", FMAXPSG_SCTN0901_VAL_DEF, "NOWMS", "0", "comment",),
	("PSGVAL__VNOWS", FMAXPSG_SCTN0901_VAL_DEF, "NOWS", "0", "comment",),
	("PSGVAL__VNOW_NOMS", FMAXPSG_SCTN0901_VAL_DEF, "NOW_NOMS", "0", "comment",),
	("PSGVAL__VNUMBER_ACTIVE_ALARMS", FMAXPSG_SCTN0901_VAL_DEF, "NUMBER_ACTIVE_ALARMS", "0", "number of alarms with not dismissed state",),
	("PSGVAL__VPREVIOUS_APPMODE", FMAXPSG_SCTN0901_VAL_DEF, "PREVIOUS_APPMODE", "APPMODE_NONE", "comment",),
	("PSGVAL__VPREV_ALARM_TYPE", FMAXPSG_SCTN0901_VAL_DEF, "PREV_ALARM_TYPE", "EVENTMODE_NONE", "previous alarm type",),
	("PSGVAL__VTIMEMS_NEXT_MOUSE_CHECK", FMAXPSG_SCTN0901_VAL_DEF, "TIMEMS_NEXT_MOUSE_CHECK", "0", "comment",),
	("PSGVAL__VTIMEMS_NEXT_MOVED", FMAXPSG_SCTN0901_VAL_DEF, "TIMEMS_NEXT_MOVED", "0", "comment",),
	("PSGVAL__VTIMEMS_NEXT_UPDATED", FMAXPSG_SCTN0901_VAL_DEF, "TIMEMS_NEXT_UPDATED", "0", "comment",),
	("PSGVAL__VTIMES_ADJUST_VALUE", FMAXPSG_SCTN0901_VAL_DEF, "TIMES_ADJUST_VALUE", "lambda H_=0, M_=0: ((60 * 60 * H_) + (M_ * 60))", "comment",),
	("PSGVAL__VTIMES_NEXT_EVENT", FMAXPSG_SCTN0901_VAL_DEF, "TIMES_NEXT_EVENT", "0", "comment",),
	("PSGVAL__VTIMES_NEXT_PERIODIC_JOB", FMAXPSG_SCTN0901_VAL_DEF, "TIMES_NEXT_PERIODIC_JOB", "0", "seconds till next housekeeping, check for next times, etc.",),
	("PSGVAL___", FMAX_NOP, "start of PySimpleGui keys",),
	("PSGVAL___ALPHA_CHANNEL", FMAXPSG_SCTN0910_STR_DEF, "ALPHA_CHANNEL", "alpha_channel", "",),
	("PSGVAL___AUTO_CLOSE", FMAXPSG_SCTN0910_STR_DEF, "AUTO_CLOSE", "auto_close", "",),
	("PSGVAL___AUTO_CLOSE_DURATION", FMAXPSG_SCTN0910_STR_DEF, "AUTO_CLOSE_DURATION", "auto_close_duration", "",),
	("PSGVAL___AUTO_SIZE_BUTTON", FMAXPSG_SCTN0910_STR_DEF, "AUTO_SIZE_BUTTON", "auto_size_button", "",),
	("PSGVAL___AUTO_SIZE_BUTTONS", FMAXPSG_SCTN0910_STR_DEF, "AUTO_SIZE_BUTTONS", "auto_size_buttons", "",),
	("PSGVAL___AUTO_SIZE_TEXT", FMAXPSG_SCTN0910_STR_DEF, "AUTO_SIZE_TEXT", "auto_size_text", "",),
	("PSGVAL___AUTO_SIZE_TEXT", FMAXPSG_SCTN0910_STR_DEF, "AUTO_SIZE_TEXT", "auto_size_text", "",),
	("PSGVAL___BACKGROUND_COLOR", FMAXPSG_SCTN0910_STR_DEF, "BACKGROUND_COLOR", "background_color", "",),
	("PSGVAL___BIND_RETURN_KEY", FMAXPSG_SCTN0910_STR_DEF, "BIND_RETURN_KEY", "bind_return_key", "",),
	("PSGVAL___BORDER_DEPTH", FMAXPSG_SCTN0910_STR_DEF, "BORDER_DEPTH", "border_depth", "",),
	("PSGVAL___BORDER_WIDTH", FMAXPSG_SCTN0910_STR_DEF, "BORDER_WIDTH", "border_width", "",),
	("PSGVAL___BUTTON_COLOR", FMAXPSG_SCTN0910_STR_DEF, "BUTTON_COLOR", "button_color", "",),
	("PSGVAL___BUTTON_TEXT", FMAXPSG_SCTN0910_STR_DEF, "BUTTON_TEXT", "button_text", "",),
	("PSGVAL___BUTTON_TYPE", FMAXPSG_SCTN0910_STR_DEF, "BUTTON_TYPE", "button_type", "",),
	("PSGVAL___CHANGE_SUBMITS", FMAXPSG_SCTN0910_STR_DEF, "CHANGE_SUBMITS", "change_submits", "",),
	("PSGVAL___CHECKBOX_COLOR", FMAXPSG_SCTN0910_STR_DEF, "CHECKBOX_COLOR", "checkbox_color", "color of background of the box that has the check mark in it. The checkmark is the same color as the text",),
	("PSGVAL___CIRCLE_COLOR", FMAXPSG_SCTN0910_STR_DEF, "CIRCLE_COLOR", "circle_color", "",),
	("PSGVAL___CLICK_SUBMITS", FMAXPSG_SCTN0910_STR_DEF, "CLICK_SUBMITS", "click_submits", "",),
	("PSGVAL___DEBUGGER_ENABLED", FMAXPSG_SCTN0910_STR_DEF, "DEBUGGER_ENABLED", "debugger_enabled", "",),
	("PSGVAL___DEFAULT", FMAXPSG_SCTN0910_STR_DEF, "DEFAULT", "default", "",),
	("PSGVAL___DEFAULT_BUTTON_ELEMENT_SIZE", FMAXPSG_SCTN0910_STR_DEF, "DEFAULT_BUTTON_ELEMENT_SIZE", "default_button_element_size", "",),
	("PSGVAL___DEFAULT_ELEMENT_SIZE", FMAXPSG_SCTN0910_STR_DEF, "DEFAULT_ELEMENT_SIZE", "default_element_size", "",),
	("PSGVAL___DEFAULT_EXTENSION", FMAXPSG_SCTN0910_STR_DEF, "DEFAULT_EXTENSION", "default_extension", "",),
	("PSGVAL___DEFAULT_VALUE", FMAXPSG_SCTN0910_STR_DEF, "DEFAULT_VALUE", "default_value", "",),
	("PSGVAL___DISABLED", FMAXPSG_SCTN0910_STR_DEF, "DISABLED", "disabled", "",),
	("PSGVAL___DISABLED_BUTTON_COLOR", FMAXPSG_SCTN0910_STR_DEF, "DISABLED_BUTTON_COLOR", "disabled_button_color", "",),
	("PSGVAL___DISABLE_CLOSE", FMAXPSG_SCTN0910_STR_DEF, "DISABLE_CLOSE", "disable_close", "",),
	("PSGVAL___DISABLE_MINIMIZE", FMAXPSG_SCTN0910_STR_DEF, "DISABLE_MINIMIZE", "disable_minimize", "",),
	("PSGVAL___ELEMENT_JUSTIFICATION", FMAXPSG_SCTN0910_STR_DEF, "ELEMENT_JUSTIFICATION", "element_justification", "",),
	("PSGVAL___ELEMENT_PADDING", FMAXPSG_SCTN0910_STR_DEF, "ELEMENT_PADDING", "element_padding", "",),
	("PSGVAL___ENABLED", FMAXPSG_SCTN0910_STR_DEF, "ENABLED", "enabled", "",),
	("PSGVAL___ENABLE_CLOSE_ATTEMPTED_EVENT", FMAXPSG_SCTN0910_STR_DEF, "ENABLE_CLOSE_ATTEMPTED_EVENT", "enable_close_attempted_event", "",),
	("PSGVAL___ENABLE_EVENTS", FMAXPSG_SCTN0910_STR_DEF, "ENABLE_EVENTS", "enable_events", "",),
	("PSGVAL___EXPAND_X", FMAXPSG_SCTN0910_STR_DEF, "EXPAND_X", "expand_x", "",),
	("PSGVAL___EXPAND_Y", FMAXPSG_SCTN0910_STR_DEF, "EXPAND_Y", "expand_y", "",),
	("PSGVAL___FILE_TYPES", FMAXPSG_SCTN0910_STR_DEF, "FILE_TYPES", "file_types", "",),
	("PSGVAL___FINALIZE", FMAXPSG_SCTN0910_STR_DEF, "FINALIZE", "finalize", "",),
	("PSGVAL___FOCUS", FMAXPSG_SCTN0910_STR_DEF, "FOCUS", "focus", "",),
	("PSGVAL___FONT_", FMAXPSG_SCTN0910_STR_DEF, "FONT", "font", "",),
	("PSGVAL___FORCE_TOPLEVEL", FMAXPSG_SCTN0910_STR_DEF, "FORCE_TOPLEVEL", "force_toplevel", "",),
	("PSGVAL___GRAB", FMAXPSG_SCTN0910_STR_DEF, "GRAB", "grab", "",),
	("PSGVAL___GRAB_ANYWHERE", FMAXPSG_SCTN0910_STR_DEF, "GRAB_ANYWHERE", "grab_anywhere", "",),
	("PSGVAL___GROUP_ID", FMAXPSG_SCTN0910_STR_DEF, "GROUP_ID", "group_id", "",),
	("PSGVAL___HIGHLIGHT_COLORS", FMAXPSG_SCTN0910_STR_DEF, "HIGHLIGHT_COLORS", "highlight_colors", "",),
	("PSGVAL___ICON", FMAXPSG_SCTN0910_STR_DEF, "ICON", "icon", "",),
	("PSGVAL___IMAGE_DATA", FMAXPSG_SCTN0910_STR_DEF, "IMAGE_DATA", "image_data", "",),
	("PSGVAL___IMAGE_FILENAME", FMAXPSG_SCTN0910_STR_DEF, "IMAGE_FILENAME", "image_filename", "",),
	("PSGVAL___IMAGE_SIZE", FMAXPSG_SCTN0910_STR_DEF, "IMAGE_SIZE", "image_size", "",),
	("PSGVAL___IMAGE_SUBSAMPLE", FMAXPSG_SCTN0910_STR_DEF, "IMAGE_SUBSAMPLE", "image_subsample", "",),
	("PSGVAL___INITIAL_FOLDER", FMAXPSG_SCTN0910_STR_DEF, "INITIAL_FOLDER", "initial_folder", "",),
	("PSGVAL___INITIAL_VALUE", FMAXPSG_SCTN0910_STR_DEF, "INITIAL_VALUE", "initial_value", "",),
	("PSGVAL___JUSTIFICATION", FMAXPSG_SCTN0910_STR_DEF, "JUSTIFICATION", "justification", "",),
	("PSGVAL___JUSTIFICATION_CENTER", FMAXPSG_SCTN0910_STR_DEF, "JUSTIFICATION_CENTER", "center", "comment",),
	("PSGVAL___JUSTIFICATION_LEFT", FMAXPSG_SCTN0910_STR_DEF, "JUSTIFICATION_LEFT", "left", "comment",),
	("PSGVAL___JUSTIFICATION_RIGHT", FMAXPSG_SCTN0910_STR_DEF, "JUSTIFICATION_RIGHT", "right", "comment",),
	("PSGVAL___K", FMAXPSG_SCTN0910_STR_DEF, "K", "k", "",),
	("PSGVAL___KEEP_ON_TOP", FMAXPSG_SCTN0910_STR_DEF, "KEEP_ON_TOP", "keep_on_top", "",),
	("PSGVAL___KEY", FMAXPSG_SCTN0910_STR_DEF, "KEY", "key", "",),
	("PSGVAL___LAYOUT", FMAXPSG_SCTN0910_STR_DEF, "LAYOUT", "layout", "",),
	("PSGVAL___LOCATION", FMAXPSG_SCTN0910_STR_DEF, "LOCATION", "location", "",),
	("PSGVAL___MARGINS", FMAXPSG_SCTN0910_STR_DEF, "MARGINS", "margins", "",),
	("PSGVAL___METADATA", FMAXPSG_SCTN0910_STR_DEF, "METADATA", "metadata", "",),
	("PSGVAL___MODAL", FMAXPSG_SCTN0910_STR_DEF, "MODAL", "modal", "",),
	("PSGVAL___NON_BLOCKING", FMAXPSG_SCTN0910_STR_DEF, "NON_BLOCKING", "non_blocking", "",),
	("PSGVAL___NO_TITLEBAR", FMAXPSG_SCTN0910_STR_DEF, "NO_TITLEBAR", "no_titlebar", "",),
	("PSGVAL___PAD", FMAXPSG_SCTN0910_STR_DEF, "PAD", "pad", "",),
	("PSGVAL___PROGRESS_BAR_COLOR", FMAXPSG_SCTN0910_STR_DEF, "PROGRESS_BAR_COLOR", "progress_bar_color", "",),
	("PSGVAL___READONLY", FMAXPSG_SCTN0910_STR_DEF, "READONLY", "readonly", "",),
	("PSGVAL___RELIEF", FMAXPSG_SCTN0910_STR_DEF, "RELIEF", "relief", "",),
	("PSGVAL___RELIEF_FLAT", FMAXPSG_SCTN0910_STR_DEF, "RELIEF_FLAT", "flat", "comment",),
	("PSGVAL___RELIEF_GROOVE", FMAXPSG_SCTN0910_STR_DEF, "RELIEF_GROOVE", "groove", "",),
	("PSGVAL___RELIEF_RAISED", FMAXPSG_SCTN0910_STR_DEF, "RELIEF_RAISED", "raised", "",),
	("PSGVAL___RELIEF_RIDGE", FMAXPSG_SCTN0910_STR_DEF, "RELIEF_RIDGE", "ridge", "",),
	("PSGVAL___RELIEF_SOLID", FMAXPSG_SCTN0910_STR_DEF, "RELIEF_SOLID", "solid", "",),
	("PSGVAL___RELIEF_SUNKEN", FMAXPSG_SCTN0910_STR_DEF, "RELIEF_SUNKEN", "sunken", "",),
	("PSGVAL___RESIZABLE", FMAXPSG_SCTN0910_STR_DEF, "RESIZABLE", "resizable", "",),
	("PSGVAL___RETURN_KEYBOARD_EVENTS", FMAXPSG_SCTN0910_STR_DEF, "RETURN_KEYBOARD_EVENTS", "return_keyboard_events", "",),
	("PSGVAL___RIGHT_CLICK_MENU", FMAXPSG_SCTN0910_STR_DEF, "RIGHT_CLICK_MENU", "right_click_menu", "",),
	("PSGVAL___RIGHT_CLICK_MENU_BACKGROUND_COLOR", FMAXPSG_SCTN0910_STR_DEF, "RIGHT_CLICK_MENU_BACKGROUND_COLOR", "right_click_menu_background_color", "",),
	("PSGVAL___RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR", FMAXPSG_SCTN0910_STR_DEF, "RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR", "right_click_menu_disabled_text_color", "",),
	("PSGVAL___RIGHT_CLICK_MENU_FONT", FMAXPSG_SCTN0910_STR_DEF, "RIGHT_CLICK_MENU_FONT", "right_click_menu_font", "",),
	("PSGVAL___RIGHT_CLICK_MENU_SELECTED_COLORS", FMAXPSG_SCTN0910_STR_DEF, "RIGHT_CLICK_MENU_SELECTED_COLORS", "right_click_menu_selected_colors", "",),
	("PSGVAL___RIGHT_CLICK_MENU_TEAROFF", FMAXPSG_SCTN0910_STR_DEF, "RIGHT_CLICK_MENU_TEAROFF", "right_click_menu_tearoff", "",),
	("PSGVAL___RIGHT_CLICK_MENU_TEXT_COLOR", FMAXPSG_SCTN0910_STR_DEF, "RIGHT_CLICK_MENU_TEXT_COLOR", "right_click_menu_text_color", "",),
	("PSGVAL___S", FMAXPSG_SCTN0910_STR_DEF, "S", "s", "",),
	("PSGVAL___SCROLLABLE", FMAXPSG_SCTN0910_STR_DEF, "SCROLLABLE", "scrollable", "can this column be scrolled bool",),
	("PSGVAL___SET_TO_INDEX", FMAXPSG_SCTN0910_STR_DEF, "SET_TO_INDEX", "set_to_index", "change selection to a particular choice starting with index = 0",),
	("PSGVAL___SIZE", FMAXPSG_SCTN0910_STR_DEF, "SIZE", "size", "",),
	("PSGVAL___TARGET", FMAXPSG_SCTN0910_STR_DEF, "TARGET", "target", "",),
	("PSGVAL___TEXT", FMAXPSG_SCTN0910_STR_DEF, "TEXT", "text", "",),
	("PSGVAL___TEXT_COLOR", FMAXPSG_SCTN0910_STR_DEF, "TEXT_COLOR", "text_color", "",),
	("PSGVAL___TEXT_JUSTIFICATION", FMAXPSG_SCTN0910_STR_DEF, "TEXT_JUSTIFICATION", "text_justification", "",),
	("PSGVAL___TIMEOUT_KEY", FMAXPSG_SCTN0910_STR_DEF, "TIMEOUT_KEY", "timeout_key", "",),
	("PSGVAL___TITLE", FMAXPSG_SCTN0910_STR_DEF, "TITLE", "title", "",),
	("PSGVAL___TITLEBAR_BACKGROUND_COLOR", FMAXPSG_SCTN0910_STR_DEF, "TITLEBAR_BACKGROUND_COLOR", "titlebar_background_color", "",),
	("PSGVAL___TITLEBAR_FONT", FMAXPSG_SCTN0910_STR_DEF, "TITLEBAR_FONT", "titlebar_font", "",),
	("PSGVAL___TITLEBAR_ICON", FMAXPSG_SCTN0910_STR_DEF, "TITLEBAR_ICON", "titlebar_icon", "",),
	("PSGVAL___TITLEBAR_TEXT_COLOR", FMAXPSG_SCTN0910_STR_DEF, "TITLEBAR_TEXT_COLOR", "titlebar_text_color", "",),
	("PSGVAL___TOOLTIP", FMAXPSG_SCTN0910_STR_DEF, "TOOLTIP", "tooltip", "",),
	("PSGVAL___TRANSPARENT_COLOR", FMAXPSG_SCTN0910_STR_DEF, "TRANSPARENT_COLOR", "transparent_color", "",),
	("PSGVAL___TTK_THEME", FMAXPSG_SCTN0910_STR_DEF, "TTK_THEME", "ttk_theme", "",),
	("PSGVAL___USE_CUSTOM_TITLEBAR", FMAXPSG_SCTN0910_STR_DEF, "USE_CUSTOM_TITLEBAR", "use_custom_titlebar", "",),
	("PSGVAL___USE_DEFAULT_FOCUS", FMAXPSG_SCTN0910_STR_DEF, "USE_DEFAULT_FOCUS", "use_default_focus", "",),
	("PSGVAL___USE_TTK_BUTTONS", FMAXPSG_SCTN0910_STR_DEF, "USE_TTK_BUTTONS", "use_ttk_buttons", "",),
	("PSGVAL___VALUE", FMAXPSG_SCTN0910_STR_DEF, "VALUE", "value", "the value of the element",),
	("PSGVAL___VALUES", FMAXPSG_SCTN0910_STR_DEF, "VALUES", "values", "list of values",),
	("PSGVAL___VERTICAL_ALIGNMENT", FMAXPSG_SCTN0910_STR_DEF, "VERTICAL_ALIGNMENT", "vertical_alignment", "",),
	("PSGVAL___VERTICAL_SCROLL_ONLY", FMAXPSG_SCTN0910_STR_DEF, "VERTICAL_SCROLL_ONLY", "verticale_scroll_only", "",),
	("PSGVAL___VISIBLE", FMAXPSG_SCTN0910_STR_DEF, "VISIBLE", "visible", "visibility of elements",),
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
# makeANormalTDD
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeANormalTDD(tupDictName_, tupDictItems_, TDDItems_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn1_ = ""

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	strToRtn_ += f"""{makeAComment(f"start of {tupDictName_} structures")}
{tupDictName_}TUP = {OPAREN}
{tupDictItems_}{CPAREN}{NEWLINE}{NEWLINE}def {tupDictName_}DICT{OPAREN}{CPAREN}:
{NTAB(1)}return dict{OPAREN}{OPAREN}x, y{CPAREN} for x, y in {tupDictName_}TUP{CPAREN}{NEWLINE}{NEWLINE}
{tupDictName_}_TDD = {OBRCE}{NEWLINE}{TDDItems_}{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeANormalTupDict
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
	dictToUse_ = sortADict(FMCF_SCTN0201_DEF_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMCF_SCTN0201_DEF_CMNT_DICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	strToRtn_ += f"""{makeAComment("SCTN0202 options structures")}"""
	strToRtn1_ = ""
	strToRtn2_ = ""
	strToRtn1_ += f"""OPTIONS = {OBRCE}{NEWLINE}{FOLD1STARTHERELN}"""
	strToRtn2_ += f"""OPTIONSHELPDICT = {OBRCE}{NEWLINE}{FOLD1STARTHERELN}"""
	dictToUse_ = sortADict(FMCF_SCTN0202_OPTIONS_DICT)
	for thisName_, values_ in dictToUse_.items():
		strToRtn1_ += f"""{NTAB(1)}{DBLQT}{thisName_}{DBLQT}: {OBRCE}{NEWLINE}{NTAB(1)}{FOLD2STARTHERELN}{values_}{NTAB(1)}{CBRCE},{NEWLINE}{NTAB(1)}{FOLD2ENDHERELN}"""
		strToRtn2_ += f"""{NTAB(1)}{DBLQT}{thisName_}{DBLQT}: {NEWLINE}{NTAB(1)}{FOLD2STARTHERELN}{TRIQT}{FMCF_SCTN0202_OPTIONSHELPDICT_DICT[thisName_]}{NTAB(1)}{TRIQT},{NEWLINE}{NTAB(1)}{FOLD2ENDHERELN}"""
	strToRtn1_ += f"""{CBRCE}{NEWLINE}{FOLD1ENDHERELN}{NEWLINE}"""
	strToRtn2_ += f"""{CBRCE}{NEWLINE}{FOLD1ENDHERELN}{NEWLINE}"""
	strToRtn_ += f"""{strToRtn1_}{strToRtn2_}"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
	strToRtn_ += f"""OPTIONSDICT = {OBRCE}{NEWLINE}"""
	dictToUse_ = sortADict(FMCF_SCTN0202_OPTIONSDICT_DICT)
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
	dictToUse_ = sortADict(FMCF_SCTN0003_TYPE_DICT)
	for thisName_, value_ in dictToUse_.items():
		value_ = FMCF_SCTN0003_TYPE_DICT[thisName_]
		strToRtn_ += f"""{thisName_} = {value_}  # {FMCF_SCTN0003_TYPE_CMNT_DICT[thisName_]}{NEWLINE}"""
	strToRtn_ += NEWLINE + NEWLINE

	## ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN101 FMAX _DEF_")}"""
	strToRtn01_ = ""
	dictToUse_ = sortADict(FMFM_SCTN0101_AX_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMFM_SCTN0101_AX_CMNT_DICT[thisName_]}{NEWLINE}"""
		strToRtn01_ += f"""{NTAB(1)}{thisName_},  # {FMFM_SCTN0101_AX_CMNT_DICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}FMAXFM_AXLST = {OBRKT}{NEWLINE}{strToRtn01_}{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN102 VAL _DEF_")}"""
	strToRtn01_ = ""
	dictToUse_ = sortADict(FMFM_SCTN0102_VAL_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMFM_SCTN0102_VAL_CMNT_DICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN103 _DICT_ _DEF_")}"""
	strToRtn01_ = ""
	dictToUse_ = sortADict(FMFM_SCTN0103_DICT_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {OBRCE}{CBRCE}  # {FMFM_SCTN0103_DICT_CMNT_DICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN104 _LIST_ _DEF_")}"""
	dictToUse_ = sortADict(FMFM_SCTN0104_LIST_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMFM_SCTN0104_LIST_CMNT_DICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}{makeAWideComment("end of managed portions of FM.py")}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{NTAB(1)}global {BKSLSH}{NEWLINE}"""

	dictToUse_ = sortADict(FMFM_SCTN0102_VAL_DICT)
	for name_, value_ in dictToUse_.items():
		strToRtn_ += f"""{NTAB(2)}{name_}, {BKSLSH}{NEWLINE}"""

	dictToUse_ = sortADict(FMFM_SCTN0103_DICT_DICT)
	for name_, value_ in dictToUse_.items():
		strToRtn_ += f"""{NTAB(2)}{name_}, {BKSLSH}{NEWLINE}"""

	dictToUse_ = sortADict(FMFM_SCTN0104_LIST_DICT)
	for name_, value_ in dictToUse_.items():
		strToRtn_ += f"""{NTAB(2)}{name_}, {BKSLSH}{NEWLINE}"""

	strToRtn_ = f"""{strToRtn_[:-4]}{NEWLINE}"""

	return strToRtn_
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
# FMFM_MAKE_ENDS


# FMPSG_MAKE_BEGINS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# makePSGClasses
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def makePSGClasses():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""

	strToRtn_ += f"""{makeAComment("SCTN0916 classes")}{NEWLINE}{NEWLINE}"""

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	for thisClass_, theseVars_ in FMPSG_SCTN0916_CLASS_DICT.items():
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		strToRtn_ += f"""class CLASS_{thisClass_}{OPAREN}object{CPAREN}:
{NTAB(1)}global {BKSLSH}
{NTAB(3)}MAINFRAME, {BKSLSH}
{NTAB(3)}MAPPDS, {BKSLSH}
{NTAB(3)}POPUPFRAME{NEWLINE}
{NTAB(1)}def __init__{OPAREN}self, thisWindow_=None{CPAREN}:
{NTAB(2)}THIS_WINDOW = thisWindow_
"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
#		print(f"""FMPSG_SCTN0916_CLASS_BTNS_DICT {FMPSG_SCTN0916_CLASS_BTNS_DICT}
#thisClass_ |{thisClass_}|
#theseVars_ |{theseVars_}|
#""")
		if thisClass_ in FMPSG_SCTN0916_CLASS_BTNS_DICT:
			for thisElementName_, thisElementVals_ in FMPSG_SCTN0916_CLASS_BTNS_DICT[thisClass_].items():
				strToRtn_ += f"""{NTAB(2)}self.{thisElementName_} = {OBRCE}  # {FMPSG_SCTN0916_CLASS_BTNS_CMNT_DICT[thisClass_][thisElementName_]}
{thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}
"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if thisClass_ in FMPSG_SCTN0916_CLASS_SPIN_DICT:
			for thisElementName_, thisElementVals_ in FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClass_].items():
				strToRtn_ += f"""{NTAB(2)}self.{thisElementName_}_SPIN_LIST = {OBRKT}
{FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClass_][thisElementName_]}{NTAB(2)}{CBRKT}{NEWLINE}
{NTAB(2)}self.{thisElementName_}_SPIN_DICT = {OBRCE}  # {FMPSG_SCTN0916_CLASS_SPIN_CMNT_DICT[thisClass_][thisElementName_]}
{thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}
"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if thisClass_ in FMPSG_SCTN0916_CLASS_CHECKBOX_DICT:
			for thisElementName_, thisElementVals_ in FMPSG_SCTN0916_CLASS_CHECKBOX_DICT[thisClass_].items():
				strToRtn_ += f"""{NTAB(2)}self.{thisElementName_} = {OBRCE}  # {FMPSG_SCTN0916_CLASS_CHECKBOX_CMNT_DICT[thisClass_][thisElementName_]}
{thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}
"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if thisClass_ in FMPSG_SCTN0916_CLASS_TEXT_DICT:
			for thisElementName_, thisElementVals_ in FMPSG_SCTN0916_CLASS_TEXT_DICT[thisClass_].items():
				strToRtn_ += f"""{NTAB(2)}self.{thisElementName_} = {OBRCE}  # {FMPSG_SCTN0916_CLASS_TEXT_CMNT_DICT[thisClass_][thisElementName_]}
{thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}
"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if thisClass_ in FMPSG_SCTN0916_CLASS_RADIO_DICT:
			for thisElementName_, thisElementVals_ in FMPSG_SCTN0916_CLASS_RADIO_DICT[thisClass_].items():
				strToRtn_ += f"""{NTAB(2)}self.{thisElementName_} = {OBRCE}  # {FMPSG_SCTN0916_CLASS_RADIO_CMNT_DICT[thisClass_][thisElementName_]}
{thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}
"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if thisClass_ in FMPSG_SCTN0916_CLASS_COMBO_DICT:
			for thisElementName_, thisElementVals_ in FMPSG_SCTN0916_CLASS_COMBO_DICT[thisClass_].items():
				strToRtn_ += f"""{NTAB(2)}self.{thisElementName_} = {OBRCE}  # {FMPSG_SCTN0916_CLASS_COMBO_CMNT_DICT[thisClass_][thisElementName_]}
{thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}
"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		strToRtn_ += f"""{NTAB(1)}def __enter__{OPAREN}self{CPAREN}:
{NTAB(2)}global {BKSLSH}
{NTAB(4)}MAINFRAME, {BKSLSH}
{NTAB(4)}MAPPDS, {BKSLSH}
{NTAB(4)}POPUPFRAME{NEWLINE}
{NTAB(2)}if {OPAREN}MAINFRAME is None{CPAREN}:
{NTAB(3)}MAINFRAME = SG.Window{OPAREN}**self.{thisClass_}_WINDOW{CPAREN}.finalize{OPAREN}{CPAREN}
{NTAB(3)}self.THIS_WINDOW = MAINFRAME
{NTAB(2)}elif {OPAREN}POPUPFRAME is None{CPAREN}:
{NTAB(3)}POPUPFRAME = SG.Window{OPAREN}**self.{thisClass_}_WINDOW{CPAREN}.finalize{OPAREN}{CPAREN}{NEWLINE}
{NTAB(3)}self.THIS_WINDOW = POPUPFRAME
{NTAB(2)}elif {OPAREN}self.THIS_WINDOW is not None{CPAREN}:
{NTAB(3)}self.THIS_WINDOW = SG.Window{OPAREN}**self.{thisClass_}_WINDOW{CPAREN}.finalize{OPAREN}{CPAREN}{NEWLINE}
{NTAB(2)}def __exit__{OPAREN}self, *args_{CPAREN}:
{NTAB(2)}global {BKSLSH}
{NTAB(4)}MAINFRAME, {BKSLSH}
{NTAB(4)}MAPPDS, {BKSLSH}
{NTAB(4)}POPUPFRAME{NEWLINE}
{NTAB(2)}self.THIS_WINDOW.close{OPAREN}{CPAREN}
{NTAB(2)}if {OPAREN}self.THIS_WINDOW == MAINFRAME{CPAREN}:
{NTAB(3)}MAINFRAME = None
{NTAB(2)}elif {OPAREN}self.THIS_WINDOW == POPUPFRAME{CPAREN}:
{NTAB(3)}POPUPFRAME = None{NEWLINE}
{NTAB(2)}self.THIS_WINDOW = None{NEWLINE}{NEWLINE}
"""

	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# makePSG
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

def makePSG():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{readFileToStr(f"{PSGTOP_NAME}")}{makeAComment("SCTN0900 DEF1")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0900_DEF1_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMPSG_SCTN0900_DEF1_CMNT_DICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0901 DEF2")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0901_DEF2_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMPSG_SCTN0901_DEF2_CMNT_DICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0910 DEF3")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0910_DEF3_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMPSG_SCTN0910_DEF3_CMNT_DICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0902 dicts")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0902_DICT_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeADict(thisName_, FMPSG_SCTN0902_DICT_CMNT_DICT[thisName_], value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0903 lists")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0903_LIST_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {OBRKT}  # {FMPSG_SCTN0903_LIST_CMNT_DICT[thisName_]}{NEWLINE}{value_}{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0904 platform equalizers")}"""
	dictToUseOuter_ = sortADict(FMPSG_SCTN0904_PLATEQ_OUTER_DICT)
	dictToUseInner_ = sortADict(FMPSG_SCTN0904_PLATEQ_INNER_DICT)
	for thisouterKey, outerVal_ in dictToUseOuter_.items():
		strToRtn_ += f""""""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0905 tupdict")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0905_TUPDICT_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeANormalTDD(thisName_, value_, FMPSG_SCTN0905_TUPDICT_TDD_DICT[thisName_])}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0913 right click menu options")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0913_RCMENU_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{thisName_} = {OBRKT}  # {FMPSG_SCTN0913_RCMENU_CMNT_DICT[thisName_]}{NEWLINE}"""
		strToRtn_ += f"""{NTAB(1)}{OBRKT}{CBRKT},{NEWLINE}{NTAB(1)}{OBRKT}{NEWLINE}{value_}{NTAB(1)}{CBRKT},{NEWLINE}{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0906 button elements")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0906_BTNS_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeADict(thisName_, FMPSG_SCTN0906_BTNS_CMNT_DICT[thisName_], value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0907 spin box elements")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0907_SPIN_DICT)  ## add FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeADict(thisName_, FMPSG_SCTN0907_SPIN_CMNT_DICT[thisName_], value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0908 checkbox elements")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0908_CHECKBOX_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeADict(thisName_, FMPSG_SCTN0908_CHECKBOX_CMNT_DICT[thisName_], value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0909 text elements")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0909_TEXT_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeADict(thisName_, FMPSG_SCTN0909_TEXT_CMNT_DICT[thisName_], value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN090A radio elements")}""" ## needs to be managed with the same structure as layouts
	dictToUse_ = sortADict(FMPSG_SCTN090A_RADIO_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeADict(thisName_, FMPSG_SCTN090A_RADIO_DICT[thisName_], value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN090B column elements")}"""
	dictToUse_ = sortADict(FMPSG_SCTN090B_COLUMN_DICT)
	for thisColumnName_, vals1_ in FMPSG_SCTN090B_COLUMN_DICT.items():
		strToRtn_ += f"""{thisColumnName_} = {OBRKT}  # {FMPSG_SCTN090B_COLUMN_CMNT_DICT[thisColumnName_]}{NEWLINE}"""
		for thisRow_, vals2_ in vals1_.items():
			thisTabLevel1_ = FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRow_][TABLEVEL]
			strToRtn_ += f"""{NTAB(thisTabLevel1_)}{OBRKT}{NEWLINE}"""
			for thisElementKey_, vals3_ in vals2_.items():
				if thisElementKey_ == TABLEVEL:
					continue
				if vals3_ != "":
					strToRtn_ += f"""{vals3_}{NTAB(thisTabLevel1_ + 1)}{CPAREN},{NEWLINE}"""
			strToRtn_ += f"""{NTAB(thisTabLevel1_)}{CBRKT},{NEWLINE}"""
		strToRtn_ += f"""{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN090E layout elements")}"""
	dictToUse_ = sortADict(FMPSG_SCTN090E_LAYOUT_DICT)
	for thisLayoutName_, vals1_ in FMPSG_SCTN090E_LAYOUT_DICT.items():
		strToRtn_ += f"""{thisLayoutName_} = {OBRKT}  # {FMPSG_SCTN090E_LAYOUT_CMNT_DICT[thisLayoutName_]}{NEWLINE}"""
		for thisRow_, vals2_ in vals1_.items():
			thisTabLevel1_ = FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRow_][TABLEVEL]
			strToRtn_ += f"""{NTAB(thisTabLevel1_)}{OBRKT}{NEWLINE}"""
			for thisElementKey_, vals3_ in vals2_.items():
				if thisElementKey_ == TABLEVEL:
					continue
				if vals3_ != "":
					strToRtn_ += f"""{vals3_}{NTAB(thisTabLevel1_ + 1)}{CPAREN},{NEWLINE}"""
			strToRtn_ += f"""{NTAB(thisTabLevel1_)}{CBRKT},{NEWLINE}"""
		strToRtn_ += f"""{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN090F window")}"""
	dictToUse_ = sortADict(FMPSG_SCTN090F_WINDOW_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeADict(thisName_, FMPSG_SCTN090F_WINDOW_CMNT_DICT[thisName_], value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN090D mainframe")}"""
	dictToUse_ = sortADict(FMPSG_SCTN090D_MAINFRAME_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeAComment(f"{thisName_}_CLASS")}class {thisName_}_CLASS{OPAREN}{CPAREN}:{NEWLINE}{NTAB(1)}global MAINFRAME, MAPPDS{NEWLINE}{NEWLINE}"""
		strToRtn_ += f"""{NTAB(1)}def __enter__{OPAREN}self{CPAREN}:{NEWLINE}{NTAB(2)}global MAINFRAME, MAPPDS{NEWLINE}"""
		strToRtn_ += f"""{NTAB(2)}MAINFRAME = SG.Window{OPAREN}{NEWLINE}{value_}"""
		strToRtn_ = strToRtn_[:-1] + f"""{NTAB(2)}MAPPDS{OBRKT}APPMODE{CBRKT} = APPMODE_{thisName_}{NEWLINE}{NEWLINE}"""
		strToRtn_ += f"""{NTAB(1)}def __exit__{OPAREN}self, *args{CPAREN}:{NEWLINE}{NTAB(2)}global MAINFRAME, MAPPDS{NEWLINE}{NTAB(2)}MAINFRAME.close(){NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0914 popupframe")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0914_POPUPFRAME_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{makeAComment(f"{thisName_}_CLASS")}class {thisName_}_CLASS{OPAREN}{CPAREN}:{NEWLINE}{NTAB(1)}global POPUPFRAME, MAPPDS, PREVIOUS_APPMODE{NEWLINE}{NEWLINE}"""
		strToRtn_ += f"""{NTAB(1)}def __enter__{OPAREN}self{CPAREN}:{NEWLINE}{NTAB(2)}global POPUPFRAME, MAPPDS, PREVIOUS_APPMODE{NEWLINE}"""
		# strToRtn_ += f"""{NTAB(2)}MAPPDS{OBRKT}APPMODE{CBRKT} = APPMODE_{thisName_}{NEWLINE}"""
		strToRtn_ += f"""{NTAB(2)}POPUPFRAME = SG.Window{OPAREN}{NEWLINE}{value_}"""
		strToRtn_ += f"""{NEWLINE}{NTAB(1)}def __exit__{OPAREN}self, *args{CPAREN}:{NEWLINE}{NTAB(2)}global POPUPFRAME, PREVIOUS_APPMODE, MAPPDS{NEWLINE}{NTAB(2)}POPUPFRAME.close(){NEWLINE}"""
		strToRtn_ += f"""{NTAB(2)}MAPPDS{OBRKT}APPMODE{CBRKT} = PREVIOUS_APPMODE{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN0915 popup dialogs")}"""
	dictToUse_ = sortADict(FMPSG_SCTN0915_PUDLG_DICT_DICT)
	for thisName_, value_ in dictToUse_.items():
		strToRtn_ += f"""{NEWLINE}{NEWLINE}{makeAComment(f"{thisName_} PUDLG")}
class CLASS_{thisName_}{OPAREN}object{CPAREN}:
{NTAB(1)}{FOLD1STARTHERELN}
{NTAB(1)}def __init__{OPAREN}self, title_, count_, splatArgs_={OBRKT}{CBRKT}{CPAREN}:
{NTAB(2)}self.{thisName_}_DICT = {OBRCE}
{value_}{NTAB(2)}{CBRCE}{NEWLINE}
{NTAB(2)}self.{thisName_}_LIST = {OBRKT}
{NTAB(3)}f{TRIQT}INTERVAL {OBRCE}title_{CBRCE} has expired {OBRCE}count_{CBRCE} times{TRIQT},
{NTAB(3)}f{TRIQT}click OK to dismiss, or wait {OBRCE}self.POPUP_INTERVAL_DICT[auto_close_duration]{CBRCE}seconds from alarm{TRIQT},
{NTAB(2)}{CBRKT}.append{OPAREN}*splatArgs_{CPAREN}{NEWLINE}
{NTAB(2)}return self{NEWLINE}
{NTAB(1)}def __enter__{OPAREN}self{CPAREN}:
{NTAB(2)}SG.{FMPSG_SCTN0915_PUDLG_TYPE_DICT[thisName_]}{OPAREN}
{NTAB(3)}*self.{thisName_}_LIST,
{NTAB(3)}**self.{thisName_}_DICT,
{NTAB(2)}{CPAREN}{NEWLINE}{NTAB(1)}{FOLD1ENDHERELN}{NEWLINE}
"""

	strToRtn_ += makePSGClasses()

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# keep MAPPDS last
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	# print(f"""SCTN090C FMPSG_SCTN090C_MAPPDS_DICT |{FMPSG_SCTN090C_MAPPDS_DICT}|{NEWLINE}FMPSG_SCTN090C_MAPPDSDICT_DICT|{FMPSG_SCTN090C_MAPPDSDICT_DICT}|""")
	strToRtn_ += f"""{makeAComment("SCTN090C MAPPDS")}"""
	dictToUse_ = sortADict(FMPSG_SCTN090C_MAPPDS_DICT)
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	for thisName_, values_ in dictToUse_.items():
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		valuesDict_ = sortADict(values_)
		strToRtn_ += f"""{thisName_} = {OBRCE}  # {FMPSG_SCTN090C_MAPPDS_CMNT_DICT[thisName_]}{NEWLINE}"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for thisKey_, thisVal_ in valuesDict_.items():
			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			strToRtn_ += f"""{thisVal_}"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			if thisKey_ in FMPSG_SCTN090C_MAPPDSDICT_DICT[thisName_]:
				# 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥
				dictToAdd_ = sortADict(FMPSG_SCTN090C_MAPPDSDICT_DICT[thisName_][thisKey_])

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
				# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
				for thisKey1_, thisVal1_ in dictToAdd_.items():
					# 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥
					strToRtn_ += f"""{NTAB(2)}{thisKey1_}: {OBRCE}{NEWLINE}"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
				# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
					# ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥
					dictToAdd2_ = sortADict(thisVal1_)
					for thisKey2_, thisVal2_ in dictToAdd2_.items():
						# 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥
						strToRtn_ += f"""{NTAB(3)}{thisKey2_}: {thisVal2_}"""
						# ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
				# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
					# ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥
					strToRtn_ += f"""{NTAB(2)}{CBRCE},{NEWLINE}"""
					# ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
				# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
				strToRtn_ += f"""{NTAB(1)}{CBRCE},{NEWLINE}"""

				# ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		strToRtn_ += f"""{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"""

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	strToRtn_ += f"""{makeAWideComment("end of managed sections of PSG.py")}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# parseTBGLST
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def parseTBGLST(FDTBGLST):
	global \
		TABLEVEL, \
		FMCF_SCTN0003_TYPE_CMNT_DICT, \
		FMCF_SCTN0003_TYPE_DICT, \
		FMCF_SCTN0201_DEF_CMNT_DICT, \
		FMCF_SCTN0201_DEF_DICT, \
		FMCF_SCTN0202_OPTIONS_CMNT_DICT, \
		FMCF_SCTN0202_OPTIONS_DICT, \
		FMCF_SCTN0202_OPTIONSDICT_CMNT_DICT, \
		FMCF_SCTN0202_OPTIONSDICT_DICT, \
		FMCF_SCTN0202_OPTIONSHELPDICT_DICT, \
		FMCF_SCTN0203_DICT_CMNT_DICT, \
		FMCF_SCTN0203_DICT_DICT, \
		FMCF_SCTN0204_LIST_CMNT_DICT, \
		FMCF_SCTN0204_LIST_DICT, \
		FMFM_SCTN0101_AX_CMNT_DICT, \
		FMFM_SCTN0101_AX_DICT, \
		FMFM_SCTN0102_VAL_CMNT_DICT, \
		FMFM_SCTN0102_VAL_DICT, \
		FMFM_SCTN0103_DICT_CMNT_DICT, \
		FMFM_SCTN0103_DICT_DICT, \
		FMFM_SCTN0104_LIST_CMNT_DICT, \
		FMFM_SCTN0104_LIST_DICT, \
		FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT, \
		FMPSG_SCTN0900_DEF1_CMNT_DICT, \
		FMPSG_SCTN0900_DEF1_DICT, \
		FMPSG_SCTN0901_DEF2_CMNT_DICT, \
		FMPSG_SCTN0901_DEF2_DICT, \
		FMPSG_SCTN0902_DICT_CMNT_DICT, \
		FMPSG_SCTN0902_DICT_DICT, \
		FMPSG_SCTN0903_LIST_CMNT_DICT, \
		FMPSG_SCTN0903_LIST_DICT, \
		FMPSG_SCTN0904_PLATEQ_INNER_CMNT_DICT, \
		FMPSG_SCTN0904_PLATEQ_INNER_DICT, \
		FMPSG_SCTN0904_PLATEQ_OUTER_CMNT_DICT, \
		FMPSG_SCTN0904_PLATEQ_OUTER_DICT, \
		FMPSG_SCTN0905_TUPDICT_CMNT_DICT, \
		FMPSG_SCTN0905_TUPDICT_DICT, \
		FMPSG_SCTN0905_TUPDICT_TDD_DICT, \
		FMPSG_SCTN0906_BTNS_CMNT_DICT, \
		FMPSG_SCTN0906_BTNS_DICT, \
		FMPSG_SCTN0907_SPIN_CMNT_DICT, \
		FMPSG_SCTN0907_SPIN_DICT, \
		FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT, \
		FMPSG_SCTN0908_CHECKBOX_CMNT_DICT, \
		FMPSG_SCTN0908_CHECKBOX_DICT, \
		FMPSG_SCTN0909_TEXT_CMNT_DICT, \
		FMPSG_SCTN0909_TEXT_DICT, \
		FMPSG_SCTN090A_RADIO_CMNT_DICT, \
		FMPSG_SCTN090A_RADIO_DICT, \
		FMPSG_SCTN090B_COLUMN_CMNT_DICT, \
		FMPSG_SCTN090B_COLUMN_DICT, \
		FMPSG_SCTN090B_COLUMN_PARMS_DICT, \
		FMPSG_SCTN090C_MAPPDS_CMNT_DICT, \
		FMPSG_SCTN090C_MAPPDS_DICT, \
		FMPSG_SCTN090C_MAPPDSDICT_DICT, \
		FMPSG_SCTN090D_MAINFRAME_CMNT_DICT, \
		FMPSG_SCTN090D_MAINFRAME_DICT, \
		FMPSG_SCTN090E_LAYOUT_CMNT_DICT, \
		FMPSG_SCTN090E_LAYOUT_DICT, \
		FMPSG_SCTN090F_WINDOW_CMNT_DICT, \
		FMPSG_SCTN090F_WINDOW_DICT, \
		FMPSG_SCTN0910_DEF3_CMNT_DICT, \
		FMPSG_SCTN0910_DEF3_DICT, \
		FMPSG_SCTN0911_COMBO_CMNT_DICT, \
		FMPSG_SCTN0911_COMBO_DICT, \
		FMPSG_SCTN0912_FRAME_CMNT_DICT, \
		FMPSG_SCTN0912_FRAME_DICT, \
		FMPSG_SCTN0913_RCMENU_CMNT_DICT, \
		FMPSG_SCTN0913_RCMENU_DICT, \
		FMPSG_SCTN0914_POPUPFRAME_CMNT_DICT, \
		FMPSG_SCTN0914_POPUPFRAME_DICT, \
		FMPSG_SCTN0915_PUDLG_CMNT_DICT, \
		FMPSG_SCTN0915_PUDLG_DICT_DICT, \
		FMPSG_SCTN0915_PUDLG_LIST_DICT, \
		FMPSG_SCTN0915_PUDLG_TYPE_DICT, \
		FMPSG_SCTN0916_CLASS_BTNS_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_BTNS_DICT, \
		FMPSG_SCTN0916_CLASS_CHECKBOX_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_CHECKBOX_DICT, \
		FMPSG_SCTN0916_CLASS_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_COLUMN_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_COLUMN_DICT, \
		FMPSG_SCTN0916_CLASS_COLUMN_PARMS_DICT, \
		FMPSG_SCTN0916_CLASS_COMBO_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_COMBO_DICT, \
		FMPSG_SCTN0916_CLASS_DICT, \
		FMPSG_SCTN0916_CLASS_DICT_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_DICT_DICT, \
		FMPSG_SCTN0916_CLASS_FRAME_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_FRAME_DICT, \
		FMPSG_SCTN0916_CLASS_LAYOUT_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_LAYOUT_DICT, \
		FMPSG_SCTN0916_CLASS_LIST_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_LIST_DICT, \
		FMPSG_SCTN0916_CLASS_RADIO_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_RADIO_DICT, \
		FMPSG_SCTN0916_CLASS_RCMENU_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_RCMENU_DICT, \
		FMPSG_SCTN0916_CLASS_SPIN_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_SPIN_DICT, \
		FMPSG_SCTN0916_CLASS_TEXT_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_TEXT_DICT, \
		FMPSG_SCTN0916_CLASS_WINDOW_CMNT_DICT, \
		FMPSG_SCTN0916_CLASS_WINDOW_DICT
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
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0003_LAMBDA_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisLambdaName_ = thisItem_[2]
			thisLambdaVal_ = thisItem_[3]
			FMCF_SCTN0003_TYPE_DICT[thisLambdaName_] = f"lambda {thisLambdaVal_}"
			FMCF_SCTN0003_TYPE_CMNT_DICT[thisLambdaName_] = "{thisComment_}"
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
			FMCF_SCTN0003_TYPE_DICT[thisTypeName_] = f"{DBLQT}{thisType_}{DBLQT}"
			FMCF_SCTN0003_TYPE_CMNT_DICT[thisTypeName_] = f"{thisComment_}"
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
			FMCF_SCTN0201_DEF_DICT[thisValName_] = f"{DBLQT}{thisVal_}{DBLQT}"
			FMCF_SCTN0201_DEF_CMNT_DICT[thisValName_] = f"{thisComment_}"
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
			FMCF_SCTN0201_DEF_DICT[thisValName_] = f"{thisVal_}"
			FMCF_SCTN0201_DEF_CMNT_DICT[thisValName_] = f"{thisComment_}"
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
			if thisParm_ not in FMCF_SCTN0202_OPTIONSHELPDICT_DICT:
				FMCF_SCTN0202_OPTIONSHELPDICT_DICT[thisParm_] = ""
			FMCF_SCTN0202_OPTIONSHELPDICT_DICT[thisParm_] += f"""{thisComment_}{NEWLINE}"""
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
			if thisParm_ not in FMCF_SCTN0202_OPTIONS_DICT:
				FMCF_SCTN0202_OPTIONS_DICT[thisParm_] = ""
			if thisParm_ not in FMCF_SCTN0202_OPTIONSHELPDICT_DICT:
				FMCF_SCTN0202_OPTIONSHELPDICT_DICT[thisParm_] = ""
			FMCF_SCTN0202_OPTIONS_DICT[thisParm_] += f"""{NTAB(2)}{DBLQT}{thisKey_}{DBLQT}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			FMCF_SCTN0202_OPTIONSHELPDICT_DICT[thisParm_] += f"""{thisComment_}{NEWLINE}"""
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
			if thisParm_ not in FMCF_SCTN0202_OPTIONS_DICT:
				FMCF_SCTN0202_OPTIONS_DICT[thisParm_] = ""
			if thisParm_ not in FMCF_SCTN0202_OPTIONSHELPDICT_DICT:
				FMCF_SCTN0202_OPTIONSHELPDICT_DICT[thisParm_] = ""
			FMCF_SCTN0202_OPTIONS_DICT[thisParm_] += f"""{NTAB(2)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			FMCF_SCTN0202_OPTIONSHELPDICT_DICT[thisParm_] += f"""{thisComment_}{NEWLINE}"""
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
			FMCF_SCTN0202_OPTIONSDICT_DICT[thisName_] = f"{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
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
			FMCF_SCTN0202_OPTIONSDICT_DICT[thisName_] = f"{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"
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
			FMCF_SCTN0204_LIST_DICT[thisListName_] = ""
			FMCF_SCTN0204_LIST_CMNT_DICT[thisListName_] = f"{thisComment_}"
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
			FMCF_SCTN0204_LIST_DICT[thisListName_] += f"{NTAB(1)}f{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
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
			FMCF_SCTN0204_LIST_DICT[thisListName_] += f"{NTAB(1)}{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
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
			FMCF_SCTN0204_LIST_DICT[thisListName_] += f"{NTAB(1)}{thisVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# FMCF_PARSE_ENDS

# FMFM_PARSE_BEGINS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0101_AX_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMFM_SCTN0101_AX_DICT[thisName_] = f"{DBLQT}{thisName_}{DBLQT}"
			FMFM_SCTN0101_AX_CMNT_DICT[thisName_] = f"{thisComment_}"
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
			FMFM_SCTN0102_VAL_DICT[thisValName_] = f"""{DBLQT}{thisVal_}{DBLQT}"""
			FMFM_SCTN0102_VAL_CMNT_DICT[thisValName_] = f"{thisComment_}"
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
			FMFM_SCTN0102_VAL_DICT[thisValName_] = thisVal_
			FMFM_SCTN0102_VAL_CMNT_DICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0103_DICT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMFM_SCTN0103_DICT_DICT[thisName_] = f"{OBRCE}{CBRCE}"
			FMFM_SCTN0103_DICT_CMNT_DICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0104_LIST_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMFM_SCTN0104_LIST_DICT[thisName_] = f"{OBRKT}{CBRKT}"
			FMFM_SCTN0104_LIST_CMNT_DICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# FMFM_PARSE_ENDS

# FMPSG_PARSE_BEGINS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0900_KEY_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			FMPSG_SCTN0900_DEF1_DICT[thisValName_] = f"""{DBLQT}{thisValName_}{DBLQT}"""
			FMPSG_SCTN0900_DEF1_CMNT_DICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0900_STR_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMPSG_SCTN0900_DEF1_DICT[thisValName_] = f"""{DBLQT}{thisVal_}{DBLQT}"""
			FMPSG_SCTN0900_DEF1_CMNT_DICT[thisValName_] = f"""{thisComment_}"""
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
			FMPSG_SCTN0900_DEF1_DICT[thisValName_] = f"""{thisVal_}"""
			FMPSG_SCTN0900_DEF1_CMNT_DICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0901_DUBLT_SS_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal1_ = thisItem_[3]
			thisVal2_ = thisItem_[4]
			FMPSG_SCTN0901_DEF2_DICT[thisValName_] = f"""{OPAREN}{DBLQT}{thisVal1_}{DBLQT}, {DBLQT}{thisVal2_}{DBLQT}{CPAREN},"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0901_DUBLT_SV_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal1_ = thisItem_[3]
			thisVal2_ = thisItem_[4]
			FMPSG_SCTN0901_DEF2_DICT[thisValName_] = f"""{OPAREN}{DBLQT}{thisVal1_}{DBLQT}, {thisVal2_}{CPAREN},"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0901_DUBLT_VS_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal1_ = thisItem_[3]
			thisVal2_ = thisItem_[4]
			FMPSG_SCTN0901_DEF2_DICT[thisValName_] = f"""{OPAREN}{thisVal1_}, {DBLQT}{thisVal2_}{DBLQT}{CPAREN},"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0901_DUBLT_VV_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal1_ = thisItem_[3]
			thisVal2_ = thisItem_[4]
			FMPSG_SCTN0901_DEF2_DICT[thisValName_] = f"""{OPAREN}{thisVal1_}, {thisVal2_}{CPAREN}"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[thisValName_] = f"""{thisComment_}"""
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
			FMPSG_SCTN0901_DEF2_DICT[thisValName_] = f"""{DBLQT}{thisValName_}{DBLQT}"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[thisValName_] = f"""{thisComment_}"""
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
			FMPSG_SCTN0901_DEF2_DICT[thisValName_] = f"""{DBLQT}{thisVal_}{DBLQT}"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[thisValName_] = f"""{thisComment_}"""
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
			FMPSG_SCTN0901_DEF2_DICT[thisValName_] = f"""{thisVal_}"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[thisValName_] = f"""{thisComment_}"""
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
			if thisDictName_ not in FMPSG_SCTN0902_DICT_DICT:
				FMPSG_SCTN0902_DICT_DICT[thisDictName_] = ""
			FMPSG_SCTN0902_DICT_CMNT_DICT[thisDictName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0902_DICT_VS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMPSG_SCTN0902_DICT_DICT:
				FMPSG_SCTN0902_DICT_DICT[thisDictName_] = ""
			FMPSG_SCTN0902_DICT_DICT[thisDictName_] += f"""{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0902_DICT_SS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMPSG_SCTN0902_DICT_DICT:
				FMPSG_SCTN0902_DICT_DICT[thisDictName_] = ""
			FMPSG_SCTN0902_DICT_DICT[thisDictName_] += f"""{NTAB(1)}{DBLQT}{thisKey_}{DBLQT}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0902_DICT_SV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMPSG_SCTN0902_DICT_DICT:
				FMPSG_SCTN0902_DICT_DICT[thisDictName_] = ""
			FMPSG_SCTN0902_DICT_DICT[thisDictName_] += f"""{NTAB(1)}{DBLQT}{thisKey_}{DBLQT}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0902_DICT_VV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMPSG_SCTN0902_DICT_DICT:
				FMPSG_SCTN0902_DICT_DICT[thisDictName_] = ""
			FMPSG_SCTN0902_DICT_DICT[thisDictName_] += f"""{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0903_LIST_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			if thisListName_ not in FMPSG_SCTN0903_LIST_DICT:
				FMPSG_SCTN0903_LIST_DICT[thisListName_] = ""
			FMPSG_SCTN0903_LIST_CMNT_DICT[thisListName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0903_LIST_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			if thisListName_ not in FMPSG_SCTN0903_LIST_DICT:
				FMPSG_SCTN0903_LIST_DICT[thisListName_] = ""
			FMPSG_SCTN0903_LIST_DICT[thisListName_] += f"""{NTAB(1)}{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0903_LIST_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			if thisListName_ not in FMPSG_SCTN0903_LIST_DICT:
				FMPSG_SCTN0903_LIST_DICT[thisListName_] = ""
			FMPSG_SCTN0903_LIST_DICT[thisListName_] += f"""{NTAB(1)}{thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0904_PLATEQ_PLAT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisPlatEqName_ = thisItem_[2]
			thisPlatEqKey_ = thisItem_[3]
			thisPlatEqCondition_ = thisItem_[4]
			if thisPlatEqName_ not in FMPSG_SCTN0904_PLATEQ_OUTER_DICT:
				FMPSG_SCTN0904_PLATEQ_OUTER_DICT[thisPlatEqName_] = ""
			FMPSG_SCTN0904_PLATEQ_OUTER_DICT[thisPlatEqName_] = f"""{thisPlatEqKey_} = {thisPlatEqCondition_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0905_TUPDICT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisTupdictName_ = thisItem_[2]
			if thisTupdictName_ not in FMPSG_SCTN0905_TUPDICT_DICT:
				FMPSG_SCTN0905_TUPDICT_DICT[thisTupdictName_] = ""
				FMPSG_SCTN0905_TUPDICT_TDD_DICT[thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICT_CMNT_DICT[thisTupdictName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0905_TUPDICT_SS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisTupdictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisTupdictName_ not in FMPSG_SCTN0905_TUPDICT_DICT:
				FMPSG_SCTN0905_TUPDICT_DICT[thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICT_DICT[thisTupdictName_] += f"""{NTAB(1)}{OPAREN}{DBLQT}{thisKey_}{DBLQT}, {DBLQT}{thisVal_}{DBLQT}{CPAREN},  # {thisComment_}{NEWLINE}"""
			FMPSG_SCTN0905_TUPDICT_TDD_DICT[thisTupdictName_] += f"""{NTAB(1)}{DBLQT}{thisKey_}{DBLQT}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0905_TUPDICT_SV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisTupdictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisTupdictName_ not in FMPSG_SCTN0905_TUPDICT_DICT:
				FMPSG_SCTN0905_TUPDICT_DICT[thisTupdictName_] = ""
				FMPSG_SCTN0905_TUPDICT_TDD_DICT[thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICT_DICT[thisTupdictName_] += f"""{NTAB(1)}{OPAREN}{DBLQT}{thisKey_}{DBLQT}, {thisVal_}{CPAREN},  # {thisComment_}{NEWLINE}"""
			FMPSG_SCTN0905_TUPDICT_TDD_DICT[thisTupdictName_] += f"""{NTAB(1)}{DBLQT}{thisKey_}{DBLQT}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0905_TUPDICT_VS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisTupdictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisTupdictName_ not in FMPSG_SCTN0905_TUPDICT_DICT:
				FMPSG_SCTN0905_TUPDICT_DICT[thisTupdictName_] = ""
				FMPSG_SCTN0905_TUPDICT_TDD_DICT[thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICT_DICT[thisTupdictName_] += f"""{NTAB(1)}{OPAREN}{thisKey_}, {DBLQT}{thisVal_}{DBLQT}{CPAREN},  # {thisComment_}{NEWLINE}"""
			FMPSG_SCTN0905_TUPDICT_TDD_DICT[thisTupdictName_] += f"""{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0905_TUPDICT_VV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisTupdictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisTupdictName_ not in FMPSG_SCTN0905_TUPDICT_DICT:
				FMPSG_SCTN0905_TUPDICT_DICT[thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICT_DICT[thisTupdictName_] += f"""{NTAB(1)}{OPAREN}{thisKey_}, {thisVal_}{CPAREN},  # {thisComment_}{NEWLINE}"""
			FMPSG_SCTN0905_TUPDICT_TDD_DICT[thisTupdictName_] += f"""{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0906_BTN_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisElementName_ = thisItem_[2]
			if thisElementName_ not in FMPSG_SCTN0906_BTNS_DICT:
				FMPSG_SCTN0906_BTNS_DICT[thisElementName_] = ""
			FMPSG_SCTN0906_BTNS_CMNT_DICT[thisElementName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0906_BTN_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisElementName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisElementName_ not in FMPSG_SCTN0906_BTNS_DICT:
				FMPSG_SCTN0906_BTNS_DICT[thisElementName_] = ""
			FMPSG_SCTN0906_BTNS_DICT[thisElementName_] += f"""{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0906_BTN_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisElementName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisElementName_ not in FMPSG_SCTN0906_BTNS_DICT:
				FMPSG_SCTN0906_BTNS_DICT[thisElementName_] = ""
			FMPSG_SCTN0906_BTNS_DICT[thisElementName_] += f"""{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0907_SPIN_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisElementName_ = thisItem_[2]
			if thisElementName_ not in FMPSG_SCTN0907_SPIN_DICT:
				FMPSG_SCTN0907_SPIN_DICT[thisElementName_] = ""
			if thisElementName_ not in FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT:
				FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = ""
			FMPSG_SCTN0907_SPIN_CMNT_DICT[thisElementName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0907_SPIN_DICT_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisElementName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisElementName_ not in FMPSG_SCTN0907_SPIN_DICT:
				FMPSG_SCTN0907_SPIN_DICT[thisElementName_] = ""
			if thisElementName_ not in FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT:
				FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = ""
			FMPSG_SCTN0907_SPIN_DICT[thisElementName_] += f"""{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0907_SPIN_DICT_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisElementName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisElementName_ not in FMPSG_SCTN0907_SPIN_DICT:
				FMPSG_SCTN0907_SPIN_DICT[thisElementName_] = ""
			if thisElementName_ not in FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT:
				FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = ""
			FMPSG_SCTN0907_SPIN_DICT[thisElementName_] += f"""{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0907_SPIN_VALUES_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisElementName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			if thisElementName_ not in FMPSG_SCTN0907_SPIN_DICT:
				FMPSG_SCTN0907_SPIN_DICT[thisElementName_] = ""
			if thisElementName_ not in FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT:
				FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = ""
			FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT[thisElementName_] += f"""{NTAB(1)}{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0907_SPIN_VALUES_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisElementName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			if thisElementName_ not in FMPSG_SCTN0907_SPIN_DICT:
				FMPSG_SCTN0907_SPIN_DICT[thisElementName_] = ""
			if thisElementName_ not in FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT:
				FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = ""
			FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT[thisElementName_] += f"""{NTAB(1)}{thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0908_CHECKBOX_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisCheckboxElementName_ = thisItem_[2]
			if thisCheckboxElementName_ not in FMPSG_SCTN0908_CHECKBOX_DICT:
				FMPSG_SCTN0908_CHECKBOX_DICT[thisCheckboxElementName_] = ""
			FMPSG_SCTN0908_CHECKBOX_CMNT_DICT[thisCheckboxElementName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0908_CHECKBOX_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisCheckboxElementName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisCheckboxElementName_ not in FMPSG_SCTN0908_CHECKBOX_DICT:
				FMPSG_SCTN0908_CHECKBOX_DICT[thisCheckboxElementName_] = ""
			FMPSG_SCTN0908_CHECKBOX_DICT[thisCheckboxElementName_] += f"""{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisCheckboxElementName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisCheckboxElementName_ not in FMPSG_SCTN0908_CHECKBOX_DICT:
				FMPSG_SCTN0908_CHECKBOX_DICT[thisCheckboxElementName_] = ""
			FMPSG_SCTN0908_CHECKBOX_DICT[thisCheckboxElementName_] += f"""{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0909_TEXT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisElementName_ = thisItem_[2]
			if thisElementName_ not in FMPSG_SCTN0909_TEXT_DICT:
				FMPSG_SCTN0909_TEXT_DICT[thisElementName_] = ""
			FMPSG_SCTN0909_TEXT_CMNT_DICT[thisElementName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0909_TEXT_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisElementName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisElementName_ not in FMPSG_SCTN0909_TEXT_DICT:
				FMPSG_SCTN0909_TEXT_DICT[thisElementName_] = ""
			FMPSG_SCTN0909_TEXT_DICT[thisElementName_] += f"""{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0909_TEXT_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisElementName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisElementName_ not in FMPSG_SCTN0909_TEXT_DICT:
				FMPSG_SCTN0909_TEXT_DICT[thisElementName_] = ""
			FMPSG_SCTN0909_TEXT_DICT[thisElementName_] += f"""{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090F_WINDOW_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisWindowName_ = thisItem_[2]
			if thisWindowName_ not in FMPSG_SCTN090F_WINDOW_DICT:
				FMPSG_SCTN090F_WINDOW_DICT[thisWindowName_] = ""
			FMPSG_SCTN090F_WINDOW_CMNT_DICT[thisWindowName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090F_WINDOW_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisWindowName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisWindowName_ not in FMPSG_SCTN090F_WINDOW_DICT:
				FMPSG_SCTN090F_WINDOW_DICT[thisWindowName_] = ""
			FMPSG_SCTN090F_WINDOW_DICT[thisWindowName_] += f"""{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090F_WINDOW_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisWindowName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisWindowName_ not in FMPSG_SCTN090F_WINDOW_DICT:
				FMPSG_SCTN090F_WINDOW_DICT[thisWindowName_] = ""
			FMPSG_SCTN090F_WINDOW_DICT[thisWindowName_] += f"""{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090B_COLUMN_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisColumnName_ = thisItem_[2]
			if thisColumnName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_] = {}
			FMPSG_SCTN090B_COLUMN_CMNT_DICT[thisColumnName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090B_COLUMN_BUTTON_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisColumnName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			if thisColumnName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Button{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090B_COLUMN_CHECKBOX_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisColumnName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			if thisColumnName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Checkbox{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090B_COLUMN_COLUMN_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisColumnName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			if thisColumnName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Col{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090B_COLUMN_COMBO_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisColumnName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem[5]
			if thisColumnName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Combo{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090B_COLUMN_PACKEDPARM_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 8:
				doErrorItem("not 8 items", thisItem_)
				continue
			thisColumnName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			thisVal_ = thisItem_[6]
			if thisColumnName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}**{thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090B_COLUMN_PARM_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 8:
				doErrorItem("not 8 items", thisItem_)
				continue
			thisColumnName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			thisVal_ = thisItem_[6]
			if thisColumnName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}{thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090B_COLUMN_RADIO_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisColumnName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			if thisColumnName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Radio{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090B_COLUMN_ROW_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisColumnName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			if thisColumnName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_] = {}
			FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][TABLEVEL] = thisTabLevel_
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090B_COLUMN_SPIN_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisColumnName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			if thisColumnName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Spin{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090B_COLUMN_TEXT_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisColumnName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			if thisColumnName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[thisColumnName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Text{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090C_MAPPDS_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisMAPPDSName_ = thisItem_[2]
			if thisMAPPDSName_ not in FMPSG_SCTN090C_MAPPDS_DICT:
				FMPSG_SCTN090C_MAPPDS_DICT[thisMAPPDSName_] = {}
			FMPSG_SCTN090C_MAPPDS_CMNT_DICT[thisMAPPDSName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090C_MAPPDS_DICT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisMAPPDSName_ = thisItem_[2]
			thisDictName_ = thisItem_[3]
			thisIndexNum_ = thisItem_[4]
			if thisMAPPDSName_ not in FMPSG_SCTN090C_MAPPDS_DICT:
				FMPSG_SCTN090C_MAPPDS_DICT[thisMAPPDSName_] = {}
			if thisMAPPDSName_ not in FMPSG_SCTN090C_MAPPDSDICT_DICT:
				FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_] = {}
			if thisDictName_ not in FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_]:
				FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_][thisDictName_] = {}
			if thisIndexNum_ not in FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_][thisDictName_]:
				FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_][thisDictName_][thisIndexNum_] = {}
			FMPSG_SCTN090C_MAPPDS_DICT[thisMAPPDSName_][thisDictName_] = f"""{NTAB(1)}{thisDictName_}: {OBRCE}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090C_MAPPDS_DICT_VS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 8:
				doErrorItem("not 8 items", thisItem_)
				continue
			thisMAPPDSName_ = thisItem_[2]
			thisDictName_ = thisItem_[3]
			thisIndexNum_ = thisItem_[4]
			thisKey_ = thisItem_[5]
			thisVal_ = thisItem_[6]
			if thisMAPPDSName_ not in FMPSG_SCTN090C_MAPPDSDICT_DICT:
				FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_] = {}
			if thisDictName_ not in FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_]:
				FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_][thisDictName_] = {}
			if thisIndexNum_ not in FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_][thisDictName_]:
				FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_][thisDictName_][thisIndexNum_] = {}
			FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_][thisDictName_][thisIndexNum_][thisKey_] = f"""{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090C_MAPPDS_DICT_VV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 8:
				doErrorItem("not 8 items", thisItem_)
				continue
			thisMAPPDSName_ = thisItem_[2]
			thisDictName_ = thisItem_[3]
			thisIndexNum_ = thisItem_[4]
			thisKey_ = thisItem_[5]
			thisVal_ = thisItem_[6]
			if thisMAPPDSName_ not in FMPSG_SCTN090C_MAPPDSDICT_DICT:
				FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_] = {}
			if thisDictName_ not in FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_]:
				FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_][thisDictName_] = {}
			if thisIndexNum_ not in FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_][thisDictName_]:
				FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_][thisDictName_][thisIndexNum_] = {}
			FMPSG_SCTN090C_MAPPDSDICT_DICT[thisMAPPDSName_][thisDictName_][thisIndexNum_][thisKey_] = f"""{thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090C_MAPPDS_VS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisMAPPDSName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisMAPPDSName_ not in FMPSG_SCTN090C_MAPPDS_DICT:
				FMPSG_SCTN090C_MAPPDS_DICT[thisMAPPDSName_] = {}
			FMPSG_SCTN090C_MAPPDS_DICT[thisMAPPDSName_][thisKey_] = f"""{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090C_MAPPDS_VV_ADD:
				# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisMAPPDSName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisMAPPDSName_ not in FMPSG_SCTN090C_MAPPDS_DICT:
				FMPSG_SCTN090C_MAPPDS_DICT[thisMAPPDSName_] = {}
			FMPSG_SCTN090C_MAPPDS_DICT[thisMAPPDSName_][thisKey_] = f"""{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090D_MAINFRAME_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisMainframeName_ = thisItem_[2]
			thisWindowName_ = thisItem_[3]
			thisFinalize_ = thisItem_[4]
			if thisFinalize_ == "True":
				FMPSG_SCTN090D_MAINFRAME_DICT[thisMainframeName_] = f"""{NTAB(3)}**{thisWindowName_},{NEWLINE}{NTAB(2)}{CPAREN}.finalize{OPAREN}{CPAREN}{NEWLINE}{NEWLINE}"""
			else:
				FMPSG_SCTN090D_MAINFRAME_DICT[thisMainframeName_] = f"""{NTAB(3)}**{thisWindowName_},{NEWLINE}{NTAB(2)}{CPAREN}{NEWLINE}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090E_LAYOUT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisLayoutName_ = thisItem_[2]
			if thisLayoutName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_] = {}
			FMPSG_SCTN090E_LAYOUT_CMNT_DICT[thisLayoutName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisLayoutName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			if thisLayoutName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Button{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisLayoutName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			if thisLayoutName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Checkbox{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisLayoutName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			if thisLayoutName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Col{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090E_LAYOUT_COMBO_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisLayoutName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem[5]
			if thisLayoutName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Combo{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090E_LAYOUT_PACKEDPARM_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 8:
				doErrorItem("not 8 items", thisItem_)
				continue
			thisLayoutName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			thisVal_ = thisItem_[6]
			if thisLayoutName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}**{thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 9:
				doErrorItem("not 9 items", thisItem_)
				continue
			thisLayoutName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			thisKey_ = thisItem_[6]
			thisVal_ = thisItem_[7]
			if thisLayoutName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}{thisKey_}={thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090E_LAYOUT_RADIO_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisLayoutName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			if thisLayoutName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Radio{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090E_LAYOUT_ROW_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisLayoutName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			if thisLayoutName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_] = {}
			FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][TABLEVEL] = thisTabLevel_
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090E_LAYOUT_SPIN_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisLayoutName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			if thisLayoutName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Spin{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090E_LAYOUT_TEXT_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisLayoutName_ = thisItem_[2]
			thisRowKey_ = thisItem_[3]
			thisTabLevel_ = thisItem_[4]
			thisTabLevel_ = int(thisTabLevel_[1:])
			thisElementKey_ = thisItem_[5]
			if thisLayoutName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_] = {}
			if thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_] = {}
			if thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[thisLayoutName_][thisRowKey_][thisElementKey_] += f"""{NTAB(thisTabLevel_)}SG.Text{OPAREN}  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090F_WINDOW_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisWindowName_ = thisItem_[2]
			if thisWindowName_ not in FMPSG_SCTN090F_WINDOW_DICT:
				FMPSG_SCTN090F_WINDOW_DICT[thisWindowName_] = ""
			FMPSG_SCTN090F_WINDOW_CMNT_DICT[thisWindowName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090F_WINDOW_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisWindowName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisWindowName_ not in FMPSG_SCTN090F_WINDOW_DICT:
				FMPSG_SCTN090F_WINDOW_DICT[thisWindowName_] = ""
			FMPSG_SCTN090F_WINDOW_DICT[thisWindowName_] += f"""{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN090F_WINDOW_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisWindowName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisWindowName_ not in FMPSG_SCTN090F_WINDOW_DICT:
				FMPSG_SCTN090F_WINDOW_DICT[thisWindowName_] = ""
			FMPSG_SCTN090F_WINDOW_DICT[thisWindowName_] += f"""{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0910_STR_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMPSG_SCTN0910_DEF3_DICT[thisValName_] = f"""{DBLQT}{thisVal_}{DBLQT}"""
			FMPSG_SCTN0910_DEF3_CMNT_DICT[thisValName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0910_VAL_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMPSG_SCTN0910_DEF3_CMNT_DICT[thisValName_] = f"""{thisComment_}"""
			FMPSG_SCTN0910_DEF3_DICT[thisValName_] += f"""{thisVal_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0913_RCMENU_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisRCMenuName_ = thisItem_[2]
			if thisRCMenuName_ not in FMPSG_SCTN0913_RCMENU_DICT:
				FMPSG_SCTN0913_RCMENU_DICT[thisRCMenuName_] = ""
			FMPSG_SCTN0913_RCMENU_CMNT_DICT[thisRCMenuName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0913_RCMENU_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisRCMenuName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			if thisRCMenuName_ not in FMPSG_SCTN0913_RCMENU_DICT:
				FMPSG_SCTN0913_RCMENU_DICT[thisRCMenuName_] = ""
			FMPSG_SCTN0913_RCMENU_DICT[thisRCMenuName_] += f"""{NTAB(2)}{thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0914_POPUPFRAME_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisMainframeName_ = thisItem_[2]
			thisWindowName_ = thisItem_[3]
			thisFinalize_ = thisItem_[4]
			if thisFinalize_ == "True":
				FMPSG_SCTN0914_POPUPFRAME_DICT[thisMainframeName_] = f"""{NTAB(3)}**{thisWindowName_},{NEWLINE}{NTAB(2)}{CPAREN}.finalize{OPAREN}{CPAREN}{NEWLINE}{NTAB(2)}POPUPFRAME.Maximize{OPAREN}{CPAREN}{NEWLINE}{NTAB(2)}POPUPFRAME.BringToFront{OPAREN}{CPAREN}{NEWLINE}"""
			else:
				FMPSG_SCTN0914_POPUPFRAME_DICT[thisMainframeName_] = f"""{NTAB(3)}**{thisWindowName_},{NEWLINE}{NTAB(2)}{CPAREN}{NEWLINE}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0915_PUDLG_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisPopupName_ = thisItem_[2]
			thisPopupType_ = thisItem_[3]
			if thisPopupName_ not in FMPSG_SCTN0915_PUDLG_DICT_DICT:
				FMPSG_SCTN0915_PUDLG_DICT_DICT[thisPopupName_] = ""
			FMPSG_SCTN0915_PUDLG_CMNT_DICT[thisPopupName_] = f"""{thisComment_}"""
			FMPSG_SCTN0915_PUDLG_TYPE_DICT[thisPopupName_] = thisPopupType_
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0915_PUDLG_DICT_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisPopupName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisPopupName_ not in FMPSG_SCTN0915_PUDLG_DICT_DICT:
				FMPSG_SCTN0915_PUDLG_DICT_DICT[thisPopupName_] = ""
			FMPSG_SCTN0915_PUDLG_DICT_DICT[thisPopupName_] += f"""{NTAB(3)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisPopupName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisPopupName_ not in FMPSG_SCTN0915_PUDLG_DICT_DICT:
				FMPSG_SCTN0915_PUDLG_DICT_DICT[thisPopupName_] = ""
			FMPSG_SCTN0915_PUDLG_DICT_DICT[thisPopupName_] += f"""{NTAB(3)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# FMPSG_PARSE_ENDS


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# fillit
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#

# CLASS_DEF_BEGINS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_DICT:
				FMPSG_SCTN0916_CLASS_DICT[thisClassName_] = {}
			FMPSG_SCTN0916_CLASS_CMNT_DICT[thisClassName_] = f"""{thisComment_}"""
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# CLASS_DEF_ENDS

# CLASS_BTN_BEGINS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_BTN_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_BTNS_DICT:
				FMPSG_SCTN0916_CLASS_BTNS_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_BTNS_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_BTNS_DICT[thisClassName_][thisElementName_] = ""
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_BTNS_CMNT_DICT:
				FMPSG_SCTN0916_CLASS_BTNS_CMNT_DICT[thisClassName_] = {}
			FMPSG_SCTN0916_CLASS_BTNS_CMNT_DICT[thisClassName_][thisElementName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_BTN_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			thisKey_ = thisItem_[4]
			thisVal_ = thisItem_[5]
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_BTNS_DICT:
				FMPSG_SCTN0916_CLASS_BTNS_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_BTNS_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_BTNS_DICT[thisClassName_][thisElementName_] = ""
			FMPSG_SCTN0916_CLASS_BTNS_DICT[thisClassName_][thisElementName_] += f"""{NTAB(3)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_BTN_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			thisKey_ = thisItem_[4]
			thisVal_ = thisItem_[5]
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_BTNS_DICT:
				FMPSG_SCTN0916_CLASS_BTNS_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_BTNS_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_BTNS_DICT[thisClassName_][thisElementName_] = ""
			FMPSG_SCTN0916_CLASS_BTNS_DICT[thisClassName_][thisElementName_] += f"""{NTAB(3)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# CLASS_BTN_ENDS

# CLASS_CHECKBOX_BEGINS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_CHECKBOX_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_CHECKBOX_DICT:
				FMPSG_SCTN0916_CLASS_CHECKBOX_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_CHECKBOX_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_CHECKBOX_DICT[thisClassName_][thisElementName_] = ""
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_CHECKBOX_CMNT_DICT:
				FMPSG_SCTN0916_CLASS_CHECKBOX_CMNT_DICT[thisClassName_] = {}
			FMPSG_SCTN0916_CLASS_CHECKBOX_CMNT_DICT[thisClassName_][thisElementName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_CHECKBOX_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			thisKey_ = thisItem_[4]
			thisVal_ = thisItem_[5]
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_CHECKBOX_DICT:
				FMPSG_SCTN0916_CLASS_CHECKBOX_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_CHECKBOX_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_CHECKBOX_DICT[thisClassName_][thisElementName_] = ""
			FMPSG_SCTN0916_CLASS_CHECKBOX_DICT[thisClassName_][thisElementName_] += f"""{NTAB(3)}{thisKey_}: {DBLQT}thisVal_{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_CHECKBOX_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			thisKey_ = thisItem_[4]
			thisVal_ = thisItem_[5]
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_CHECKBOX_DICT:
				FMPSG_SCTN0916_CLASS_CHECKBOX_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_CHECKBOX_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_CHECKBOX_DICT[thisClassName_][thisElementName_] = ""
			FMPSG_SCTN0916_CLASS_CHECKBOX_DICT[thisClassName_][thisElementName_] += f"""{NTAB(3)}{thisKey_}: thisVal_,  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# CLASS_CHECKBOX_ENDS

# CLASS_DICT_BEGINS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_DICT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			TthisClassName_ = thisItem_[2]
			thisDictName_ = thisItem_[3]

			if thisClassName_ not in FMPSG_SCTN0916_CLASS_DICT:
				FMPSG_SCTN0916_CLASS_DICT[thisClassName_] = {}
			if thisDictName_ not in FMPSG_SCTN0916_CLASS_DICT:
				FMPSG_SCTN0916_CLASS_DICT[thisDictName_] = ""

			FMPSG_SCTN0916_CLASS_CMNT_DICT[thisDictName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_DICT_SS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisDictName_ = thisItem_[3]
			thisKey_ = thisItem_[4]
			thisVal_ = thisItem_[5]

			if thisClassName_ not in FMPSG_SCTN0916_CLASS_DICT:
				FMPSG_SCTN0916_CLASS_DICT[thisClassName_] = []
			if thisDictName_ not in FMPSG_SCTN0916_CLASS_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_DICT[thisClassName_][thisDictName_] = ""

			FMPSG_SCTN0916_CLASS_DICT[thisClassName_][thisDictName_] += f"""{NTAB(1)}{DBLQT}{thisKey_}{DBLQT}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_DICT_SV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisDictName_ = thisItem_[3]
			thisKey_ = thisItem_[4]
			thisVal_ = thisItem_[5]

			if thisClassName_ not in FMPSG_SCTN0916_CLASS_DICT:
				FMPSG_SCTN0916_CLASS_DICT[thisClassName_] = []
			if thisDictName_ not in FMPSG_SCTN0916_CLASS_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_DICT[thisClassName_][thisDictName_] = ""

			FMPSG_SCTN0916_CLASS_DICT[thisClassName_][thisDictName_] += f"""{NTAB(1)}{DBLQT}{thisKey_}{DBLQT}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_DICT_VS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisDictName_ = thisItem_[3]
			thisKey_ = thisItem_[4]
			thisVal_ = thisItem_[5]

			if thisClassName_ not in FMPSG_SCTN0916_CLASS_DICT:
				FMPSG_SCTN0916_CLASS_DICT[thisClassName_] = []
			if thisDictName_ not in FMPSG_SCTN0916_CLASS_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_DICT[thisClassName_][thisDictName_] = ""

			FMPSG_SCTN0916_CLASS_DICT[thisClassName_][thisDictName_] += f"""{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_DICT_VV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisDictName_ = thisItem_[3]
			thisKey_ = thisItem_[4]
			thisVal_ = thisItem_[5]

			if thisClassName_ not in FMPSG_SCTN0916_CLASS_DICT:
				FMPSG_SCTN0916_CLASS_DICT[thisClassName_] = []
			if thisDictName_ not in FMPSG_SCTN0916_CLASS_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_DICT[thisClassName_][thisDictName_] = ""

			FMPSG_SCTN0916_CLASS_DICT[thisClassName_][thisDictName_] += f"""{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2


	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# CLASS_DICT_ENDS

# CLASS_LIST_BEGINS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0903_LIST_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			if thisListName_ not in FMPSG_SCTN0903_LIST_DICT:
				FMPSG_SCTN0903_LIST_DICT[thisListName_] = ""
			FMPSG_SCTN0903_LIST_CMNT_DICT[thisListName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0903_LIST_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			if thisListName_ not in FMPSG_SCTN0903_LIST_DICT:
				FMPSG_SCTN0903_LIST_DICT[thisListName_] = ""
			FMPSG_SCTN0903_LIST_DICT[thisListName_] += f"""{NTAB(1)}{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0903_LIST_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			if thisListName_ not in FMPSG_SCTN0903_LIST_DICT:
				FMPSG_SCTN0903_LIST_DICT[thisListName_] = ""
			FMPSG_SCTN0903_LIST_DICT[thisListName_] += f"""{NTAB(1)}{thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# CLASS_LIST_ENDS

# CLASS_SPIN_BEGINS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_SPIN_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]

			if thisClassName_ not in FMPSG_SCTN0916_CLASS_SPIN_DICT:
				FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_] = {}

			if thisClassName_ not in FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT:
				FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_]:
				FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_][thisElementName_] = ""

			if thisClassName_ not in FMPSG_SCTN0916_CLASS_SPIN_CMNT_DICT:
				FMPSG_SCTN0916_CLASS_SPIN_CMNT_DICT[thisClassName_] = {}
			FMPSG_SCTN0916_CLASS_SPIN_CMNT_DICT[thisClassName_][thisElementName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			thisKey_ = thisItem_[4]
			thisVal_ = thisItem_[5]

			if thisClassName_ not in FMPSG_SCTN0916_CLASS_SPIN_DICT:
				FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_] = {}

			if thisClassName_ not in FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT:
				FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_]:
				FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_][thisElementName_] = ""

			FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_][thisElementName_] += f"""{NTAB(3)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_SPIN_DICT_VV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			thisKey_ = thisItem_[4]
			thisVal_ = thisItem_[5]

			if thisClassName_ not in FMPSG_SCTN0916_CLASS_SPIN_DICT:
				FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_][thisElementName_] = ""

			if thisClassName_ not in FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT:
				FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_]:
				FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_][thisElementName_] = ""

			FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_][thisElementName_] += f"""{NTAB(3)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_SPIN_LIST_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			thisVal_ = thisItem_[4]

			if thisClassName_ not in FMPSG_SCTN0916_CLASS_SPIN_DICT:
				FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_] = {}

			if thisClassName_ not in FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT:
				FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_]:
				FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_][thisElementName_] = ""

			FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_][thisElementName_] += f"""{NTAB(3)}{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_SPIN_LIST_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			thisVal_ = thisItem_[4]

			if thisClassName_ not in FMPSG_SCTN0916_CLASS_SPIN_DICT:
				FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_SPIN_DICT[thisClassName_] = {}

			if thisClassName_ not in FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT:
				FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_]:
				FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_][thisElementName_] = ""

			FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[thisClassName_][thisElementName_] += f"""{NTAB(3)}{thisVal_},  # {thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# CLASS_SPIN_ENDS

# CLASS_TEXT_BEGINS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_TEXT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_TEXT_DICT:
				FMPSG_SCTN0916_CLASS_TEXT_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_TEXT_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_TEXT_DICT[thisClassName_][thisElementName_] = ""
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_TEXT_CMNT_DICT:
				FMPSG_SCTN0916_CLASS_TEXT_CMNT_DICT[thisClassName_] = {}
			FMPSG_SCTN0916_CLASS_TEXT_CMNT_DICT[thisClassName_][thisElementName_] = f"""{thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_TEXT_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			thisKey_ = thisItem_[4]
			thisVal_ = thisItem_[5]
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_TEXT_DICT:
				FMPSG_SCTN0916_CLASS_TEXT_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_TEXT_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_TEXT_DICT[thisClassName_][thisElementName_] = ""
			FMPSG_SCTN0916_CLASS_TEXT_DICT[thisClassName_][thisElementName_] += f"""{NTAB(3)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXPSG_SCTN0916_CLASS_TEXT_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 7:
				doErrorItem("not 7 items", thisItem_)
				continue
			thisClassName_ = thisItem_[2]
			thisElementName_ = thisItem_[3]
			thisKey_ = thisItem_[4]
			thisVal_ = thisItem_[5]
			if thisClassName_ not in FMPSG_SCTN0916_CLASS_TEXT_DICT:
				FMPSG_SCTN0916_CLASS_TEXT_DICT[thisClassName_] = {}
			if thisElementName_ not in FMPSG_SCTN0916_CLASS_TEXT_DICT[thisClassName_]:
				FMPSG_SCTN0916_CLASS_TEXT_DICT[thisClassName_][thisElementName_] = ""
			FMPSG_SCTN0916_CLASS_TEXT_DICT[thisClassName_][thisElementName_] += f"""{NTAB(3)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# CLASS_TEXT_ENDS

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# fillit
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#



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
