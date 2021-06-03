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
CACHE_DIR = "/home/will/.cache/"
CONFIG_DIR = "/home/will/.config/"


#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0002 value_ constants
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


AO_NAME = "newAO.py"
AOTOP_NAME = f"""{CONFIGDIR}AOTOP.py"""
BIN04 = lambda __X__: f"""{__X__:04b}"""
BIN08 = lambda __X__: f"""{__X__:08b}"""
BIN16 = lambda __X__: f"""{__X__:016b}"""
BIN32 = lambda __X__: f"""{__X__:032b}"""
BIN64 = lambda __X__: f"""{__X__:064b}"""
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
HEX08 = lambda __X__: f"""{__X__:02H}"""  # {thisComment_}
HEX16 = lambda __X__: f"""{__X__:04H}"""  # {thisComment_}
HEX32 = lambda __X__: f"""{__X__:08H}"""  # {thisComment_}
HEX64 = lambda __X__: f"""{__X__:016H}"""  # {thisComment_}
IMPORTANTSTR = f"""# * {"!-" * (CMNTLEN // 2)}"""  # important line marker
INDENTIN = " -=> "  # display arrow RIGHT
INDENTOUT = " <=- "  # display arrow LEFT
INFOSTR = f"""# * {"%_" * (CMNTLEN // 2)}"""  # INFO _STR_ line
IO_NAME = "newIO.py"
IOTOP_NAME = f"""{CONFIGDIR}IOTOP.py"""
LINESUP = lambda __NUM__: f"""{ESC}[{__NUM__}A"""
MARK1END = lambda __TAG__: f"""# {"⥣1 " * (CMNTLEN // 3)} {__TAG__}"""
MARK1ENDLN = lambda __TAG__: f"""# {"⥣1 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK1MID = lambda __TAG__: f"""# {"⥣1⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK1MIDLN = lambda __TAG__: f"""# {"⥣1⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK1START = lambda __TAG__: f"""# {"1⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK1STARTLN = lambda __TAG__: f"""# {"1⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK2END = lambda __TAG__: f"""# {"⥣2 " * (CMNTLEN // 3)} {__TAG__}"""
MARK2ENDLN = lambda __TAG__: f"""# {"⥣2 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK2MID = lambda __TAG__: f"""# {"⥣2⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK2MIDLN = lambda __TAG__: f"""# {"⥣2⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK2START = lambda __TAG__: f"""# {"2⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK2STARTLN = lambda __TAG__: f"""# {"2⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK3END = lambda __TAG__: f"""# {"⥣3 " * (CMNTLEN // 3)} {__TAG__}"""
MARK3ENDLN = lambda __TAG__: f"""# {"⥣3 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK3MID = lambda __TAG__: f"""# {"⥣3⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK3MIDLN = lambda __TAG__: f"""# {"⥣3⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK3START = lambda __TAG__: f"""# {"3⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK3STARTLN = lambda __TAG__: f"""# {"3⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK4END = lambda __TAG__: f"""# {"⥣4 " * (CMNTLEN // 3)} {__TAG__}"""
MARK4ENDLN = lambda __TAG__: f"""# {"⥣4 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK4MID = lambda __TAG__: f"""# {"⥣4⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK4MIDLN = lambda __TAG__: f"""# {"⥣4⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK4START = lambda __TAG__: f"""# {"4⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK4STARTLN = lambda __TAG__: f"""# {"4⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK5END = lambda __TAG__: f"""# {"⥣5 " * (CMNTLEN // 3)} {__TAG__}"""
MARK5ENDLN = lambda __TAG__: f"""# {"⥣5 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK5MID = lambda __TAG__: f"""# {"⥣5⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK5MIDLN = lambda __TAG__: f"""# {"⥣5⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK5START = lambda __TAG__: f"""# {"5⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK5STARTLN = lambda __TAG__: f"""# {"5⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK6END = lambda __TAG__: f"""# {"⥣6 " * (CMNTLEN // 3)} {__TAG__}"""
MARK6ENDLN = lambda __TAG__: f"""# {"⥣6 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK6MID = lambda __TAG__: f"""# {"⥣6⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK6MIDLN = lambda __TAG__: f"""# {"⥣6⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK6START = lambda __TAG__: f"""# {"6⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK6STARTLN = lambda __TAG__: f"""# {"6⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK7END = lambda __TAG__: f"""# {"⥣7 " * (CMNTLEN // 3)} {__TAG__}"""
MARK7ENDLN = lambda __TAG__: f"""# {"⥣7 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK7MID = lambda __TAG__: f"""# {"⥣7⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK7MIDLN = lambda __TAG__: f"""# {"⥣7⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK7START = lambda __TAG__: f"""# {"7⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK7STARTLN = lambda __TAG__: f"""# {"7⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK8END = lambda __TAG__: f"""# {"⥣8 " * (CMNTLEN // 3)} {__TAG__}"""
MARK8ENDLN = lambda __TAG__: f"""# {"⥣8 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK8MID = lambda __TAG__: f"""# {"⥣8⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK8MIDLN = lambda __TAG__: f"""# {"⥣8⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK8START = lambda __TAG__: f"""# {"8⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK8STARTLN = lambda __TAG__: f"""# {"8⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK9END = lambda __TAG__: f"""# {"⥣9 " * (CMNTLEN // 3)} {__TAG__}"""
MARK9ENDLN = lambda __TAG__: f"""# {"⥣9 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK9MID = lambda __TAG__: f"""# {"⥣9⥥ " * (CMNTLEN // 4)} {__TAG__}"""
MARK9MIDLN = lambda __TAG__: f"""# {"⥣9⥥ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK9START = lambda __TAG__: f"""# {"9⥥ " * (CMNTLEN // 3)} {__TAG__}"""
MARK9STARTLN = lambda __TAG__: f"""# {"9⥥ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARKLINES_NAME = f"""{CONFIGDIR}MARKLINES.py"""
MOVELEFT = lambda __NUM__: f"""{ESC}[{__NUM__}D"""
MOVETO = lambda __LN__, __COL__: f"""{ESC}[{__LN__};{__COL__}H"""
NCR = lambda __NUM__: f"""{CRSTR * __NUM__}"""
NNL = lambda __NUM__: f"""{NEWLINE * __NUM__}"""
NSPC = lambda __NUM__: f"""{SPCSTR * __NUM__}"""  # returns a string with __NUM__ SPC
NTAB = lambda __NUM__: f"""{TABSTR * __NUM__}"""  # returns a string with __NUM__ TAB
PSG_NAME = f"""newPSG.py"""
PSGTOP_NAME = f"""{CONFIGDIR}PSGTOP.py"""
QTSET = [DBLQT, SGLQT, BKQT]  # set of all quote characters
SCTN0102NAME = f"""{CONFIGDIR}SCTN0102.py"""
SCTNSNAME = f"""{CONFIGDIR}SCTNS.md"""
SERIALNUMBER = lambda __NUM__: f"""{(__NUM__ % 0XFFFFFFFF):08X}"""
SP_NAME = "newSP.py"
SPTOP_NAME = f"""{CONFIGDIR}SPTOP.py"""
TBGLST_NAME = "TBGLST.py"
USER_CACHE_URL = lambda __FILENAME__: f"""{USER_CACHE_DIR}{__FILENAME__}"""
USER_CONFIG_URL = lambda __FILENAME__: f"""{USER_CONFIG_DIR}{__FILENAME__}"""
VO_NAME = "newVO.py"
VOTOP_NAME = f"""{CONFIGDIR}VOTOP.py"""
WHIRLCOUNT = 0
WHIRLSTR = f"""-{BKSLSH}|/*"""


DAYMS = (60 * 60 * 24 * 1000)  # 86400000
DAYSECS = (60 * 60 * 24)  # 86400
HALFDAYSECS = (60 * 60 * 12)  # 43200
HALFHOURSECS = (60 * 30)  # 1800
HOURSECS = (60 * 60)  # 3600
MINUTESECS = 60 # 60
QUARTERDAYSECS = (60 * 60 * 6)
QUARTERHOURSECS = (60 * 15)  # 900
TIME995959 = (60 * 60 * 100)  # 360000


STR_SUBST_DICT = {
	"%CBRCE%": f"""{CBRCE}""",
	"%CBRKT%": f"""{CBRKT}""",
	"%CPAREN%": f"""{CPAREN}""",
	"%DQ%": f"""{DBLQT}""",
	"%FOLDLN1E%": f"""{FOLD1ENDHERELN}""",
	"%FOLDLN2E%": f"""{FOLD2ENDHERELN}""",
	"%FOLDLN3E%": f"""{FOLD3ENDHERELN}""",
	"%FOLDLN1S%": f"""{FOLD1STARTHERELN}""",
	"%FOLDLN2S%": f"""{FOLD2STARTHERELN}""",
	"%FOLDLN3S%": f"""{FOLD3STARTHERELN}""",
	"%FTQ%": f"""f{TRIQT}""",
	"%NEWLINE%": f"""{NEWLINE}""",
	"%OBRCE%": f"""{OBRCE}""",
	"%OBRKT%": f"""{OBRKT}""",
	"%OPAREN%": f"""{OPAREN}""",
	"%SQ%": f"""{SGLQT}""",
	"%TAB1%": f"""{NTAB(1)}""",
	"%TAB2%": f"""{NTAB(2)}""",
	"%TAB3%": f"""{NTAB(3)}""",
	"%TAB4%": f"""{NTAB(4)}""",
	"%TAB5%": f"""{NTAB(5)}""",
	"%TAB6%": f"""{NTAB(6)}""",
	"%TAB7%": f"""{NTAB(7)}""",
	"%TAB8%": f"""{NTAB(8)}""",
	"%TAB9%": f"""{NTAB(9)}""",
	"%TABA%": f"""{NTAB(10)}""",
	"%TQ%": f"""{TRIQT}""",
}


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
FMAXCF_SCTN0003_LAMBDA_DEF = "FMAXCF_SCTN0003_LAMBDA_DEF"  # define a lambda function <NAC><K_EVENT_NAME><lambda str>
FMAXCF_SCTN0003_TYPE_DEF = "FMAXCF_SCTN0003_TYPE_DEF"  # define a fake type used in the translation dict <NAC><K_EVENT_NAME><TYPE>
FMAXCF_SCTN0201_STR_DEF = "FMAXCF_SCTN0201_STR_DEF"  # define a STR in SCTN0201 <NAC><K_EVENT_NAME><str>
FMAXCF_SCTN0201_VAL_DEF = "FMAXCF_SCTN0201_VAL_DEF"  # define a VAL in SCTN0201 <NAC><K_EVENT_NAME><VAL>
FMAXCF_SCTN0202_OPTIONS_ADD_HELP_LINE = "FMAXCF_SCTN0202_OPTIONS_ADD_HELP_LINE"  # add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>
FMAXCF_SCTN0202_OPTIONS_STR_ADD = "FMAXCF_SCTN0202_OPTIONS_STR_ADD"  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
FMAXCF_SCTN0202_OPTIONS_VAL_ADD = "FMAXCF_SCTN0202_OPTIONS_VAL_ADD"  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD = "FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD"  # define a OPTNAME: 'str' in SCTN0202 <NAC><KEY><PARM><STRDEFAULT>
FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD = "FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD"  # define a OPTNAME: VAL in SCTN0202 <NAC><KEY><PARM><VALDEFAULT>
FMAXCF_SCTN0203_DICT_DEF = "FMAXCF_SCTN0203_DICT_DEF"  # define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>
FMAXCF_SCTN0203_DICT_VS_ADD = "FMAXCF_SCTN0203_DICT_VS_ADD"  # define a dict STR in SCTN203 <NAC><DICTNAME><STR>
FMAXCF_SCTN0203_DICT_VV_ADD = "FMAXCF_SCTN0203_DICT_VV_ADD"  # define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>
FMAXCF_SCTN0204_LIST_DEF = "FMAXCF_SCTN0204_LIST_DEF"  # define a list in SCTN204 <NAC><LISTNAME>
FMAXCF_SCTN0204_LIST_STR_ADD = "FMAXCF_SCTN0204_LIST_STR_ADD"  # define a list STR in SCTN204 <NAC><LISTNAME><STR>
FMAXCF_SCTN0204_LIST_VAL_ADD = "FMAXCF_SCTN0204_LIST_VAL_ADD"  # define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>
FMAXFM_SCTN0101_AX_DEF = "FMAXFM_SCTN0101_AX_DEF"  # define a new FM action <NAC>
FMAXFM_SCTN0102_STR_DEF = "FMAXFM_SCTN0102_STR_DEF"  # define a FM string <NAC><VALNAME><STR>
FMAXFM_SCTN0102_VAL_DEF = "FMAXFM_SCTN0102_VAL_DEF"  # define a FM _value_ <NAC><VALNAME><VAL>
FMAXFM_SCTN0103_DICT_DEF = "FMAXFM_SCTN0103_DICT_DEF"  # define a dict for FM <NAC>
FMAXFM_SCTN0104_LIST_DEF = "FMAXFM_SCTN0104_LIST_DEF"  # define a list in FM <NAC>
FMAXFM_SCTN0105_LDICT_DEF = "FMAXFM_SCTN0105_LDICT_DEF"  # define a dict for FM <NAC>
FMAXFM_SCTN0105_LDICT_VS_ADD = "FMAXFM_SCTN0105_LDICT_VS_ADD"  # define a dict for FM <NAC>
FMAXFM_SCTN0105_LDICT_VV_ADD = "FMAXFM_SCTN0105_LDICT_VV_ADD"  # define a dict for FM <NAC>
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
FMAXPSG_SCTN090C_APPDS_DEF = "FMAXPSG_SCTN090C_APPDS_DEF"  # add a nested dict holding all of the variables passed between PySimpleGUI and this app
FMAXPSG_SCTN090C_APPDS_DICT_DEF = "FMAXPSG_SCTN090C_APPDS_DICT_DEF"  # add a dict to the mainapp dict <NAC><DICTNAME
FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD = "FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD"  # add a string to a dict mainapp dict <NAC><DICTNAME><KEY><STR>
FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD = "FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD"  # add a value to a dict mainapp dict <NAC><DICTNAME><KEY><VAL>
FMAXPSG_SCTN090C_APPDS_VS_ADD = "FMAXPSG_SCTN090C_APPDS_VS_ADD"  # add a string to the mainapp dict <NAC><KEY><STR>
FMAXPSG_SCTN090C_APPDS_VV_ADD = "FMAXPSG_SCTN090C_APPDS_VV_ADD"  # add a value to the mainapp dict <NAC><KEY><VAL>
FMAXPSG_SCTN090D_FORMMAIN_DEF = "FMAXPSG_SCTN090D_FORMMAIN_DEF"  # define a frame <NAC><FRAMENAME><_WINDOW_><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)
FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD = "FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD"  # add a button to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090E_LAYOUT_CHECKBOX_ADD = "FMAXPSG_SCTN090E_LAYOUT_CHECKBOX_ADD"  # add a checkbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD = "FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD"  # add a column to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090E_LAYOUT_COMBO_ADD = "FMAXPSG_SCTN090E_LAYOUT_COMBO_ADD"  # add a combo to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090E_LAYOUT_DEF = "FMAXPSG_SCTN090E_LAYOUT_DEF"  # define a layout <NAC><LAYOUTNAME>
FMAXPSG_SCTN090E_LAYOUT_KEY_ADD = "FMAXPSG_SCTN090E_LAYOUT_KEY_ADD"  # add a key to a layout element 'key=' will be added automatically <NAC><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>
FMAXPSG_SCTN090E_LAYOUT_PACKEDPARM_ADD = "FMAXPSG_SCTN090E_LAYOUT_PACKEDPARM_ADD"  # add packedparms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD = "FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD"  # add parms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN090E_LAYOUT_RADIO_ADD = "FMAXPSG_SCTN090E_LAYOUT_RADIO_ADD"  # add a radio to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090E_LAYOUT_ROW_ADD = "FMAXPSG_SCTN090E_LAYOUT_ROW_ADD"  # add a row [] to a layout <NAC><LAYOUTNAME><ROWKEY><LEVEL>
FMAXPSG_SCTN090E_LAYOUT_SPIN_ADD = "FMAXPSG_SCTN090E_LAYOUT_SPIN_ADD"  # add a spinbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090E_LAYOUT_TEXT_ADD = "FMAXPSG_SCTN090E_LAYOUT_TEXT_ADD"  # add a text element to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN090F_WINDOW_DEF = "FMAXPSG_SCTN090F_WINDOW_DEF"  # define a window element <NAC><WINDOWNAME>
FMAXPSG_SCTN090F_WINDOW_STR_ADD = "FMAXPSG_SCTN090F_WINDOW_STR_ADD"  # add a str to the window element <NAC><WINDOWNAME><VALNAME><VAL>
FMAXPSG_SCTN090F_WINDOW_VAL_ADD = "FMAXPSG_SCTN090F_WINDOW_VAL_ADD"  # add a str to the window element <NAC><WINDOWNAME><VALNAME><VAL>
FMAXPSG_SCTN0910_DUBLT_SS_DEF = "FMAXPSG_SCTN0910_DUBLT_SS_DEF"  # define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0910_DUBLT_SV_DEF = "FMAXPSG_SCTN0910_DUBLT_SV_DEF"  # define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0910_DUBLT_VS_DEF = "FMAXPSG_SCTN0910_DUBLT_VS_DEF"  # define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0910_DUBLT_VV_DEF = "FMAXPSG_SCTN0910_DUBLT_VV_DEF"  # define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>
FMAXPSG_SCTN0910_STR_DEF = "FMAXPSG_SCTN0910_STR_DEF"  # define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0910_VAL_DEF = "FMAXPSG_SCTN0910_VAL_DEF"  # define a value in the second define section in PSG.py <NAC><VALNAME><VAL>
FMAXPSG_SCTN0911_COMBO_DEF = "FMAXPSG_SCTN0911_COMBO_DEF"  # define a combo box <NAC><COMBOBOXNAME>
FMAXPSG_SCTN0912_FRAMEELEMENT_DEF = "FMAXPSG_SCTN0912_FRAMEELEMENT_DEF"  # define a frame element <NAC><FENAME>
FMAXPSG_SCTN0913_RCMENU_DEF = "FMAXPSG_SCTN0913_RCMENU_DEF"  # define a right click menu <NAC><RCMENUNAME>
FMAXPSG_SCTN0913_RCMENU_VAL_ADD = "FMAXPSG_SCTN0913_RCMENU_VAL_ADD"  # define a right click menu <NAC><RCMENUNAME><VAL>
FMAXPSG_SCTN0914_FORMPOPUP_DEF = "FMAXPSG_SCTN0914_FORMPOPUP_DEF"  # define a frame <NAC><FRAMENAME><_WINDOW_><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)
FMAXPSG_SCTN0915_PUDLG_DEF = "FMAXPSG_SCTN0915_PUDLG_DEF"  # define a popup dialog <NAC><POPUPNAME><POPUPTYPE>
FMAXPSG_SCTN0915_PUDLG_DICT_STR_ADD = "FMAXPSG_SCTN0915_PUDLG_DICT_STR_ADD"  # add a str to a text element <NAC><POPUPNAME><KEY><VAL>
FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD = "FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD"  # add a val to a text element <NAC><POPUPNAME><KEY><VAL>
FMAXPSG_SCTN0915_PUDLG_LIST_STR_ADD = "FMAXPSG_SCTN0915_PUDLG_LIST_STR_ADD"  # add a str to a text element <NAC><POPUPNAME><KEY><VAL>
FMAXPSG_SCTN0915_PUDLG_LIST_VAL_ADD = "FMAXPSG_SCTN0915_PUDLG_LIST_VAL_ADD"  # add a val to a text element <NAC><POPUPNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_BTN_DEF = "FMAXPSG_SCTN09FF_CLASS_BTN_DEF"  # define a button <NAC><CLASSNAME><BTNNAME>
FMAXPSG_SCTN09FF_CLASS_BTN_STR_ADD = "FMAXPSG_SCTN09FF_CLASS_BTN_STR_ADD"  # add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_BTN_VAL_ADD = "FMAXPSG_SCTN09FF_CLASS_BTN_VAL_ADD"  # add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_CHECKBOX_DEF = "FMAXPSG_SCTN09FF_CLASS_CHECKBOX_DEF"  # define a checkbox <NAC><CLASSNAME><CHECKBOXNAME>
FMAXPSG_SCTN09FF_CLASS_CHECKBOX_PARM_ADD = "FMAXPSG_SCTN09FF_CLASS_CHECKBOX_PARM_ADD"  # add a parameter to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_CHECKBOX_STR_ADD = "FMAXPSG_SCTN09FF_CLASS_CHECKBOX_STR_ADD"  # add a str to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_CHECKBOX_VAL_ADD = "FMAXPSG_SCTN09FF_CLASS_CHECKBOX_VAL_ADD"  # add a val to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_COLUMN_BUTTON_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_BUTTON_ADD"  # add a button to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_COLUMN_CHECKBOX_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_CHECKBOX_ADD"  # add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_ADD"  # add a column to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_PARM_STR_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_PARM_STR_ADD"  # add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_PARM_VAL_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_PARM_VAL_ADD"  # add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_COLUMN_COMBO_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_COMBO_ADD"  # add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_COLUMN_DEF = "FMAXPSG_SCTN09FF_CLASS_COLUMN_DEF"  # define a column <NAC><CLASSNAME><COLUMNNAME>
FMAXPSG_SCTN09FF_CLASS_COLUMN_KEY_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_KEY_ADD"  # add a key to a column element 'key=' will be added automatically <NAC><CLASSNAME><COLUMNNAME><ROWKEY><ELEMENTKEY><VAL>
FMAXPSG_SCTN09FF_CLASS_COLUMN_PACKEDPARM_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_PACKEDPARM_ADD"  # add packedparms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD"  # add parms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN09FF_CLASS_COLUMN_RADIO_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_RADIO_ADD"  # add a radio to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD"  # add a row [] to a column <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL>
FMAXPSG_SCTN09FF_CLASS_COLUMN_SPIN_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_SPIN_ADD"  # add a spinbox to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD = "FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD"  # add a text element to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_COMBO_DEF = "FMAXPSG_SCTN09FF_CLASS_COMBO_DEF"  # define a combo box <NAC><COMBOBOXNAME>
FMAXPSG_SCTN09FF_CLASS_DEF = "FMAXPSG_SCTN09FF_CLASS_DEF"  # define a class <NAC><CLASSNAME>
FMAXPSG_SCTN09FF_CLASS_DICT_DEF = "FMAXPSG_SCTN09FF_CLASS_DICT_DEF"  # define a dict in PSG <NAC><CLASSNAME><DICTNAME>
FMAXPSG_SCTN09FF_CLASS_DICT_SS_ADD = "FMAXPSG_SCTN09FF_CLASS_DICT_SS_ADD"  # add a str-str to a dict <NAC><CLASSNAME><DICTNAME><STR><STR>
FMAXPSG_SCTN09FF_CLASS_DICT_SV_ADD = "FMAXPSG_SCTN09FF_CLASS_DICT_SV_ADD"  # add a str-val to a dict <NAC><CLASSNAME><DICTNAME><STR><VAL>
FMAXPSG_SCTN09FF_CLASS_DICT_VS_ADD = "FMAXPSG_SCTN09FF_CLASS_DICT_VS_ADD"  # add a str to a dict <NAC><CLASSNAME><DICTNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD = "FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD"  # add a val to a dict in PSG <NAC><CLASSNAME><DICTNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_DPD_DEF = "FMAXPSG_SCTN09FF_CLASS_DPD_DEF"  # define a DPD debugPrintDict in PSG <NAC><CLASSNAME><DPDNAME>
FMAXPSG_SCTN09FF_CLASS_DPD_VV_ADD = "FMAXPSG_SCTN09FF_CLASS_DPD_VV_ADD"  # add a val to a DPD debugPrintDict in PSG <NAC><CLASSNAME><DPDNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_FORMMAIN_DEF = "FMAXPSG_SCTN09FF_CLASS_FORMMAIN_DEF"  # define a class mainframe
FMAXPSG_SCTN09FF_CLASS_FORMPOPUP_DEF = "FMAXPSG_SCTN09FF_CLASS_FORMPOPUP_DEF"  # define a class mainframe
FMAXPSG_SCTN09FF_CLASS_FRAMEELEMENT_DEF = "FMAXPSG_SCTN09FF_CLASS_FRAMEELEMENT_DEF"  # define a frame element
FMAXPSG_SCTN09FF_CLASS_FUNCTION_BLANKLINE = "FMAXPSG_SCTN09FF_CLASS_FUNCTION_BLANKLINE"  # define a class <NAC><CLASSNAME><FUNCNAME><PARMS>
FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF = "FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF"  # define a class <NAC><CLASSNAME><FUNCNAME><PARMS>
FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE = "FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE"  # define a class <NAC><CLASSNAME><FUNCNAME><FILENAME>
FMAXPSG_SCTN09FF_CLASS_FUNCTION_LAMBDA1_DEF = "FMAXPSG_SCTN09FF_CLASS_FUNCTION_LAMBDA1_DEF"  # add a lambda to the top of a function, usually for absorbing things
FMAXPSG_SCTN09FF_CLASS_FUNCTION_LAMBDA2_DEF = "FMAXPSG_SCTN09FF_CLASS_FUNCTION_LAMBDA2_DEF"  # add a lambda to the top of a function, usually for absorbing things
FMAXPSG_SCTN09FF_CLASS_FUNCTION_LINE_ADD = "FMAXPSG_SCTN09FF_CLASS_FUNCTION_LINE_ADD"  # define a class <NAC><CLASSNAME><FUNCNAME><LINE>
FMAXPSG_SCTN09FF_CLASS_FUNCTION_READ_FROM_FILE = "FMAXPSG_SCTN09FF_CLASS_FUNCTION_READ_FROM_FILE"  # define a class <NAC><CLASSNAME><FUNCNAME><FILENAME>
FMAXPSG_SCTN09FF_CLASS_FUNCTION_STR1_DEF = "FMAXPSG_SCTN09FF_CLASS_FUNCTION_STR1_DEF"  # define a string in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_FUNCTION_STR2_DEF = "FMAXPSG_SCTN09FF_CLASS_FUNCTION_STR2_DEF"  # define a string in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_FUNCTION_VAL1_DEF = "FMAXPSG_SCTN09FF_CLASS_FUNCTION_VAL1_DEF"  # define a value in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_FUNCTION_VAL2_DEF = "FMAXPSG_SCTN09FF_CLASS_FUNCTION_VAL2_DEF"  # define a value in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LAMBDA = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LAMBDA"  # define a string in the class <NAC><CLASSNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LINE = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LINE"  # define a class <NAC><CLASSNAME><LINE>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_READ_FROM_FILE = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_READ_FROM_FILE"  # read a section of __init__ from a file in res/functions <NAC><CLASSNAME><FILENAME>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_STR = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_STR"  # define a string in the class <NAC><CLASSNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL"  # define a value in the class <NAC><CLASSNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_SS = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_SS"  # add a str-str to a dict <NAC><CLASSNAME><STR><STR>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_SV = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_SV"  # add a str-val to a dict <NAC><CLASSNAME><STR><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VS = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VS"  # add a str to a dict <NAC><CLASSNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV"  # add a val to a dict in PSG <NAC><CLASSNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY"  # add values to _KEY_DICT_, _KEY_DICT_REVERSE_ for external elements like buttons and checkboxes <NAC><CLASSNAME><KEY>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_LAMBDA = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_LAMBDA"  # define a value in the class <NAC><CLASSNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_LINE = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_LINE"  # define a class <NAC><CLASSNAME><LINE>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_READ_FROM_FILE = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_READ_FROM_FILE"  # read a section of __init__ from a file in res/functions <NAC><CLASSNAME><FILENAME>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_STR = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_STR"  # define a string in the class <NAC><CLASSNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL"  # define a value in the class <NAC><CLASSNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE = "FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE"  # define a class <NAC><CLASSNAME><LINE>
FMAXPSG_SCTN09FF_CLASS_INIT_DEF = "FMAXPSG_SCTN09FF_CLASS_INIT_DEF"  # define a class <NAC><CLASSNAME><PARMS>
FMAXPSG_SCTN09FF_CLASS_LAYOUT_BUTTON_ADD = "FMAXPSG_SCTN09FF_CLASS_LAYOUT_BUTTON_ADD"  # add a button to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_LAYOUT_CHECKBOX_ADD = "FMAXPSG_SCTN09FF_CLASS_LAYOUT_CHECKBOX_ADD"  # add a checkbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_LAYOUT_COLUMN_ADD = "FMAXPSG_SCTN09FF_CLASS_LAYOUT_COLUMN_ADD"  # add a column to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_LAYOUT_COMBO_ADD = "FMAXPSG_SCTN09FF_CLASS_LAYOUT_COMBO_ADD"  # add a combo to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_LAYOUT_DEF = "FMAXPSG_SCTN09FF_CLASS_LAYOUT_DEF"  # define layouts
FMAXPSG_SCTN09FF_CLASS_LAYOUT_KEY_ADD = "FMAXPSG_SCTN09FF_CLASS_LAYOUT_KEY_ADD"  # add a key to a layout element 'key=' will be added automatically <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>
FMAXPSG_SCTN09FF_CLASS_LAYOUT_PACKEDPARM_ADD = "FMAXPSG_SCTN09FF_CLASS_LAYOUT_PACKEDPARM_ADD"  # add packedparms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD = "FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD"  # add parms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
FMAXPSG_SCTN09FF_CLASS_LAYOUT_RADIO_ADD = "FMAXPSG_SCTN09FF_CLASS_LAYOUT_RADIO_ADD"  # add a radio to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_LAYOUT_ROW_ADD = "FMAXPSG_SCTN09FF_CLASS_LAYOUT_ROW_ADD"  # add a row [] to a layout <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL>
FMAXPSG_SCTN09FF_CLASS_LAYOUT_SPIN_ADD = "FMAXPSG_SCTN09FF_CLASS_LAYOUT_SPIN_ADD"  # add a spinbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_LAYOUT_TEXT_ADD = "FMAXPSG_SCTN09FF_CLASS_LAYOUT_TEXT_ADD"  # add a text element to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
FMAXPSG_SCTN09FF_CLASS_LIST_DEF = "FMAXPSG_SCTN09FF_CLASS_LIST_DEF"  # define a list in PSG <NAC><CLASSNAME><LISTNAME>
FMAXPSG_SCTN09FF_CLASS_LIST_STR_ADD = "FMAXPSG_SCTN09FF_CLASS_LIST_STR_ADD"  # add a str to a list in PSG <NAC><CLASSNAME><LISTNAME><STR>
FMAXPSG_SCTN09FF_CLASS_LIST_VAL_ADD = "FMAXPSG_SCTN09FF_CLASS_LIST_VAL_ADD"  # add a val to a list in PSG <NAC><CLASSNAME><LISTNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_RADIO_DEF = "FMAXPSG_SCTN09FF_CLASS_RADIO_DEF"  # define a radio button element
FMAXPSG_SCTN09FF_CLASS_RCMENU_DEF = "FMAXPSG_SCTN09FF_CLASS_RCMENU_DEF"  # define a right click menu
FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD = "FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD"  # define a right click menu
FMAXPSG_SCTN09FF_CLASS_SPIN_DEF = "FMAXPSG_SCTN09FF_CLASS_SPIN_DEF"  # define a spin box entry <NAC><CLASSNAME><SPINNAME>
FMAXPSG_SCTN09FF_CLASS_SPIN_DICT_VS_ADD = "FMAXPSG_SCTN09FF_CLASS_SPIN_DICT_VS_ADD"  # add a STR to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><STR>
FMAXPSG_SCTN09FF_CLASS_SPIN_DICT_VV_ADD = "FMAXPSG_SCTN09FF_CLASS_SPIN_DICT_VV_ADD"  # add a VAL to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_SPIN_LIST_STR_ADD = "FMAXPSG_SCTN09FF_CLASS_SPIN_LIST_STR_ADD"  # add a STR to the values list <NAC><CLASSNAME><SPINNAME><STR>
FMAXPSG_SCTN09FF_CLASS_SPIN_LIST_VAL_ADD = "FMAXPSG_SCTN09FF_CLASS_SPIN_LIST_VAL_ADD"  # add a VAL to the values list <NAC><CLASSNAME><SPINNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_TEXT_DEF = "FMAXPSG_SCTN09FF_CLASS_TEXT_DEF"  # define a text <NAC><CLASSNAME><TEXTNAME><ISATIME>
FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD = "FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD"  # add a PARM to a text element <NAC><CLASSNAME><TEXTNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_TEXT_STR_ADD = "FMAXPSG_SCTN09FF_CLASS_TEXT_STR_ADD"  # add a str to a text element <NAC><CLASSNAME><TEXTNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD = "FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD"  # add a val to a text element <NAC><CLASSNAME><TEXTNAME>
FMAXPSG_SCTN09FF_CLASS_WINDOW_DEF = "FMAXPSG_SCTN09FF_CLASS_WINDOW_DEF"  # define a main dictdict <NAC><CLASSNAME><MAINNAME>
FMAXPSG_SCTN09FF_CLASS_WINDOW_STR_ADD = "FMAXPSG_SCTN09FF_CLASS_WINDOW_STR_ADD"  # add a str to the main dictdict
FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD = "FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD"  # add a str to the main dictdict


FMAXFM_AXLST = [
	FMAX_NOP,  # skip this entry
	FMAXCF_SCTN0003_LAMBDA_DEF,  # define a lambda function <NAC><K_EVENT_NAME><lambda str>
	FMAXCF_SCTN0003_TYPE_DEF,  # define a fake type used in the translation dict <NAC><K_EVENT_NAME><TYPE>
	FMAXCF_SCTN0201_STR_DEF,  # define a STR in SCTN0201 <NAC><K_EVENT_NAME><str>
	FMAXCF_SCTN0201_VAL_DEF,  # define a VAL in SCTN0201 <NAC><K_EVENT_NAME><VAL>
	FMAXCF_SCTN0202_OPTIONS_ADD_HELP_LINE,  # add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>
	FMAXCF_SCTN0202_OPTIONS_STR_ADD,  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
	FMAXCF_SCTN0202_OPTIONS_VAL_ADD,  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
	FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD,  # define a OPTNAME: 'str' in SCTN0202 <NAC><KEY><PARM><STRDEFAULT>
	FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD,  # define a OPTNAME: VAL in SCTN0202 <NAC><KEY><PARM><VALDEFAULT>
	FMAXCF_SCTN0203_DICT_DEF,  # define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>
	FMAXCF_SCTN0203_DICT_VS_ADD,  # define a dict STR in SCTN203 <NAC><DICTNAME><STR>
	FMAXCF_SCTN0203_DICT_VV_ADD,  # define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>
	FMAXCF_SCTN0204_LIST_DEF,  # define a list in SCTN204 <NAC><LISTNAME>
	FMAXCF_SCTN0204_LIST_STR_ADD,  # define a list STR in SCTN204 <NAC><LISTNAME><STR>
	FMAXCF_SCTN0204_LIST_VAL_ADD,  # define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>
	FMAXFM_SCTN0101_AX_DEF,  # define a new FM action <NAC>
	FMAXFM_SCTN0102_STR_DEF,  # define a FM string <NAC><VALNAME><STR>
	FMAXFM_SCTN0102_VAL_DEF,  # define a FM _value_ <NAC><VALNAME><VAL>
	FMAXFM_SCTN0103_DICT_DEF,  # define a dict for FM <NAC>
	FMAXFM_SCTN0104_LIST_DEF,  # define a list in FM <NAC>
	FMAXFM_SCTN0105_LDICT_DEF,  # define a dict for FM <NAC>
	FMAXFM_SCTN0105_LDICT_VS_ADD,  # define a dict for FM <NAC>
	FMAXFM_SCTN0105_LDICT_VV_ADD,  # define a dict for FM <NAC>
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
	FMAXPSG_SCTN090C_APPDS_DEF,  # add a nested dict holding all of the variables passed between PySimpleGUI and this app
	FMAXPSG_SCTN090C_APPDS_DICT_DEF,  # add a dict to the mainapp dict <NAC><DICTNAME
	FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD,  # add a string to a dict mainapp dict <NAC><DICTNAME><KEY><STR>
	FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD,  # add a value to a dict mainapp dict <NAC><DICTNAME><KEY><VAL>
	FMAXPSG_SCTN090C_APPDS_VS_ADD,  # add a string to the mainapp dict <NAC><KEY><STR>
	FMAXPSG_SCTN090C_APPDS_VV_ADD,  # add a value to the mainapp dict <NAC><KEY><VAL>
	FMAXPSG_SCTN090D_FORMMAIN_DEF,  # define a frame <NAC><FRAMENAME><_WINDOW_><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)
	FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD,  # add a button to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090E_LAYOUT_CHECKBOX_ADD,  # add a checkbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD,  # add a column to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090E_LAYOUT_COMBO_ADD,  # add a combo to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090E_LAYOUT_DEF,  # define a layout <NAC><LAYOUTNAME>
	FMAXPSG_SCTN090E_LAYOUT_KEY_ADD,  # add a key to a layout element 'key=' will be added automatically <NAC><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>
	FMAXPSG_SCTN090E_LAYOUT_PACKEDPARM_ADD,  # add packedparms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD,  # add parms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN090E_LAYOUT_RADIO_ADD,  # add a radio to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090E_LAYOUT_ROW_ADD,  # add a row [] to a layout <NAC><LAYOUTNAME><ROWKEY><LEVEL>
	FMAXPSG_SCTN090E_LAYOUT_SPIN_ADD,  # add a spinbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090E_LAYOUT_TEXT_ADD,  # add a text element to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN090F_WINDOW_DEF,  # define a window element <NAC><WINDOWNAME>
	FMAXPSG_SCTN090F_WINDOW_STR_ADD,  # add a str to the window element <NAC><WINDOWNAME><VALNAME><VAL>
	FMAXPSG_SCTN090F_WINDOW_VAL_ADD,  # add a str to the window element <NAC><WINDOWNAME><VALNAME><VAL>
	FMAXPSG_SCTN0910_DUBLT_SS_DEF,  # define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0910_DUBLT_SV_DEF,  # define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0910_DUBLT_VS_DEF,  # define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0910_DUBLT_VV_DEF,  # define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>
	FMAXPSG_SCTN0910_STR_DEF,  # define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0910_VAL_DEF,  # define a value in the second define section in PSG.py <NAC><VALNAME><VAL>
	FMAXPSG_SCTN0911_COMBO_DEF,  # define a combo box <NAC><COMBOBOXNAME>
	FMAXPSG_SCTN0912_FRAMEELEMENT_DEF,  # define a frame element <NAC><FENAME>
	FMAXPSG_SCTN0913_RCMENU_DEF,  # define a right click menu <NAC><RCMENUNAME>
	FMAXPSG_SCTN0913_RCMENU_VAL_ADD,  # define a right click menu <NAC><RCMENUNAME><VAL>
	FMAXPSG_SCTN0914_FORMPOPUP_DEF,  # define a frame <NAC><FRAMENAME><_WINDOW_><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)
	FMAXPSG_SCTN0915_PUDLG_DEF,  # define a popup dialog <NAC><POPUPNAME><POPUPTYPE>
	FMAXPSG_SCTN0915_PUDLG_DICT_STR_ADD,  # add a str to a text element <NAC><POPUPNAME><KEY><VAL>
	FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD,  # add a val to a text element <NAC><POPUPNAME><KEY><VAL>
	FMAXPSG_SCTN0915_PUDLG_LIST_STR_ADD,  # add a str to a text element <NAC><POPUPNAME><KEY><VAL>
	FMAXPSG_SCTN0915_PUDLG_LIST_VAL_ADD,  # add a val to a text element <NAC><POPUPNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_BTN_DEF,  # define a button <NAC><CLASSNAME><BTNNAME>
	FMAXPSG_SCTN09FF_CLASS_BTN_STR_ADD,  # add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_BTN_VAL_ADD,  # add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_CHECKBOX_DEF,  # define a checkbox <NAC><CLASSNAME><CHECKBOXNAME>
	FMAXPSG_SCTN09FF_CLASS_CHECKBOX_PARM_ADD,  # add a parameter to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_CHECKBOX_STR_ADD,  # add a str to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_CHECKBOX_VAL_ADD,  # add a val to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_BUTTON_ADD,  # add a button to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_CHECKBOX_ADD,  # add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_ADD,  # add a column to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_PARM_STR_ADD,  # add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_PARM_VAL_ADD,  # add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_COMBO_ADD,  # add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_DEF,  # define a column <NAC><CLASSNAME><COLUMNNAME>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_KEY_ADD,  # add a key to a column element 'key=' will be added automatically <NAC><CLASSNAME><COLUMNNAME><ROWKEY><ELEMENTKEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_PACKEDPARM_ADD,  # add packedparms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD,  # add parms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_RADIO_ADD,  # add a radio to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD,  # add a row [] to a column <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_SPIN_ADD,  # add a spinbox to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD,  # add a text element to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_COMBO_DEF,  # define a combo box <NAC><COMBOBOXNAME>
	FMAXPSG_SCTN09FF_CLASS_DEF,  # define a class <NAC><CLASSNAME>
	FMAXPSG_SCTN09FF_CLASS_DICT_DEF,  # define a dict in PSG <NAC><CLASSNAME><DICTNAME>
	FMAXPSG_SCTN09FF_CLASS_DICT_SS_ADD,  # add a str-str to a dict <NAC><CLASSNAME><DICTNAME><STR><STR>
	FMAXPSG_SCTN09FF_CLASS_DICT_SV_ADD,  # add a str-val to a dict <NAC><CLASSNAME><DICTNAME><STR><VAL>
	FMAXPSG_SCTN09FF_CLASS_DICT_VS_ADD,  # add a str to a dict <NAC><CLASSNAME><DICTNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD,  # add a val to a dict in PSG <NAC><CLASSNAME><DICTNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_DPD_DEF,  # define a DPD debugPrintDict in PSG <NAC><CLASSNAME><DPDNAME>
	FMAXPSG_SCTN09FF_CLASS_DPD_VV_ADD,  # add a val to a DPD debugPrintDict in PSG <NAC><CLASSNAME><DPDNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_FORMMAIN_DEF,  # define a class mainframe
	FMAXPSG_SCTN09FF_CLASS_FORMPOPUP_DEF,  # define a class mainframe
	FMAXPSG_SCTN09FF_CLASS_FRAMEELEMENT_DEF,  # define a frame element
	FMAXPSG_SCTN09FF_CLASS_FUNCTION_BLANKLINE,  # define a class <NAC><CLASSNAME><FUNCNAME><PARMS>
	FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF,  # define a class <NAC><CLASSNAME><FUNCNAME><PARMS>
	FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE,  # define a class <NAC><CLASSNAME><FUNCNAME><FILENAME>
	FMAXPSG_SCTN09FF_CLASS_FUNCTION_LAMBDA1_DEF,  # add a lambda to the top of a function, usually for absorbing things
	FMAXPSG_SCTN09FF_CLASS_FUNCTION_LAMBDA2_DEF,  # add a lambda to the top of a function, usually for absorbing things
	FMAXPSG_SCTN09FF_CLASS_FUNCTION_LINE_ADD,  # define a class <NAC><CLASSNAME><FUNCNAME><LINE>
	FMAXPSG_SCTN09FF_CLASS_FUNCTION_READ_FROM_FILE,  # define a class <NAC><CLASSNAME><FUNCNAME><FILENAME>
	FMAXPSG_SCTN09FF_CLASS_FUNCTION_STR1_DEF,  # define a string in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_FUNCTION_STR2_DEF,  # define a string in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_FUNCTION_VAL1_DEF,  # define a value in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_FUNCTION_VAL2_DEF,  # define a value in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LAMBDA,  # define a string in the class <NAC><CLASSNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LINE,  # define a class <NAC><CLASSNAME><LINE>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_READ_FROM_FILE,  # read a section of __init__ from a file in res/functions <NAC><CLASSNAME><FILENAME>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_STR,  # define a string in the class <NAC><CLASSNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL,  # define a value in the class <NAC><CLASSNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_SS,  # add a str-str to a dict <NAC><CLASSNAME><STR><STR>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_SV,  # add a str-val to a dict <NAC><CLASSNAME><STR><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VS,  # add a str to a dict <NAC><CLASSNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV,  # add a val to a dict in PSG <NAC><CLASSNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY,  # add values to _KEY_DICT_, _KEY_DICT_REVERSE_ for external elements like buttons and checkboxes <NAC><CLASSNAME><KEY>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_LAMBDA,  # define a value in the class <NAC><CLASSNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_LINE,  # define a class <NAC><CLASSNAME><LINE>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_READ_FROM_FILE,  # read a section of __init__ from a file in res/functions <NAC><CLASSNAME><FILENAME>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_STR,  # define a string in the class <NAC><CLASSNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL,  # define a value in the class <NAC><CLASSNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE,  # define a class <NAC><CLASSNAME><LINE>
	FMAXPSG_SCTN09FF_CLASS_INIT_DEF,  # define a class <NAC><CLASSNAME><PARMS>
	FMAXPSG_SCTN09FF_CLASS_LAYOUT_BUTTON_ADD,  # add a button to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_LAYOUT_CHECKBOX_ADD,  # add a checkbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_LAYOUT_COLUMN_ADD,  # add a column to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_LAYOUT_COMBO_ADD,  # add a combo to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_LAYOUT_DEF,  # define layouts
	FMAXPSG_SCTN09FF_CLASS_LAYOUT_KEY_ADD,  # add a key to a layout element 'key=' will be added automatically <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_LAYOUT_PACKEDPARM_ADD,  # add packedparms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD,  # add parms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_LAYOUT_RADIO_ADD,  # add a radio to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_LAYOUT_ROW_ADD,  # add a row [] to a layout <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL>
	FMAXPSG_SCTN09FF_CLASS_LAYOUT_SPIN_ADD,  # add a spinbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_LAYOUT_TEXT_ADD,  # add a text element to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>
	FMAXPSG_SCTN09FF_CLASS_LIST_DEF,  # define a list in PSG <NAC><CLASSNAME><LISTNAME>
	FMAXPSG_SCTN09FF_CLASS_LIST_STR_ADD,  # add a str to a list in PSG <NAC><CLASSNAME><LISTNAME><STR>
	FMAXPSG_SCTN09FF_CLASS_LIST_VAL_ADD,  # add a val to a list in PSG <NAC><CLASSNAME><LISTNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_RADIO_DEF,  # define a radio button element
	FMAXPSG_SCTN09FF_CLASS_RCMENU_DEF,  # define a right click menu
	FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD,  # define a right click menu
	FMAXPSG_SCTN09FF_CLASS_SPIN_DEF,  # define a spin box entry <NAC><CLASSNAME><SPINNAME>
	FMAXPSG_SCTN09FF_CLASS_SPIN_DICT_VS_ADD,  # add a STR to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><STR>
	FMAXPSG_SCTN09FF_CLASS_SPIN_DICT_VV_ADD,  # add a VAL to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_SPIN_LIST_STR_ADD,  # add a STR to the values list <NAC><CLASSNAME><SPINNAME><STR>
	FMAXPSG_SCTN09FF_CLASS_SPIN_LIST_VAL_ADD,  # add a VAL to the values list <NAC><CLASSNAME><SPINNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_TEXT_DEF,  # define a text <NAC><CLASSNAME><TEXTNAME><ISATIME>
	FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD,  # add a PARM to a text element <NAC><CLASSNAME><TEXTNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_TEXT_STR_ADD,  # add a str to a text element <NAC><CLASSNAME><TEXTNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD,  # add a val to a text element <NAC><CLASSNAME><TEXTNAME>
	FMAXPSG_SCTN09FF_CLASS_WINDOW_DEF,  # define a main dictdict <NAC><CLASSNAME><MAINNAME>
	FMAXPSG_SCTN09FF_CLASS_WINDOW_STR_ADD,  # add a str to the main dictdict
	FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD,  # add a str to the main dictdict
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
FMFM_SCTN0105_LDICT_CMNT_DICT = {}  # SCTN105 ldict defined
FMFM_SCTN0105_LDICT_DICT = {}  # SCTN105 ldict defined
FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN0900_DEF1_CMNT_DICT = {}  #
FMPSG_SCTN0900_DEF1_DICT = {}  #
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
FMPSG_SCTN0906_BTNS_CMNT_DICT = {}  #
FMPSG_SCTN0906_BTNS_DICT = {}  #
FMPSG_SCTN0907_SPIN_CMNT_DICT = {}  # holds the spin element stuffs (TUPDICT)f
FMPSG_SCTN0907_SPIN_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN0908_CHECKBOX_CMNT_DICT = {}  #
FMPSG_SCTN0908_CHECKBOX_DICT = {}  #
FMPSG_SCTN0909_TEXT_CMNT_DICT = {}  #
FMPSG_SCTN0909_TEXT_DICT = {}  #
FMPSG_SCTN090A_RADIO_CMNT_DICT = {}  #
FMPSG_SCTN090A_RADIO_DICT = {}  #
FMPSG_SCTN090B_COLUMN_CMNT_DICT = {}  #
FMPSG_SCTN090B_COLUMN_DICT = {}  #
FMPSG_SCTN090B_COLUMN_PARMS_DICT = {}  #
FMPSG_SCTN090C_APPDS_CMNT_DICT = {}  # the main app dict for this app
FMPSG_SCTN090C_APPDS_DICT = {}  # the main app dict for this app
FMPSG_SCTN090C_APPDSDICT_DICT = {}  # the main app dict+dict for this app
FMPSG_SCTN090D_FORMMAIN_CMNT_DICT = {}  #
FMPSG_SCTN090D_FORMMAIN_DICT = {}  #
FMPSG_SCTN090E_LAYOUT_CMNT_DICT = {}  #
FMPSG_SCTN090E_LAYOUT_DICT = {}  #
FMPSG_SCTN090F_WINDOW_CMNT_DICT = {}  #
FMPSG_SCTN090F_WINDOW_DICT = {}  #
FMPSG_SCTN0910_DEF3_CMNT_DICT = {}  #
FMPSG_SCTN0910_DEF3_DICT = {}  #
FMPSG_SCTN0911_COMBO_CMNT_DICT = {}  #
FMPSG_SCTN0911_COMBO_DICT = {}  #
FMPSG_SCTN0912_FRAME_CMNT_DICT = {}  #
FMPSG_SCTN0912_FRAME_DICT = {}  #
FMPSG_SCTN0913_RCMENU_CMNT_DICT = {}  #
FMPSG_SCTN0913_RCMENU_DICT = {}  #
FMPSG_SCTN0914_FORMPOPUP_CMNT_DICT = {}  #
FMPSG_SCTN0914_FORMPOPUP_DICT = {}  #
FMPSG_SCTN0915_PUDLG_CMNT_DICT = {}  #
FMPSG_SCTN0915_PUDLG_DICT_DICT = {}  #
FMPSG_SCTN0915_PUDLG_LIST_DICT = {}  #
FMPSG_SCTN0915_PUDLG_TYPE_DICT = {}  #
FMPSG_SCTN09FF_CLASS_BTNS_ADDON_DICT = {}  #
FMPSG_SCTN09FF_CLASS_BTNS_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_BTNS_DICT = {}  #
FMPSG_SCTN09FF_CLASS_CDS_DICT = {}  # class data storage
FMPSG_SCTN09FF_CLASS_CHECKBOX_ADDON_DICT = {}  #
FMPSG_SCTN09FF_CLASS_CHECKBOX_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT = {}  #
FMPSG_SCTN09FF_CLASS_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_COLUMN_ADDON_DICT = {}  #
FMPSG_SCTN09FF_CLASS_COLUMN_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_COLUMN_DICT = {}  #
FMPSG_SCTN09FF_CLASS_COLUMN_PARMS_DICT = {}  #
FMPSG_SCTN09FF_CLASS_COMBO_ADDON_DICT = {}  #
FMPSG_SCTN09FF_CLASS_COMBO_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_COMBO_DICT = {}  #
FMPSG_SCTN09FF_CLASS_DEF_DICT = {}  # str and val defines in a class
FMPSG_SCTN09FF_CLASS_DICT = {}  #
FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_DICT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_FRAME_ADDON_DICT = {}  #
FMPSG_SCTN09FF_CLASS_FRAME_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_FRAME_DICT = {}  #
FMPSG_SCTN09FF_CLASS_FUNCTION_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_FUNCTION_DEF1_DICT = {}  #
FMPSG_SCTN09FF_CLASS_FUNCTION_DEF2_DICT = {}  #
FMPSG_SCTN09FF_CLASS_FUNCTION_DICT = {}  #
FMPSG_SCTN09FF_CLASS_INIT_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT = {}  #
FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT = {}  #
FMPSG_SCTN09FF_CLASS_INIT_DEF3_DICT = {}  #
FMPSG_SCTN09FF_CLASS_INIT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT = {}  #
FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT = {}  #
FMPSG_SCTN09FF_CLASS_LAYOUT_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_LAYOUT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_LIST_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_LIST_DICT = {}  #
FMPSG_SCTN09FF_CLASS_RADIO_ADDON_DICT = {}  #
FMPSG_SCTN09FF_CLASS_RADIO_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_RADIO_DICT = {}  #
FMPSG_SCTN09FF_CLASS_RCMENU_ADDON_DICT = {}  #
FMPSG_SCTN09FF_CLASS_RCMENU_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_RCMENU_DICT = {}  #
FMPSG_SCTN09FF_CLASS_SPIN_ADDON_DICT = {}  #
FMPSG_SCTN09FF_CLASS_SPIN_CMNT_DICT = {}  # holds the spin element stuffs (TUPDICT)f
FMPSG_SCTN09FF_CLASS_SPIN_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT = {}  #
FMPSG_SCTN09FF_CLASS_TEXT_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_TEXT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_WINDOW_CMNT_DICT = {}  #
FMPSG_SCTN09FF_CLASS_WINDOW_DICT = {}  #


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
	("FMAXCF_SCTN0003_LAMBDA_DEF", FMAXFM_SCTN0101_AX_DEF, "define a lambda function <NAC><K_EVENT_NAME><lambda str>",),
	("FMAXCF_SCTN0003_TYPE_DEF", FMAXFM_SCTN0101_AX_DEF, "define a fake type used in the translation dict <NAC><K_EVENT_NAME><TYPE>",),
	("FMAXCF_SCTN0201_STR_DEF", FMAXFM_SCTN0101_AX_DEF, "define a STR in SCTN0201 <NAC><K_EVENT_NAME><str>",),
	("FMAXCF_SCTN0201_VAL_DEF", FMAXFM_SCTN0101_AX_DEF, "define a VAL in SCTN0201 <NAC><K_EVENT_NAME><VAL>",),
	("FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "define a OPTNAME: 'str' in SCTN0202 <NAC><KEY><PARM><STRDEFAULT>",),
	("FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a OPTNAME: VAL in SCTN0202 <NAC><KEY><PARM><VALDEFAULT>",),
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
	("FMAXFM_SCTN0102_VAL_DEF", FMAXFM_SCTN0101_AX_DEF, "define a FM _value_ <NAC><VALNAME><VAL>",),
	("FMAXFM_SCTN0103_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a dict for FM <NAC>",),
	("FMAXFM_SCTN0104_LIST_DEF", FMAXFM_SCTN0101_AX_DEF, "define a list in FM <NAC>",),
	("FMAXFM_SCTN0105_LDICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a dict for FM <NAC>",),
	("FMAXFM_SCTN0105_LDICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "define a dict for FM <NAC>",),
	("FMAXFM_SCTN0105_LDICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "define a dict for FM <NAC>",),
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
	("FMAXPSG_SCTN090C_APPDS_DEF", FMAXFM_SCTN0101_AX_DEF, "add a nested dict holding all of the variables passed between PySimpleGUI and this app",),
	("FMAXPSG_SCTN090C_APPDS_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "add a dict to the mainapp dict <NAC><DICTNAME",),
	("FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a string to a dict mainapp dict <NAC><DICTNAME><KEY><STR>",),
	("FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to a dict mainapp dict <NAC><DICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN090C_APPDS_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a string to the mainapp dict <NAC><KEY><STR>",),
	("FMAXPSG_SCTN090C_APPDS_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a value to the mainapp dict <NAC><KEY><VAL>",),
	("FMAXPSG_SCTN090D_FORMMAIN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a frame <NAC><FRAMENAME><_WINDOW_><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)",),
	("FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD", FMAXFM_SCTN0101_AX_DEF, "add a button to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090E_LAYOUT_CHECKBOX_ADD", FMAXFM_SCTN0101_AX_DEF, "add a checkbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090E_LAYOUT_COMBO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090E_LAYOUT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a layout <NAC><LAYOUTNAME>",),
	("FMAXPSG_SCTN090E_LAYOUT_KEY_ADD", FMAXFM_SCTN0101_AX_DEF, "add a key to a layout element 'key=' will be added automatically <NAC><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN090E_LAYOUT_PACKEDPARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add packedparms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add parms to a layout entry <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN090E_LAYOUT_RADIO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a radio to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090E_LAYOUT_ROW_ADD", FMAXFM_SCTN0101_AX_DEF, "add a row [] to a layout <NAC><LAYOUTNAME><ROWKEY><LEVEL>",),
	("FMAXPSG_SCTN090E_LAYOUT_SPIN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a spinbox to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090E_LAYOUT_TEXT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a text element to a row <NAC><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN090F_WINDOW_DEF", FMAXFM_SCTN0101_AX_DEF, "define a window element <NAC><WINDOWNAME>",),
	("FMAXPSG_SCTN090F_WINDOW_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the window element <NAC><WINDOWNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN090F_WINDOW_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the window element <NAC><WINDOWNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN0910_DUBLT_SS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>",),
	("FMAXPSG_SCTN0910_DUBLT_SV_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>",),
	("FMAXPSG_SCTN0910_DUBLT_VS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>",),
	("FMAXPSG_SCTN0910_DUBLT_VV_DEF", FMAXFM_SCTN0101_AX_DEF, "define a (x,y) tuple <NAC><DUBTUPNAME><VAL1><VAL2>",),
	("FMAXPSG_SCTN0910_STR_DEF", FMAXFM_SCTN0101_AX_DEF, "define a string in the second section of defines in PSG.py <NAC><VALNAME><VAL>",),
	("FMAXPSG_SCTN0910_VAL_DEF", FMAXFM_SCTN0101_AX_DEF, "define a value in the second define section in PSG.py <NAC><VALNAME><VAL>",),
	("FMAXPSG_SCTN0911_COMBO_DEF", FMAXFM_SCTN0101_AX_DEF, "define a combo box <NAC><COMBOBOXNAME>",),
	("FMAXPSG_SCTN0912_FRAMEELEMENT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a frame element <NAC><FENAME>",),
	("FMAXPSG_SCTN0913_RCMENU_DEF", FMAXFM_SCTN0101_AX_DEF, "define a right click menu <NAC><RCMENUNAME>",),
	("FMAXPSG_SCTN0913_RCMENU_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a right click menu <NAC><RCMENUNAME><VAL>",),
	("FMAXPSG_SCTN0914_FORMPOPUP_DEF", FMAXFM_SCTN0101_AX_DEF, "define a frame <NAC><FRAMENAME><_WINDOW_><FINALIZEBOOL> (** added automatically bool adds or not chained finalize() call)",),
	("FMAXPSG_SCTN0915_PUDLG_DEF", FMAXFM_SCTN0101_AX_DEF, "define a popup dialog <NAC><POPUPNAME><POPUPTYPE>",),
	("FMAXPSG_SCTN0915_PUDLG_DICT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a text element <NAC><POPUPNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0915_PUDLG_DICT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a text element <NAC><POPUPNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0915_PUDLG_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a text element <NAC><POPUPNAME><KEY><VAL>",),
	("FMAXPSG_SCTN0915_PUDLG_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a text element <NAC><POPUPNAME><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_BTN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a button <NAC><CLASSNAME><BTNNAME>",),
	("FMAXPSG_SCTN09FF_CLASS_BTN_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_BTN_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a (VAL,VAL) to a tupdict <NAC><CLASSNAME><BTNNAME><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_CHECKBOX_DEF", FMAXFM_SCTN0101_AX_DEF, "define a checkbox <NAC><CLASSNAME><CHECKBOXNAME>",),
	("FMAXPSG_SCTN09FF_CLASS_CHECKBOX_PARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add a parameter to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_CHECKBOX_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_CHECKBOX_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a checkbox <NAC><CLASSNAME><CHECKBOXNAME><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_BUTTON_ADD", FMAXFM_SCTN0101_AX_DEF, "add a button to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_CHECKBOX_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_PARM_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_PARM_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column parm to the column to a row <NAC><CLASSNAME><COLUMNNAME>[ROWKEY]<LEVEL><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_COMBO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a column <NAC><CLASSNAME><COLUMNNAME>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_KEY_ADD", FMAXFM_SCTN0101_AX_DEF, "add a key to a column element 'key=' will be added automatically <NAC><CLASSNAME><COLUMNNAME><ROWKEY><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_PACKEDPARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add packedparms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add parms to a column entry <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_RADIO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a radio to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD", FMAXFM_SCTN0101_AX_DEF, "add a row [] to a column <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_SPIN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a spinbox to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a text element to a row <NAC><CLASSNAME><COLUMNNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_COMBO_DEF", FMAXFM_SCTN0101_AX_DEF, "define a combo box <NAC><COMBOBOXNAME>",),
	("FMAXPSG_SCTN09FF_CLASS_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME>",),
	("FMAXPSG_SCTN09FF_CLASS_DICT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a dict in PSG <NAC><CLASSNAME><DICTNAME>",),
	("FMAXPSG_SCTN09FF_CLASS_DICT_SS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str-str to a dict <NAC><CLASSNAME><DICTNAME><STR><STR>",),
	("FMAXPSG_SCTN09FF_CLASS_DICT_SV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str-val to a dict <NAC><CLASSNAME><DICTNAME><STR><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a dict <NAC><CLASSNAME><DICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a dict in PSG <NAC><CLASSNAME><DICTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_DPD_DEF", FMAXFM_SCTN0101_AX_DEF, "define a DPD debugPrintDict in PSG <NAC><CLASSNAME><DPDNAME>",),
	("FMAXPSG_SCTN09FF_CLASS_DPD_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a DPD debugPrintDict in PSG <NAC><CLASSNAME><DPDNAME><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_FORMMAIN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class mainframe",),
	("FMAXPSG_SCTN09FF_CLASS_FORMPOPUP_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class mainframe",),
	("FMAXPSG_SCTN09FF_CLASS_FRAMEELEMENT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a frame element",),
	("FMAXPSG_SCTN09FF_CLASS_FUNCTION_BLANKLINE", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><FUNCNAME><PARMS>",),
	("FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><FUNCNAME><PARMS>",),
	("FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><FUNCNAME><FILENAME>",),
	("FMAXPSG_SCTN09FF_CLASS_FUNCTION_LAMBDA1_DEF", FMAXFM_SCTN0101_AX_DEF, "add a lambda to the top of a function, usually for absorbing things",),
	("FMAXPSG_SCTN09FF_CLASS_FUNCTION_LAMBDA2_DEF", FMAXFM_SCTN0101_AX_DEF, "add a lambda to the top of a function, usually for absorbing things",),
	("FMAXPSG_SCTN09FF_CLASS_FUNCTION_LINE_ADD", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><FUNCNAME><LINE>",),
	("FMAXPSG_SCTN09FF_CLASS_FUNCTION_READ_FROM_FILE", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><FUNCNAME><FILENAME>",),
	("FMAXPSG_SCTN09FF_CLASS_FUNCTION_STR1_DEF", FMAXFM_SCTN0101_AX_DEF, "define a string in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_FUNCTION_STR2_DEF", FMAXFM_SCTN0101_AX_DEF, "define a string in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_FUNCTION_VAL1_DEF", FMAXFM_SCTN0101_AX_DEF, "define a value in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_FUNCTION_VAL2_DEF", FMAXFM_SCTN0101_AX_DEF, "define a value in the class <NAC><CLASSNAME><FUNCNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LAMBDA", FMAXFM_SCTN0101_AX_DEF, "define a string in the class <NAC><CLASSNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LINE", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><LINE>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_READ_FROM_FILE", FMAXFM_SCTN0101_AX_DEF, "read a section of __init__ from a file in res/functions <NAC><CLASSNAME><FILENAME>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_STR", FMAXFM_SCTN0101_AX_DEF, "define a string in the class <NAC><CLASSNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL", FMAXFM_SCTN0101_AX_DEF, "define a value in the class <NAC><CLASSNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_SS", FMAXFM_SCTN0101_AX_DEF, "add a str-str to a dict <NAC><CLASSNAME><STR><STR>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_SV", FMAXFM_SCTN0101_AX_DEF, "add a str-val to a dict <NAC><CLASSNAME><STR><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VS", FMAXFM_SCTN0101_AX_DEF, "add a str to a dict <NAC><CLASSNAME><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV", FMAXFM_SCTN0101_AX_DEF, "add a val to a dict in PSG <NAC><CLASSNAME><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY", FMAXFM_SCTN0101_AX_DEF, "add values to _KEY_DICT_, _KEY_DICT_REVERSE_ for external elements like buttons and checkboxes <NAC><CLASSNAME><KEY>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_LAMBDA", FMAXFM_SCTN0101_AX_DEF, "define a value in the class <NAC><CLASSNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_LINE", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><LINE>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_READ_FROM_FILE", FMAXFM_SCTN0101_AX_DEF, "read a section of __init__ from a file in res/functions <NAC><CLASSNAME><FILENAME>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_STR", FMAXFM_SCTN0101_AX_DEF, "define a string in the class <NAC><CLASSNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL", FMAXFM_SCTN0101_AX_DEF, "define a value in the class <NAC><CLASSNAME><VALNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><LINE>",),
	("FMAXPSG_SCTN09FF_CLASS_INIT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a class <NAC><CLASSNAME><PARMS>",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_BUTTON_ADD", FMAXFM_SCTN0101_AX_DEF, "add a button to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_CHECKBOX_ADD", FMAXFM_SCTN0101_AX_DEF, "add a checkbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_COLUMN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a column to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_COMBO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a combo to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a layout <NAC><CLASSNAME><LAYOUTNAME>",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_DEF", FMAXFM_SCTN0101_AX_DEF, "define layouts",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_KEY_ADD", FMAXFM_SCTN0101_AX_DEF, "add a key to a layout element 'key=' will be added automatically <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_PACKEDPARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add packedparms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add parms to a layout entry <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_RADIO_ADD", FMAXFM_SCTN0101_AX_DEF, "add a radio to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_ROW_ADD", FMAXFM_SCTN0101_AX_DEF, "add a row [] to a layout <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL>",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_SPIN_ADD", FMAXFM_SCTN0101_AX_DEF, "add a spinbox to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_LAYOUT_TEXT_ADD", FMAXFM_SCTN0101_AX_DEF, "add a text element to a row <NAC><CLASSNAME><LAYOUTNAME><ROWKEY><LEVEL><ELEMENTKEY>",),
	("FMAXPSG_SCTN09FF_CLASS_LIST_DEF", FMAXFM_SCTN0101_AX_DEF, "define a list in PSG <NAC><CLASSNAME><LISTNAME>",),
	("FMAXPSG_SCTN09FF_CLASS_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a list in PSG <NAC><CLASSNAME><LISTNAME><STR>",),
	("FMAXPSG_SCTN09FF_CLASS_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a list in PSG <NAC><CLASSNAME><LISTNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_RADIO_DEF", FMAXFM_SCTN0101_AX_DEF, "define a radio button element",),
	("FMAXPSG_SCTN09FF_CLASS_RCMENU_DEF", FMAXFM_SCTN0101_AX_DEF, "define a right click menu",),
	("FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "define a right click menu",),
	("FMAXPSG_SCTN09FF_CLASS_SPIN_DEF", FMAXFM_SCTN0101_AX_DEF, "define a spin box entry <NAC><CLASSNAME><SPINNAME>",),
	("FMAXPSG_SCTN09FF_CLASS_SPIN_DICT_VS_ADD", FMAXFM_SCTN0101_AX_DEF, "add a STR to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><STR>",),
	("FMAXPSG_SCTN09FF_CLASS_SPIN_DICT_VV_ADD", FMAXFM_SCTN0101_AX_DEF, "add a VAL to the SPINDICT <NAC><CLASSNAME><SPINNAME><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_SPIN_LIST_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a STR to the values list <NAC><CLASSNAME><SPINNAME><STR>",),
	("FMAXPSG_SCTN09FF_CLASS_SPIN_LIST_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a VAL to the values list <NAC><CLASSNAME><SPINNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_TEXT_DEF", FMAXFM_SCTN0101_AX_DEF, "define a text <NAC><CLASSNAME><TEXTNAME><ISATIME>",),
	("FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD", FMAXFM_SCTN0101_AX_DEF, "add a PARM to a text element <NAC><CLASSNAME><TEXTNAME><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_TEXT_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to a text element <NAC><CLASSNAME><TEXTNAME><KEY><VAL>",),
	("FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a val to a text element <NAC><CLASSNAME><TEXTNAME>",),
	("FMAXPSG_SCTN09FF_CLASS_WINDOW_DEF", FMAXFM_SCTN0101_AX_DEF, "define a main dictdict <NAC><CLASSNAME><MAINNAME>",),
	("FMAXPSG_SCTN09FF_CLASS_WINDOW_STR_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),
	("FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD", FMAXFM_SCTN0101_AX_DEF, "add a str to the main dictdict",),
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
	("FMFM_SCTN0101_AX_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN101 FMAX defined",),
	("FMFM_SCTN0101_AX_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN101 FMAX defined",),
	("FMFM_SCTN0102_VAL_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN102 val",),
	("FMFM_SCTN0102_VAL_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN102 val",),
	("FMFM_SCTN0103_DICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN103 dict defined",),
	("FMFM_SCTN0103_DICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN103 dict defined",),
	("FMFM_SCTN0104_LIST_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN201 device defines",),
	("FMFM_SCTN0104_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN201 device defines",),
	("FMFM_SCTN0105_LDICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN105 ldict defined",),
	("FMFM_SCTN0105_LDICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "SCTN105 ldict defined",),
	("FMFM_____", FMAX_NOP, "FMFM_ENDS",),
	("FMPSG", FMAX_NOP, "FMPSG_BEGINS",),
	("FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)",),
	("FMPSG_SCTN0900_DEF1_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0900_DEF1_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
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
	("FMPSG_SCTN0906_BTNS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0906_BTNS_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0907_SPIN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)f",),
	("FMPSG_SCTN0907_SPIN_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)",),
	("FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)",),
	("FMPSG_SCTN0908_CHECKBOX_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0908_CHECKBOX_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0909_TEXT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0909_TEXT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN090A_RADIO_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN090A_RADIO_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN090B_COLUMN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN090B_COLUMN_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN090B_COLUMN_PARMS_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN090C_APPDSDICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "the main app dict+dict for this app",),
	("FMPSG_SCTN090C_APPDS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "the main app dict for this app",),
	("FMPSG_SCTN090C_APPDS_DICT", FMAXFM_SCTN0103_DICT_DEF, "the main app dict for this app",),
	("FMPSG_SCTN090D_FORMMAIN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN090D_FORMMAIN_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN090E_LAYOUT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN090E_LAYOUT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN090F_WINDOW_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN090F_WINDOW_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0910_DEF3_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0910_DEF3_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0911_COMBO_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0911_COMBO_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0912_FRAME_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0912_FRAME_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0913_RCMENU_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0913_RCMENU_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0914_FORMPOPUP_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0914_FORMPOPUP_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0915_PUDLG_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0915_PUDLG_DICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0915_PUDLG_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN0915_PUDLG_TYPE_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_BTNS_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_BTNS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_BTNS_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_CDS_DICT", FMAXFM_SCTN0103_DICT_DEF, "class data storage",),
	("FMPSG_SCTN09FF_CLASS_CHECKBOX_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_CHECKBOX_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_COLUMN_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_COLUMN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_COLUMN_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_COLUMN_PARMS_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_COMBO_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_COMBO_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_COMBO_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_DEF_DICT", FMAXFM_SCTN0103_DICT_DEF, "str and val defines in a class",),
	("FMPSG_SCTN09FF_CLASS_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_DICT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_FRAME_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_FRAME_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_FRAME_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_FUNCTION_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_FUNCTION_DEF1_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_FUNCTION_DEF2_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_FUNCTION_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_INIT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_INIT_DEF3_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_INIT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_LAYOUT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_LAYOUT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_LIST_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_LIST_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_RADIO_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_RADIO_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_RADIO_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_RCMENU_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_RCMENU_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_RCMENU_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_SPIN_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_SPIN_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)f",),
	("FMPSG_SCTN09FF_CLASS_SPIN_DICT", FMAXFM_SCTN0103_DICT_DEF, "holds the spin element stuffs (TUPDICT)",),
	("FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_TEXT_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_TEXT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_WINDOW_CMNT_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_SCTN09FF_CLASS_WINDOW_DICT", FMAXFM_SCTN0103_DICT_DEF, "",),
	("FMPSG_____", FMAX_NOP, "FMPSG_ENDS",),
	("FMVAl_TABLEVEL", FMAXFM_SCTN0102_STR_DEF, "TABLEVEL", "TABLEVEL", "key for tab levels",),
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
	("PSGVAL_COLOR_TEXT_SPIN", FMAXPSG_SCTN0900_STR_DEF, "COLOR_TEXT_SPIN", "#CCFF66", "the color the clock digits are",),
	("PSGVAL_COLOR_TIME_CLOCK", FMAXPSG_SCTN0900_STR_DEF, "COLOR_TIME_CLOCK", "#CC66FF", "color of the clock on any window/frame/etc.",),
	("PSGVAL_COLOR_TIME_ELAPSED", FMAXPSG_SCTN0900_STR_DEF, "COLOR_TIME_ELAPSED", "#447733", "color of the clock on any window/frame/etc.",),
	("PSGVAL_COLOR_TIME_TOGO", FMAXPSG_SCTN0900_STR_DEF, "COLOR_TIME_TOGO", "#AA6600", "color of the clock on any window/frame/etc.",),
	("PSGVAL_COLOR_WHITE", FMAXPSG_SCTN0900_STR_DEF, "COLOR_WHITE", "#FFFFFF", "white",),
	("PSGVAL_DPD_ROOT00", FMAXPSG_SCTN0902_DICT_DEF, "DPD_ROOT", "DPD_ROOT defined",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_COMPAREBBOX", "False", "DPD_ROOT entry compareBBox",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_COMPAREXY", "False", "DPD_ROOT entry compareXY",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_DOIT", "False", "DPD_ROOT entry doit",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_DOMIDNIGHTWORK", "False", "DPD_ROOT entry doMidnightWork",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_DOSTARTUP", "False", "DPD_ROOT entry doStartup",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_FINDNEXTALARMEVENT", "False", "DPD_ROOT entry findNextAlarmEvent",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_FIXTIMEATNEXT", "False", "DPD_ROOT entry fixTimeAtNext",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_GETBBOX", "False", "DPD_ROOT entry getBBox",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_GETCLOSEBBOX", "False", "DPD_ROOT entry getCloseBBox",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_GETMOUSEPOS", "False", "DPD_ROOT entry getMousePos",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_INNERLOOP", "False", "DPD_ROOT entry outerLoop",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_ISINBBOX", "False", "DPD_ROOT entry isInBBox",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_LOCALTIMES", "False", "DPD_ROOT entry localTimes",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_OUTERLOOP", "False", "DPD_ROOT entry outerLoop",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_SPLITBBOXTORAW", "False", "DPD_ROOT entry splitBBoxToRaw",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_SPLITXYTORAW", "False", "DPD_ROOT entry splitXYToRaw",),
	("PSGVAL_DPD_ROOT01", FMAXPSG_SCTN0902_DICT_VV_ADD, "DPD_ROOT", "F_UPDATEINTERVAL", "False", "DPD_ROOT entry updateInterval",),
	("PSGVAL_EMPTY_BBOX", FMAXPSG_SCTN0901_VAL_DEF, "EMPTY_BBOX", "(0, 0, 0, 0)", "empty XY dict",),
	("PSGVAL_EMPTY_XY", FMAXPSG_SCTN0901_VAL_DEF, "EMPTY_XY", "(0, 0)", "empty XY dict",),
	("PSGVAL_FONT_DEFAULT", FMAXPSG_SCTN0901_STR_DEF, "FONT_DEFAULT", "Source Code Pro", "default font my favorite readable font",),
	("PSGVAL_F_APPDSDECODE", FMAXPSG_SCTN0900_KEY_DEF, "F_APPDSDECODE", "fkey ENTRY appdsDecode",),
	("PSGVAL_F_COMPAREBBOX", FMAXPSG_SCTN0900_KEY_DEF, "F_COMPAREBBOX", "FKEY entry compareBBox",),
	("PSGVAL_F_COMPAREXY", FMAXPSG_SCTN0900_KEY_DEF, "F_COMPAREXY", "FKEY entry compareXY",),
	("PSGVAL_F_DOIT", FMAXPSG_SCTN0900_KEY_DEF, "F_DOIT", "FKEY entry doit",),
	("PSGVAL_F_DOMIDNIGHTWORK", FMAXPSG_SCTN0900_KEY_DEF, "F_DOMIDNIGHTWORK", "FKEY entry doMidnightWork",),
	("PSGVAL_F_DOSTARTUP", FMAXPSG_SCTN0900_KEY_DEF, "F_DOSTARTUP", "FKEY entry doStartup",),
	("PSGVAL_F_FINDNEXTALARMEVENT", FMAXPSG_SCTN0900_KEY_DEF, "F_FINDNEXTALARMEVENT", "FKEY entry findNextAlarmEvent",),
	("PSGVAL_F_FIXTIMEATNEXT", FMAXPSG_SCTN0900_KEY_DEF, "F_FIXTIMEATNEXT", "FKEY entry fixTimeAtNext",),
	("PSGVAL_F_GETBBOX", FMAXPSG_SCTN0900_KEY_DEF, "F_GETBBOX", "FKEY entry getBBox",),
	("PSGVAL_F_GETCLOSEBBOX", FMAXPSG_SCTN0900_KEY_DEF, "F_GETCLOSEBBOX", "FKEY entry getCloseBBox",),
	("PSGVAL_F_GETMOUSEPOS", FMAXPSG_SCTN0900_KEY_DEF, "F_GETMOUSEPOS", "FKEY entry getMousePos",),
	("PSGVAL_F_INNERLOOP", FMAXPSG_SCTN0900_KEY_DEF, "F_INNERLOOP", "FKEY entry doit",),
	("PSGVAL_F_ISINBBOX", FMAXPSG_SCTN0900_KEY_DEF, "F_ISINBBOX", "FKEY entry isInBBox",),
	("PSGVAL_F_LOCALTIMES", FMAXPSG_SCTN0900_KEY_DEF, "F_LOCALTIMES", "FKEY entry localTimes",),
	("PSGVAL_F_OUTERLOOP", FMAXPSG_SCTN0900_KEY_DEF, "F_OUTERLOOP", "FKEY entry outerLoop",),
	("PSGVAL_F_SPLITBBOXTORAW", FMAXPSG_SCTN0900_KEY_DEF, "F_SPLITBBOXTORAW", "FKEY entry splitBBoxToRaw",),
	("PSGVAL_F_SPLITXYTORAW", FMAXPSG_SCTN0900_KEY_DEF, "F_SPLITXYTORAW", "FKEY entry splitXYToRaw",),
	("PSGVAL_F_UPDATEINTERVAL", FMAXPSG_SCTN0900_KEY_DEF, "F_UPDATEINTERVAL", "FKEY entry updateInterval",),
	("PSGVAL_F___INIT__", FMAXPSG_SCTN0900_KEY_DEF, "F___INIT__", "FKEY entry doit",),
	("PSGVAL_INDEX_EAST", FMAXPSG_SCTN0900_VAL_DEF, "INDEX_EAST", "2", "EAST",),
	("PSGVAL_INDEX_NORTH", FMAXPSG_SCTN0900_VAL_DEF, "INDEX_NORTH", "1", "NORTH",),
	("PSGVAL_INDEX_SOUTH", FMAXPSG_SCTN0900_VAL_DEF, "INDEX_SOUTH", "3", "SOUTH",),
	("PSGVAL_INDEX_WEST", FMAXPSG_SCTN0900_VAL_DEF, "INDEX_WEST", "0", "WEST",),
	("PSGVAL_INDEX_X", FMAXPSG_SCTN0900_VAL_DEF, "INDEX_X", "0", "X",),
	("PSGVAL_INDEX_Y", FMAXPSG_SCTN0900_VAL_DEF, "INDEX_Y", "1", "Y",),
	("PSGVAL_KEY", FMAX_NOP, "keys defined",),
	("PSGVAL_KEY_ALARMPOPUP_PROPER", FMAXPSG_SCTN0900_KEY_DEF, "K_ALARMPOPUP_PROPER", "key for the button return for the popup",),
	("PSGVAL_KEY_ALARMPOPUP_TEXT_TEXT", FMAXPSG_SCTN0900_KEY_DEF, "K_ALARMPOPUP_TEXT_TEXT", "key for the text on a popup",),
	("PSGVAL_KEY_ALPHA_CHANNEL", FMAXPSG_SCTN0900_KEY_DEF, "K_ALPHA_CHANNEL", "alpha channel key",),
	("PSGVAL_KEY_ALPHA_HIGH", FMAXPSG_SCTN0900_KEY_DEF, "K_ALPHA_HIGH", "alphahigh key",),
	("PSGVAL_KEY_ALPHA_LOW", FMAXPSG_SCTN0900_KEY_DEF, "K_ALPHA_LOW", "",),
	("PSGVAL_KEY_APPMODE", FMAXPSG_SCTN0900_KEY_DEF, "K_APPMODE", "app mode key",),
	("PSGVAL_KEY_APPMODE_CLOCKS", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_CLOCKS", "mode clocks only",),
	("PSGVAL_KEY_APPMODE_EDIT", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_EDIT", "edit mode on top of main window",),
	("PSGVAL_KEY_APPMODE_MAIN", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_MAIN", "main mode (xpand from clocks to this)",),
	("PSGVAL_KEY_APPMODE_MOUSE_OVER", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_MOUSE_OVER", "mouseOver mode (xpand from clocks to this)",),
	("PSGVAL_KEY_APPMODE_NEW_ALARMPOPUP", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_NEW_ALARMPOPUP", "main mode (xpand from clocks to this)",),
	("PSGVAL_KEY_APPMODE_NONE", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_NONE", "NONE mode",),
	("PSGVAL_KEY_APPMODE_THECLOCK", FMAXPSG_SCTN0900_KEY_DEF, "APPMODE_THECLOCK", "theClock mode (xpand from clocks to this)",),
	("PSGVAL_KEY_AUTO_CLOSE_DURATION", FMAXPSG_SCTN0900_KEY_DEF, "K_AUTO_CLOSE_DURATION", "",),
	("PSGVAL_KEY_BBOX", FMAXPSG_SCTN0900_KEY_DEF, "K_BBOX", "",),
	("PSGVAL_KEY_BTN_DISMISS", FMAXPSG_SCTN0900_KEY_DEF, "K_BTN_DISMISS", "",),
	("PSGVAL_KEY_BTN_DOWN", FMAXPSG_SCTN0900_KEY_DEF, "K_BTN_DOWN", "",),
	("PSGVAL_KEY_BTN_EDIT", FMAXPSG_SCTN0900_KEY_DEF, "K_BTN_EDIT", "",),
	("PSGVAL_KEY_BTN_QUIT_ALL", FMAXPSG_SCTN0900_KEY_DEF, "K_BTN_QUIT_ALL", "",),
	("PSGVAL_KEY_BTN_QUIT_EDITOR", FMAXPSG_SCTN0900_KEY_DEF, "K_BTN_QUIT_EDITOR", "",),
	("PSGVAL_KEY_BTN_UP", FMAXPSG_SCTN0900_KEY_DEF, "K_BTN_UP", "",),
	("PSGVAL_KEY_BTN_XPAND", FMAXPSG_SCTN0900_KEY_DEF, "K_BTN_XPAND", "",),
	("PSGVAL_KEY_BTN_ZERO", FMAXPSG_SCTN0900_KEY_DEF, "K_BTN_ZERO", "",),
	("PSGVAL_KEY_CHANGED_EVENTS", FMAXPSG_SCTN0900_KEY_DEF, "K_CHANGED_EVENTS", "",),
	("PSGVAL_KEY_CHANGED_VALUES", FMAXPSG_SCTN0900_KEY_DEF, "K_CHANGED_VALUES", "",),
	("PSGVAL_KEY_CHECKBOX_ALPHADIM", FMAXPSG_SCTN0900_KEY_DEF, "K_CHECKBOX_ALPHADIM", "is the clock transparent under mouse (ineffective if mouse is avoided)",),
	("PSGVAL_KEY_CHECKBOX_ALPHA_DIM", FMAXPSG_SCTN0900_KEY_DEF, "K_CHECKBOX_ALPHA_DIM", "is the clock transparent under mouse (ineffective if mouse is avoided)",),
	("PSGVAL_KEY_CHECKBOX_DISMISSED", FMAXPSG_SCTN0900_KEY_DEF, "K_CHECKBOX_DISMISSED", "key for avoiding the mouse bool",),
	("PSGVAL_KEY_CHECKBOX_ENABLED", FMAXPSG_SCTN0900_KEY_DEF, "K_CHECKBOX_ENABLED", "key for avoiding the mouse bool",),
	("PSGVAL_KEY_CHECKBOX_FIRSTRUN", FMAXPSG_SCTN0900_KEY_DEF, "K_CHECKBOX_FIRSTRUN", "key for avoiding the mouse bool",),
	("PSGVAL_KEY_CHECKBOX_HOVER_DATE", FMAXPSG_SCTN0900_KEY_DEF, "K_CHECKBOX_HOVER_DATE", "KEY FOR K_CHECKBOX_HOVER_DATE",),
	("PSGVAL_KEY_CHECKBOX_IS_ALERTING_NOW", FMAXPSG_SCTN0900_KEY_DEF, "K_CHECKBOX_IS_ALERTING_NOW", "key for avoiding the mouse bool",),
	("PSGVAL_KEY_CHECKBOX_PREDISMISSABLE", FMAXPSG_SCTN0900_KEY_DEF, "K_CHECKBOX_PREDISMISSABLE", "key for avoiding the mouse bool",),
	("PSGVAL_KEY_CHECKBOX_RUNAWAY", FMAXPSG_SCTN0900_KEY_DEF, "K_CHECKBOX_RUNAWAY", "key for avoiding the mouse bool",),
	("PSGVAL_KEY_CHECKBOX_SNOOZABLE", FMAXPSG_SCTN0900_KEY_DEF, "K_CHECKBOX_SNOOZABLE", "key for avoiding the mouse bool",),
	("PSGVAL_KEY_CHECKBOX_SNOOZED", FMAXPSG_SCTN0900_KEY_DEF, "K_CHECKBOX_SNOOZED", "key for avoiding the mouse bool",),
	("PSGVAL_KEY_CLOSE_BBOX", FMAXPSG_SCTN0900_KEY_DEF, "K_CLOSE_BBOX", "",),
	("PSGVAL_KEY_COLUMN01", FMAXPSG_SCTN0900_KEY_DEF, "K_COLUMN01", "",),
	("PSGVAL_KEY_COLUMN02", FMAXPSG_SCTN0900_KEY_DEF, "K_COLUMN02", "",),
	("PSGVAL_KEY_CURRENTLY_DIMMED", FMAXPSG_SCTN0900_KEY_DEF, "K_CURRENTLY_DIMMED", "",),
	("PSGVAL_KEY_CURRENT_EVENT", FMAXPSG_SCTN0900_KEY_DEF, "K_CURRENT_EVENT", "",),
	("PSGVAL_KEY_CURRENT_EVENTMODE", FMAXPSG_SCTN0900_KEY_DEF, "K_CURRENT_EVENTMODE", "",),
	("PSGVAL_KEY_CURRENT_LOCATION", FMAXPSG_SCTN0900_KEY_DEF, "K_CURRENT_LOCATION", "",),
	("PSGVAL_KEY_CURRENT_MOUSE_LOCATION", FMAXPSG_SCTN0900_KEY_DEF, "K_CURRENT_MOUSE_LOCATION", "",),
	("PSGVAL_KEY_CURRENT_MOUSE_STATUS", FMAXPSG_SCTN0900_KEY_DEF, "K_CURRENT_MOUSE_STATUS", "",),
	("PSGVAL_KEY_CURRENT_RESULT", FMAXPSG_SCTN0900_KEY_DEF, "K_CURRENT_RESULT", "",),
	("PSGVAL_KEY_CURRENT_VALUE", FMAXPSG_SCTN0900_KEY_DEF, "K_CURRENT_VALUE", "",),
	("PSGVAL_KEY_DEBUG_PRINT_DICT", FMAXPSG_SCTN0900_KEY_DEF, "K_DEBUG_PRINT_DICT", "debug print key",),
	("PSGVAL_KEY_DICTIN", FMAXPSG_SCTN0900_KEY_DEF, "K_DICTIN", "",),
	("PSGVAL_KEY_DICTINSTR", FMAXPSG_SCTN0900_KEY_DEF, "K_DICTINSTR", "",),
	("PSGVAL_KEY_DICTOUT", FMAXPSG_SCTN0900_KEY_DEF, "K_DICTOUT", "",),
	("PSGVAL_KEY_DICT_KEYS_INT", FMAXPSG_SCTN0900_KEY_DEF, "K_DICT_KEYS_INT", "",),
	("PSGVAL_KEY_DICT_KEYS_TIME", FMAXPSG_SCTN0900_KEY_DEF, "K_DICT_KEYS_TIME", "",),
	("PSGVAL_KEY_DISMISSED", FMAXPSG_SCTN0900_KEY_DEF, "K_DISMISSED", "alarm dismissed bool",),
	("PSGVAL_KEY_DPD", FMAXPSG_SCTN0900_KEY_DEF, "K_DPD", "alarm dismissed bool",),
	("PSGVAL_KEY_ENABLED", FMAXPSG_SCTN0900_KEY_DEF, "K_ENABLED", "",),
	("PSGVAL_KEY_EVENTMODE", FMAXPSG_SCTN0900_KEY_DEF, "K_EVENTMODE", "what mode is this event",),
	("PSGVAL_KEY_EVENTMODE_ALARM", FMAXPSG_SCTN0900_KEY_DEF, "EVENTMODE_ALARM", "",),
	("PSGVAL_KEY_EVENTMODE_INTERVAL", FMAXPSG_SCTN0900_KEY_DEF, "EVENTMODE_INTERVAL", "",),
	("PSGVAL_KEY_EVENTMODE_NONE", FMAXPSG_SCTN0900_KEY_DEF, "EVENTMODE_NONE", "what mode is this event",),
	("PSGVAL_KEY_EVENT_ENTRIES", FMAXPSG_SCTN0900_KEY_DEF, "K_EVENT_ENTRIES", "",),
	("PSGVAL_KEY_EVENT_NAME", FMAXPSG_SCTN0900_KEY_DEF, "K_EVENT_NAME", "name of the event",),
	("PSGVAL_KEY_FIRSTRUN", FMAXPSG_SCTN0900_KEY_DEF, "K_FIRSTRUN", "True if just started, false after init1()",),
	("PSGVAL_KEY_FORM_NAME", FMAXPSG_SCTN0900_KEY_DEF, "K_FRAMENAME", "the name of the form",),
	("PSGVAL_KEY_FRAME_CLOCKS", FMAXPSG_SCTN0900_KEY_DEF, "FRAME_CLOCKS", "holds all of clocks form entries",),
	("PSGVAL_KEY_FRAME_EDITENTRY", FMAXPSG_SCTN0900_KEY_DEF, "FRAME_EDITENTRY", "holds all of form edit-entry entries",),
	("PSGVAL_KEY_FRAME_EDITOR", FMAXPSG_SCTN0900_KEY_DEF, "FRAME_EDITOR", "holds all of form editor entries",),
	("PSGVAL_KEY_FRAME_MAIN", FMAXPSG_SCTN0900_KEY_DEF, "FRAME_MAIN", "holds all of form main entries",),
	("PSGVAL_KEY_FRAME_POPUP01", FMAXPSG_SCTN0900_KEY_DEF, "FRAME_POPUP01", "holds all of form popup entries",),
	("PSGVAL_KEY_FRAME_POPUP02", FMAXPSG_SCTN0900_KEY_DEF, "FRAME_POPUP02", "holds all of form popup entries",),
	("PSGVAL_KEY_FRAME_POPUP03", FMAXPSG_SCTN0900_KEY_DEF, "FRAME_POPUP03", "holds all of form popup entries",),
	("PSGVAL_KEY_FRAME_POPUP04", FMAXPSG_SCTN0900_KEY_DEF, "FRAME_POPUP04", "holds all of form popup entries",),
	("PSGVAL_KEY_FRAME_POPUP05", FMAXPSG_SCTN0900_KEY_DEF, "FRAME_POPUP05", "holds all of form popup entries",),
	("PSGVAL_KEY_FRAME_THECLOCK", FMAXPSG_SCTN0900_KEY_DEF, "FRAME_THECLOCK", "holds all of theclock form entries",),
	("PSGVAL_KEY_INDEX_OF_NEXT_EVENT", FMAXPSG_SCTN0900_KEY_DEF, "K_INDEX_OF_NEXT_EVENT", "index of the next event to alert",),
	("PSGVAL_KEY_INTERVAL_COUNT", FMAXPSG_SCTN0900_KEY_DEF, "K_INTERVAL_COUNT", "count of the number of times since last reset this interval has triggered an alert",),
	("PSGVAL_KEY_IS_ALERTING_NOW", FMAXPSG_SCTN0900_KEY_DEF, "K_IS_ALERTING_NOW", "",),
	("PSGVAL_KEY_KEY_DICT", FMAXPSG_SCTN0900_KEY_DEF, "K_KEY_DICT", "",),
	("PSGVAL_KEY_KEY_DICT_REVERSE", FMAXPSG_SCTN0900_KEY_DEF, "K_KEY_DICT_REVERSE", "",),
	("PSGVAL_KEY_KEY_LIST_TIMES", FMAXPSG_SCTN0900_KEY_DEF, "K_KEY_LIST_TIMES", "",),
	("PSGVAL_KEY_LAST_EVENT", FMAXPSG_SCTN0900_KEY_DEF, "K_LAST_EVENT", "",),
	("PSGVAL_KEY_LAST_LOCATION", FMAXPSG_SCTN0900_KEY_DEF, "K_LAST_LOCATION", "",),
	("PSGVAL_KEY_LAST_MOUSE_LOCATION", FMAXPSG_SCTN0900_KEY_DEF, "K_LAST_MOUSE_LOCATION", "",),
	("PSGVAL_KEY_LAST_MOUSE_STATUS", FMAXPSG_SCTN0900_KEY_DEF, "K_LAST_MOUSE_STATUS", "",),
	("PSGVAL_KEY_LAST_VALUES", FMAXPSG_SCTN0900_KEY_DEF, "K_LAST_VALUES", "",),
	("PSGVAL_KEY_LAYOUT", FMAXPSG_SCTN0900_KEY_DEF, "K_LAYOUT", "",),
	("PSGVAL_KEY_MAINFRAME", FMAXPSG_SCTN0900_KEY_DEF, "K_MAINFRAME", "",),
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
	("PSGVAL_KEY_MOUSE_STATUS_NONE", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_NONE", "mouse is unknown",),
	("PSGVAL_KEY_MOUSE_STATUS_NW", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_NW", "mouse is northwest of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_OVER", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_OVER", "mouse is over top of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_S", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_S", "mouse is south of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_SE", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_SE", "mouse is southeast of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_SW", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_SW", "mouse is southwest of checked element",),
	("PSGVAL_KEY_MOUSE_STATUS_W", FMAXPSG_SCTN0900_KEY_DEF, "MOUSE_STATUS_W", "mouse is west of checked element",),
	("PSGVAL_KEY_MPX", FMAXPSG_SCTN0900_KEY_DEF, "K_MPX", "",),
	("PSGVAL_KEY_NAME", FMAXPSG_SCTN0900_KEY_DEF, "K_NAME", "",),
	("PSGVAL_KEY_NAME_NEXT_EVENT", FMAXPSG_SCTN0900_KEY_DEF, "K_NAME_NEXT_EVENT", "name of the next event up",),
	("PSGVAL_KEY_PERIODIC", FMAXPSG_SCTN0900_KEY_DEF, "K_PERIODIC", "",),
	("PSGVAL_KEY_PREDISMISSABLE", FMAXPSG_SCTN0900_KEY_DEF, "K_PREDISMISSABLE", "event can be dismissed in advance",),
	("PSGVAL_KEY_SCREEN_DIMS", FMAXPSG_SCTN0900_KEY_DEF, "K_SCREEN_DIMS", "",),
	("PSGVAL_KEY_SIZE", FMAXPSG_SCTN0900_KEY_DEF, "K_SIZE", "",),
	("PSGVAL_KEY_SNOOZABLE", FMAXPSG_SCTN0900_KEY_DEF, "K_SNOOZABLE", "can this event be snoozed",),
	("PSGVAL_KEY_SNOOZED", FMAXPSG_SCTN0900_KEY_DEF, "K_SNOOZED", "is this event snoozed bool",),
	("PSGVAL_KEY_TEXT_INTERVAL_COUNT_KEY", FMAXPSG_SCTN0900_KEY_DEF, "K_TEXT_INTERVAL_COUNT", "",),
	("PSGVAL_KEY_TEXT_NAME_NEXT_EVENT_KEY", FMAXPSG_SCTN0900_KEY_DEF, "K_TEXT_NAME_NEXT_EVENT", "",),
	("PSGVAL_KEY_TEXT_TIME_AT_NEXT_ALERT_KEY", FMAXPSG_SCTN0900_KEY_DEF, "K_TEXT_TIME_AT_NEXT_ALERT", "",),
	("PSGVAL_KEY_TEXT_TIME_AT_ZEROELAPSE_KEY", FMAXPSG_SCTN0900_KEY_DEF, "K_TEXT_TIME_AT_ZEROELAPSE", "",),
	("PSGVAL_KEY_TEXT_TIME_CLOCK_KEY", FMAXPSG_SCTN0900_KEY_DEF, "K_TEXT_TIME_CLOCK", "",),
	("PSGVAL_KEY_TEXT_TIME_ELAPSED_KEY", FMAXPSG_SCTN0900_KEY_DEF, "K_TEXT_TIME_ELAPSED", "",),
	("PSGVAL_KEY_TEXT_TIME_TOGO_KEY", FMAXPSG_SCTN0900_KEY_DEF, "K_TEXT_TIME_TOGO", "",),
	("PSGVAL_KEY_THIS_FORM_NAME", FMAXPSG_SCTN0900_KEY_DEF, "K_THIS_FORM_NAME", "",),
	("PSGVAL_KEY_THIS_KEY_BASE", FMAXPSG_SCTN0900_KEY_DEF, "K_THIS_KEY_BASE", "",),
	("PSGVAL_KEY_TIME_ALARM", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_ALARM", "the alarm time",),
	("PSGVAL_KEY_TIME_AT_LAST_RUN", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_AT_LAST_RUN", "timeS of last alarm ",),
	("PSGVAL_KEY_TIME_AT_NEXT_ALERT", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_AT_NEXT_ALERT", "what time is the next alarm, == KEY_TIME_ALARM is tomorrow",),
	("PSGVAL_KEY_TIME_AT_ZEROELAPSE", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_AT_ZEROELAPSE", "the time at last zero to keep elapsed time accurate despite other things hogging CPU time",),
	("PSGVAL_KEY_TIME_CLOCK", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_CLOCK", "the main clock time",),
	("PSGVAL_KEY_TIME_ELAPSED", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_ELAPSED", "key for all clocks elapsed",),
	("PSGVAL_KEY_TIME_INTERVAL", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_INTERVAL", "interval timer starting time, reset each time the interval goes off",),
	("PSGVAL_KEY_TIME_INTERVAL_START", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_INTERVAL_START", "interval timer starting time, reset each time the interval goes off",),
	("PSGVAL_KEY_TIME_INTERVAL__BEGIN", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_INTERVAL__BEGIN", "key for time interval starts alerting",),
	("PSGVAL_KEY_TIME_INTERVAL__END", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_INTERVAL__END", "key for time an interval goes to leep and stops alerting",),
	("PSGVAL_KEY_TIME_LEN_OF_ALERT", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_LEN_OF_ALERT", "length of alerting",),
	("PSGVAL_KEY_TIME_TOGO", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_TOGO", "down counter to next event on this window/alarm/interval/reminder",),
	("PSGVAL_KEY_TIME_TO_CHECK_MOUSE", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_TO_CHECK_MOUSE", "",),
	("PSGVAL_KEY_TIME_TO_MOVE", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_TO_MOVE", "",),
	("PSGVAL_KEY_TIME_TO_UPDATE", FMAXPSG_SCTN0900_KEY_DEF, "K_TIME_TO_UPDATE", "",),
	("PSGVAL_KEY_USE_THIS_KEY", FMAXPSG_SCTN0900_KEY_DEF, "K_USE_THIS_KEY", "",),
	("PSGVAL_KEY_VERSION", FMAXPSG_SCTN0900_KEY_DEF, "K_VERSION", "True if pkl is to be updated from APPDS_MAIN",),
	("PSGVAL_KEY_WINDOW", FMAXPSG_SCTN0900_KEY_DEF, "K_WINDOW", "",),
	("PSGVAL_SZ_ALERT_TEXT", FMAXPSG_SCTN0900_VAL_DEF, "SZ_ALERT_TEXT", "20", "font size of alert text",),
	("PSGVAL_SZ_ALPHA_DIM", FMAXPSG_SCTN0900_VAL_DEF, "SZ_ALPHA_DIM", "True", "default alpha dim state",),
	("PSGVAL_SZ_ALPHA_HIGH", FMAXPSG_SCTN0900_VAL_DEF, "SZ_ALPHA_HIGH", "1.0", "high alpha",),
	("PSGVAL_SZ_ALPHA_LOW", FMAXPSG_SCTN0900_VAL_DEF, "SZ_ALPHA_LOW", "0.2", "low alpha",),
	("PSGVAL_SZ_BORDER_DEPTH", FMAXPSG_SCTN0900_VAL_DEF, "SZ_BORDER_DEPTH", "0", "border depth",),
	("PSGVAL_SZ_BTNS", FMAXPSG_SCTN0900_VAL_DEF, "SZ_BTNS", "6", "font size for button text",),
	("PSGVAL_SZ_CLOCKS_TIME_CLOCK", FMAXPSG_SCTN0900_VAL_DEF, "SZ_CLOCKS_TIME_CLOCK", "26", "font size of the main clock on the clocks only floating widget",),
	("PSGVAL_SZ_CLOCKS_TIME_ELAPSED", FMAXPSG_SCTN0900_VAL_DEF, "SZ_CLOCKS_TIME_ELAPSED", "13", "font size of the elapsed clock on the clocks only floating widget",),
	("PSGVAL_SZ_CLOCKS_TIME_TOGO", FMAXPSG_SCTN0900_VAL_DEF, "SZ_CLOCKS_TIME_TOGO", "13", "font size of the main togo clock on the clocks only floating widget",),
	("PSGVAL_SZ_CLOSE", FMAXPSG_SCTN0900_VAL_DEF, "SZ_CLOSE", "80", "close enough to move from the mouse",),
	("PSGVAL_SZ_EDIT_TIME_CLOCK", FMAXPSG_SCTN0900_VAL_DEF, "SZ_EDIT_TIME_CLOCK", "20", "font size of the main clock on the clocks only floating widget",),
	("PSGVAL_SZ_EDIT_TIME_ELAPSED", FMAXPSG_SCTN0900_VAL_DEF, "SZ_EDIT_TIME_ELAPSED", "10", "font size of the elapsed clock on the clocks only floating widget",),
	("PSGVAL_SZ_EDIT_TIME_TOGO", FMAXPSG_SCTN0900_VAL_DEF, "SZ_EDIT_TIME_TOGO", "10", "font size of the main togo clock on the clocks only floating widget",),
	("PSGVAL_SZ_INTERVAL_COUNT", FMAXPSG_SCTN0900_VAL_DEF, "SZ_INTERVAL_COUNT", "10", "font size of the main interval count",),
	("PSGVAL_SZ_MAIN_TIME_CLOCK", FMAXPSG_SCTN0900_VAL_DEF, "SZ_MAIN_TIME_CLOCK", "60", "font size of the main clock on the clocks only floating widget",),
	("PSGVAL_SZ_MAIN_TIME_ELAPSED", FMAXPSG_SCTN0900_VAL_DEF, "SZ_MAIN_TIME_ELAPSED", "30", "font size of the elapsed clock on the clocks only floating widget",),
	("PSGVAL_SZ_MAIN_TIME_TOGO", FMAXPSG_SCTN0900_VAL_DEF, "SZ_MAIN_TIME_TOGO", "30", "font size of the main togo clock on the clocks only floating widget",),
	("PSGVAL_SZ_MARGINS_ALL", FMAXPSG_SCTN0900_VAL_DEF, "SZ_MARGINS_ALL", "(0, 0)", "all margins default",),
	("PSGVAL_SZ_MAX_DELTA", FMAXPSG_SCTN0900_VAL_DEF, "SZ_MAX_DELTA", "100", "maximum possible change per move",),
	("PSGVAL_SZ_MOVE_DIST", FMAXPSG_SCTN0900_VAL_DEF, "SZ_MOVE_DIST", "50", "move by this pixels each jump",),
	("PSGVAL_SZ_PAD_ALL", FMAXPSG_SCTN0900_VAL_DEF, "SZ_PAD_ALL", "((1, 1), (1, 1))", "add padding to all the things",),
	("PSGVAL_SZ_PKLNAME_DEV", FMAXPSG_SCTN0900_STR_DEF, "SZ_PKLNAME_DEV", "runawayClock_DEV.pkl", "name of the pkl file for the app in dev",),
	("PSGVAL_SZ_PKLNAME_PROD", FMAXPSG_SCTN0900_STR_DEF, "SZ_PKLNAME_PROD", "runawayClock.pkl", "name of the pkl file for the app in use",),
	("PSGVAL_SZ_RUNAWAY", FMAXPSG_SCTN0900_VAL_DEF, "SZ_RUNAWAY", "False", "default runaway state",),
	("PSGVAL_SZ_TIMEMS_BETWEEN_MOUSE_CHECKS", FMAXPSG_SCTN0900_VAL_DEF, "SZ_TIMEMS_BETWEEN_MOUSE_CHECKS", "300", "throttle mouse checking",),
	("PSGVAL_SZ_TIMEMS_BETWEEN_MOVES", FMAXPSG_SCTN0900_VAL_DEF, "SZ_TIMEMS_BETWEEN_MOVES", "500", "time_ms between moves",),
	("PSGVAL_SZ_TIMEMS_BETWEEN_UPDATES", FMAXPSG_SCTN0900_VAL_DEF, "SZ_TIMEMS_BETWEEN_UPDATES", "500", "time_ms between updating windows/frames/etc",),
	("PSGVAL_SZ_TIMEOUT_MS", FMAXPSG_SCTN0900_VAL_DEF, "SZ_TIMEOUT_MS", "100", "timeout for PSG",),
	("PSGVAL_SZ_TIMES_BETWEEN_PERIODIC_JOB", FMAXPSG_SCTN0900_VAL_DEF, "SZ_TIMES_BTWN_PERIODIC_JOB", "900", "time between periodic job runnings",),
	("PSGVAL_TIMEH_ADJUST_HRS", FMAXPSG_SCTN0900_VAL_DEF, "TIMEH_ADJUST_HRS", "0", "comment",),
	("PSGVAL_TIMEM_ADJUST_MINS", FMAXPSG_SCTN0900_VAL_DEF, "TIMEM_ADJUST_MINS", "0", "comment",),
	("PSGVAL_TITLE", FMAX_NOP, "titles start here",),
	("PSGVAL_TITLE_ALARMPOPUP", FMAXPSG_SCTN0900_STR_DEF, "TITLE_ALARMPOPUP", "ALERT", "string with window title for APPMODE_CLOCKS",),
	("PSGVAL_TITLE_CLOCKS", FMAXPSG_SCTN0900_STR_DEF, "TITLE_CLOCKS", "CLOCKS", "string with window title for APPMODE_CLOCKS",),
	("PSGVAL_TITLE_EDIT", FMAXPSG_SCTN0900_STR_DEF, "TITLE_EDIT", "edit an event", "string with window title for APPMODE_CLOCKS",),
	("PSGVAL_TITLE_MAIN", FMAXPSG_SCTN0900_STR_DEF, "TITLE_MAIN", "Main window which is xpanded from CLOCKS window and pops up EDIT windows", "string with window title for APPMODE_CLOCKS",),
	("PSGVAL_TITLE_THECLOCK", FMAXPSG_SCTN0900_STR_DEF, "TITLE_THECLOCK", "THECLOCK", "string with window title for APPMODE_CLOCKS",),
	("PSGVAL_ZERO_CLOCK", FMAXPSG_SCTN0900_VAL_DEF, "ZERO_CLOCK", "0", "all the zeros",),
	("PSGVAL_ZERO_CLOCKSTR", FMAXPSG_SCTN0900_STR_DEF, "ZERO_CLOCKSTR", "00:00:00", "all the zeros",),
	("PSGVAL__ALL_THE_FRAMES", FMAXPSG_SCTN0902_DICT_DEF, "ALL_THE_FRAMES", "comment",),
	("PSGVAL__ALL_THE_FRAMES", FMAXPSG_SCTN0902_DICT_VV_ADD, "ALL_THE_FRAMES", "FRAME_CLOCKS", "None", "ENTRY IN FORMS",),
	("PSGVAL__ALL_THE_FRAMES", FMAXPSG_SCTN0902_DICT_VV_ADD, "ALL_THE_FRAMES", "FRAME_POPUP01", "None", "ENTRY IN FORMS",),
	("PSGVAL__ALL_THE_FRAMES", FMAXPSG_SCTN0902_DICT_VV_ADD, "ALL_THE_FRAMES", "FRAME_POPUP02", "None", "ENTRY IN FORMS",),
	("PSGVAL__ALL_THE_FRAMES", FMAXPSG_SCTN0902_DICT_VV_ADD, "ALL_THE_FRAMES", "FRAME_POPUP03", "None", "ENTRY IN FORMS",),
	("PSGVAL__ALL_THE_FRAMES", FMAXPSG_SCTN0902_DICT_VV_ADD, "ALL_THE_FRAMES", "FRAME_POPUP04", "None", "ENTRY IN FORMS",),
	("PSGVAL__ALL_THE_FRAMES", FMAXPSG_SCTN0902_DICT_VV_ADD, "ALL_THE_FRAMES", "FRAME_POPUP05", "None", "ENTRY IN FORMS",),
	("PSGVAL__ALL_TIMES_LIST00", FMAXPSG_SCTN0903_LIST_DEF, "ALL_TIMES_LIST", "list of all times",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_AT_LAST_RUN", "list of all times K_TIME_AT_LAST_RUN",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_AT_NEXT_ALERT", "list of all times K_TIME_AT_NEXT_ALERT",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_AT_ZEROELAPSE", "list of all times K_TIME_AT_ZEROELAPSE",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_CLOCK", "list of all times K_TIME_CLOCK",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_ELAPSED", "list of all times K_TIME_ELAPSED",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_INTERVAL", "list of all times K_TIME_INTERVAL",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_INTERVAL_START", "list of all times K_TIME_INTERVAL_START",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_INTERVAL__BEGIN", "list of all times K_TIME_INTERVAL__BEGIN",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_INTERVAL__END", "list of all times K_TIME_INTERVAL__END",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_LEN_OF_ALERT", "list of all times K_TIME_LEN_OF_ALERT",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_TOGO", "list of all times K_TIME_TOGO",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_TO_CHECK_MOUSE", "list of all times K_TIME_TO_CHECK_MOUSE",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_TO_MOVE", "list of all times K_TIME_TO_MOVE",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_TO_UPDATE", "list of all times K_TIME_TO_UPDATE",),
	("PSGVAL__ALL_TIMES_LIST01", FMAXPSG_SCTN0903_LIST_VAL_ADD, "ALL_TIMES_LIST", "K_TIME_ALARM", "list of all times K_TIME_ALARM",),
	("PSGVAL__APPDS", FMAX_NOP, "APP Data Storage",),
	("PSGVAL__APPDS_MAIN_00", FMAXPSG_SCTN090C_APPDS_DEF, "APPDS_MAIN", "the struct holding everything passed betwixt PySimpleGUI and this app",),
	("PSGVAL__APPDS_MAIN_01", FMAXPSG_SCTN090C_APPDS_VS_ADD, "APPDS_MAIN", "K_VERSION", "00000001", "version number hex string",),
	("PSGVAL__APPDS_MAIN_01", FMAXPSG_SCTN090C_APPDS_VV_ADD, "APPDS_MAIN", "K_APPMODE", "APPMODE_NONE", "no appmode set",),
	("PSGVAL__APPDS_MAIN_01", FMAXPSG_SCTN090C_APPDS_VV_ADD, "APPDS_MAIN", "K_CHECKBOX_ALPHA_DIM", "True", "dim when mouse over bool",),
	("PSGVAL__APPDS_MAIN_01", FMAXPSG_SCTN090C_APPDS_VV_ADD, "APPDS_MAIN", "K_CHECKBOX_RUNAWAY", "False", "runaway from the mouse bool",),
	("PSGVAL__APPDS_MAIN_01", FMAXPSG_SCTN090C_APPDS_VV_ADD, "APPDS_MAIN", "K_INDEX_OF_NEXT_EVENT", "0", "index of the next event to alert",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_DEF, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "holds events",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_ALARMPOPUP_TEXT_TEXT", "get up, move around", "alarm text for this event",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_EVENT_NAME", "MOVE", "this entry's name",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_AUTO_CLOSE_DURATION", "10", "time of this event",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_DISMISSED", "False", "is this event dismissed",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_ENABLED", "True", "is this event enabled",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_EVENTMODE", "EVENTMODE_INTERVAL", "this entry's event_mode",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_FIRSTRUN", "True", "are we initializing or not",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_FRAMENAME", "None", "time of this event",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_INTERVAL_COUNT", "0", "count of number of times this has alerted since last reset",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_IS_ALERTING_NOW", "False", "count of number of times this has alerted since last reset",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_PREDISMISSABLE", "True", "is this event dismissable in advance",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_SNOOZABLE", "False", "can this event be snoozed",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_SNOOZED", "False", "is this event snoozed",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_TIME_ALARM", "0", "time of this event if it an alarm",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_TIME_AT_LAST_RUN", "0", "time this alarm last ran, now if running",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_TIME_AT_NEXT_ALERT", "ZERO_CLOCK", "time next time this alarm goes off",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_TIME_INTERVAL", "CF.HALFHOURSECS", "interval of this event",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_TIME_INTERVAL_START", "ZERO_CLOCK", "time of the day this round of interval started",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_TIME_INTERVAL__BEGIN", "ZERO_CLOCK", "time of the day this interval is made active",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_TIME_INTERVAL__END", "ZERO_CLOCK", "time of the day this interval is no longer active",),
	("PSGVAL__APPDS_MAIN_02", FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD, "APPDS_MAIN", "K_EVENT_ENTRIES", "0", "K_TIME_LEN_OF_ALERT", "ZERO_CLOCK", "length of time to alert this event before auto closing it",),
	("PSGVAL__APPDS_MIDNIGHT_FIX_TIMES_LIST", FMAXPSG_SCTN0903_LIST_DEF, "APPDS_MIDNIGHT_FIX_TIMES_LIST", "list of times to be updated at midnight",),
	("PSGVAL__APPDS_MIDNIGHT_FIX_TIMES_LIST", FMAXPSG_SCTN0903_LIST_VAL_ADD, "APPDS_MIDNIGHT_FIX_TIMES_LIST", "K_TIME_AT_NEXT_ALERT", "list of times to be updated at midnight",),
	("PSGVAL__APPDS_MIDNIGHT_FIX_TIMES_LIST", FMAXPSG_SCTN0903_LIST_VAL_ADD, "APPDS_MIDNIGHT_FIX_TIMES_LIST", "K_TIME_TO_CHECK_MOUSE", "list of times to be updated at midnight",),
	("PSGVAL__APPDS_MIDNIGHT_FIX_TIMES_LIST", FMAXPSG_SCTN0903_LIST_VAL_ADD, "APPDS_MIDNIGHT_FIX_TIMES_LIST", "K_TIME_TO_MOVE", "list of times to be updated at midnight",),
	("PSGVAL__APPDS_MIDNIGHT_FIX_TIMES_LIST", FMAXPSG_SCTN0903_LIST_VAL_ADD, "APPDS_MIDNIGHT_FIX_TIMES_LIST", "K_TIME_TO_UPDATE", "list of times to be updated at midnight",),
	("PSGVAL__BTN_DISMISS20", FMAX_NOP, "start of the dismiss button for alarms",),
	("PSGVAL__BTN_DISMISS2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_DISMISS20", "",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_DISMISS20", "BUTTON_TEXT", "", "button_text empty for the DOWN button",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_DISMISS20", "IMAGE_FILENAME", "res/dismiss20.png", "filename for the button icon",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DISMISS20", "BORDER_WIDTH", "0", "button xpand key",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DISMISS20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DISMISS20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DISMISS20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DISMISS20", "KEY", "K_BTN_DISMISS", "button xpand font",),
	("PSGVAL__BTN_DISMISS2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DISMISS20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_DOWN20", FMAX_NOP, "clocks down20 button",),
	("PSGVAL__BTN_DOWN2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_DOWN20", "",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_DOWN20", "BUTTON_TEXT", "", "button_text empty for the DOWN button",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_DOWN20", "IMAGE_FILENAME", "res/down20.png", "filename for the button icon",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN20", "BORDER_WIDTH", "0", "button xpand key",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN20", "KEY", "K_BTN_DOWN", "button xpand font",),
	("PSGVAL__BTN_DOWN2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_DOWN32", FMAX_NOP, "clocks down32 button",),
	("PSGVAL__BTN_DOWN3200", FMAXPSG_SCTN0906_BTN_DEF, "BTN_DOWN32", "",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_DOWN32", "BUTTON_TEXT", "", "button_text empty for the DOWN button",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_DOWN32", "IMAGE_FILENAME", "res/down32.png", "filename for the button icon",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN32", "BORDER_WIDTH", "0", "button xpand key",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN32", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN32", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN32", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN32", "KEY", "K_BTN_DOWN", "focus on click",),
	("PSGVAL__BTN_DOWN3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_DOWN32", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_EDIT20", FMAX_NOP, "clocks edit20 button",),
	("PSGVAL__BTN_EDIT2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_EDIT20", "",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_EDIT20", "BUTTON_TEXT", "", "button_text empty for the EDIT button",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_EDIT20", "IMAGE_FILENAME", "res/edit20.png", "filename for the button icon",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT20", "KEY", "K_BTN_EDIT", "button xpand font",),
	("PSGVAL__BTN_EDIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_EDIT32", FMAX_NOP, "clocks edit32 button",),
	("PSGVAL__BTN_EDIT3200", FMAXPSG_SCTN0906_BTN_DEF, "BTN_EDIT32", "",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_EDIT32", "BUTTON_TEXT", "", "button_text empty for the EDIT button",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_EDIT32", "IMAGE_FILENAME", "res/edit32.png", "filename for the button icon",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT32", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT32", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT32", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT32", "KEY", "K_BTN_EDIT", "button xpand key",),
	("PSGVAL__BTN_EDIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_EDIT32", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_QUIT20", FMAX_NOP, "clocks quit20 button",),
	("PSGVAL__BTN_QUIT2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_QUIT20", "",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_QUIT20", "BUTTON_TEXT", "", "button_text empty for the QUIT button",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_QUIT20", "IMAGE_FILENAME", "res/quit20.png", "filename for the button icon",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_QUIT20", "TOOLTIP", "quit the app", "button_text empty for the QUIT button",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT20", "KEY", "K_BTN_QUIT_ALL", "button xpand font",),
	("PSGVAL__BTN_QUIT2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_QUIT32", FMAX_NOP, "clocks quit32 button",),
	("PSGVAL__BTN_QUIT3200", FMAXPSG_SCTN0906_BTN_DEF, "BTN_QUIT32", "",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_QUIT32", "BUTTON_TEXT", "", "button_text empty for the QUIT button",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_QUIT32", "IMAGE_FILENAME", "res/quit32.png", "filename for the button icon",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_QUIT32", "TOOLTIP", "quit the app", "button_text empty for the QUIT button",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT32", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT32", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT32", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT32", "KEY", "K_BTN_QUIT_ALL", "button xpand font",),
	("PSGVAL__BTN_QUIT3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_QUIT32", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_UP20", FMAX_NOP, "clocks up20 button",),
	("PSGVAL__BTN_UP2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_UP20", "",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_UP20", "BUTTON_TEXT", "", "button_text empty for the UP button",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_UP20", "IMAGE_FILENAME", "res/up20.png", "filename for the button icon",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP20", "KEY", "K_BTN_UP", "button xpand font",),
	("PSGVAL__BTN_UP2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_UP32", FMAX_NOP, "clocks up32 button",),
	("PSGVAL__BTN_UP3200", FMAXPSG_SCTN0906_BTN_DEF, "BTN_UP32", "",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_UP32", "BUTTON_TEXT", "", "button_text empty for the UP button",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_UP32", "IMAGE_FILENAME", "res/up32.png", "filename for the button icon",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP32", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP32", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP32", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP32", "KEY", "K_BTN_UP", "button up key",),
	("PSGVAL__BTN_UP3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_UP32", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_XPAND20", FMAX_NOP, "clocks xpand20 button",),
	("PSGVAL__BTN_XPAND2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_XPAND20", "",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_XPAND20", "BUTTON_TEXT", "", "button_text empty for the XPAND button",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_XPAND20", "IMAGE_FILENAME", "res/xpand20.png", "filename for the button icon",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_XPAND20", "TOOLTIP", "expand to the big window from where you can edit events", "tooltip",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND20", "KEY", "K_BTN_XPAND", "focus on click",),
	("PSGVAL__BTN_XPAND2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_XPAND32", FMAX_NOP, "clocks xpand32 button",),
	("PSGVAL__BTN_XPAND3200", FMAXPSG_SCTN0906_BTN_DEF, "BTN_XPAND32", "",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_XPAND32", "BUTTON_TEXT", "", "button_text empty for the XPAND button",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_XPAND32", "IMAGE_FILENAME", "res/xpand32.png", "filename for the button icon",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_XPAND32", "TOOLTIP", "expand to the big window from where you can edit events", "tooltip",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND32", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND32", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND32", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND32", "KEY", "K_BTN_XPAND", "button xpand font",),
	("PSGVAL__BTN_XPAND3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_XPAND32", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_ZERO20", FMAX_NOP, "clocks zero20 button",),
	("PSGVAL__BTN_ZERO2000", FMAXPSG_SCTN0906_BTN_DEF, "BTN_ZERO20", "",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_ZERO20", "BUTTON_TEXT", "", "button_text empty for the ZERO button",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_ZERO20", "IMAGE_FILENAME", "res/zero20.png", "filename for the button icon",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_ZERO20", "TOOLTIP", "zero the elapsed timer", "tooltip",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO20", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO20", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO20", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO20", "KEY", "K_BTN_ZERO", "button zero key",),
	("PSGVAL__BTN_ZERO2001", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO20", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__BTN_ZERO32", FMAX_NOP, "clocks zero32 button",),
	("PSGVAL__BTN_ZERO3200", FMAXPSG_SCTN0906_BTN_DEF, "BTN_ZERO32", "",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_ZERO32", "BUTTON_TEXT", "", "button_text empty for the ZERO button",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_ZERO32", "IMAGE_FILENAME", "res/zero32.png", "filename for the button icon",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_STR_ADD, "BTN_ZERO32", "TOOLTIP", "zero the elapsed timer", "tooltip",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO32", "BUTTON_COLOR", "COLORS_BTN_NORMAL", "default button color",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO32", "FOCUS", "True", "focus on click",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO32", "FONT", "FONTSZ_BTNS", "button xpand font",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO32", "KEY", "K_BTN_ZERO", "button zero key",),
	("PSGVAL__BTN_ZERO3201", FMAXPSG_SCTN0906_BTN_VAL_ADD, "BTN_ZERO32", "PAD", "SZ_PAD_ALL", "button xpand key",),
	("PSGVAL__CHECKBOX_ALPHA_DIM01", FMAX_NOP, "alpha=0 under mouse",),
	("PSGVAL__CHECKBOX_ALPHA_DIM0100", FMAXPSG_SCTN0908_CHECKBOX_DEF, "CHECKBOX_ALPHA_DIM01", "checkbox for alpha under mouse",),
	("PSGVAL__CHECKBOX_ALPHA_DIM0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_ALPHA_DIM01", "TEXT", "K_ALPHA_LOW", "simple text reminder",),
	("PSGVAL__CHECKBOX_ALPHA_DIM0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_ALPHA_DIM01", "TOOLTIP", "low alpha under mouse", "comment",),
	("PSGVAL__CHECKBOX_ALPHA_DIM0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_ALPHA_DIM01", "DEFAULT", "True", "leave it on by default",),
	("PSGVAL__CHECKBOX_ALPHA_DIM0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_ALPHA_DIM01", "ENABLE_EVENTS", "True", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_ALPHA_DIM0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_ALPHA_DIM01", "KEY", "K_CHECKBOX_ALPHA_DIM", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_DISMISSED01", FMAX_NOP, "dismissed or not checkbox",),
	("PSGVAL__CHECKBOX_DISMISSED0100", FMAXPSG_SCTN0908_CHECKBOX_DEF, "CHECKBOX_DISMISSED01", "checkbox for dismissed from mouse behavior",),
	("PSGVAL__CHECKBOX_DISMISSED0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_DISMISSED01", "TEXT", "K_DISMISSED", "text label",),
	("PSGVAL__CHECKBOX_DISMISSED0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_DISMISSED01", "TOOLTIP", "bool dismiss this event early", "event has been dismissed bool",),
	("PSGVAL__CHECKBOX_DISMISSED0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_DISMISSED01", "DEFAULT", "False", "leave it off by default",),
	("PSGVAL__CHECKBOX_DISMISSED0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_DISMISSED01", "ENABLE_EVENTS", "True", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_DISMISSED0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_DISMISSED01", "KEY", "K_CHECKBOX_DISMISSED", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_ENABLED01", FMAX_NOP, "enabled or not checkbox",),
	("PSGVAL__CHECKBOX_ENABLED0100", FMAXPSG_SCTN0908_CHECKBOX_DEF, "CHECKBOX_ENABLED01", "checkbox for dismissed from mouse behavior",),
	("PSGVAL__CHECKBOX_ENABLED0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_ENABLED01", "TEXT", "ENABLED", "text label",),
	("PSGVAL__CHECKBOX_ENABLED0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_ENABLED01", "TOOLTIP", "event enabled bool", "tooltip",),
	("PSGVAL__CHECKBOX_ENABLED0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_ENABLED01", "DEFAULT", "False", "leave it off by default",),
	("PSGVAL__CHECKBOX_ENABLED0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_ENABLED01", "ENABLE_EVENTS", "True", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_ENABLED0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_ENABLED01", "KEY", "K_CHECKBOX_ENABLED", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_FIRSTRUN01", FMAX_NOP, "firstrun or not checkbox",),
	("PSGVAL__CHECKBOX_FIRSTRUN0100", FMAXPSG_SCTN0908_CHECKBOX_DEF, "CHECKBOX_FIRSTRUN01", "checkbox for dismissed from mouse behavior",),
	("PSGVAL__CHECKBOX_FIRSTRUN0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_FIRSTRUN01", "TEXT", "K_FIRSTRUN", "text label",),
	("PSGVAL__CHECKBOX_FIRSTRUN0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_FIRSTRUN01", "TOOLTIP", "first run bool", "tooltip",),
	("PSGVAL__CHECKBOX_FIRSTRUN0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_FIRSTRUN01", "DEFAULT", "False", "leave it off by default",),
	("PSGVAL__CHECKBOX_FIRSTRUN0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_FIRSTRUN01", "ENABLE_EVENTS", "True", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_FIRSTRUN0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_FIRSTRUN01", "KEY", "K_CHECKBOX_FIRSTRUN", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_HOVER_DATE01", FMAX_NOP, "dismissed or not checkbox",),
	("PSGVAL__CHECKBOX_HOVER_DATE0100", FMAXPSG_SCTN0908_CHECKBOX_DEF, "CHECKBOX_HOVER_DATE01", "checkbox for dismissed from mouse behavior",),
	("PSGVAL__CHECKBOX_HOVER_DATE0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_HOVER_DATE01", "TEXT", "DT on hover", "text label",),
	("PSGVAL__CHECKBOX_HOVER_DATE0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_HOVER_DATE01", "TOOLTIP", "show date when hovering over clock", "tooltip",),
	("PSGVAL__CHECKBOX_HOVER_DATE0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_HOVER_DATE01", "DEFAULT", "True", "leave it on by default",),
	("PSGVAL__CHECKBOX_HOVER_DATE0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_HOVER_DATE01", "ENABLE_EVENTS", "True", "set the events on for the checkbox",),
	("PSGVAL__CHECKBOX_HOVER_DATE0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_HOVER_DATE01", "KEY", "K_CHECKBOX_HOVER_DATE", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_IS_ALERTING_NOW01", FMAX_NOP, "is alerting now or not checkbox",),
	("PSGVAL__CHECKBOX_IS_ALERTING_NOW0100", FMAXPSG_SCTN0908_CHECKBOX_DEF, "CHECKBOX_IS_ALERTING_NOW01", "checkbox for dismissed from mouse behavior",),
	("PSGVAL__CHECKBOX_IS_ALERTING_NOW0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_IS_ALERTING_NOW01", "TEXT", "IS_ALERTING_NOW", "text label",),
	("PSGVAL__CHECKBOX_IS_ALERTING_NOW0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_IS_ALERTING_NOW01", "TOOLTIP", "run away from mouse when checked", "tooltip",),
	("PSGVAL__CHECKBOX_IS_ALERTING_NOW0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_IS_ALERTING_NOW01", "DEFAULT", "False", "leave it off by default",),
	("PSGVAL__CHECKBOX_IS_ALERTING_NOW0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_IS_ALERTING_NOW01", "ENABLE_EVENTS", "True", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_IS_ALERTING_NOW0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_IS_ALERTING_NOW01", "KEY", "K_CHECKBOX_IS_ALERTING_NOW", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_PREDISMISSABLE01", FMAX_NOP, "pre-dismissable or not checkbox",),
	("PSGVAL__CHECKBOX_PREDISMISSABLE0100", FMAXPSG_SCTN0908_CHECKBOX_DEF, "CHECKBOX_PREDISMISSABLE01", "checkbox for dismissed from mouse behavior",),
	("PSGVAL__CHECKBOX_PREDISMISSABLE0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_PREDISMISSABLE01", "TEXT", "K_PREDISMISSABLE", "text label",),
	("PSGVAL__CHECKBOX_PREDISMISSABLE0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_PREDISMISSABLE01", "TOOLTIP", "run away from mouse when checked", "tooltip",),
	("PSGVAL__CHECKBOX_PREDISMISSABLE0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_PREDISMISSABLE01", "DEFAULT", "False", "leave it off by default",),
	("PSGVAL__CHECKBOX_PREDISMISSABLE0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_PREDISMISSABLE01", "ENABLE_EVENTS", "True", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_PREDISMISSABLE0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_PREDISMISSABLE01", "KEY", "K_CHECKBOX_PREDISMISSABLE", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_RUNAWAY01", FMAX_NOP, "run away or not checkbox",),
	("PSGVAL__CHECKBOX_RUNAWAY0100", FMAXPSG_SCTN0908_CHECKBOX_DEF, "CHECKBOX_RUNAWAY01", "checkbox for runaway from mouse behavior",),
	("PSGVAL__CHECKBOX_RUNAWAY0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_RUNAWAY01", "TEXT", "RUNAWAY", "text label",),
	("PSGVAL__CHECKBOX_RUNAWAY0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_RUNAWAY01", "TOOLTIP", "run away from mouse when checked", "tooltip",),
	("PSGVAL__CHECKBOX_RUNAWAY0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_RUNAWAY01", "DEFAULT", "False", "leave it off by default",),
	("PSGVAL__CHECKBOX_RUNAWAY0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_RUNAWAY01", "ENABLE_EVENTS", "True", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_RUNAWAY0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_RUNAWAY01", "KEY", "K_CHECKBOX_RUNAWAY", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_SNOOZABLE01", FMAX_NOP, "snoozable or not checkbox",),
	("PSGVAL__CHECKBOX_SNOOZABLE0100", FMAXPSG_SCTN0908_CHECKBOX_DEF, "CHECKBOX_SNOOZABLE01", "checkbox for dismissed from mouse behavior",),
	("PSGVAL__CHECKBOX_SNOOZABLE0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_SNOOZABLE01", "TEXT", "K_SNOOZABLE", "text label",),
	("PSGVAL__CHECKBOX_SNOOZABLE0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_SNOOZABLE01", "TOOLTIP", "run away from mouse when checked", "tooltip",),
	("PSGVAL__CHECKBOX_SNOOZABLE0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_SNOOZABLE01", "DEFAULT", "False", "leave it off by default",),
	("PSGVAL__CHECKBOX_SNOOZABLE0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_SNOOZABLE01", "ENABLE_EVENTS", "True", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_SNOOZABLE0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_SNOOZABLE01", "KEY", "K_CHECKBOX_SNOOZABLE", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_SNOOZED01", FMAX_NOP, "snoozed or not checkbox",),
	("PSGVAL__CHECKBOX_SNOOZED0100", FMAXPSG_SCTN0908_CHECKBOX_DEF, "CHECKBOX_SNOOZED01", "checkbox for dismissed from mouse behavior",),
	("PSGVAL__CHECKBOX_SNOOZED0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_SNOOZED01", "TEXT", "K_SNOOZED", "text label",),
	("PSGVAL__CHECKBOX_SNOOZED0101", FMAXPSG_SCTN0908_CHECKBOX_STR_ADD, "CHECKBOX_SNOOZED01", "TOOLTIP", "run away from mouse when checked", "tooltip",),
	("PSGVAL__CHECKBOX_SNOOZED0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_SNOOZED01", "DEFAULT", "False", "leave it off by default",),
	("PSGVAL__CHECKBOX_SNOOZED0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_SNOOZED01", "ENABLE_EVENTS", "True", "set the key for the checkbox",),
	("PSGVAL__CHECKBOX_SNOOZED0101", FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD, "CHECKBOX_SNOOZED01", "KEY", "K_CHECKBOX_SNOOZED", "set the key for the checkbox",),
	("PSGVAL__CLOCKS", FMAXPSG_SCTN09FF_CLASS_DEF, "CLOCKS", "comment",),
	("PSGVAL__CLOCKS_COLUMN01", FMAX_NOP, "the COLUMN01 for APPMODE_CLOCKS",),
	("PSGVAL__CLOCKS_COLUMN0100", FMAXPSG_SCTN09FF_CLASS_COLUMN_DEF, "CLOCKS", "_COLUMN01_", "the column that puts the two smaller clocks below the main one",),
	("PSGVAL__CLOCKS_COLUMN0101", FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_00", "L03", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0102", FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_00", "L04", "COLUMN01_E01", "add a new TEXT element to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0103", FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_00", "L05", "COLUMN01_E01", "**self._TEXT_TIME_CLOCK_", "add the main clock",),
	("PSGVAL__CLOCKS_COLUMN0104", FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_01", "L03", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0105", FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_01", "L04", "COLUMN01_E02", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0106", FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_01", "L05", "COLUMN01_E02", "**self._TEXT_TIME_AT_ZEROELAPSE_", "add time to go",),
	("PSGVAL__CLOCKS_COLUMN0107", FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_01", "L04", "COLUMN01_E03", "add a new text element to row01 clocks column",),
	("PSGVAL__CLOCKS_COLUMN0108", FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_01", "L05", "COLUMN01_E03", "**self._TEXT_TIME_ELAPSED_", "add elapsed time",),
	("PSGVAL__CLOCKS_COLUMN0109", FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_02", "L03", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN010A", FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_02", "L04", "COLUMN01_E04", "add a new text element to row01 clocks column",),
	("PSGVAL__CLOCKS_COLUMN010B", FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_02", "L05", "COLUMN01_E04", "**self._TEXT_TIME_TOGO_", "add elapsed time",),
	("PSGVAL__CLOCKS_COLUMN010C", FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_02", "L04", "COLUMN01_E05", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN010D", FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_02", "L05", "COLUMN01_E05", "**self._TEXT_TIME_AT_NEXT_ALERT_", "add time to go",),
	("PSGVAL__CLOCKS_COLUMN010E", FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_03", "L03", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN010F", FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_03", "L04", "COLUMN01_E08", "add a new text element to row01 clocks column",),
	("PSGVAL__CLOCKS_COLUMN0110", FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_03", "L05", "COLUMN01_E08", "**self._TEXT_NAME_NEXT_EVENT_", "add the main clock",),
	("PSGVAL__CLOCKS_COLUMN0111", FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_04", "L03", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0112", FMAXPSG_SCTN09FF_CLASS_COLUMN_CHECKBOX_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_04", "L04", "COLUMN01_E06", "add a new text element to row01 clocks column",),
	("PSGVAL__CLOCKS_COLUMN0113", FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_04", "L05", "COLUMN01_E06", "**CHECKBOX_RUNAWAY01", "add elapsed time",),
	("PSGVAL__CLOCKS_COLUMN0114", FMAXPSG_SCTN09FF_CLASS_COLUMN_CHECKBOX_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_04", "L04", "COLUMN01_E07", "add a new text element to row01 clocks column",),
	("PSGVAL__CLOCKS_COLUMN0115", FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN01_", "COLUMN01_ROW_04", "L05", "COLUMN01_E07", "**CHECKBOX_ALPHA_DIM01", "add elapsed time",),
	("PSGVAL__CLOCKS_COLUMN02", FMAX_NOP, "the COLUMN02 for APPMODE_CLOCKS",),
	("PSGVAL__CLOCKS_COLUMN0200", FMAXPSG_SCTN09FF_CLASS_COLUMN_DEF, "CLOCKS", "_COLUMN02_", "the column that puts the two smaller clocks below the main one",),
	("PSGVAL__CLOCKS_COLUMN0201", FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_01", "L03", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0202", FMAXPSG_SCTN09FF_CLASS_COLUMN_BUTTON_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_01", "L04", "COLUMN02_E01", "add a button element to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0203", FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_01", "L05", "COLUMN02_E01", "**BTN_QUIT20", "add the xpand button to clocks",),
	("PSGVAL__CLOCKS_COLUMN0204", FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_02", "L03", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0205", FMAXPSG_SCTN09FF_CLASS_COLUMN_BUTTON_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_02", "L04", "COLUMN02_E02", "add reset button for elapsed time",),
	("PSGVAL__CLOCKS_COLUMN0206", FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_02", "L05", "COLUMN02_E02", "**BTN_ZERO20", "add the zero button to clocks",),
	("PSGVAL__CLOCKS_COLUMN0207", FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_03", "L03", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN0208", FMAXPSG_SCTN09FF_CLASS_COLUMN_BUTTON_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_03", "L04", "COLUMN02_E03", "add reset button for elapsed time",),
	("PSGVAL__CLOCKS_COLUMN0209", FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_03", "L05", "COLUMN02_E03", "**BTN_XPAND20", "add the zero button to clocks",),
	("PSGVAL__CLOCKS_COLUMN020A", FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_04", "L03", "add a new row to clocks column",),
	("PSGVAL__CLOCKS_COLUMN020B", FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_04", "L04", "COLUMN02_E04", "add reset button for elapsed time",),
	("PSGVAL__CLOCKS_COLUMN020C", FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD, "CLOCKS", "_COLUMN02_", "COLUMN02_ROW_04", "L05", "COLUMN02_E04", "**self._TEXT_INTERVAL_COUNT_", "add the zero button to clocks",),
	("PSGVAL__CLOCKS_DICT_KEYS_INT00", FMAXPSG_SCTN09FF_CLASS_DICT_DEF, "CLOCKS", "_DICT_KEYS_INT_", "dict of integer keys and their format",),
	("PSGVAL__CLOCKS_DICT_KEYS_INT01", FMAXPSG_SCTN09FF_CLASS_DICT_VS_ADD, "CLOCKS", "_DICT_KEYS_INT_", "K_INTERVAL_COUNT", "04d", "intervalCount:04d",),
	("PSGVAL__CLOCKS_DICT_KEYS_TIME00", FMAXPSG_SCTN09FF_CLASS_DICT_DEF, "CLOCKS", "_DICT_KEYS_TIME_", "dict of time keys and their max value int seconds",),
	("PSGVAL__CLOCKS_DICT_KEYS_TIME01", FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD, "CLOCKS", "_DICT_KEYS_TIME_", "K_TIME_AT_NEXT_ALERT", "CF.DAYSECS", "comment",),
	("PSGVAL__CLOCKS_DICT_KEYS_TIME01", FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD, "CLOCKS", "_DICT_KEYS_TIME_", "K_TIME_AT_ZEROELAPSE", "CF.DAYSECS", "comment",),
	("PSGVAL__CLOCKS_DICT_KEYS_TIME01", FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD, "CLOCKS", "_DICT_KEYS_TIME_", "K_TIME_CLOCK", "CF.DAYSECS", "",),
	("PSGVAL__CLOCKS_DICT_KEYS_TIME01", FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD, "CLOCKS", "_DICT_KEYS_TIME_", "K_TIME_ELAPSED", "CF.TIME995959", "",),
	("PSGVAL__CLOCKS_DICT_KEYS_TIME01", FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD, "CLOCKS", "_DICT_KEYS_TIME_", "K_TIME_TOGO", "CF.DAYSECS", "",),
	("PSGVAL__CLOCKS_DPD00", FMAXPSG_SCTN09FF_CLASS_DPD_DEF, "CLOCKS", "_DPD_", "define a DPD CLOCKS:/",),
	("PSGVAL__CLOCKS_DPD01", FMAXPSG_SCTN09FF_CLASS_DPD_VV_ADD, "CLOCKS", "_DPD_", "F___INIT__", "True", "define a DPD /",),
	("PSGVAL__CLOCKS_FORMMAIN", FMAX_NOP, "the form for clocks",),
	("PSGVAL__CLOCKS_FORMMAIN00", FMAXPSG_SCTN09FF_CLASS_FORMMAIN_DEF, "CLOCKS", "_WINDOW_", "True", "the clocks form defined and done",),
	("PSGVAL__CLOCKS_FUNC_00_INIT", FMAXPSG_SCTN09FF_CLASS_INIT_DEF, "CLOCKS", ", keyBase_, formName_", "init parms defined",),
	("PSGVAL__CLOCKS_FUNC_00_INIT000", FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL, "CLOCKS", "_THIS_KEY_BASE_", "keyBase_", "adopt keyBase_",),
	("PSGVAL__CLOCKS_FUNC_00_INIT001", FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LAMBDA, "CLOCKS", "_USE_THIS_KEY_", "__KEY_TEXT__: %FTQ%%OBRCE%__KEY_TEXT__%CBRCE%%OBRCE%self._THIS_KEY_BASE_%CBRCE%%TQ%", "make a local key sourcer",),
	("PSGVAL__CLOCKS_FUNC_00_INIT002", FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL, "CLOCKS", "_THIS_FORM_NAME_", "formName_", "adopt formName_",),
	("PSGVAL__CLOCKS_FUNC_00_INIT003", FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL, "CLOCKS", "_KEY_DICT_REVERSE_", "{}", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT003", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_KEY_LIST_TIMES_", "[]", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL, "CLOCKS", "_KEY_DICT_", "{}", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_ALPHA_CHANNEL_", "SZ_ALPHA_HIGH", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_ALPHA_HIGH_", "SZ_ALPHA_HIGH", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_ALPHA_LOW_", "SZ_ALPHA_LOW", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_BBOX_", "EMPTY_BBOX", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CHANGED_EVENTS_", "False", "comment",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CHANGED_VALUES_", "False", "comment",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CHECKBOX_RUNAWAY_", "SZ_RUNAWAY", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CLOSE_BBOX_", "EMPTY_BBOX", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENTLY_DIMMED_", "False", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_EVENTMODE_", "None", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_EVENT_", "None", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_LOCATION_", "EMPTY_XY", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_MOUSE_LOCATION_", "EMPTY_XY", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_MOUSE_STATUS_", "MOUSE_STATUS_NONE", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_RESULT_", "None", "comment",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_CURRENT_VALUES", "{}", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_LAST_EVENT_", "None", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_LAST_LOCATION_", "EMPTY_XY", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_LAST_MOUSE_LOCATION_", "EMPTY_XY", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_LAST_MOUSE_STATUS_", "MOUSE_STATUS_NONE", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_LAST_VALUES_", "{}", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_MAINFRAME_", "None", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_MPX_", "EMPTY_XY", "comment",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_SCREEN_DIMS_", "EMPTY_XY", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_SIZE_", "EMPTY_XY", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_TIME_TO_CHECK_MOUSE_", "ZERO_CLOCK", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_TIME_TO_MOVE_", "ZERO_CLOCK", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL, "CLOCKS", "_TIME_TO_UPDATE_", "ZERO_CLOCK", "",),
	("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VS, "CLOCKS", "K_NAME_NEXT_EVENT", "", "True", "name of next event",),
	("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_CHECKBOX_ALPHA_DIM", "False", "False", "value of the alphas dim checkbox",),
	("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_CHECKBOX_RUNAWAY", "False", "False", "value of runaway checkbox",),
	("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_INTERVAL_COUNT", "0", "True", "interval count",),
	("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_TIME_AT_NEXT_ALERT", "ZERO_CLOCK", "True", "time at next event",),
	("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_TIME_AT_ZEROELAPSE", "ZERO_CLOCK", "True", "time at last zero of elapsed timer",),
	("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_TIME_CLOCK", "ZERO_CLOCK", "True", "time clock or wall clock",),
	("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_TIME_ELAPSED", "ZERO_CLOCK", "True", "time elapsed",),
	("PSGVAL__CLOCKS_FUNC_00_INIT02_DICTIN01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV, "CLOCKS", "K_TIME_TOGO", "ZERO_CLOCK", "True", "countdown to next event",),
	("PSGVAL__CLOCKS_FUNC_00_INIT03_KEY01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY, "CLOCKS", "K_CHECKBOX_ALPHA_DIM", "K_CHECKBOX_ALPHA_DIM", "False", "add foreign key for alpha dimming",),
	("PSGVAL__CLOCKS_FUNC_00_INIT03_KEY01", FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY, "CLOCKS", "K_CHECKBOX_RUNAWAY", "K_CHECKBOX_RUNAWAY", "False", "add foreign key for runningaway",),
	("PSGVAL__CLOCKS_FUNC_00_INIT03_LINE0100", FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE, "CLOCKS", "if (self._DPD_[F___INIT__] is True):", "see if debug printing is on",),
	("PSGVAL__CLOCKS_FUNC_00_INIT03_LINE0101", FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE, "CLOCKS", "%TAB1%self.debugPrint(", "debugPrint",),
	("PSGVAL__CLOCKS_FUNC_00_INIT03_LINE0102", FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE, "CLOCKS", "%TAB2%title_=%DQ%__INIT__3%DQ%,", "print _KEY_DICT_REVERSE_",),
	("PSGVAL__CLOCKS_FUNC_00_INIT03_LINE0103", FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE, "CLOCKS", "%TAB2%printDictinS_=True,", "print _KEY_DICT_",),
	("PSGVAL__CLOCKS_FUNC_00_INIT03_LINE0104", FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE, "CLOCKS", "%TAB2%message_=%FTQ%self._KEY_DICT_ {self._KEY_DICT_}", "print _KEY_DICT_",),
	("PSGVAL__CLOCKS_FUNC_00_INIT03_LINE0105", FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE, "CLOCKS", "self._KEY_DICT_REVERSE_ {self._KEY_DICT_REVERSE_}%TQ%)", "print _KEY_DICT_REVERSE_",),
	("PSGVAL__CLOCKS_FUNC_01_ENTER", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "__enter__", "__enter__.py", "False", "define __enter__",),
	("PSGVAL__CLOCKS_FUNC_02_EXIT", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "__exit__", "__exit__.py", "False", "define __exit__ in CLOCKS",),
	("PSGVAL__CLOCKS_FUNC_03_CHECK_MOUSE", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "checkMouse", "checkMouse.py", "False", "define checkMouse",),
	("PSGVAL__CLOCKS_FUNC_03_DEBUG_PRINT", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "debugPrint", "debugPrint.py", "False", "read the frame and set self._RESULT_",),
	("PSGVAL__CLOCKS_FUNC_03_DICTINSTR_REPL", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "dictinstrRepl", "dictinstrRepl.py", "False", "define runaway",),
	("PSGVAL__CLOCKS_FUNC_03_DICTIN_REPL", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "dictinRepl", "dictinRepl.py", "False", "define runaway",),
	("PSGVAL__CLOCKS_FUNC_03_EASY_UPDATE", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "easyUpdate", "easyUpdate.py", "False", "load the whole thing from the file for easyUpdate",),
	("PSGVAL__CLOCKS_FUNC_03_EASY_UPDATEPARMS", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "easyUpdateParms", "easyUpdateParms.py", "False", "load the whole thing from the file for easyUpdate",),
	("PSGVAL__CLOCKS_FUNC_03_ENINT", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "enint", "enint.py", "False", "read the frame and set self._RESULT_",),
	("PSGVAL__CLOCKS_FUNC_03_ENSTRING", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "enstring", "enstring.py", "False", "read the frame and set self._RESULT_",),
	("PSGVAL__CLOCKS_FUNC_03_INTERVALCOUNTOFF", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "intervalCountOff", "intervalCountOff.py", "False", "turn interval count off",),
	("PSGVAL__CLOCKS_FUNC_03_INTERVALCOUNTON", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "intervalCountOn", "intervalCountOn.py", "False", "turn interval count on",),
	("PSGVAL__CLOCKS_FUNC_03_QUICK_READ", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "quickRead", "quickRead.py", "False", "read the frame and set self._RESULT_",),
	("PSGVAL__CLOCKS_FUNC_03_RUNAWAY", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "runaway", "runaway.py", "False", "define runaway",),
	("PSGVAL__CLOCKS_FUNC_03_SETCHECKBOX", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "setCheckbox", "setCheckbox.py", "False", "define runaway",),
	("PSGVAL__CLOCKS_FUNC_03_UPDATE_FROM_DICT", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "updateFromDict", "updateFromDict.py", "False", "update the displayed info from a dict or the default _DICTIN_",),
	("PSGVAL__CLOCKS_FUNC_FF_UPDATE", FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE, "CLOCKS", "update", "update.py", "False", "define the required update function",),
	("PSGVAL__CLOCKS_LAYOUT", FMAX_NOP, "layout for APPMODE_CLOCKS",),
	("PSGVAL__CLOCKS_LAYOUT00", FMAXPSG_SCTN09FF_CLASS_LAYOUT_DEF, "CLOCKS", "_LAYOUT_", "layout for APPMODE_CLOCKS",),
	("PSGVAL__CLOCKS_LAYOUT01", FMAXPSG_SCTN09FF_CLASS_LAYOUT_ROW_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L03", "add a row to the layout",),
	("PSGVAL__CLOCKS_LAYOUT02", FMAXPSG_SCTN09FF_CLASS_LAYOUT_COLUMN_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L04", "LAYOUT_E01", "add a column",),
	("PSGVAL__CLOCKS_LAYOUT03", FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L05", "LAYOUT_E01", "layout", "self._COLUMN01_", "comment",),
	("PSGVAL__CLOCKS_LAYOUT04", FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L05", "LAYOUT_E01", "pad", "SZ_PAD_ALL", "comment",),
	("PSGVAL__CLOCKS_LAYOUT05", FMAXPSG_SCTN09FF_CLASS_LAYOUT_COLUMN_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L04", "LAYOUT_E02", "add a column",),
	("PSGVAL__CLOCKS_LAYOUT06", FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L05", "LAYOUT_E02", "layout", "self._COLUMN02_", "comment",),
	("PSGVAL__CLOCKS_LAYOUT07", FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD, "CLOCKS", "_LAYOUT_", "LAYOUT_ROW_00", "L05", "LAYOUT_E02", "pad", "SZ_PAD_ALL", "comment",),
	("PSGVAL__CLOCKS_RCMENU01", FMAXPSG_SCTN09FF_CLASS_RCMENU_DEF, "CLOCKS", "_RCMENU01_", "right click to do the things",),
	("PSGVAL__CLOCKS_RCMENU0101", FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD, "CLOCKS", "_RCMENU01_", "K_BTN_QUIT_ALL", "quit by right click",),
	("PSGVAL__CLOCKS_RCMENU0101", FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD, "CLOCKS", "_RCMENU01_", "K_BTN_XPAND", "quit by right click",),
	("PSGVAL__CLOCKS_RCMENU0101", FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD, "CLOCKS", "_RCMENU01_", "K_BTN_ZERO", "quit by right click",),
	("PSGVAL__CLOCKS_RCMENU0101", FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD, "CLOCKS", "_RCMENU01_", "K_CHECKBOX_ALPHA_DIM", "toggle K_CHECKBOX_ALPHA_DIM",),
	("PSGVAL__CLOCKS_RCMENU0101", FMAXPSG_SCTN09FF_CLASS_RCMENU_VAL_ADD, "CLOCKS", "_RCMENU01_", "K_CHECKBOX_RUNAWAY", "toggle K_CHECKBOX_RUNAWAY",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT00", FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_INTERVAL_COUNT_", "False", "class text for interval count",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_INTERVAL_COUNT_", "**TEXT_INTERVAL_COUNT", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_INTERVAL_COUNT_", "KEY", "K_INTERVAL_COUNT", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT00", FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_NAME_NEXT_EVENT_", "False", "class text for interval count",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_NAME_NEXT_EVENT_", "**TEXT_NAME_NEXT_EVENT", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_NAME_NEXT_EVENT_", "KEY", "K_NAME_NEXT_EVENT", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT_ALERT00", FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_TIME_AT_NEXT_ALERT_", "True", "class text for interval count",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT_ALERT01", FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_TIME_AT_NEXT_ALERT_", "**TEXT_TIME_AT_NEXT_ALERT", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_NEXT_ALERT01", FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_TIME_AT_NEXT_ALERT_", "KEY", "K_TIME_AT_NEXT_ALERT", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZERO00", FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_TIME_AT_ZEROELAPSE_", "True", "class text for interval count",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZERO01", FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_TIME_AT_ZEROELAPSE_", "**TEXT_TIME_AT_ZEROELAPSE", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_TIME_AT_ZERO01", FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_TIME_AT_ZEROELAPSE_", "KEY", "K_TIME_AT_ZEROELAPSE", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK00", FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_TIME_CLOCK_", "True", "class text for interval count",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_TIME_CLOCK_", "**TEXT_TIME_CLOCK", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_TIME_CLOCK01", FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_TIME_CLOCK_", "KEY", "K_TIME_CLOCK", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED00", FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_TIME_ELAPSED_", "True", "class text for interval count",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_TIME_ELAPSED_", "**TEXT_TIME_ELAPSED", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_TIME_ELAPSED01", FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_TIME_ELAPSED_", "KEY", "K_TIME_ELAPSED", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO00", FMAXPSG_SCTN09FF_CLASS_TEXT_DEF, "CLOCKS", "_TEXT_TIME_TOGO_", "True", "class text for interval count",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD, "CLOCKS", "_TEXT_TIME_TOGO_", "**TEXT_TIME_TOGO", "interval count template",),
	("PSGVAL__CLOCKS_TEXT_TIME_TOGO01", FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD, "CLOCKS", "_TEXT_TIME_TOGO_", "KEY", "K_TIME_TOGO", "interval count template",),
	("PSGVAL__CLOCKS_WINDOW", FMAX_NOP, "the window for APPMODE_CLOCKS",),
	("PSGVAL__CLOCKS_WINDOW00", FMAXPSG_SCTN09FF_CLASS_WINDOW_DEF, "CLOCKS", "_WINDOW_", "define the clocks window",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "ALPHA_CHANNEL", "SZ_ALPHA_HIGH", "set the high alpha as the default",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "BACKGROUND_COLOR", "COLOR_BACKGROUND", "eliminate all not useful on the floating clocks",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "BORDER_DEPTH", "SZ_BORDER_DEPTH", "border depth to zero",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "ELEMENT_PADDING", "SZ_PAD_ALL", "all padding for elements ((1, 1), (1, 1)) by default",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "FORCE_TOPLEVEL", "None", "",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "GRAB_ANYWHERE", "True", "eliminate all not useful on the floating clocks",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "KEEP_ON_TOP", "True", "eliminate all not useful on the floating clocks",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "LAYOUT", "self._LAYOUT_", "add the layout for CLOCKS_WINDOW",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "MARGINS", "SZ_MARGINS_ALL", "",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "NO_TITLEBAR", "True", "no titlebar on APPMODE_CLOCKS window",),
	("PSGVAL__CLOCKS_WINDOW01", FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD, "CLOCKS", "_WINDOW_", "TITLE", "TITLE_CLOCKS", "",),
	("PSGVAL__COLORS", FMAX_NOP, "colors defines",),
	("PSGVAL__COLORS_BTN_NORMAL", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_BTN_NORMAL", "(COLOR_TEXT_NORMAL, COLOR_BACKGROUND)", "comment",),
	("PSGVAL__COLORS_TEXT_HIGH", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_TEXT_HIGH", "(COLOR_TEXT_HIGH, COLOR_BACKGROUND)", "combined colors for a clock text element",),
	("PSGVAL__COLORS_TEXT_LOW", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_TEXT_LOW", "(COLOR_TEXT_LOW, COLOR_BACKGROUND)", "combined colors for a clock text element",),
	("PSGVAL__COLORS_TEXT_NORMAL", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_TEXT_NORMAL", "(COLOR_TEXT_NORMAL, COLOR_BACKGROUND)", "combined colors for a clock text element",),
	("PSGVAL__COLORS_TIME_CLOCK", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_TIME_CLOCK", "(COLOR_TIME_CLOCK, COLOR_CLOCK_BACKGROUND)", "combined colors for a clock text element",),
	("PSGVAL__COLORS_TIME_ELAPSED", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_TIME_ELAPSED", "(COLOR_TIME_ELAPSED, COLOR_CLOCK_BACKGROUND)", "combined colors for a clock text element",),
	("PSGVAL__COLORS_TIME_TOGO", FMAXPSG_SCTN0901_VAL_DEF, "COLORS_TIME_TOGO", "(COLOR_TIME_TOGO, COLOR_CLOCK_BACKGROUND)", "combined colors for a clock text element",),
	("PSGVAL__FONTSZ_ALERT_TEXT", FMAXPSG_SCTN0901_VAL_DEF, "FONTSZ_ALERT_TEXT", "(FONT_DEFAULT, SZ_ALERT_TEXT)", "the font for the clocks only clock",),
	("PSGVAL__FONTSZ_BTNS", FMAXPSG_SCTN0901_VAL_DEF, "FONTSZ_BTNS", "(FONT_DEFAULT, SZ_BTNS)", "comment",),
	("PSGVAL__FONTSZ_CLOCKS_INTERVAL_COUNT", FMAXPSG_SCTN0901_VAL_DEF, "FONTSZ_CLOCKS_INTERVAL_COUNT", "(FONT_DEFAULT, SZ_INTERVAL_COUNT)", "the font for the clocks only clock",),
	("PSGVAL__FONTSZ_CLOCKS_TIME_CLOCK", FMAXPSG_SCTN0901_VAL_DEF, "FONTSZ_CLOCKS_TIME_CLOCK", "(FONT_DEFAULT, SZ_CLOCKS_TIME_CLOCK)", "the font for the clocks only clock",),
	("PSGVAL__FONTSZ_CLOCKS_TIME_ELAPSED", FMAXPSG_SCTN0901_VAL_DEF, "FONTSZ_CLOCKS_TIME_ELAPSED", "(FONT_DEFAULT, SZ_CLOCKS_TIME_ELAPSED)", "the font for the clocks only clock",),
	("PSGVAL__FONTSZ_CLOCKS_TIME_TOGO", FMAXPSG_SCTN0901_VAL_DEF, "FONTSZ_CLOCKS_TIME_TOGO", "(FONT_DEFAULT, SZ_CLOCKS_TIME_TOGO)", "the font for the clocks only clock",),
	("PSGVAL__TEXT_INTERVAL_COUNT", FMAX_NOP, "CLOCKS text interval count",),
	("PSGVAL__TEXT_INTERVAL_COUNT00", FMAXPSG_SCTN0909_TEXT_DEF, "TEXT_INTERVAL_COUNT", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_STR_ADD, "TEXT_INTERVAL_COUNT", "TEXT", "0000", "the text to fill in",),
	("PSGVAL__TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_INTERVAL_COUNT", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_INTERVAL_COUNT", "ENABLE_EVENTS", "False", "this is clickable",),
	("PSGVAL__TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_INTERVAL_COUNT", "FONT", "FONTSZ_CLOCKS_INTERVAL_COUNT", "font+size line",),
	("PSGVAL__TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_INTERVAL_COUNT", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_INTERVAL_COUNT", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_INTERVAL_COUNT", "SIZE", "(4, 1)", "characters, lines size line",),
	("PSGVAL__TEXT_INTERVAL_COUNT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_INTERVAL_COUNT", "TEXT_COLOR", "COLOR_TIME_TOGO", "the text color for a clock_time element",),
	("PSGVAL__TEXT_NAME_NEXT_EVENT", FMAX_NOP, "CLOCKS text K_TIME_AT_NEXT_ALERT",),
	("PSGVAL__TEXT_NAME_NEXT_EVENT00", FMAXPSG_SCTN0909_TEXT_DEF, "TEXT_NAME_NEXT_EVENT", "define the text element for CLOCK_TIME",),
	("PSGVAL__TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_STR_ADD, "TEXT_NAME_NEXT_EVENT", "TEXT", "", "the text to fill in",),
	("PSGVAL__TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_NAME_NEXT_EVENT", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_NAME_NEXT_EVENT", "ENABLE_EVENTS", "False", "this is clickable",),
	("PSGVAL__TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_NAME_NEXT_EVENT", "FONT", "FONTSZ_CLOCKS_TIME_TOGO", "font+size line",),
	("PSGVAL__TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_NAME_NEXT_EVENT", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_NAME_NEXT_EVENT", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_NAME_NEXT_EVENT", "SIZE", "(16, 1)", "characters, lines size line",),
	("PSGVAL__TEXT_NAME_NEXT_EVENT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_NAME_NEXT_EVENT", "TEXT_COLOR", "COLOR_TIME_TOGO", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_AT_NEXT_ALERT", FMAX_NOP, "CLOCKS text NAME_NEXT_EVENT_STR",),
	("PSGVAL__TEXT_TIME_AT_NEXT_ALERT00", FMAXPSG_SCTN0909_TEXT_DEF, "TEXT_TIME_AT_NEXT_ALERT", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__TEXT_TIME_AT_NEXT_ALERT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_NEXT_ALERT", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__TEXT_TIME_AT_NEXT_ALERT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_NEXT_ALERT", "ENABLE_EVENTS", "False", "this is clickable",),
	("PSGVAL__TEXT_TIME_AT_NEXT_ALERT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_NEXT_ALERT", "FONT", "FONTSZ_CLOCKS_TIME_TOGO", "font+size line",),
	("PSGVAL__TEXT_TIME_AT_NEXT_ALERT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_NEXT_ALERT", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__TEXT_TIME_AT_NEXT_ALERT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_NEXT_ALERT", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_AT_NEXT_ALERT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_NEXT_ALERT", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__TEXT_TIME_AT_NEXT_ALERT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_NEXT_ALERT", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_AT_NEXT_ALERT01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_NEXT_ALERT", "TEXT_COLOR", "COLOR_TIME_TOGO", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_AT_ZEROELAPSE", FMAX_NOP, "CLOCKS text K_TIME_AT_ZEROELAPSE",),
	("PSGVAL__TEXT_TIME_AT_ZEROELAPSE00", FMAXPSG_SCTN0909_TEXT_DEF, "TEXT_TIME_AT_ZEROELAPSE", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_ZEROELAPSE", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_ZEROELAPSE", "ENABLE_EVENTS", "False", "this is clickable",),
	("PSGVAL__TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_ZEROELAPSE", "FONT", "FONTSZ_CLOCKS_TIME_ELAPSED", "font+size line",),
	("PSGVAL__TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_ZEROELAPSE", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_ZEROELAPSE", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_ZEROELAPSE", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_ZEROELAPSE", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_AT_ZEROELAPSE01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_AT_ZEROELAPSE", "TEXT_COLOR", "COLOR_TIME_ELAPSED", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_CLOCK", FMAX_NOP, "CLOCKS text K_TIME_CLOCK",),
	("PSGVAL__TEXT_TIME_CLOCK00", FMAXPSG_SCTN0909_TEXT_DEF, "TEXT_TIME_CLOCK", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_STR_ADD, "TEXT_TIME_CLOCK", "TOOLTIP", "Tue_March(03)_10_1964", "date in the tooltip for the clock",),
	("PSGVAL__TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_CLOCK", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_CLOCK", "ENABLE_EVENTS", "True", "this is clickable",),
	("PSGVAL__TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_CLOCK", "FONT", "FONTSZ_CLOCKS_TIME_CLOCK", "font+size line",),
	("PSGVAL__TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_CLOCK", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_CLOCK", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_CLOCK", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_CLOCK", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_CLOCK", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_CLOCK01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_CLOCK", "TEXT_COLOR", "COLOR_TIME_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_ELAPSED", FMAX_NOP, "CLOCKS text K_TIME_ELAPSED",),
	("PSGVAL__TEXT_TIME_ELAPSED00", FMAXPSG_SCTN0909_TEXT_DEF, "TEXT_TIME_ELAPSED", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_ELAPSED", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_ELAPSED", "FONT", "FONTSZ_CLOCKS_TIME_ELAPSED", "font+size line",),
	("PSGVAL__TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_ELAPSED", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_ELAPSED", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_ELAPSED", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_ELAPSED", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_ELAPSED01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_ELAPSED", "TEXT_COLOR", "COLOR_TIME_ELAPSED", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_TOGO", FMAX_NOP, "CLOCKS text K_TIME_TOGO",),
	("PSGVAL__TEXT_TIME_TOGO00", FMAXPSG_SCTN0909_TEXT_DEF, "TEXT_TIME_TOGO", "define the text element for CLOCKS_CLOCK_TIME",),
	("PSGVAL__TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_TOGO", "BACKGROUND_COLOR", "COLOR_CLOCK_BACKGROUND", "background color for the clock elements",),
	("PSGVAL__TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_TOGO", "FONT", "FONTSZ_CLOCKS_TIME_TOGO", "font+size line",),
	("PSGVAL__TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_TOGO", "JUSTIFICATION", "JUSTIFICATION_CENTER", "center everything",),
	("PSGVAL__TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_TOGO", "PAD", "SZ_PAD_ALL", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_TOGO", "SIZE", "(8, 1)", "characters, lines size line",),
	("PSGVAL__TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_TOGO", "TEXT", "ZERO_CLOCK", "the text color for a clock_time element",),
	("PSGVAL__TEXT_TIME_TOGO01", FMAXPSG_SCTN0909_TEXT_VAL_ADD, "TEXT_TIME_TOGO", "TEXT_COLOR", "COLOR_TIME_TOGO", "the text color for a clock_time element",),
	("PSGVAL__VCURRENT_EVENTMODE_VAL", FMAXPSG_SCTN0901_VAL_DEF, "CURRENT_EVENTMODE_VAL", "EVENTMODE_NONE", "comment",),
	("PSGVAL__VCURRENT_INTERVAL_COUNT", FMAXPSG_SCTN0901_VAL_DEF, "CURRENT_INTERVAL_COUNT", "0", "comment",),
	("PSGVAL__VDEVMODE", FMAXPSG_SCTN0901_VAL_DEF, "DEVMODE", "False", "comment",),
	("PSGVAL__VMLCN", FMAXPSG_SCTN0901_VAL_DEF, "MLCN", "DISP.Display().screen().root.query_pointer", "short cut to get mouse position",),
	("PSGVAL__VNOWM", FMAXPSG_SCTN0901_VAL_DEF, "NOWM", "0", "comment",),
	("PSGVAL__VNOWMS", FMAXPSG_SCTN0901_VAL_DEF, "NOWMS", "0", "comment",),
	("PSGVAL__VNOWS", FMAXPSG_SCTN0901_VAL_DEF, "NOWS", "0", "comment",),
	("PSGVAL__VNOW_NOMS", FMAXPSG_SCTN0901_VAL_DEF, "NOW_NOMS", "0", "comment",),
	("PSGVAL__VPKLJAR", FMAXPSG_SCTN0901_VAL_DEF, "_pklJar_", "None", "comment",),
	("PSGVAL__VTIMEMS_NEXT_MOUSE_CHECK", FMAXPSG_SCTN0901_VAL_DEF, "TIMEMS_NEXT_MOUSE_CHECK", "0", "comment",),
	("PSGVAL__VTIMEMS_NEXT_MOVED", FMAXPSG_SCTN0901_VAL_DEF, "TIMEMS_NEXT_MOVED", "0", "comment",),
	("PSGVAL__VTIMEMS_NEXT_UPDATED", FMAXPSG_SCTN0901_VAL_DEF, "TIMEMS_NEXT_UPDATED", "0", "comment",),
	("PSGVAL__VTIMES_ADJUST_VALUE", FMAXPSG_SCTN0901_VAL_DEF, "TIMES_ADJUST_VALUE", "lambda H_=0, M_=0: ((60 * 60 * H_) + (M_ * 60))", "comment",),
	("PSGVAL__VTIME_S_ADJUST_VALUE", FMAXPSG_SCTN0901_VAL_DEF, "TIME_S_ADJUST_VALUE", "lambda H_=0, M_=0: ((60 * 60 * H_) + (M_ * 60))", "comment",),
	("PSGVAL__VTIME_S_AT_NEXT_EVENT", FMAXPSG_SCTN0901_VAL_DEF, "TIME_S_AT_NEXT_EVENT", "0", "comment",),
	("PSGVAL__VTIME_S_AT_NEXT_PERIODIC_JOB", FMAXPSG_SCTN0901_VAL_DEF, "TIME_S_AT_NEXT_PERIODIC_JOB", "0", "seconds till next housekeeping, check for next times, etc.",),
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
	_strToRtn_ = ""
	_strToRtn_ += f"""{CMNTLINE}{NEWLINE}# * {comment_}{NEWLINE}{CMNTLINE}{NEWLINE}"""
	return _strToRtn_
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
	_strToRtn_ = ""
	_strToRtn_ += f"""#{NEWLINE}#{NEWLINE}{CMNTLINE}{NEWLINE}# * {comment_}{NEWLINE}{CMNTLINE}{NEWLINE}#{NEWLINE}#{NEWLINE}"""
	return _strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeADict
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeADict(dictName_, dictComment_, dictItems_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_strToRtn_ = ""
	_strToRtn_ += f"""{dictName_} = {OBRCE}  # {dictComment_}
{dictItems_}{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"""
	return _strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# sortADict
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def sortADict(dictToSort_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_dictToRtn_ = {}
	for _thisKey_ in sorted(dictToSort_.keys(), key=lambda __KEY__: __KEY__.lower()):
		_dictToRtn_[_thisKey_] = dictToSort_[_thisKey_]
	return _dictToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeAList
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeAList(listName_, listComment_, listItems_, listItemCmntDict_=None, addQuotes_=False):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_strToRtn_ = ""
	_strToRtn_ += f"""{listName_} = {OBRKT}  # {listComment_}{NEWLINE}"""
	for _thisItem_ in listItems_:
		if listItemCmntDict_ is None:
			if addQuotes_ is True:
				_strToRtn_ += f"""{NTAB(1)}{DBLQT}{_thisItem_}{DBLQT}"""
			else:
				_strToRtn_ += f"""{NTAB(1)}{_thisItem_}"""
		else:
			if addQuotes_ is True:
				_strToRtn_ += f"""{NTAB(1)}{DBLQT}{_thisItem_}{DBLQT},  # {listItemCmntDict_[_thisItem_]}{NEWLINE}"""
			else:
				_strToRtn_ += f"""{NTAB(1)}{_thisItem_},  # {listItemCmntDict_[_thisItem_]}{NEWLINE}"""
	_strToRtn_ += f"""{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""
	return _strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeANormalTDD
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeANormalTDD(tupDictName_, tupDictItems_, TDDItems_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_strToRtn_ = ""
	_strToRtn1_ = ""

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	_strToRtn_ += f"""{makeAComment(f"start of {tupDictName_} structures")}
{tupDictName_}TUP = {OPAREN}
{tupDictItems_}{CPAREN}{NEWLINE}{NEWLINE}def {tupDictName_}DICT{OPAREN}{CPAREN}:
{NTAB(1)}return dict{OPAREN}{OPAREN}x, y{CPAREN} for x, y in {tupDictName_}TUP{CPAREN}{NEWLINE}{NEWLINE}
{tupDictName_}_TDD = {OBRCE}{NEWLINE}{TDDItems_}{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"""
	return _strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeANormalTupDict
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeANormalTupDict(tupDictName_, tupDictItems_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_strToRtn_ = ""
	_strToRtn1_ = ""

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	_strToRtn_ += f"""{makeAComment(f"start of {tupDictName_} structures")}
{tupDictName_}TUP = {OPAREN}
{tupDictItems_}{CPAREN}{NEWLINE}{NEWLINE}def {tupDictName_}DICT{OPAREN}{CPAREN}:
{NTAB(1)}return dict{OPAREN}{OPAREN}x, y{CPAREN} for x, y in {tupDictName_}TUP{CPAREN}{NEWLINE}{NEWLINE}{NEWLINE}"""
	return _strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# makeASidecarTupDic
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def makeASidecarTupDic(tupDictName_, tupDictItems_, tupDictSidecars_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_strToRtn_ = ""
	_strToRtn1_ = ""
	_strToRtn_ += f"""{makeAComment(f"start of {tupDictName_} structures")}{NEWLINE}"""
	for _key_, _items_ in tupDictSidecars_.items():
		_strToRtn_ += f"""{tupDictName_}_{_key_}TUP = {OPAREN}{NEWLINE}{_items_}{CPAREN}{NEWLINE}{NEWLINE}"""
		_strToRtn1_ += f"""{NTAB(1)}_listToRtn_ = list((x) for x in {tupDictName_}_{_key_}TUP){NEWLINE}"""
	_strToRtn_ += f"""{tupDictName_}TUP = {OPAREN}
{tupDictItems_}{CPAREN}{NEWLINE}{NEWLINE}def {tupDictName_}DICT{OPAREN}{CPAREN}:
{NTAB(1)}_dictToRtn_ = dict{OPAREN}{OPAREN}x, y{CPAREN} for x, y in {tupDictName_}TUP{CPAREN}{NEWLINE}{_strToRtn1_}{NTAB(1)}return _listToRtn_, _dictToRtn_{NEWLINE}{NEWLINE}{NEWLINE}"""
	return _strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# makeAFullTupDict (sidecar is a single item list, or alist of strings that will be concatenated before substitution)
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def makeAFullTupDict(tupDictName_, tupDictItems_, tupDictSidecars_, tupDictParms_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

	subParmsStr_ = f"""{NTAB(1)}def {tupDictName_}_subParms(listIn_, tupDictParms_):
{NTAB(2)}_listToRtn_ = []
{NTAB(2)}for _thisStr_ in listIn_:
{NTAB(3)}for _subParm_, _replaceStr_ in tupDictParms_:
{NTAB(4)}_thisStr_ = _thisStr_.replace(_subParm_, _replaceStr_)
{NTAB(3)}_listToRtn_.append(_thisStr_)
{NTAB(2)}return _listToRtn_{NEWLINE}{NEWLINE}"""

	_strToRtn1_ = ""
	_strToRtn2_ = ""
	sideCarToRtn = {}
	_parmsNames_ = ""
	_sideCar_ = {}

	for _subParm_, _replaceStr_ in tupDictParms_:
		_parmsNames_ += f"""{_replaceStr_}, """
	_parmsNames_ = _parmsNames_[:-2]

	_strToRtn1_ += f"""{makeAComment(f"start of {tupDictName_} structures")}{NEWLINE}"""

	strToRtn3_ = f"""{NTAB(1)}{tupDictName_}_PARMS = {OBRKT}{NEWLINE}"""
	for _subParm_, _replaceStr_ in tupDictParms_:
		strToRtn3_ += f"""{NTAB(2)}{OPAREN}{DBLQT}{_subParm_}{DBLQT}, {_replaceStr_}{CPAREN},{NEWLINE}"""
	strToRtn3_ = strToRtn3_[:-1] + f"""{NEWLINE}{NTAB(1)}{CBRKT}{NEWLINE}"""

	for _key_, _items_ in tupDictSidecars_.items():
		_strToRtn1_ += f"""{tupDictName_}_{_key_}TUP = {OPAREN}{NEWLINE}{_items_}{CPAREN}{NEWLINE}{NEWLINE}"""
		_strToRtn2_ += f"""{NTAB(1)}_listToRtn_ = list((x) for x in {tupDictName_}_{_key_}TUP){NEWLINE}"""
		_strToRtn2_ += f"""{NTAB(1)}_listToRtn_ = CF.subParms(_listToRtn_, {tupDictName_}_PARMS)"""
	_strToRtn1_ += f"""{tupDictName_}TUP = {OPAREN}
{tupDictItems_}{CPAREN}{NEWLINE}{NEWLINE}def {tupDictName_}DICT{OPAREN}{_parmsNames_}{CPAREN}:{NEWLINE}{strToRtn3_}
{NTAB(1)}_dictToRtn_ = dict{OPAREN}{OPAREN}x, y{CPAREN} for x, y in {tupDictName_}TUP{CPAREN}{NEWLINE}"""

	_strToRtn1_ += f"""{_strToRtn2_}{NEWLINE}{NTAB(1)}return _listToRtn_, _dictToRtn_{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1
	return _strToRtn1_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# readFileToStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def readFileToStr(FILENAME_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_strToRtn_ = ""
	with open(FILENAME_, "tr") as _FDIn_:
		_strToRtn_ += _FDIn_.read()
	return _strToRtn_
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
	_strToRtn_ = ""
	_strToRtn_ += f"""{NTAB(1)}{OPAREN}{DBLQT}{itemToExplode_[0]}{DBLQT}, {itemToExplode_[1]}, """
	for _index_ in range(2, len(itemToExplode_)):
		_strToRtn_ += f"""{DBLQT}{itemToExplode_[_index_]}{DBLQT}, """
	_strToRtn_ = f"""{_strToRtn_[:-1]}{CPAREN},{NEWLINE}"""
	return _strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# FMCF_MAKE_BEGINS
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeCF
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeCF():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_strToRtn_ = ""
	_strToRtn_ += f"""{readFileToStr(CFTOP_NAME)}{readFileToStr(SCTN0102NAME)}"""

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	_strToRtn_ += f"""{makeAComment("SCTN0201 CF defines")}"""
	_dictToUse_ = sortADict(FMCF_SCTN0201_DEF_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{_thisName_} = {_value_}  # {FMCF_SCTN0201_DEF_CMNT_DICT[_thisName_]}{NEWLINE}"""
	_strToRtn_ += f"""{NEWLINE}{NEWLINE}"""
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	_strToRtn_ += f"""{makeAComment("SCTN0202 options structures")}"""
	_strToRtn1_ = ""
	_strToRtn2_ = ""
	_strToRtn1_ += f"""OPTIONS = {OBRCE}{NEWLINE}{FOLD1STARTHERELN}"""
	_strToRtn2_ += f"""OPTIONSHELPDICT = {OBRCE}{NEWLINE}{FOLD1STARTHERELN}"""
	_dictToUse_ = sortADict(FMCF_SCTN0202_OPTIONS_DICT)
	for _thisName_, _values_ in _dictToUse_.items():
		_strToRtn1_ += f"""{NTAB(1)}{DBLQT}{_thisName_}{DBLQT}: {OBRCE}{NEWLINE}{NTAB(1)}{FOLD2STARTHERELN}{_values_}{NTAB(1)}{CBRCE},{NEWLINE}{NTAB(1)}{FOLD2ENDHERELN}"""
		_strToRtn2_ += f"""{NTAB(1)}{DBLQT}{_thisName_}{DBLQT}: {NEWLINE}{NTAB(1)}{FOLD2STARTHERELN}{TRIQT}{FMCF_SCTN0202_OPTIONSHELPDICT_DICT[_thisName_]}{NTAB(1)}{TRIQT},{NEWLINE}{NTAB(1)}{FOLD2ENDHERELN}"""
	_strToRtn1_ += f"""{CBRCE}{NEWLINE}{FOLD1ENDHERELN}{NEWLINE}"""
	_strToRtn2_ += f"""{CBRCE}{NEWLINE}{FOLD1ENDHERELN}{NEWLINE}"""
	_strToRtn_ += f"""{_strToRtn1_}{_strToRtn2_}"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
	_strToRtn_ += f"""OPTIONSDICT = {OBRCE}{NEWLINE}"""
	_dictToUse_ = sortADict(FMCF_SCTN0202_OPTIONSDICT_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{_value_}"""
	_strToRtn_ += f"""{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"""
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	_strToRtn_ += f"""{makeAWideComment("end of managed sections of CF.py")}{NEWLINE}{NEWLINE}"""
	return _strToRtn_

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
# FMCF_MAKE_ENDS


# FMFM_MAKE_BEGINS
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeFM
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeFM():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	_strToRtn_ = ""
	_strToRtn_ += f"""{readFileToStr(FMTOP_NAME)}{readFileToStr(SCTN0102NAME)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN003 TYPEs and lambda")}"""
	_dictToUse_ = sortADict(FMCF_SCTN0003_TYPE_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_value_ = FMCF_SCTN0003_TYPE_DICT[_thisName_]
		_strToRtn_ += f"""{_thisName_} = {_value_}  # {FMCF_SCTN0003_TYPE_CMNT_DICT[_thisName_]}{NEWLINE}"""
	_strToRtn_ += NEWLINE + NEWLINE

	## ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN101 FMAX _DEF_")}"""
	strToRtn01_ = ""
	_dictToUse_ = sortADict(FMFM_SCTN0101_AX_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{_thisName_} = {_value_}  # {FMFM_SCTN0101_AX_CMNT_DICT[_thisName_]}{NEWLINE}"""
		strToRtn01_ += f"""{NTAB(1)}{_thisName_},  # {FMFM_SCTN0101_AX_CMNT_DICT[_thisName_]}{NEWLINE}"""
	_strToRtn_ += f"""{NEWLINE}{NEWLINE}FMAXFM_AXLST = {OBRKT}{NEWLINE}{strToRtn01_}{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN102 VAL _DEF_")}"""
	strToRtn01_ = ""
	_dictToUse_ = sortADict(FMFM_SCTN0102_VAL_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{_thisName_} = {_value_}  # {FMFM_SCTN0102_VAL_CMNT_DICT[_thisName_]}{NEWLINE}"""
	_strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN103 _DICT_ _DEF_")}"""
	strToRtn01_ = ""
	_dictToUse_ = sortADict(FMFM_SCTN0103_DICT_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{_thisName_} = {OBRCE}{CBRCE}  # {FMFM_SCTN0103_DICT_CMNT_DICT[_thisName_]}{NEWLINE}"""
	_strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN104 _LIST_ _DEF_")}"""
	_dictToUse_ = sortADict(FMFM_SCTN0104_LIST_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{_thisName_} = {_value_}  # {FMFM_SCTN0104_LIST_CMNT_DICT[_thisName_]}{NEWLINE}"""
	_strToRtn_ += f"""{NEWLINE}{NEWLINE}{makeAWideComment("end of managed portions of FM.py")}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{NTAB(1)}global {BKSLSH}{NEWLINE}"""

	_dictToUse_ = sortADict(FMFM_SCTN0102_VAL_DICT)
	for _name_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{NTAB(2)}{_name_}, {BKSLSH}{NEWLINE}"""

	_dictToUse_ = sortADict(FMFM_SCTN0103_DICT_DICT)
	for _name_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{NTAB(2)}{_name_}, {BKSLSH}{NEWLINE}"""

	_dictToUse_ = sortADict(FMFM_SCTN0104_LIST_DICT)
	for _name_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{NTAB(2)}{_name_}, {BKSLSH}{NEWLINE}"""

	_strToRtn_ = f"""{_strToRtn_[:-4]}{NEWLINE}"""

	return _strToRtn_
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
# FMFM_MAKE_ENDS


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# subMyPlaceKpr
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def subMyPlaceKpr(sourceStr_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_strToRtn_ = sourceStr_
	for _thisSrcStr_, _thisDestStr_ in STR_SUBST_DICT.items():
		_strToRtn_ = _strToRtn_.replace(_thisSrcStr_, _thisDestStr_)

	return _strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# FMPSG_MAKE_BEGINS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# makePSGClasses
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def makePSGClasses():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_strToRtn_ = ""

	_strToRtn_ += f"""{makeAComment("SCTN09FF classes")}{NEWLINE}{NEWLINE}"""

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	_dictToUse1_ = sortADict(FMPSG_SCTN09FF_CLASS_DICT)
	for _thisClassName_, _theseVars_ in _dictToUse1_.items():
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥

		_strToRtn_ += f"""class CLASS_{_thisClassName_}{OPAREN}object{CPAREN}:
{NTAB(1)}{FOLD1STARTHERE}
{NTAB(1)}global {BKSLSH}
{NTAB(2)}ALL_THE_FRAMES{NEWLINE}
"""
		_strToRtn_ += f"""{NTAB(1)}def __init__{OPAREN}self{FMPSG_SCTN09FF_CLASS_INIT_DICT[_thisClassName_].pop(0)}{CPAREN}:{NEWLINE}{NTAB(2)}{FOLD2STARTHERELN}"""

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisItem_ in FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT[_thisClassName_]:
			_strToRtn_ += f"""{_thisItem_}"""

		_strToRtn_ += f"""{NEWLINE}"""

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisItem_ in FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT[_thisClassName_]:
			_strToRtn_ += f"""{_thisItem_}"""

			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if (_thisClassName_ in FMPSG_SCTN09FF_CLASS_DEF_DICT):
				# print(f"""FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT {FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT}""")

				# 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥
				for _thisValName_, _thisVal_ in FMPSG_SCTN09FF_CLASS_DEF_DICT[_thisClassName_].items():
					_strToRtn_ += f"""{NTAB(2)}self.{_thisValName_} = {_thisVal_}{NEWLINE}"""

				_strToRtn_ += f"""{NEWLINE}"""
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

		_strToRtn_ += f"""{NEWLINE}"""

		_strToRtn_ += f"""{NTAB(2)}self._DICTIN_ = {OBRCE}{NEWLINE}{NTAB(2)}{FOLD3STARTHERELN}"""
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisItem_ in FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT[_thisClassName_]:
			_strToRtn_ += f"""{_thisItem_}"""

		_strToRtn_ += f"""{NTAB(2)}{CBRCE}{NEWLINE}{FOLD3ENDHERELN}{NEWLINE}"""

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		_strToRtn_ += f"""{NTAB(2)}self._DICTINSTR_ = {OBRCE}{NEWLINE}{NTAB(2)}{FOLD3STARTHERELN}"""
		for _thisItem_ in FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT[_thisClassName_]:
			_strToRtn_ += f"""{_thisItem_}"""

		_strToRtn_ += f"""{NTAB(2)}{CBRCE}{NEWLINE}{FOLD3ENDHERELN}{NEWLINE}"""

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if _thisClassName_ in FMPSG_SCTN09FF_CLASS_DICT_DICT:
			# print(f"""FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT {FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT}""")
			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			for _thisElementName_, _thisElementVals_ in FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_].items():
				_strToRtn_ += f"""{NTAB(2)}self.{_thisElementName_} = {OBRCE}  # {FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT[_thisClassName_][_thisElementName_]}
{NTAB(2)}{FOLD3STARTHERELN}{_thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}{NTAB(2)}{FOLD3ENDHERELN}{NEWLINE}"""
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if _thisClassName_ in FMPSG_SCTN09FF_CLASS_LIST_DICT:
			# print(f"""FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT {FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT}""")
			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			for _thisElementName_, _thisElementVals_ in FMPSG_SCTN09FF_CLASS_LIST_DICT[_thisClassName_].items():
				_strToRtn_ += f"""{NTAB(2)}self.{_thisElementName_} = {OBRKT}  # {FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT[_thisClassName_][_thisElementName_]}
{NTAB(2)}{FOLD3STARTHERELN}{_thisElementVals_}{NTAB(2)}{CBRKT}{NEWLINE}{NTAB(2)}{FOLD3ENDHERELN}"""
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
### right click menu goes here

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# all elements go after this marker :: elements are not order sensitive, don't do anything in an entry to be broken by that
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if _thisClassName_ in FMPSG_SCTN09FF_CLASS_BTNS_DICT:
			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			for _thisElementName_, _thisElementVals_ in FMPSG_SCTN09FF_CLASS_BTNS_DICT[_thisClassName_].items():
				_strToRtn_ += f"""{NTAB(2)}self.{_thisElementName_} = {OBRCE}  # {FMPSG_SCTN09FF_CLASS_BTNS_CMNT_DICT[_thisClassName_][_thisElementName_]}
{NTAB(2)}{FOLD3STARTHERELN}{_thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}{NTAB(2)}{FOLD3ENDHERELN}
"""
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if _thisClassName_ in FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT:
			for _thisElementName_, _thisElementVals_ in FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT[_thisClassName_].items():
				_strToRtn_ += f"""{NTAB(2)}self.{_thisElementName_} = {OBRCE}  # {FMPSG_SCTN09FF_CLASS_CHECKBOX_CMNT_DICT[_thisClassName_][_thisElementName_]}
{NTAB(2)}{FOLD3STARTHERELN}{_thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}{NTAB(2)}{FOLD3ENDHERELN}"""
				if _thisElementName_ in FMPSG_SCTN09FF_CLASS_CHECKBOX_ADDON_DICT[_thisClassName_]:
					_strToRtn_ += f"""{FMPSG_SCTN09FF_CLASS_CHECKBOX_ADDON_DICT[_thisClassName_][_thisElementName_]}"""

				_strToRtn_ += f"""{NEWLINE}"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if _thisClassName_ in FMPSG_SCTN09FF_CLASS_COMBO_DICT:
			for _thisElementName_, _thisElementVals_ in FMPSG_SCTN09FF_CLASS_COMBO_DICT[_thisClassName_].items():
				_strToRtn_ += f"""{NTAB(2)}self.{_thisElementName_} = {OBRCE}  # {FMPSG_SCTN09FF_CLASS_COMBO_CMNT_DICT[_thisClassName_][_thisElementName_]}
{NTAB(2)}{FOLD3STARTHERELN}{_thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}{NTAB(2)}{FOLD3ENDHERELN}
"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if _thisClassName_ in FMPSG_SCTN09FF_CLASS_RADIO_DICT:
			for _thisElementName_, _thisElementVals_ in FMPSG_SCTN09FF_CLASS_RADIO_DICT[_thisClassName_].items():
				_strToRtn_ += f"""{NTAB(2)}self.{_thisElementName_} = {OBRCE}  # {FMPSG_SCTN09FF_CLASS_RADIO_CMNT_DICT[_thisClassName_][_thisElementName_]}
{NTAB(2)}{FOLD3STARTHERELN}{_thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}{NTAB(2)}{FOLD3ENDHERELN}
"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if _thisClassName_ in FMPSG_SCTN09FF_CLASS_SPIN_DICT:
			for _thisElementName_, _thisElementVals_ in FMPSG_SCTN09FF_CLASS_SPIN_DICT[_thisClassName_].items():
				_strToRtn_ += f"""{NTAB(2)}self.{_thisElementName_}_SPIN_LIST = {OBRKT}
{FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[_thisClassName_][_thisElementName_]}{NTAB(2)}{CBRKT}{NEWLINE}
{NTAB(2)}self.{_thisElementName_}_SPIN_DICT = {OBRCE}  # {FMPSG_SCTN09FF_CLASS_SPIN_CMNT_DICT[_thisClassName_][_thisElementName_]}
{NTAB(2)}{FOLD3STARTHERELN}{_thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}{NTAB(2)}{FOLD3ENDHERELN}
"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if _thisClassName_ in FMPSG_SCTN09FF_CLASS_TEXT_DICT:
			for _thisElementName_, _thisElementVals_ in FMPSG_SCTN09FF_CLASS_TEXT_DICT[_thisClassName_].items():
				_strToRtn_ += f"""{NTAB(2)}self.{_thisElementName_} = {OBRCE}  # {FMPSG_SCTN09FF_CLASS_TEXT_CMNT_DICT[_thisClassName_][_thisElementName_]}
{NTAB(2)}{FOLD3STARTHERELN}{_thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}{NTAB(2)}{FOLD3ENDHERELN}"""
				if _thisElementName_ in FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_]:
					_strToRtn_ += f"""{FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_][_thisElementName_]}"""

				_strToRtn_ += f"""{NEWLINE}"""

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# all elements go above this marker :: NOT order sensitive up to the top marker very sensitive below this marker
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if _thisClassName_ in FMPSG_SCTN09FF_CLASS_COLUMN_DICT:
			_dictToUse2_ = sortADict(FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_])

			for _thisElementName_, _vals1_ in _dictToUse2_.items():
				_strToRtn_ += f"""{NTAB(2)}self.{_thisElementName_} = {OBRKT}  # {FMPSG_SCTN09FF_CLASS_COLUMN_CMNT_DICT[_thisClassName_][_thisElementName_]}{NEWLINE}{NTAB(2)}{FOLD3STARTHERELN}"""

				for _thisRow_, _vals2_ in _vals1_.items():
					_thisTabLevel1_ = FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisElementName_][_thisRow_][TABLEVEL]
					_strToRtn_ += f"""{NTAB(_thisTabLevel1_)}{OBRKT}{NEWLINE}"""

					for _thisElementKey_, _vals3_ in _vals2_.items():

						if _thisElementKey_ == TABLEVEL:
							continue

						if _vals3_ != "":
							_strToRtn_ += f"""{_vals3_}{NTAB(_thisTabLevel1_ + 1)}{CPAREN},{NEWLINE}"""

					_strToRtn_ += f"""{NTAB(_thisTabLevel1_)}{CBRKT},{NEWLINE}"""

				_strToRtn_ += f"""{NTAB(_thisTabLevel1_ - 1)}{CBRKT}{NEWLINE}{NTAB(2)}{FOLD3ENDHERELN}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if _thisClassName_ in FMPSG_SCTN09FF_CLASS_LAYOUT_DICT:
			_dictToUse2_ = sortADict(FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_])

			for _thisElementName_, _vals1_ in _dictToUse2_.items():
				_strToRtn_ += f"""{NTAB(2)}self.{_thisElementName_} = {OBRKT}  # {FMPSG_SCTN09FF_CLASS_LAYOUT_CMNT_DICT[_thisClassName_][_thisElementName_]}{NEWLINE}{NTAB(2)}{FOLD3STARTHERELN}"""

				for _thisRow_, _vals2_ in _vals1_.items():
					_thisTabLevel1_ = FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisElementName_][_thisRow_][TABLEVEL]
					_strToRtn_ += f"""{NTAB(_thisTabLevel1_)}{OBRKT}{NEWLINE}"""

					for _thisElementKey_, _vals3_ in _vals2_.items():

						if _thisElementKey_ == TABLEVEL:
							continue

						if _vals3_ != "":
							_strToRtn_ += f"""{_vals3_}{NTAB(_thisTabLevel1_ + 1)}{CPAREN},{NEWLINE}"""

					_strToRtn_ += f"""{NTAB(_thisTabLevel1_)}{CBRKT},{NEWLINE}"""

				_strToRtn_ += f"""{NTAB(_thisTabLevel1_ - 1)}{CBRKT}{NEWLINE}{NTAB(2)}{FOLD3ENDHERELN}{NEWLINE}"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if _thisClassName_ in FMPSG_SCTN09FF_CLASS_WINDOW_DICT:
			for _thisElementName_, _thisElementVals_ in FMPSG_SCTN09FF_CLASS_WINDOW_DICT[_thisClassName_].items():
				_strToRtn_ += f"""{NTAB(2)}self.{_thisElementName_} = {OBRCE}  # {FMPSG_SCTN09FF_CLASS_WINDOW_CMNT_DICT[_thisClassName_][_thisElementName_]}{NEWLINE}{NTAB(2)}{FOLD3STARTHERE}
{_thisElementVals_}{NTAB(2)}{CBRCE}{NEWLINE}{NTAB(2)}{FOLD3ENDHERELN}
"""

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

### *frame goes here

### * functions go here
	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥

		_strToRtn_ += f"""{NTAB(2)}self.__CDS__ = {OBRCE}{NEWLINE}{NTAB(2)}{FOLD3STARTHERELN}"""
		for _thisItem_ in FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_]:
			_strToRtn_ += f"""{_thisItem_}"""

		_strToRtn_ += f"""{NTAB(2)}{CBRCE}{NEWLINE}{NTAB(2)}{FOLD3ENDHERELN}{NEWLINE}"""

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisItem_ in FMPSG_SCTN09FF_CLASS_INIT_DEF3_DICT[_thisClassName_]:
			_strToRtn_ += f"""{_thisItem_}"""

		_strToRtn_ += f"""{NEWLINE}{NTAB(2)}{FOLD2ENDHERELN}{NEWLINE}"""

#		print(f"""FMPSG_SCTN09FF_CLASS_FUNCTION_DICT {FMPSG_SCTN09FF_CLASS_FUNCTION_DICT}""")
		if _thisClassName_ in FMPSG_SCTN09FF_CLASS_FUNCTION_DICT:
			for __thisFuncName__, __funcVals__ in FMPSG_SCTN09FF_CLASS_FUNCTION_DICT[_thisClassName_].items():
				for __thisElement__ in __funcVals__:
					_strToRtn_ += f"""{__thisElement__}{NEWLINE}"""

	_strToRtn_ += f"""{NTAB(1)}{FOLD1ENDHERELN}{NEWLINE}{NEWLINE}"""
	return _strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# makePSG
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

def makePSG():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_strToRtn_ = ""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{readFileToStr(f"{PSGTOP_NAME}")}{makeAComment("SCTN0900 DEF1")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN0900_DEF1_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{_thisName_} = {_value_}  # {FMPSG_SCTN0900_DEF1_CMNT_DICT[_thisName_]}{NEWLINE}"""
	_strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN0901 DEF2")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN0901_DEF2_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{_thisName_} = {_value_}  # {FMPSG_SCTN0901_DEF2_CMNT_DICT[_thisName_]}{NEWLINE}"""
	_strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN0910 DEF3")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN0910_DEF3_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{_thisName_} = {_value_}  # {FMPSG_SCTN0910_DEF3_CMNT_DICT[_thisName_]}{NEWLINE}"""
	_strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN0902 dicts")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN0902_DICT_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{makeADict(_thisName_, FMPSG_SCTN0902_DICT_CMNT_DICT[_thisName_], _value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN0903 lists")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN0903_LIST_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{_thisName_} = {OBRKT}  # {FMPSG_SCTN0903_LIST_CMNT_DICT[_thisName_]}{NEWLINE}{_value_}{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN0904 platform equalizers")}"""
	dictToUseOuter_ = sortADict(FMPSG_SCTN0904_PLATEQ_OUTER_DICT)
	dictToUseInner_ = sortADict(FMPSG_SCTN0904_PLATEQ_INNER_DICT)
	for thisouterKey, outerVal_ in dictToUseOuter_.items():
		_strToRtn_ += f""""""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN0905 tupdict")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN0905_TUPDICT_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{makeANormalTDD(_thisName_, _value_, FMPSG_SCTN0905_TUPDICT_TDD_DICT[_thisName_])}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN0913 right click menu options")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN0913_RCMENU_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{_thisName_} = {OBRKT}  # {FMPSG_SCTN0913_RCMENU_CMNT_DICT[_thisName_]}{NEWLINE}"""
		_strToRtn_ += f"""{NTAB(1)}{OBRKT}{CBRKT},{NEWLINE}{NTAB(1)}{OBRKT}{NEWLINE}{_value_}{NTAB(1)}{CBRKT},{NEWLINE}{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN0906 button elements")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN0906_BTNS_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{makeADict(_thisName_, FMPSG_SCTN0906_BTNS_CMNT_DICT[_thisName_], _value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN0907 spin box elements")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN0907_SPIN_DICT)  ## add FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{makeADict(_thisName_, FMPSG_SCTN0907_SPIN_CMNT_DICT[_thisName_], _value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN0908 checkbox elements")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN0908_CHECKBOX_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{makeADict(_thisName_, FMPSG_SCTN0908_CHECKBOX_CMNT_DICT[_thisName_], _value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN0909 text elements")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN0909_TEXT_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{makeADict(_thisName_, FMPSG_SCTN0909_TEXT_CMNT_DICT[_thisName_], _value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN090A radio elements")}""" ## needs to be managed with the same structure as layouts
	_dictToUse_ = sortADict(FMPSG_SCTN090A_RADIO_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{makeADict(_thisName_, FMPSG_SCTN090A_RADIO_DICT[_thisName_], _value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN090B column elements")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN090B_COLUMN_DICT)
	for _thisElementName_, _vals1_ in FMPSG_SCTN090B_COLUMN_DICT.items():
		_strToRtn_ += f"""{_thisElementName_} = {OBRKT}  # {FMPSG_SCTN090B_COLUMN_CMNT_DICT[_thisElementName_]}{NEWLINE}"""
		for _thisRow_, _vals2_ in _vals1_.items():
			_thisTabLevel1_ = FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRow_][TABLEVEL]
			_strToRtn_ += f"""{NTAB(_thisTabLevel1_)}{OBRKT}{NEWLINE}"""
			for _thisElementKey_, _vals3_ in _vals2_.items():
				if _thisElementKey_ == TABLEVEL:
					continue
				if _vals3_ != "":
					_strToRtn_ += f"""{_vals3_}{NTAB(_thisTabLevel1_ + 1)}{CPAREN},{NEWLINE}"""
			_strToRtn_ += f"""{NTAB(_thisTabLevel1_)}{CBRKT},{NEWLINE}"""
		_strToRtn_ += f"""{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN090E layout elements")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN090E_LAYOUT_DICT)
	for _thisElementName_, _vals1_ in FMPSG_SCTN090E_LAYOUT_DICT.items():
		_strToRtn_ += f"""{_thisElementName_} = {OBRKT}  # {FMPSG_SCTN090E_LAYOUT_CMNT_DICT[_thisElementName_]}{NEWLINE}"""
		for _thisRow_, _vals2_ in _vals1_.items():
			_thisTabLevel1_ = FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRow_][TABLEVEL]
			_strToRtn_ += f"""{NTAB(_thisTabLevel1_)}{OBRKT}{NEWLINE}"""
			for _thisElementKey_, _vals3_ in _vals2_.items():
				if _thisElementKey_ == TABLEVEL:
					continue
				if _vals3_ != "":
					_strToRtn_ += f"""{_vals3_}{NTAB(_thisTabLevel1_ + 1)}{CPAREN},{NEWLINE}"""
			_strToRtn_ += f"""{NTAB(_thisTabLevel1_)}{CBRKT},{NEWLINE}"""
		_strToRtn_ += f"""{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN090F window")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN090F_WINDOW_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{makeADict(_thisName_, FMPSG_SCTN090F_WINDOW_CMNT_DICT[_thisName_], _value_)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN090D mainframe")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN090D_FORMMAIN_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{makeAComment(f"{_thisName_}_CLASS")}class {_thisName_}_CLASS{OPAREN}{CPAREN}:{NEWLINE}{NTAB(1)}global FORMMAIN, APPDS{NEWLINE}{NEWLINE}"""
		_strToRtn_ += f"""{NTAB(1)}def __enter__{OPAREN}self{CPAREN}:{NEWLINE}{NTAB(2)}global FORMMAIN, APPDS{NEWLINE}"""
		_strToRtn_ += f"""{NTAB(2)}FORMMAIN = SG.Window{OPAREN}{NEWLINE}{_value_}"""
		_strToRtn_ = _strToRtn_[:-1] + f"""{NTAB(2)}APPDS{OBRKT}K_APPMODE{CBRKT} = APPMODE_{_thisName_}{NEWLINE}{NEWLINE}"""
		_strToRtn_ += f"""{NTAB(1)}def __exit__{OPAREN}self, *args{CPAREN}:{NEWLINE}{NTAB(2)}global FORMMAIN, APPDS{NEWLINE}{NTAB(2)}FORMMAIN.close(){NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	_strToRtn_ += f"""{makeAComment("SCTN0914 popupframe")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN0914_FORMPOPUP_DICT)
	for _thisName_, _value_ in _dictToUse_.items():
		_strToRtn_ += f"""{makeAComment(f"{_thisName_}_CLASS")}class {_thisName_}_CLASS{OPAREN}{CPAREN}:{NEWLINE}{NTAB(1)}global FORMPOPUP, APPDS, PREVIOUS_APPMODE{NEWLINE}{NEWLINE}"""
		_strToRtn_ += f"""{NTAB(1)}def __enter__{OPAREN}self{CPAREN}:{NEWLINE}{NTAB(2)}global FORMPOPUP, APPDS, PREVIOUS_APPMODE{NEWLINE}"""
		# _strToRtn_ += f"""{NTAB(2)}APPDS{OBRKT}K_APPMODE{CBRKT} = APPMODE_{_thisName_}{NEWLINE}"""
		_strToRtn_ += f"""{NTAB(2)}FORMPOPUP = SG.Window{OPAREN}{NEWLINE}{_value_}"""
		_strToRtn_ += f"""{NEWLINE}{NTAB(1)}def __exit__{OPAREN}self, *args{CPAREN}:{NEWLINE}{NTAB(2)}global FORMPOPUP, PREVIOUS_APPMODE, APPDS{NEWLINE}{NTAB(2)}FORMPOPUP.close(){NEWLINE}"""
		_strToRtn_ += f"""{NTAB(2)}APPDS{OBRKT}K_APPMODE{CBRKT} = PREVIOUS_APPMODE{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
#	_strToRtn_ += f"""{makeAComment("SCTN0915 popup dialogs")}"""
#	_dictToUse_ = sortADict(FMPSG_SCTN0915_PUDLG_DICT_DICT)
# 	for _thisName_, _value_ in _dictToUse_.items():
# 		_strToRtn_ += f"""{NEWLINE}{NEWLINE}{makeAComment(f"{_thisName_} PUDLG")}
# class CLASS_{_thisName_}{OPAREN}object{CPAREN}:
# {NTAB(1)}{FOLD1STARTHERELN}
# {NTAB(1)}def __init__{OPAREN}self, title_, count_, splatArgs_={OBRKT}{CBRKT}{CPAREN}:
# {NTAB(2)}self.DICT = {OBRCE}
# {_value_}{NTAB(2)}{CBRCE}{NEWLINE}
# {NTAB(2)}self.LIST = {OBRKT}
# {NTAB(3)}f{TRIQT}INTERVAL {OBRCE}title_{CBRCE} has expired {OBRCE}count_{CBRCE} times{TRIQT},
# {NTAB(3)}f{TRIQT}click OK to dismiss, or wait {OBRCE}self.POPUP_INTERVAL_DICT[auto_close_duration]{CBRCE}seconds from alarm{TRIQT},
# {NTAB(2)}{CBRKT}.append{OPAREN}*splatArgs_{CPAREN}{NEWLINE}
# {NTAB(2)}return self{NEWLINE}
# {NTAB(1)}def __enter__{OPAREN}self{CPAREN}:
# {NTAB(2)}SG.{FMPSG_SCTN0915_PUDLG_TYPE_DICT[_thisName_]}{OPAREN}
# {NTAB(3)}*self.{_thisName_}_LIST,
# {NTAB(3)}**self.{_thisName_}_DICT,
# {NTAB(2)}{CPAREN}{NEWLINE}{NTAB(1)}{FOLD1ENDHERELN}{NEWLINE}
# """

	_strToRtn_ += makePSGClasses()

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# keep APPDS last
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	# print(f"""SCTN090C FMPSG_SCTN090C_APPDS_DICT |{FMPSG_SCTN090C_APPDS_DICT}|{NEWLINE}FMPSG_SCTN090C_APPDSDICT_DICT|{FMPSG_SCTN090C_APPDSDICT_DICT}|""")
	_strToRtn_ += f"""{makeAComment("SCTN090C APPDS")}"""
	_dictToUse_ = sortADict(FMPSG_SCTN090C_APPDS_DICT)
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	for _thisName_, _values_ in _dictToUse_.items():
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		_valuesDict_ = sortADict(_values_)
		_strToRtn_ += f"""{_thisName_} = {OBRCE}  # {FMPSG_SCTN090C_APPDS_CMNT_DICT[_thisName_]}{NEWLINE}"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisKey_, _thisVal_ in _valuesDict_.items():
			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			_strToRtn_ += f"""{_thisVal_}"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			if _thisKey_ in FMPSG_SCTN090C_APPDSDICT_DICT[_thisName_]:
				# 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥
				_dictToAdd_ = sortADict(FMPSG_SCTN090C_APPDSDICT_DICT[_thisName_][_thisKey_])

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
				# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
				for _thisKey1_, _thisVal1_ in _dictToAdd_.items():
					# 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥
					_strToRtn_ += f"""{NTAB(2)}{_thisKey1_}: {OBRCE}{NEWLINE}"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
				# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
					# ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥
					dictToAdd2_ = sortADict(_thisVal1_)
					for thisKey2_, _thisVal2_ in dictToAdd2_.items():
						# 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥
						_strToRtn_ += f"""{NTAB(3)}{thisKey2_}: {_thisVal2_}"""
						# ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
				# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
					# ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥
					_strToRtn_ += f"""{NTAB(2)}{CBRCE},{NEWLINE}"""
					# ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
				# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
				_strToRtn_ += f"""{NTAB(1)}{CBRCE},{NEWLINE}"""

				# ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		_strToRtn_ += f"""{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"""

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	_strToRtn_ += f"""{makeAWideComment("end of managed sections of PSG.py")}"""
	_strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	return _strToRtn_
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
		FMFM_SCTN0105_LDICT_CMNT_DICT, \
		FMFM_SCTN0105_LDICT_DICT, \
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
		FMPSG_SCTN090C_APPDS_CMNT_DICT, \
		FMPSG_SCTN090C_APPDS_DICT, \
		FMPSG_SCTN090C_APPDSDICT_DICT, \
		FMPSG_SCTN090D_FORMMAIN_CMNT_DICT, \
		FMPSG_SCTN090D_FORMMAIN_DICT, \
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
		FMPSG_SCTN0914_FORMPOPUP_CMNT_DICT, \
		FMPSG_SCTN0914_FORMPOPUP_DICT, \
		FMPSG_SCTN0915_PUDLG_CMNT_DICT, \
		FMPSG_SCTN0915_PUDLG_DICT_DICT, \
		FMPSG_SCTN0915_PUDLG_LIST_DICT, \
		FMPSG_SCTN0915_PUDLG_TYPE_DICT, \
		FMPSG_SCTN09FF_CLASS_BTNS_ADDON_DICT, \
		FMPSG_SCTN09FF_CLASS_BTNS_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_BTNS_DICT, \
		FMPSG_SCTN09FF_CLASS_CDS_DICT, \
		FMPSG_SCTN09FF_CLASS_CHECKBOX_ADDON_DICT, \
		FMPSG_SCTN09FF_CLASS_CHECKBOX_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT, \
		FMPSG_SCTN09FF_CLASS_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_COLUMN_ADDON_DICT, \
		FMPSG_SCTN09FF_CLASS_COLUMN_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_COLUMN_DICT, \
		FMPSG_SCTN09FF_CLASS_COLUMN_PARMS_DICT, \
		FMPSG_SCTN09FF_CLASS_COMBO_ADDON_DICT, \
		FMPSG_SCTN09FF_CLASS_COMBO_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_COMBO_DICT, \
		FMPSG_SCTN09FF_CLASS_DEF_DICT, \
		FMPSG_SCTN09FF_CLASS_DICT, \
		FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_DICT_DICT, \
		FMPSG_SCTN09FF_CLASS_FRAME_ADDON_DICT, \
		FMPSG_SCTN09FF_CLASS_FRAME_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_FRAME_DICT, \
		FMPSG_SCTN09FF_CLASS_FUNCTION_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_FUNCTION_DEF1_DICT, \
		FMPSG_SCTN09FF_CLASS_FUNCTION_DEF2_DICT, \
		FMPSG_SCTN09FF_CLASS_FUNCTION_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_DEF3_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT, \
		FMPSG_SCTN09FF_CLASS_LAYOUT_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_LAYOUT_DICT, \
		FMPSG_SCTN09FF_CLASS_LIST_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_LIST_DICT, \
		FMPSG_SCTN09FF_CLASS_RADIO_ADDON_DICT, \
		FMPSG_SCTN09FF_CLASS_RADIO_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_RADIO_DICT, \
		FMPSG_SCTN09FF_CLASS_RCMENU_ADDON_DICT, \
		FMPSG_SCTN09FF_CLASS_RCMENU_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_RCMENU_DICT, \
		FMPSG_SCTN09FF_CLASS_SPIN_ADDON_DICT, \
		FMPSG_SCTN09FF_CLASS_SPIN_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_SPIN_DICT, \
		FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT, \
		FMPSG_SCTN09FF_CLASS_TEXT_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_TEXT_DICT, \
		FMPSG_SCTN09FF_CLASS_WINDOW_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_WINDOW_DICT
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	for _thisItem_ in TBGLST:
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ for _thisItem_ in TBGLST:

		FDTBGLST.write(f"{explodeItem(_thisItem_)}")
		_thisItemLen_ = len(_thisItem_)
		if _thisItemLen_ < 3:
			doErrorItem("fewer than 3 elements", _thisItem_)
			continue
		if not isinstance(_thisItem_, tuple):
			doErrorItem("not a tuple", _thisItem_)
			continue
		_thisName_ = _thisItem_[0]
		_thisAX_ = _thisItem_[1]
		_thisComment_ = _thisItem_[-1]
		if _thisAX_ not in FMAXFM_AXLST:
			doErrorItem("not a supported action in FM", _thisItem_)
			continue

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		if _thisAX_ is None or _thisAX_ == FMAX_NOP:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

# FMCF_PARSE_BEGINS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0003_LAMBDA_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisLambdaName_ = _thisItem_[2]
			thisLambdaVal_ = _thisItem_[3]
			FMCF_SCTN0003_TYPE_DICT[_thisLambdaName_] = f"lambda {thisLambdaVal_}"
			FMCF_SCTN0003_TYPE_CMNT_DICT[_thisLambdaName_] = "{_thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0003_TYPE_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisTypeName_ = _thisItem_[2]
			_thisType_ = _thisItem_[3]
			FMCF_SCTN0003_TYPE_DICT[_thisTypeName_] = f"{DBLQT}{_thisType_}{DBLQT}"
			FMCF_SCTN0003_TYPE_CMNT_DICT[_thisTypeName_] = f"{_thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0201_STR_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMCF_SCTN0201_DEF_DICT[_thisValName_] = f"{DBLQT}{_thisVal_}{DBLQT}"
			FMCF_SCTN0201_DEF_CMNT_DICT[_thisValName_] = f"{_thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0201_VAL_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMCF_SCTN0201_DEF_DICT[_thisValName_] = f"{_thisVal_}"
			FMCF_SCTN0201_DEF_CMNT_DICT[_thisValName_] = f"{_thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0202_OPTIONS_ADD_HELP_LINE:  # define a '-a[=]' in SCTN22 <NAC><KEY><PARM><VAL>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisParm_ = _thisItem_[2]
			if _thisParm_ not in FMCF_SCTN0202_OPTIONSHELPDICT_DICT:
				FMCF_SCTN0202_OPTIONSHELPDICT_DICT[_thisParm_] = ""
			FMCF_SCTN0202_OPTIONSHELPDICT_DICT[_thisParm_] += f"""{_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0202_OPTIONS_STR_ADD:  # define a '-a[=]' in SCTN22 <NAC><KEY><PARM><VAL>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisParm_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisParm_ not in FMCF_SCTN0202_OPTIONS_DICT:
				FMCF_SCTN0202_OPTIONS_DICT[_thisParm_] = ""
			if _thisParm_ not in FMCF_SCTN0202_OPTIONSHELPDICT_DICT:
				FMCF_SCTN0202_OPTIONSHELPDICT_DICT[_thisParm_] = ""
			FMCF_SCTN0202_OPTIONS_DICT[_thisParm_] += f"""{NTAB(2)}{DBLQT}{_thisKey_}{DBLQT}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			FMCF_SCTN0202_OPTIONSHELPDICT_DICT[_thisParm_] += f"""{_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0202_OPTIONS_VAL_ADD:  # define a '-a[=]' in SCTN22 <NAC><KEY><PARM><VAL>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisParm_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisParm_ not in FMCF_SCTN0202_OPTIONS_DICT:
				FMCF_SCTN0202_OPTIONS_DICT[_thisParm_] = ""
			if _thisParm_ not in FMCF_SCTN0202_OPTIONSHELPDICT_DICT:
				FMCF_SCTN0202_OPTIONSHELPDICT_DICT[_thisParm_] = ""
			FMCF_SCTN0202_OPTIONS_DICT[_thisParm_] += f"""{NTAB(2)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""
			FMCF_SCTN0202_OPTIONSHELPDICT_DICT[_thisParm_] += f"""{_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0202_OPTIONSDICT_STR_ADD:  # define a OPTNAME: 'str' in SCTN202 <NAC><KEY><STRDEFAULT>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisKey_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMCF_SCTN0202_OPTIONSDICT_DICT[_thisName_] = f"{NTAB(1)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0202_OPTIONSDICT_VAL_ADD:  # define a OPTNAME: VAL in SCTN202 <NAC><KEY><VALDEFAULT>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisKey_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMCF_SCTN0202_OPTIONSDICT_DICT[_thisName_] = f"{NTAB(1)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0204_LIST_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisListName_ = _thisItem_[2]
			FMCF_SCTN0204_LIST_DICT[_thisListName_] = ""
			FMCF_SCTN0204_LIST_CMNT_DICT[_thisListName_] = f"{_thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0204_LIST_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisListName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMCF_SCTN0204_LIST_DICT[_thisListName_] += f"{NTAB(1)}f{DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0204_LIST_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisListName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMCF_SCTN0204_LIST_DICT[_thisListName_] += f"{NTAB(1)}{DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXCF_SCTN0204_LIST_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisListName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMCF_SCTN0204_LIST_DICT[_thisListName_] += f"{NTAB(1)}{_thisVal_},  # {_thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# FMCF_PARSE_ENDS

# FMFM_PARSE_BEGINS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXFM_SCTN0101_AX_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 3:
				doErrorItem("not 3 items", _thisItem_)
				continue
			FMFM_SCTN0101_AX_DICT[_thisName_] = f"{DBLQT}{_thisName_}{DBLQT}"
			FMFM_SCTN0101_AX_CMNT_DICT[_thisName_] = f"{_thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXFM_SCTN0102_STR_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMFM_SCTN0102_VAL_DICT[_thisValName_] = f"""{DBLQT}{_thisVal_}{DBLQT}"""
			FMFM_SCTN0102_VAL_CMNT_DICT[_thisValName_] = f"{_thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXFM_SCTN0102_VAL_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMFM_SCTN0102_VAL_DICT[_thisValName_] = _thisVal_
			FMFM_SCTN0102_VAL_CMNT_DICT[_thisValName_] = f"{_thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXFM_SCTN0103_DICT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 3:
				doErrorItem("not 3 items", _thisItem_)
				continue
			FMFM_SCTN0103_DICT_DICT[_thisName_] = f"{OBRCE}{CBRCE}"
			FMFM_SCTN0103_DICT_CMNT_DICT[_thisName_] = f"{_thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXFM_SCTN0104_LIST_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 3:
				doErrorItem("not 3 items", _thisItem_)
				continue
			FMFM_SCTN0104_LIST_DICT[_thisName_] = f"{OBRKT}{CBRKT}"
			FMFM_SCTN0104_LIST_CMNT_DICT[_thisName_] = f"{_thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# FMFM_PARSE_ENDS

# FMPSG_PARSE_BEGINS
# SCTN0900_BEGINS_DEF1
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0900_KEY_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			FMPSG_SCTN0900_DEF1_DICT[_thisValName_] = f"""{DBLQT}{_thisValName_}{DBLQT}"""
			FMPSG_SCTN0900_DEF1_CMNT_DICT[_thisValName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0900_STR_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMPSG_SCTN0900_DEF1_DICT[_thisValName_] = f"""{DBLQT}{_thisVal_}{DBLQT}"""
			FMPSG_SCTN0900_DEF1_CMNT_DICT[_thisValName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0900_VAL_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMPSG_SCTN0900_DEF1_DICT[_thisValName_] = f"""{_thisVal_}"""
			FMPSG_SCTN0900_DEF1_CMNT_DICT[_thisValName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0900_ENDS_DEF1

# sctn0901_BEGINS_DEF2
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0901_DUBLT_SS_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal1_ = _thisItem_[3]
			_thisVal2_ = _thisItem_[4]
			FMPSG_SCTN0901_DEF2_DICT[_thisValName_] = f"""{OPAREN}{DBLQT}{_thisVal1_}{DBLQT}, {DBLQT}{_thisVal2_}{DBLQT}{CPAREN},"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[_thisValName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0901_DUBLT_SV_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal1_ = _thisItem_[3]
			_thisVal2_ = _thisItem_[4]
			FMPSG_SCTN0901_DEF2_DICT[_thisValName_] = f"""{OPAREN}{DBLQT}{_thisVal1_}{DBLQT}, {_thisVal2_}{CPAREN},"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[_thisValName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0901_DUBLT_VS_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal1_ = _thisItem_[3]
			_thisVal2_ = _thisItem_[4]
			FMPSG_SCTN0901_DEF2_DICT[_thisValName_] = f"""{OPAREN}{_thisVal1_}, {DBLQT}{_thisVal2_}{DBLQT}{CPAREN},"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[_thisValName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0901_DUBLT_VV_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal1_ = _thisItem_[3]
			_thisVal2_ = _thisItem_[4]
			FMPSG_SCTN0901_DEF2_DICT[_thisValName_] = f"""{OPAREN}{_thisVal1_}, {_thisVal2_}{CPAREN}"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[_thisValName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0901_KEY_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			FMPSG_SCTN0901_DEF2_DICT[_thisValName_] = f"""{DBLQT}{_thisValName_}{DBLQT}"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[_thisValName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0901_STR_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMPSG_SCTN0901_DEF2_DICT[_thisValName_] = f"""{DBLQT}{_thisVal_}{DBLQT}"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[_thisValName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0901_VAL_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMPSG_SCTN0901_DEF2_DICT[_thisValName_] = f"""{_thisVal_}"""
			FMPSG_SCTN0901_DEF2_CMNT_DICT[_thisValName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0901_ENDS_DEF2

# SCTN0902_BEGINS_DICT
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0902_DICT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisDictName_ = _thisItem_[2]
			if _thisDictName_ not in FMPSG_SCTN0902_DICT_DICT:
				FMPSG_SCTN0902_DICT_DICT[_thisDictName_] = ""
			FMPSG_SCTN0902_DICT_CMNT_DICT[_thisDictName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0902_DICT_VS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisDictName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisDictName_ not in FMPSG_SCTN0902_DICT_DICT:
				FMPSG_SCTN0902_DICT_DICT[_thisDictName_] = ""
			FMPSG_SCTN0902_DICT_DICT[_thisDictName_] += f"""{NTAB(1)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0902_DICT_SS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisDictName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisDictName_ not in FMPSG_SCTN0902_DICT_DICT:
				FMPSG_SCTN0902_DICT_DICT[_thisDictName_] = ""
			FMPSG_SCTN0902_DICT_DICT[_thisDictName_] += f"""{NTAB(1)}{DBLQT}{_thisKey_}{DBLQT}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0902_DICT_SV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisDictName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisDictName_ not in FMPSG_SCTN0902_DICT_DICT:
				FMPSG_SCTN0902_DICT_DICT[_thisDictName_] = ""
			FMPSG_SCTN0902_DICT_DICT[_thisDictName_] += f"""{NTAB(1)}{DBLQT}{_thisKey_}{DBLQT}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0902_DICT_VV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisDictName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisDictName_ not in FMPSG_SCTN0902_DICT_DICT:
				FMPSG_SCTN0902_DICT_DICT[_thisDictName_] = ""
			FMPSG_SCTN0902_DICT_DICT[_thisDictName_] += f"""{NTAB(1)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0902_ENDS_DICT

# SCTN0903_BEGINS_LIST
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0903_LIST_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisListName_ = _thisItem_[2]
			if _thisListName_ not in FMPSG_SCTN0903_LIST_DICT:
				FMPSG_SCTN0903_LIST_DICT[_thisListName_] = ""
			FMPSG_SCTN0903_LIST_CMNT_DICT[_thisListName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0903_LIST_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisListName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			if _thisListName_ not in FMPSG_SCTN0903_LIST_DICT:
				FMPSG_SCTN0903_LIST_DICT[_thisListName_] = ""
			FMPSG_SCTN0903_LIST_DICT[_thisListName_] += f"""{NTAB(1)}{DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0903_LIST_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisListName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			if _thisListName_ not in FMPSG_SCTN0903_LIST_DICT:
				FMPSG_SCTN0903_LIST_DICT[_thisListName_] = ""
			FMPSG_SCTN0903_LIST_DICT[_thisListName_] += f"""{NTAB(1)}{_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0903_ENDS_LIST

# SCTN0904_BEGINS_PLATFORMEQ
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0904_PLATEQ_PLAT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisPlatEqName_ = _thisItem_[2]
			_thisPlatEqKey_ = _thisItem_[3]
			_thisPlatEqCondition_ = _thisItem_[4]
			if _thisPlatEqName_ not in FMPSG_SCTN0904_PLATEQ_OUTER_DICT:
				FMPSG_SCTN0904_PLATEQ_OUTER_DICT[_thisPlatEqName_] = ""
			FMPSG_SCTN0904_PLATEQ_OUTER_DICT[_thisPlatEqName_] = f"""{_thisPlatEqKey_} = {_thisPlatEqCondition_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0904_ENDS_PLATFORMEQ

# SCTN0905_BEGINS_TUPDICT
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0905_TUPDICT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisTupdictName_ = _thisItem_[2]
			if _thisTupdictName_ not in FMPSG_SCTN0905_TUPDICT_DICT:
				FMPSG_SCTN0905_TUPDICT_DICT[_thisTupdictName_] = ""
				FMPSG_SCTN0905_TUPDICT_TDD_DICT[_thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICT_CMNT_DICT[_thisTupdictName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0905_TUPDICT_SS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisTupdictName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisTupdictName_ not in FMPSG_SCTN0905_TUPDICT_DICT:
				FMPSG_SCTN0905_TUPDICT_DICT[_thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICT_DICT[_thisTupdictName_] += f"""{NTAB(1)}{OPAREN}{DBLQT}{_thisKey_}{DBLQT}, {DBLQT}{_thisVal_}{DBLQT}{CPAREN},  # {_thisComment_}{NEWLINE}"""
			FMPSG_SCTN0905_TUPDICT_TDD_DICT[_thisTupdictName_] += f"""{NTAB(1)}{DBLQT}{_thisKey_}{DBLQT}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0905_TUPDICT_SV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisTupdictName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisTupdictName_ not in FMPSG_SCTN0905_TUPDICT_DICT:
				FMPSG_SCTN0905_TUPDICT_DICT[_thisTupdictName_] = ""
				FMPSG_SCTN0905_TUPDICT_TDD_DICT[_thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICT_DICT[_thisTupdictName_] += f"""{NTAB(1)}{OPAREN}{DBLQT}{_thisKey_}{DBLQT}, {_thisVal_}{CPAREN},  # {_thisComment_}{NEWLINE}"""
			FMPSG_SCTN0905_TUPDICT_TDD_DICT[_thisTupdictName_] += f"""{NTAB(1)}{DBLQT}{_thisKey_}{DBLQT}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0905_TUPDICT_VS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisTupdictName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisTupdictName_ not in FMPSG_SCTN0905_TUPDICT_DICT:
				FMPSG_SCTN0905_TUPDICT_DICT[_thisTupdictName_] = ""
				FMPSG_SCTN0905_TUPDICT_TDD_DICT[_thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICT_DICT[_thisTupdictName_] += f"""{NTAB(1)}{OPAREN}{_thisKey_}, {DBLQT}{_thisVal_}{DBLQT}{CPAREN},  # {_thisComment_}{NEWLINE}"""
			FMPSG_SCTN0905_TUPDICT_TDD_DICT[_thisTupdictName_] += f"""{NTAB(1)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0905_TUPDICT_VV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisTupdictName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisTupdictName_ not in FMPSG_SCTN0905_TUPDICT_DICT:
				FMPSG_SCTN0905_TUPDICT_DICT[_thisTupdictName_] = ""
			FMPSG_SCTN0905_TUPDICT_DICT[_thisTupdictName_] += f"""{NTAB(1)}{OPAREN}{_thisKey_}, {_thisVal_}{CPAREN},  # {_thisComment_}{NEWLINE}"""
			FMPSG_SCTN0905_TUPDICT_TDD_DICT[_thisTupdictName_] += f"""{NTAB(1)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0905_ENDS_TUPDICT

# SCTN0906_BEGINS_BTN
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0906_BTN_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			if _thisElementName_ not in FMPSG_SCTN0906_BTNS_DICT:
				FMPSG_SCTN0906_BTNS_DICT[_thisElementName_] = ""
			FMPSG_SCTN0906_BTNS_CMNT_DICT[_thisElementName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0906_BTN_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisElementName_ not in FMPSG_SCTN0906_BTNS_DICT:
				FMPSG_SCTN0906_BTNS_DICT[_thisElementName_] = ""
			FMPSG_SCTN0906_BTNS_DICT[_thisElementName_] += f"""{NTAB(1)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0906_BTN_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisElementName_ not in FMPSG_SCTN0906_BTNS_DICT:
				FMPSG_SCTN0906_BTNS_DICT[_thisElementName_] = ""
			FMPSG_SCTN0906_BTNS_DICT[_thisElementName_] += f"""{NTAB(1)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0906_ENDS_BTN

# SCTN0907_BEGINS_SPIN
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0907_SPIN_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			if _thisElementName_ not in FMPSG_SCTN0907_SPIN_DICT:
				FMPSG_SCTN0907_SPIN_DICT[_thisElementName_] = ""
			if _thisElementName_ not in FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT:
				FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = ""
			FMPSG_SCTN0907_SPIN_CMNT_DICT[_thisElementName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0907_SPIN_DICT_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisElementName_ not in FMPSG_SCTN0907_SPIN_DICT:
				FMPSG_SCTN0907_SPIN_DICT[_thisElementName_] = ""
			if _thisElementName_ not in FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT:
				FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = ""
			FMPSG_SCTN0907_SPIN_DICT[_thisElementName_] += f"""{NTAB(1)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0907_SPIN_DICT_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisElementName_ not in FMPSG_SCTN0907_SPIN_DICT:
				FMPSG_SCTN0907_SPIN_DICT[_thisElementName_] = ""
			if _thisElementName_ not in FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT:
				FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = ""
			FMPSG_SCTN0907_SPIN_DICT[_thisElementName_] += f"""{NTAB(1)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0907_SPIN_VALUES_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			if _thisElementName_ not in FMPSG_SCTN0907_SPIN_DICT:
				FMPSG_SCTN0907_SPIN_DICT[_thisElementName_] = ""
			if _thisElementName_ not in FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT:
				FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = ""
			FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT[_thisElementName_] += f"""{NTAB(1)}{DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0907_SPIN_VALUES_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			if _thisElementName_ not in FMPSG_SCTN0907_SPIN_DICT:
				FMPSG_SCTN0907_SPIN_DICT[_thisElementName_] = ""
			if _thisElementName_ not in FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT:
				FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT = ""
			FMPSG_SCTN0907_SPIN_VALUES_LIST_DICT[_thisElementName_] += f"""{NTAB(1)}{_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0907_ENDS_SPIN

# SCTN0908_BEGINS_CHECKBOX
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0908_CHECKBOX_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			if _thisElementName_ not in FMPSG_SCTN0908_CHECKBOX_DICT:
				FMPSG_SCTN0908_CHECKBOX_DICT[_thisElementName_] = ""
			FMPSG_SCTN0908_CHECKBOX_CMNT_DICT[_thisElementName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0908_CHECKBOX_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisElementName_ not in FMPSG_SCTN0908_CHECKBOX_DICT:
				FMPSG_SCTN0908_CHECKBOX_DICT[_thisElementName_] = ""
			FMPSG_SCTN0908_CHECKBOX_DICT[_thisElementName_] += f"""{NTAB(1)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0908_CHECKBOX_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisElementName_ not in FMPSG_SCTN0908_CHECKBOX_DICT:
				FMPSG_SCTN0908_CHECKBOX_DICT[_thisElementName_] = ""
			FMPSG_SCTN0908_CHECKBOX_DICT[_thisElementName_] += f"""{NTAB(1)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0908_ENDS_CHECKBOX

# SCTN0909_BEGINS_TEXT
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0909_TEXT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue

			_thisElementName_ = _thisItem_[2]

			if _thisElementName_ not in FMPSG_SCTN0909_TEXT_DICT:
				FMPSG_SCTN0909_TEXT_DICT[_thisElementName_] = ""

			FMPSG_SCTN0909_TEXT_CMNT_DICT[_thisElementName_] = f"""{_thisComment_}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0909_TEXT_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisElementName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]

			if _thisElementName_ not in FMPSG_SCTN0909_TEXT_DICT:
				FMPSG_SCTN0909_TEXT_DICT[_thisElementName_] = ""

			FMPSG_SCTN0909_TEXT_DICT[_thisElementName_] += f"""{NTAB(1)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0909_TEXT_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisElementName_ not in FMPSG_SCTN0909_TEXT_DICT:
				FMPSG_SCTN0909_TEXT_DICT[_thisElementName_] = ""
			FMPSG_SCTN0909_TEXT_DICT[_thisElementName_] += f"""{NTAB(1)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0909_ENDS_TEXT

# SCTN090A_BEGINS_??
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN090A_ENDS_??

# SCTN090B_BEGINS_COLUMN
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090B_COLUMN_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			if _thisElementName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_] = {}
			FMPSG_SCTN090B_COLUMN_CMNT_DICT[_thisElementName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090B_COLUMN_BUTTON_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			if _thisElementName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Button{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090B_COLUMN_CHECKBOX_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			if _thisElementName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Checkbox{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090B_COLUMN_COLUMN_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			if _thisElementName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Col{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090B_COLUMN_COMBO_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = thisItem[5]
			if _thisElementName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Combo{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090B_COLUMN_PACKEDPARM_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			_thisVal_ = _thisItem_[6]
			if _thisElementName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}**{_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090B_COLUMN_PARM_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			_thisVal_ = _thisItem_[6]
			if _thisElementName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}{_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090B_COLUMN_RADIO_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			if _thisElementName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Radio{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090B_COLUMN_ROW_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			if _thisElementName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_] = {}
			FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][TABLEVEL] = _thisTabLevel_
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090B_COLUMN_SPIN_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			if _thisElementName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Spin{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090B_COLUMN_TEXT_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			if _thisElementName_ not in FMPSG_SCTN090B_COLUMN_DICT:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090B_COLUMN_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Text{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN090B_ENDS_COLUMN

# SCTN090C_BEGINS_APPDS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090C_APPDS_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisAPPDSName_ = _thisItem_[2]
			if _thisAPPDSName_ not in FMPSG_SCTN090C_APPDS_DICT:
				FMPSG_SCTN090C_APPDS_DICT[_thisAPPDSName_] = {}
			FMPSG_SCTN090C_APPDS_CMNT_DICT[_thisAPPDSName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090C_APPDS_DICT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisAPPDSName_ = _thisItem_[2]
			_thisDictName_ = _thisItem_[3]
			_thisIndexNum_ = _thisItem_[4]
			if _thisAPPDSName_ not in FMPSG_SCTN090C_APPDS_DICT:
				FMPSG_SCTN090C_APPDS_DICT[_thisAPPDSName_] = {}
			if _thisAPPDSName_ not in FMPSG_SCTN090C_APPDSDICT_DICT:
				FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_] = {}
			if _thisDictName_ not in FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_]:
				FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_][_thisDictName_] = {}
			if _thisIndexNum_ not in FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_][_thisDictName_]:
				FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_][_thisDictName_][_thisIndexNum_] = {}
			FMPSG_SCTN090C_APPDS_DICT[_thisAPPDSName_][_thisDictName_] = f"""{NTAB(1)}{_thisDictName_}: {OBRCE}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090C_APPDS_DICT_VS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue
			_thisAPPDSName_ = _thisItem_[2]
			_thisDictName_ = _thisItem_[3]
			_thisIndexNum_ = _thisItem_[4]
			_thisKey_ = _thisItem_[5]
			_thisVal_ = _thisItem_[6]
			if _thisAPPDSName_ not in FMPSG_SCTN090C_APPDSDICT_DICT:
				FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_] = {}
			if _thisDictName_ not in FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_]:
				FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_][_thisDictName_] = {}
			if _thisIndexNum_ not in FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_][_thisDictName_]:
				FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_][_thisDictName_][_thisIndexNum_] = {}
			FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_][_thisDictName_][_thisIndexNum_][_thisKey_] = f"""{DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090C_APPDS_DICT_VV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue
			_thisAPPDSName_ = _thisItem_[2]
			_thisDictName_ = _thisItem_[3]
			_thisIndexNum_ = _thisItem_[4]
			_thisKey_ = _thisItem_[5]
			_thisVal_ = _thisItem_[6]
			if _thisAPPDSName_ not in FMPSG_SCTN090C_APPDSDICT_DICT:
				FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_] = {}
			if _thisDictName_ not in FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_]:
				FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_][_thisDictName_] = {}
			if _thisIndexNum_ not in FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_][_thisDictName_]:
				FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_][_thisDictName_][_thisIndexNum_] = {}
			FMPSG_SCTN090C_APPDSDICT_DICT[_thisAPPDSName_][_thisDictName_][_thisIndexNum_][_thisKey_] = f"""{_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090C_APPDS_VS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisAPPDSName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisAPPDSName_ not in FMPSG_SCTN090C_APPDS_DICT:
				FMPSG_SCTN090C_APPDS_DICT[_thisAPPDSName_] = {}
			FMPSG_SCTN090C_APPDS_DICT[_thisAPPDSName_][_thisKey_] = f"""{NTAB(1)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090C_APPDS_VV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisAPPDSName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisAPPDSName_ not in FMPSG_SCTN090C_APPDS_DICT:
				FMPSG_SCTN090C_APPDS_DICT[_thisAPPDSName_] = {}
			FMPSG_SCTN090C_APPDS_DICT[_thisAPPDSName_][_thisKey_] = f"""{NTAB(1)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN	090C_ENDS_APPDS

# SCTN090D_BEGINS_FORMMAIN
# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
#	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
#		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
#		elif _thisAX_ == FMAXPSG_SCTN090D_FORMMAIN_DEF:
#			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
#			if _thisItemLen_ != 6:
#				doErrorItem("not 6 items", _thisItem_)
#				continue
#			thisMainframeName_ = _thisItem_[2]
#			_thisElementName_ = _thisItem_[3]
#			thisFinalize_ = _thisItem_[4]
#			if thisFinalize_ == "True":
#				FMPSG_SCTN090D_FORMMAIN_DICT[thisMainframeName_] = f"""{NTAB(3)}**{_thisElementName_},{NEWLINE}{NTAB(2)}{CPAREN}.finalize{OPAREN}{CPAREN}{NEWLINE}{NEWLINE}"""
#			else:
#				FMPSG_SCTN090D_FORMMAIN_DICT[thisMainframeName_] = f"""{NTAB(3)}**{_thisElementName_},{NEWLINE}{NTAB(2)}{CPAREN}{NEWLINE}{NEWLINE}"""
#			continue
#			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN090D_ENDS_FORMMAIN

# SCTN090E_BEGINS_LAYOUT
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090E_LAYOUT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			if _thisElementName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_] = {}
			FMPSG_SCTN090E_LAYOUT_CMNT_DICT[_thisElementName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			if _thisElementName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Button{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090E_LAYOUT_BUTTON_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			if _thisElementName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Checkbox{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090E_LAYOUT_COLUMN_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			if _thisElementName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Col{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090E_LAYOUT_COMBO_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = thisItem[5]
			if _thisElementName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Combo{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090E_LAYOUT_PACKEDPARM_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			_thisVal_ = _thisItem_[6]
			if _thisElementName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}**{_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090E_LAYOUT_PARM_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 9:
				doErrorItem("not 9 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			_thisKey_ = _thisItem_[6]
			_thisVal_ = _thisItem_[7]
			if _thisElementName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}{_thisKey_}={_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090E_LAYOUT_RADIO_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			if _thisElementName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Radio{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090E_LAYOUT_ROW_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			if _thisElementName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_] = {}
			FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][TABLEVEL] = _thisTabLevel_
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090E_LAYOUT_SPIN_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			if _thisElementName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Spin{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090E_LAYOUT_TEXT_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisRowKey_ = _thisItem_[3]
			_thisTabLevel_ = _thisItem_[4]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[5]
			if _thisElementName_ not in FMPSG_SCTN090E_LAYOUT_DICT:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_] = {}
			if _thisRowKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_] = {}
			if _thisElementKey_ not in FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] = ""
			FMPSG_SCTN090E_LAYOUT_DICT[_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Text{OPAREN}  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN090E_ENDS_LAYOUT

# SCTN090F_BEGINS_WINDOW
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090F_WINDOW_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			if _thisElementName_ not in FMPSG_SCTN090F_WINDOW_DICT:
				FMPSG_SCTN090F_WINDOW_DICT[_thisElementName_] = ""
			FMPSG_SCTN090F_WINDOW_CMNT_DICT[_thisElementName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090F_WINDOW_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisElementName_ not in FMPSG_SCTN090F_WINDOW_DICT:
				FMPSG_SCTN090F_WINDOW_DICT[_thisElementName_] = ""
			FMPSG_SCTN090F_WINDOW_DICT[_thisElementName_] += f"""{NTAB(1)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN090F_WINDOW_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			if _thisElementName_ not in FMPSG_SCTN090F_WINDOW_DICT:
				FMPSG_SCTN090F_WINDOW_DICT[_thisElementName_] = ""
			FMPSG_SCTN090F_WINDOW_DICT[_thisElementName_] += f"""{NTAB(1)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN090F_ENDS_WINDOW

# SCTN0910_BEGINS_DEF3
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0910_STR_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMPSG_SCTN0910_DEF3_DICT[_thisValName_] = f"""{DBLQT}{_thisVal_}{DBLQT}"""
			FMPSG_SCTN0910_DEF3_CMNT_DICT[_thisValName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0910_VAL_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisValName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			FMPSG_SCTN0910_DEF3_CMNT_DICT[_thisValName_] = f"""{_thisComment_}"""
			FMPSG_SCTN0910_DEF3_DICT[_thisValName_] += f"""{_thisVal_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0910_ENDS_DEF3

# SCTN0913_BEGINS_RCMENU
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0913_RCMENU_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			if _thisElementName_ not in FMPSG_SCTN0913_RCMENU_DICT:
				FMPSG_SCTN0913_RCMENU_DICT[_thisElementName_] = ""
			FMPSG_SCTN0913_RCMENU_CMNT_DICT[_thisElementName_] = f"""{_thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0913_RCMENU_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue
			_thisElementName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]
			if _thisElementName_ not in FMPSG_SCTN0913_RCMENU_DICT:
				FMPSG_SCTN0913_RCMENU_DICT[_thisElementName_] = ""
			FMPSG_SCTN0913_RCMENU_DICT[_thisElementName_] += f"""{NTAB(2)}{_thisVal_},  # {_thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0913_ENDS_RCMENU

# SCTN0915_BEGINS_??
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN0915_ENDS_??

# SCTN09FF_BEGINS_CLASS
# SCTN09FF_00_BEGINS_CLASS
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 4:
				doErrorItem("not 4 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_DICT:
				FMPSG_SCTN09FF_CLASS_DICT[_thisClassName_] = {}

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_INIT_DICT:
				FMPSG_SCTN09FF_CLASS_INIT_DICT[_thisClassName_] = []

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_CDS_DICT:
				FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_] = []

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT:
				FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT[_thisClassName_] = []

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT:
				FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT[_thisClassName_] = []

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_INIT_DEF3_DICT:
				FMPSG_SCTN09FF_CLASS_INIT_DEF3_DICT[_thisClassName_] = []

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_FUNCTION_DICT:
				FMPSG_SCTN09FF_CLASS_FUNCTION_DEF2_DICT[_thisClassName_] = []

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_FUNCTION_DEF1_DICT:
				FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT[_thisClassName_] = []

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_FUNCTION_DEF2_DICT:
				FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT[_thisClassName_] = []

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT:
				FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT[_thisClassName_] = []
				FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT[_thisClassName_] = []

			FMPSG_SCTN09FF_CLASS_CMNT_DICT[_thisClassName_] = f"""{_thisComment_}"""
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_00_ENDS_CLASS

# SCTN09FF_01_BEGINS_CLASS_BTN
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_BTN_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_BTNS_DICT:
				FMPSG_SCTN09FF_CLASS_BTNS_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_BTNS_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_BTNS_DICT[_thisClassName_][_thisElementName_] = ""

			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisElementName_[1:-1]}: self.{_thisElementName_},  # {_thisComment_}{NEWLINE}""")

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_BTNS_CMNT_DICT:
				FMPSG_SCTN09FF_CLASS_BTNS_CMNT_DICT[_thisClassName_] = {}

			FMPSG_SCTN09FF_CLASS_BTNS_CMNT_DICT[_thisClassName_][_thisElementName_] = f"""{_thisComment_}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_BTN_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			if (_thisKey_ == "KEY"):
				thisValStr_ = f"""f{TRIQT}{OBRCE}self._USE_THIS_KEY_{OPAREN}{_thisVal_}{CPAREN}{CBRCE}{TRIQT}"""
			else:
				thisValStr_ = f"""{DBLQT}{_thisVal_}{DBLQT}"""

			FMPSG_SCTN09FF_CLASS_BTNS_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisKey_}: {thisValStr_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_BTN_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			if (_thisKey_ == "KEY"):
				thisValStr_ = f"""f{TRIQT}{OBRCE}self._USE_THIS_KEY_{OPAREN}{_thisVal_}{CPAREN}{CBRCE}{TRIQT}"""
			else:
				thisValStr_ = f"""{DBLQT}{_thisVal_}{DBLQT}"""

			FMPSG_SCTN09FF_CLASS_BTNS_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisKey_}: {thisValStr_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_01_ENDS_CLASS_BTN

# SCTN09FF_02_BEGINS_CLASS_CHECKBOX
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_CHECKBOX_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT:
				FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT[_thisClassName_][_thisElementName_] = ""

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_CHECKBOX_CMNT_DICT:
				FMPSG_SCTN09FF_CLASS_CHECKBOX_CMNT_DICT[_thisClassName_] = {}

			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K{_thisElementName_[:-1]}: self.{_thisElementName_},  # {_thisComment_}{NEWLINE}""")
			FMPSG_SCTN09FF_CLASS_CHECKBOX_CMNT_DICT[_thisClassName_][_thisElementName_] = f"""{_thisComment_}"""

			thisValStr_ = f"""{_thisElementName_}{CPAREN}{CBRCE}{TRIQT}"""

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_CHECKBOX_ADDON_DICT:
				FMPSG_SCTN09FF_CLASS_CHECKBOX_ADDON_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_CHECKBOX_ADDON_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_CHECKBOX_ADDON_DICT[_thisClassName_][_thisElementName_] = ""

			FMPSG_SCTN09FF_CLASS_CHECKBOX_ADDON_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(2)}self._KEY_DICT_{OBRKT}K{_thisElementName_[:-1]}{CBRKT} = K{_thisElementName_[:-1]}{NEWLINE}"""
			FMPSG_SCTN09FF_CLASS_CHECKBOX_ADDON_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(2)}self._KEY_DICT_REVERSE_{OBRKT}K{_thisElementName_[:-1]}{CBRKT} = K{_thisElementName_[:-1]}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
			# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif (_thisAX_ == FMAXPSG_SCTN09FF_CLASS_CHECKBOX_PARM_ADD):
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]

			FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisVal_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_CHECKBOX_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisKey_}: {DBLQT}_thisVal_{DBLQT},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_CHECKBOX_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisKey_}: _thisVal_,  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_02_ENDS_CLASS_CHECKBOX

# SCTN09FF_03_BEGINS_CLASS_COLUMN
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_COLUMN_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_COLUMN_DICT:
				FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisElementName_] = {}

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_COLUMN_CMNT_DICT:
				FMPSG_SCTN09FF_CLASS_COLUMN_CMNT_DICT[_thisClassName_] = {}

			FMPSG_SCTN09FF_CLASS_COLUMN_CMNT_DICT[_thisClassName_][_thisElementName_] = f"""{_thisComment_}"""
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisElementName_[1:-1]}: self.{_thisElementName_},  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_COLUMN_BUTTON_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			if _thisElementKey_ not in FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_]:
				FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_][_thisElementKey_] = ""

			FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Button{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_COLUMN_CHECKBOX_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			if _thisElementKey_ not in FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_]:
				FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_][_thisElementKey_] = ""

			FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Checkbox{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_COLUMN_COLUMN_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			if _thisElementKey_ not in FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_]:
				FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_][_thisElementKey_] = ""

			FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Column{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_COLUMN_COMBO_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			if _thisElementKey_ not in FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_]:
				FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_][_thisElementKey_] = ""

			FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Combo{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_COLUMN_PACKEDPARM_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			if _thisElementKey_ not in FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_]:
				FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_][_thisElementKey_] = ""

			FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}**{_thisElementKey_}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_COLUMN_PARM_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 9:
				doErrorItem("not 9 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisColumnName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]
			_thisVal_ = _thisItem_[7]

			if _thisElementKey_ not in FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_]:
				FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_][_thisElementKey_] = ""

			FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}{_thisVal_}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_COLUMN_RADIO_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			if _thisElementKey_ not in FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_]:
				FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_][_thisElementKey_] = ""

			FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Radio{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_COLUMN_ROW_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisColumnName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])

			if _thisRowKey_ not in FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_]:
				FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_] = {}

			FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][TABLEVEL] = _thisTabLevel_

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_COLUMN_SPIN_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisColumnName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			if _thisElementKey_ not in FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_]:
				FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_][_thisElementKey_] = ""

			FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Spin{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_COLUMN_TEXT_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisColumnName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			if _thisElementKey_ not in FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_]:
				FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_][_thisElementKey_] = ""

			FMPSG_SCTN09FF_CLASS_COLUMN_DICT[_thisClassName_][_thisColumnName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Text{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_03_ENDS_CLASS_COLUMN

# SCTN09FF_04_BEGINS_CLASS_COMBO
# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_04_ENDS_CLASS_COMBO

# SCTN09FF_05_BEGINS_CLASS_DICT
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_DICT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisDictName_ = _thisItem_[3]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_DICT_DICT:
				FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_] = {}
			if _thisDictName_ not in FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_][_thisDictName_] = ""

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT:
				FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT[_thisClassName_] = {}

			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K{_thisDictName_[:-1]}: self.{_thisDictName_},  # {_thisComment_}{NEWLINE}""")
			FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT[_thisClassName_][_thisDictName_] = f"""{_thisComment_}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_DICT_SS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisDictName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_][_thisDictName_] += f"""{NTAB(3)}{DBLQT}{_thisKey_}{DBLQT}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_DICT_SV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisDictName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_][_thisDictName_] += f"""{NTAB(3)}{DBLQT}{_thisKey_}{DBLQT}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_DICT_VS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisDictName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_][_thisDictName_] += f"""{NTAB(3)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_DICT_VV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisDictName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_][_thisDictName_] += f"""{NTAB(3)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_05_ENDS_CLASS_DICT

# SCTN09FF_05_BEGINS_CLASS_DPD
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_DPD_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisDictName_ = _thisItem_[3]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_DICT_DICT:
				FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_] = {}
			if _thisDictName_ not in FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_][_thisDictName_] = ""

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT:
				FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT[_thisClassName_] = {}

			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K{_thisDictName_[:-1]}: self.{_thisDictName_},  # {_thisComment_}{NEWLINE}""")
			FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT[_thisClassName_][_thisDictName_] = f"""{_thisComment_}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_DPD_VV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisDictName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN0900_DEF1_DICT[_thisKey_] = f"""{DBLQT}{_thisKey_}{DBLQT}"""
			FMPSG_SCTN0900_DEF1_CMNT_DICT[_thisKey_] = f"""{_thisComment_}"""
			FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_][_thisDictName_] += f"""{NTAB(3)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_05_ENDS_CLASS_DPD

# SCTN09FF_04_BEGINS_CLASS_FRAMEELEMENT
# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_04_ENDS_CLASS_FRAMEELEMENT

# SCTN09FF_06_BEGINS_CLASS_FUNCTION
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_theseParms_ = _thisItem_[4]
			_thisDPDBool_ = _thisItem_[5]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_FUNCTION_DICT:
				FMPSG_SCTN09FF_CLASS_FUNCTION_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_FUNCTION_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_FUNCTION_DICT[_thisClassName_][_thisElementName_] = []

			FMPSG_SCTN09FF_CLASS_FUNCTION_DICT[_thisClassName_][_thisElementName_].append(f"""{NTAB(1)}def {_thisElementName_}{OPAREN}self{_theseParms_}{CPAREN}:""")

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_FUNCTION_CMNT_DICT:
				FMPSG_SCTN09FF_CLASS_FUNCTION_CMNT_DICT[_thisClassName_] = {}

			FMPSG_SCTN09FF_CLASS_FUNCTION_CMNT_DICT[_thisClassName_][_thisElementName_] = f"""{_thisComment_}"""

			FMPSG_SCTN0900_DEF1_DICT[_thisElementName_.upper()] = f"""F_{DBLQT}{_thisElementName_.upper()}{DBLQT}"""
			FMPSG_SCTN0900_DEF1_CMNT_DICT[_thisElementName_.upper()] = f"""{_thisComment_}"""
			FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_]["_DPD_"] += f"""{NTAB(3)}{_thisKey_}: {_thisDPDBool_},  # {_thisComment_}{NEWLINE}"""

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_DICT_DICT:
				FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_] = {}
			if "_DPD_" not in FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_]["_DPD_"] = ""

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT:
				FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT[_thisClassName_] = {}

			FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_]["_DPD_"] += f"""{NTAB(3)}F_{_thisElementName_.upper()}: {_thisDPDBool_},  # {_thisComment_}{NEWLINE}"""
			FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT[_thisClassName_]["_DPD_"] = f"""{_thisComment_}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_FUNCTION_DEF_FROM_FILE:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisFilename_ = _thisItem_[4]
			_thisDPDBool_ = _thisItem_[5]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_FUNCTION_DICT:
				FMPSG_SCTN09FF_CLASS_FUNCTION_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_FUNCTION_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_FUNCTION_DICT[_thisClassName_][_thisElementName_] = []

			FMPSG_SCTN09FF_CLASS_FUNCTION_DICT[_thisClassName_][_thisElementName_].append(f"""{readFileToStr("res/functions/" + _thisFilename_)}""")

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_FUNCTION_CMNT_DICT:
				FMPSG_SCTN09FF_CLASS_FUNCTION_CMNT_DICT[_thisClassName_] = {}

			FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_]["_DPD_"] += f"""{NTAB(3)}F_{_thisElementName_.upper()}: {_thisDPDBool_},  # {_thisComment_}{NEWLINE}"""
			FMPSG_SCTN09FF_CLASS_FUNCTION_CMNT_DICT[_thisClassName_][_thisElementName_] = f"""{_thisComment_}"""
			FMPSG_SCTN0900_DEF1_DICT[f"""F_{_thisElementName_.upper()}"""] = f"""{DBLQT}F_{_thisElementName_.upper()}{DBLQT}"""
			FMPSG_SCTN0900_DEF1_CMNT_DICT[f"""F_{_thisElementName_.upper()}"""] = f"""{_thisComment_}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_FUNCTION_BLANKLINE:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]

			FMPSG_SCTN09FF_CLASS_FUNCTION_DICT[_thisClassName_][_thisElementName_].append(f"""{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_FUNCTION_LINE_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisLine_ = _thisItem_[4]

			FMPSG_SCTN09FF_CLASS_FUNCTION_DICT[_thisClassName_][_thisElementName_].append(f"""{NTAB(2)}{_thisLine_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_FUNCTION_READ_FROM_FILE:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisFilename_ = _thisItem_[4]

			FMPSG_SCTN09FF_CLASS_FUNCTION_DICT[_thisClassName_][_thisElementName_].append(f"""{readFileToStr("res/functions/" + _thisFilename_)}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_FUNCTION_STR1_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisValName_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN09FF_CLASS_FUNCTION_DEF1_DICT[_thisClassName_][_thisElementName_].append(f"""{NTAB(2)}{_thisValName_} = {DBLQT}{_thisVal_}{DBLQT}  # {_thisComment_}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_FUNCTION_STR2_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisValName_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN09FF_CLASS_FUNCTION_DEF2_DICT[_thisClassName_][_thisElementName_].append(f"""{NTAB(2)}{_thisValName_} = {DBLQT}{_thisVal_}{DBLQT}  # {_thisComment_}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif (_thisAX_ == FMAXPSG_SCTN09FF_CLASS_FUNCTION_VAL1_DEF):
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisValName_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN09FF_CLASS_FUNCTION_DEF1_DICT[_thisClassName_][_thisElementName_].append(f"""{NTAB(2)}{_thisValName_} = {_thisVal_}  # {_thisComment_}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif (_thisAX_ == FMAXPSG_SCTN09FF_CLASS_FUNCTION_VAL2_DEF):
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisValName_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN09FF_CLASS_FUNCTION_DEF2_DICT[_thisClassName_][_thisElementName_].append(f"""{NTAB(2)}{_thisValName_} = {_thisVal_}  # {_thisComment_}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_06_ENDS_CLASS_FUNCTIONS

# SCTN09FF_07_BEGINS_CLASS_INIT
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisParmStr_ = _thisItem_[3]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_INIT_DICT:
				FMPSG_SCTN09FF_CLASS_INIT_DICT[_thisClassName_] = []

			FMPSG_SCTN09FF_CLASS_INIT_DICT[_thisClassName_].append(f"""{_thisParmStr_}""")
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_DICTIN: self._DICTIN_,{NEWLINE}""")
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_DICTINSTR: self._DICTINSTR_,{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LAMBDA:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisValName_ = _thisItem_[3]
			_thisLambda_ = _thisItem_[4]

			_thisLambda_ = subMyPlaceKpr(_thisLambda_)
			FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT[_thisClassName_].append(f"""{NTAB(2)}self.{_thisValName_} = lambda {_thisLambda_}  # {_thisComment_}{NEWLINE}""")
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisValName_[1:-1]}: self.{_thisValName_},{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_LINE:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisLine_ = _thisItem_[3]
			_thisLine_ = subMyPlaceKpr(_thisLine_)

			FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT[_thisClassName_].append(f"""{NTAB(2)}{_thisLine_}  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_READ_FROM_FILE:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisFilename_ = _thisItem_[3]

			FMPSG_SCTN09FF_CLASS_INIT_DICT[_thisClassName_].append(f"""{readFileToStr(_thisFilename_)}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_STR:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisValName_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]

			FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT[_thisClassName_].append(f"""{NTAB(2)}self.{_thisValName_} = {DBLQT}{_thisVal_}{DBLQT}  # {_thisComment_}{NEWLINE}""")
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisValName_[1:-1]}: self.{_thisValName_},{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD1_VAL:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisValName_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]

			FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT[_thisClassName_].append(f"""{NTAB(2)}self.{_thisValName_} = {_thisVal_}  # {_thisComment_}{NEWLINE}""")
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisValName_[1:-1]}: self.{_thisValName_},{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_SS:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]

			FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT[_thisClassName_].append(f"""{NTAB(3)}{DBLQT}{_thisKey_}{DBLQT}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}""")
			FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT[_thisClassName_].append(f"""{NTAB(3)}{DBLQT}{_thisKey_}{DBLQT}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_SV:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]

			FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT[_thisClassName_].append(f"""{NTAB(3)}{DBLQT}{_thisKey_}{DBLQT}: {_thisVal_},  # {_thisComment_}{NEWLINE}""")
			FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT[_thisClassName_].append(f"""{NTAB(3)}{DBLQT}{_thisKey_}{DBLQT}: {_thisVal_},  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VS:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			_isARevKeyItem_ = _thisItem_[5]

			if (_isARevKeyItem_ == "True"):
				FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT[_thisClassName_].append(f"""{NTAB(3)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}""")
				FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT[_thisClassName_].append(f"""{NTAB(3)}f{TRIQT}{OBRCE}self._USE_THIS_KEY_{OPAREN}{_thisKey_}{CPAREN}{CBRCE}{TRIQT}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}""")

			else:
				FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT[_thisClassName_].append(f"""{NTAB(3)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}""")
				FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT[_thisClassName_].append(f"""{NTAB(3)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_DICTIN_VV:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]
			_isARevKeyItem_ = _thisItem_[5]

			if (_isARevKeyItem_ == "True"):
				FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT[_thisClassName_].append(f"""{NTAB(3)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}""")
				FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT[_thisClassName_].append(f"""{NTAB(3)}f{TRIQT}{OBRCE}self._USE_THIS_KEY_{OPAREN}{_thisKey_}{CPAREN}{CBRCE}{TRIQT}: {_thisVal_},  # {_thisComment_}{NEWLINE}""")

			else:
				FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT[_thisClassName_].append(f"""{NTAB(3)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}""")
				FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT[_thisClassName_].append(f"""{NTAB(3)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisKey_ = _thisItem_[3]
			_thisReverseKey_ = _thisItem_[4]
			_isARevKeyItem_ = _thisItem_[5]

			if _isARevKeyItem_ == "True":
				FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT[_thisClassName_].append(f"""{NTAB(2)}self._KEY_DICT_{OBRKT}{_thisKey_}{CBRKT} = {_thisReverseKey_}  # {_thisComment_}{NEWLINE}""")
				FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT[_thisClassName_].append(f"""{NTAB(2)}self._KEY_DICT_REVERSE_{OBRKT}{_thisReverseKey_}{CBRKT} = {_thisKey_}  # {_thisComment_}{NEWLINE}""")

			else:
				FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT[_thisClassName_].append(f"""{NTAB(2)}self._KEY_DICT_{OBRKT}{_thisKey_}{CBRKT} = {_thisReverseKey_}  # {_thisComment_}{NEWLINE}""")
				FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT[_thisClassName_].append(f"""{NTAB(2)}self._KEY_DICT_REVERSE_{OBRKT}{_thisReverseKey_}{CBRKT} = {_thisKey_}  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_LAMBDA:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisValName_ = _thisItem_[3]
			_thisLambda_ = _thisItem_[4]

			_thisLambda_ = subMyPlaceKpr(_thisLambda_)
			FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT[_thisClassName_].append(f"""{NTAB(2)}self.{_thisValName_} = lambda {_thisLambda_}  # {_thisComment_}{NEWLINE}""")
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisValName_[1:-1]}: self.{_thisValName_},{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_LINE:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisLine_ = _thisItem_[3]
			_thisLine_ = subMyPlaceKpr(_thisLine_)

			FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT[_thisClassName_].append(f"""{NTAB(2)}{_thisLine_}  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_STR:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisValName_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]

			FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT[_thisClassName_].append(f"""{NTAB(2)}self.{_thisValName_} = {DBLQT}{_thisVal_}{DBLQT}  # {_thisComment_}{NEWLINE}""")
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisValName_[1:-1]}: self.{_thisValName_},{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_VAL:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisValName_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]

			FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT[_thisClassName_].append(f"""{NTAB(2)}self.{_thisValName_} = {_thisVal_}  # {_thisComment_}{NEWLINE}""")
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisValName_[1:-1]}: self.{_thisValName_},{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_INIT_ADD3_LINE:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisLine_ = _thisItem_[3]
			_thisLine_ = subMyPlaceKpr(_thisLine_)

			FMPSG_SCTN09FF_CLASS_INIT_DEF3_DICT[_thisClassName_].append(f"""{NTAB(2)}{_thisLine_}  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_07_ENDS_CLASS_INIT

# SCTN09FF_08_BEGINS_CLASS_LAYOUT
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_LAYOUT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_LAYOUT_DICT:
				FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisElementName_] = {}

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_LAYOUT_CMNT_DICT:
				FMPSG_SCTN09FF_CLASS_LAYOUT_CMNT_DICT[_thisClassName_] = {}

			FMPSG_SCTN09FF_CLASS_LAYOUT_CMNT_DICT[_thisClassName_][_thisElementName_] = f"""{_thisComment_}"""
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisElementName_[1:-1]}: self.{_thisElementName_},  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_LAYOUT_BUTTON_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Button{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_LAYOUT_CHECKBOX_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Checkbox{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_LAYOUT_COLUMN_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			if _thisElementKey_ not in FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisElementName_][_thisRowKey_]:
				FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] = ""

			FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Column{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_LAYOUT_COMBO_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Combo{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_LAYOUT_PACKEDPARM_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 9:
				doErrorItem("not 9 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]
			_thisVal_ = _thisItem_[7]

			FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}**{_thisVal_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_LAYOUT_PARM_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 10:
				doErrorItem("not 10 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisLayoutName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]
			_thisValKey_ = _thisItem_[7]
			_thisVal_ = _thisItem_[8]

			FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisLayoutName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}{_thisValKey_}={_thisVal_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_LAYOUT_RADIO_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisElementName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Radio{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_LAYOUT_ROW_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisLayoutName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])

			if _thisRowKey_ not in FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisLayoutName_]:
				FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisLayoutName_][_thisRowKey_] = {}

			FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisLayoutName_][_thisRowKey_][TABLEVEL] = _thisTabLevel_

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_LAYOUT_SPIN_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisLayoutName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			if _thisElementKey_ not in FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_][_thisLayoutName_][thisRowKey_]:
				FMPSG_SCTN09FF_CLASS_DICT_DICT[_thisClassName_][_thisLayoutName_][_thisRowKey_][_thisElementKey_] = {}

			FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisLayoutName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Spin{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_LAYOUT_TEXT_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 8:
				doErrorItem("not 8 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisLayoutName_ = _thisItem_[3]
			_thisRowKey_ = _thisItem_[4]
			_thisTabLevel_ = _thisItem_[5]
			_thisTabLevel_ = int(_thisTabLevel_[1:])
			_thisElementKey_ = _thisItem_[6]

			FMPSG_SCTN09FF_CLASS_LAYOUT_DICT[_thisClassName_][_thisLayoutName_][_thisRowKey_][_thisElementKey_] += f"""{NTAB(_thisTabLevel_)}SG.Text{OPAREN}  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_08_ENDS_CLASS_LAYOUT

# SCTN09FF_09_BEGINS_CLASS_LIST
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0903_LIST_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisListName_ = _thisItem_[3]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_LIST_DICT:
				FMPSG_SCTN09FF_CLASS_LIST_DICT[_thisClassName_] = {}
			if _thisListName_ not in FMPSG_SCTN09FF_CLASS_LIST_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_LIST_DICT[_thisClassName_][_thisListName_] = ""

			FMPSG_SCTN09FF_CLASS_LIST_CMNT_DICT[_thisListName_] = f"""{_thisComment_}"""
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisElementName_[1:-1]}: self.{_thisElementName_},  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0903_LIST_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisListName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]

			FMPSG_SCTN0903_LIST_DICT[_thisListName_] += f"""{NTAB(1)}{DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN0903_LIST_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisListName_ = _thisItem_[2]
			_thisVal_ = _thisItem_[3]

			FMPSG_SCTN0903_LIST_DICT[_thisListName_] += f"""{NTAB(1)}{_thisVal_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_09_ENDS_CLASS_LIST

# SCTN09FF_04_BEGINS_CLASS_RADIO
# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_04_ENDS_CLASS_RADIO

# SCTN09FF_04_BEGINS_CLASS_RCMENU
# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_04_ENDS_CLASS_RCMENU

# SCTN09FF_0A_BEGINS_CLASS_SPIN
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_SPIN_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_SPIN_DICT:
				FMPSG_SCTN09FF_CLASS_SPIN_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_SPIN_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_SPIN_DICT[_thisClassName_][_thisElementName_] = {}

			if _thisClassName_ not in FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT:
				FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[_thisClassName_]:
				FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[_thisClassName_][_thisElementName_] = ""

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_SPIN_CMNT_DICT:
				FMPSG_SCTN09FF_CLASS_SPIN_CMNT_DICT[_thisClassName_] = {}

			FMPSG_SCTN09FF_CLASS_SPIN_CMNT_DICT[_thisClassName_][_thisElementName_] = f"""{_thisComment_}"""
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisElementName_[1:-1]}: self.{_thisElementName_},  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_SPIN_DICT_VS_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			if (_thisKey_ == "VALUES") and (_thisVal_ == "%LIST%"):
				thisValStr_ = f"""self.{_thisClassName_}{_thisElementName_}_LIST"""
			else:
				thisValStr_ = f"""{DBLQT}{_thisVal_}{DBLQT}"""

			FMPSG_SCTN09FF_CLASS_SPIN_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisKey_}: {thisValStr_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_SPIN_DICT_VV_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			if (_thisKey_ == "VALUES") and (_thisVal_ == "%LIST%"):
				thisValStr_ = f"""self.{_thisElementName_}_SPIN_LIST"""
			else:
				thisValStr_ = f"""{_thisVal_}"""

			FMPSG_SCTN09FF_CLASS_SPIN_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisKey_}: {thisValStr_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_SPIN_LIST_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]

			FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_SPIN_LIST_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]

			FMPSG_SCTB0916_CLASS_SPIN_LIST_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisVal_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_0A_ENDS_CLASS_SPIN

# SCTN09FF_0B_BEGINS_CLASS_TEXT
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_TEXT_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_isThisATime_ = _thisItem_[4]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_TEXT_DICT:
				FMPSG_SCTN09FF_CLASS_TEXT_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_TEXT_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_TEXT_DICT[_thisClassName_][_thisElementName_] = ""

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT:
				FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_][_thisElementName_] = ""

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_TEXT_CMNT_DICT:
				FMPSG_SCTN09FF_CLASS_TEXT_CMNT_DICT[_thisClassName_] = {}

			if _isThisATime_ == "True":
				FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(2)}self._KEY_LIST_TIMES_.append({_thisElementName_[1:-1]}){NEWLINE}"""
				FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(2)}self._KEY_LIST_TIMES_.append(self._USE_THIS_KEY_({_thisElementName_[1:-1]})){NEWLINE}"""

			FMPSG_SCTN09FF_CLASS_TEXT_CMNT_DICT[_thisClassName_][_thisElementName_] = f"""{_thisComment_}"""
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisElementName_[1:-1]}: self.{_thisElementName_},  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_TEXT_PARM_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 6:
				doErrorItem("not 6 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisVal_ = _thisItem_[4]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT:
				FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_][_thisElementName_] = ""

			FMPSG_SCTN09FF_CLASS_TEXT_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisVal_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_TEXT_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue
			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT:
				FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_] = {}

			if (_thisKey_ == "KEY"):
				thisValStr_ = f"""f{TRIQT}{OBRCE}self._USE_THIS_KEY_{OPAREN}{_thisVal_}{CPAREN}{CBRCE}{TRIQT}"""

				if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_]:
					FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_][_thisElementName_] = ""

				FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(2)}self._KEY_DICT_{OBRKT}{_thisVal_}{CBRKT} = f{TRIQT}{OBRCE}self._USE_THIS_KEY_{OPAREN}{_thisVal_}{CPAREN}{CBRCE}{TRIQT}{NEWLINE}"""
				FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(2)}self._KEY_DICT_REVERSE_{OBRKT}f{TRIQT}{OBRCE}self._USE_THIS_KEY_{OPAREN}{_thisVal_}{CPAREN}{CBRCE}{TRIQT}{CBRKT} = {_thisVal_}{NEWLINE}"""

			else:
				thisValStr_ = f"""{_thisVal_}"""

			FMPSG_SCTN09FF_CLASS_TEXT_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisKey_}: {DBLQT}{thisValStr_}{DBLQT},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_TEXT_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			if (_thisKey_ == "KEY"):
				thisValStr_ = f"""f{TRIQT}{OBRCE}self._USE_THIS_KEY_{OPAREN}{_thisVal_}{CPAREN}{CBRCE}{TRIQT}"""

				if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_]:
					FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_][_thisElementName_] = ""

				FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(2)}self._KEY_DICT_{OBRKT}{_thisVal_}{CBRKT} = f{TRIQT}{OBRCE}self._USE_THIS_KEY_{OPAREN}{_thisVal_}{CPAREN}{CBRCE}{TRIQT}{NEWLINE}"""
				FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(2)}self._KEY_DICT_REVERSE_{OBRKT}f{TRIQT}{OBRCE}self._USE_THIS_KEY_{OPAREN}{_thisVal_}{CPAREN}{CBRCE}{TRIQT}{CBRKT} = {_thisVal_}{NEWLINE}"""

			else:
				thisValStr_ = f"""{_thisVal_}"""

			FMPSG_SCTN09FF_CLASS_TEXT_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisKey_}: {thisValStr_},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_0B_ENDS_CLASS_TEXT

# SCTN09FF_89_BEGINS_CLASS_WINDOW
	# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_WINDOW_DEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 5:
				doErrorItem("not 5 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_WINDOW_DICT:
				FMPSG_SCTN09FF_CLASS_WINDOW_DICT[_thisClassName_] = {}
			if _thisElementName_ not in FMPSG_SCTN09FF_CLASS_WINDOW_DICT[_thisClassName_]:
				FMPSG_SCTN09FF_CLASS_WINDOW_DICT[_thisClassName_][_thisElementName_] = ""

			if _thisClassName_ not in FMPSG_SCTN09FF_CLASS_WINDOW_CMNT_DICT:
				FMPSG_SCTN09FF_CLASS_WINDOW_CMNT_DICT[_thisClassName_] = {}

			FMPSG_SCTN09FF_CLASS_WINDOW_CMNT_DICT[_thisClassName_][_thisElementName_] = f"""{_thisComment_}"""
			FMPSG_SCTN09FF_CLASS_CDS_DICT[_thisClassName_].append(f"""{NTAB(3)}K_{_thisElementName_[1:-1]}: self.{_thisElementName_},  # {_thisComment_}{NEWLINE}""")

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_WINDOW_STR_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN09FF_CLASS_WINDOW_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisKey_}: {DBLQT}{_thisVal_}{DBLQT},  # {_thisComment_}{NEWLINE}"""

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for _thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if _thisAX_ …
		elif _thisAX_ == FMAXPSG_SCTN09FF_CLASS_WINDOW_VAL_ADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if _thisItemLen_ != 7:
				doErrorItem("not 7 items", _thisItem_)
				continue

			_thisClassName_ = _thisItem_[2]
			_thisElementName_ = _thisItem_[3]
			_thisKey_ = _thisItem_[4]
			_thisVal_ = _thisItem_[5]

			FMPSG_SCTN09FF_CLASS_WINDOW_DICT[_thisClassName_][_thisElementName_] += f"""{NTAB(3)}{_thisKey_}: {_thisVal_},  # {_thisComment_}{NEWLINE}"""

			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2


	# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
# SCTN09FF_89_ENDS_CLASS_WINDOW

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
# SCTN09FF_ENDS


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# __main__
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def __main__():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

	# FMFM_MAIN_BEGINS
	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	with open(TBGLST_NAME, "tw") as __FDOut__:
		__FDOut__.write(f"TBGLST = {OBRKT}{NEWLINE}{NTAB(1)}{FOLD1STARTHERE}{NEWLINE}")
		parseTBGLST(__FDOut__)
		__FDOut__.write(f"{NTAB(1)}{FOLD1ENDHERE}{NEWLINE}{CBRKT}{NEWLINE}")

	with open(FM_NAME, "tw") as __FDOut__:
		strToWrt_ = makeFM()
		__FDOut__.writelines(strToWrt_)
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# FMFM_MAIN_ENDS

	# FMCF_MAIN_BEGINS
	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	with open(CF_NAME, "tw") as __FDOut__:
		strToWrt_ = makeCF()
		__FDOut__.writelines(strToWrt_)
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# FMCF_MAIN_ENDS

	# FMPSG_MAIN_BEGINS
	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	with open(PSG_NAME, "tw") as __FDOut__:
		strToWrt_ = makePSG()
		__FDOut__.writelines(strToWrt_)
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
