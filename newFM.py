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
	"%REVKEY%": lambda __key__: f"""f{TRIQT}{OBRCE}self._KEY_DICT_REVERSE_[{__key__}]{CBRCE}{TRIQT}"""
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
FMAXPSG_SCTN09FF_CLASS_INIT_BLANKLINE = "FMAXPSG_SCTN09FF_CLASS_INIT_BLANKLINE"  # blank line in __init__ <NAC><CLASSNAME>
FMAXPSG_SCTN09FF_CLASS_INIT_DEF = "FMAXPSG_SCTN09FF_CLASS_INIT_DEF"  # define a class <NAC><CLASSNAME><PARMS>
FMAXPSG_SCTN09FF_CLASS_INIT_DICTIN_SS_ADD = "FMAXPSG_SCTN09FF_CLASS_INIT_DICTIN_SS_ADD"  # add a str-str to a dict <NAC><CLASSNAME><STR><STR>
FMAXPSG_SCTN09FF_CLASS_INIT_DICTIN_SV_ADD = "FMAXPSG_SCTN09FF_CLASS_INIT_DICTIN_SV_ADD"  # add a str-val to a dict <NAC><CLASSNAME><STR><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_DICTIN_VS_ADD = "FMAXPSG_SCTN09FF_CLASS_INIT_DICTIN_VS_ADD"  # add a str to a dict <NAC><CLASSNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_DICTIN_VV_ADD = "FMAXPSG_SCTN09FF_CLASS_INIT_DICTIN_VV_ADD"  # add a val to a dict in PSG <NAC><CLASSNAME><KEY><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_LAMBDA1_DEF = "FMAXPSG_SCTN09FF_CLASS_INIT_LAMBDA1_DEF"  # define a string in the class <NAC><CLASSNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_LAMBDA2_DEF = "FMAXPSG_SCTN09FF_CLASS_INIT_LAMBDA2_DEF"  # define a value in the class <NAC><CLASSNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_LINE_ADD = "FMAXPSG_SCTN09FF_CLASS_INIT_LINE_ADD"  # define a class <NAC><CLASSNAME><LINE>
FMAXPSG_SCTN09FF_CLASS_INIT_READ_FROM_FILE = "FMAXPSG_SCTN09FF_CLASS_INIT_READ_FROM_FILE"  # define a class <NAC><CLASSNAME><FILENAME>
FMAXPSG_SCTN09FF_CLASS_INIT_STR1_DEF = "FMAXPSG_SCTN09FF_CLASS_INIT_STR1_DEF"  # define a string in the class <NAC><CLASSNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_STR2_DEF = "FMAXPSG_SCTN09FF_CLASS_INIT_STR2_DEF"  # define a string in the class <NAC><CLASSNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_VAL1_DEF = "FMAXPSG_SCTN09FF_CLASS_INIT_VAL1_DEF"  # define a value in the class <NAC><CLASSNAME><VALNAME><VAL>
FMAXPSG_SCTN09FF_CLASS_INIT_VAL2_DEF = "FMAXPSG_SCTN09FF_CLASS_INIT_VAL2_DEF"  # define a value in the class <NAC><CLASSNAME><VALNAME><VAL>
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
	FMAXPSG_SCTN09FF_CLASS_INIT_BLANKLINE,  # blank line in __init__ <NAC><CLASSNAME>
	FMAXPSG_SCTN09FF_CLASS_INIT_DEF,  # define a class <NAC><CLASSNAME><PARMS>
	FMAXPSG_SCTN09FF_CLASS_INIT_DICTIN_SS_ADD,  # add a str-str to a dict <NAC><CLASSNAME><STR><STR>
	FMAXPSG_SCTN09FF_CLASS_INIT_DICTIN_SV_ADD,  # add a str-val to a dict <NAC><CLASSNAME><STR><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_DICTIN_VS_ADD,  # add a str to a dict <NAC><CLASSNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_DICTIN_VV_ADD,  # add a val to a dict in PSG <NAC><CLASSNAME><KEY><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_LAMBDA1_DEF,  # define a string in the class <NAC><CLASSNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_LAMBDA2_DEF,  # define a value in the class <NAC><CLASSNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_LINE_ADD,  # define a class <NAC><CLASSNAME><LINE>
	FMAXPSG_SCTN09FF_CLASS_INIT_READ_FROM_FILE,  # define a class <NAC><CLASSNAME><FILENAME>
	FMAXPSG_SCTN09FF_CLASS_INIT_STR1_DEF,  # define a string in the class <NAC><CLASSNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_STR2_DEF,  # define a string in the class <NAC><CLASSNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_VAL1_DEF,  # define a value in the class <NAC><CLASSNAME><VALNAME><VAL>
	FMAXPSG_SCTN09FF_CLASS_INIT_VAL2_DEF,  # define a value in the class <NAC><CLASSNAME><VALNAME><VAL>
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
FMPSG_SCTN090C_APPDS_CMNT_DICT = {}  # the main app dict for this app
FMPSG_SCTN090C_APPDS_DICT = {}  # the main app dict for this app
FMPSG_SCTN090C_APPDSDICT_DICT = {}  # the main app dict+dict for this app
FMPSG_SCTN090D_FORMMAIN_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN090D_FORMMAIN_DICT = {}  # holds all of the button entriess (TUPDICT)
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
FMPSG_SCTN0914_FORMPOPUP_CMNT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN0914_FORMPOPUP_DICT = {}  # holds all of the DIALOG DIALOG (TUPDICT)
FMPSG_SCTN0915_PUDLG_CMNT_DICT = {}  # holds all of the DIALOG DIALOG (TUPDICT)
FMPSG_SCTN0915_PUDLG_DICT_DICT = {}  # holds all of the DIALOG DIALOG (TUPDICT)
FMPSG_SCTN0915_PUDLG_LIST_DICT = {}  # holds all of the DIALOG DIALOG (TUPDICT)
FMPSG_SCTN0915_PUDLG_TYPE_DICT = {}  # holds all of the DIALOG DIALOG (TUPDICT)
FMPSG_SCTN09FF_CLASS_BTNS_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN09FF_CLASS_BTNS_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN09FF_CLASS_CDS_DICT = {}  # class data storage
FMPSG_SCTN09FF_CLASS_CHECKBOX_CMNT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN09FF_CLASS_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_COLUMN_CMNT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN09FF_CLASS_COLUMN_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN09FF_CLASS_COLUMN_PARMS_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN09FF_CLASS_COMBO_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_COMBO_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_DEF_DICT = {}  # str and val defines in a class
FMPSG_SCTN09FF_CLASS_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_DICT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_FRAME_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_FRAME_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_FUNCTION_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_FUNCTION_DEF1_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_FUNCTION_DEF2_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_FUNCTION_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_INIT_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_INIT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_LAYOUT_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN09FF_CLASS_LAYOUT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN09FF_CLASS_LIST_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_LIST_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_RADIO_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN09FF_CLASS_RADIO_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN09FF_CLASS_RCMENU_CMNT_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_RCMENU_DICT = {}  # define the dict to hold everything in SCTN0900
FMPSG_SCTN09FF_CLASS_SPIN_CMNT_DICT = {}  # holds the spin element stuffs (TUPDICT)f
FMPSG_SCTN09FF_CLASS_SPIN_DICT = {}  # holds the spin element stuffs (TUPDICT)
FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN09FF_CLASS_TEXT_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN09FF_CLASS_TEXT_DICT = {}  # holds all of the button entriess (TUPDICT)
FMPSG_SCTN09FF_CLASS_WINDOW_CMNT_DICT = {}  # holds all of the button entries (TUPDICT)
FMPSG_SCTN09FF_CLASS_WINDOW_DICT = {}  # holds all of the button entriess (TUPDICT)


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
		FMPSG_SCTN09FF_CLASS_BTNS_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_BTNS_DICT, \
		FMPSG_SCTN09FF_CLASS_CDS_DICT, \
		FMPSG_SCTN09FF_CLASS_CHECKBOX_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_CHECKBOX_DICT, \
		FMPSG_SCTN09FF_CLASS_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_COLUMN_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_COLUMN_DICT, \
		FMPSG_SCTN09FF_CLASS_COLUMN_PARMS_DICT, \
		FMPSG_SCTN09FF_CLASS_COMBO_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_COMBO_DICT, \
		FMPSG_SCTN09FF_CLASS_DEF_DICT, \
		FMPSG_SCTN09FF_CLASS_DICT, \
		FMPSG_SCTN09FF_CLASS_DICT_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_DICT_DICT, \
		FMPSG_SCTN09FF_CLASS_FRAME_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_FRAME_DICT, \
		FMPSG_SCTN09FF_CLASS_FUNCTION_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_FUNCTION_DEF1_DICT, \
		FMPSG_SCTN09FF_CLASS_FUNCTION_DEF2_DICT, \
		FMPSG_SCTN09FF_CLASS_FUNCTION_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_DEF1_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_DEF2_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_DICTIN_DICT, \
		FMPSG_SCTN09FF_CLASS_INIT_DICTINSTR_DICT, \
		FMPSG_SCTN09FF_CLASS_LAYOUT_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_LAYOUT_DICT, \
		FMPSG_SCTN09FF_CLASS_LIST_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_LIST_DICT, \
		FMPSG_SCTN09FF_CLASS_RADIO_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_RADIO_DICT, \
		FMPSG_SCTN09FF_CLASS_RCMENU_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_RCMENU_DICT, \
		FMPSG_SCTN09FF_CLASS_SPIN_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_SPIN_DICT, \
		FMPSG_SCTN09FF_CLASS_TEXT_ADDON_DICT, \
		FMPSG_SCTN09FF_CLASS_TEXT_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_TEXT_DICT, \
		FMPSG_SCTN09FF_CLASS_WINDOW_CMNT_DICT, \
		FMPSG_SCTN09FF_CLASS_WINDOW_DICT
