

# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# start of managed sections and file CF.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

from datetime import datetime as DT
from datetime import timedelta as TD
from dateutil import parser as PD
from dateutil import tz as TZ
from dateutil.relativedelta import relativedelta as RD
from sys import argv
from sys import exit
from time import localtime as LT
from time import mktime as MT
from time import monotonic as TMT
from time import time as WALLSECS
from time import time_ns as TNS
import datedelta as DD
import datetime
import gc
import hashlib as HL
import inspect
import os.path as OSPATH
import pickle as PD
import pprint


ABSPATH = OSPATH.abspath
ABS_DOT = ABSPATH(".")
EXISTS = OSPATH.exists
gc.enable()
HOME = f"{OSPATH.expanduser('~')}"
PP = pprint.PrettyPrinter(indent=2)
TMTSS = DT.timestamp
GMTOFFSET = LT().tm_gmtoff


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# modules defined in CF.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * class withPickles(object):
# * def dateIntvlM(dateToUse, months):
# * def dateToStr(dateIn):
# * def displayStats(LN_, COL_, statsStr_):
# * def doAHash(HASH_, stringToHash):
# * def doError(strToOutToErr_):
# * def frameIt(name_, value_):
# * def getDebugInfo():
# * def gmdate(dtObj=DT.now()):
# * def HMSToInt(HMS_):
# * def HMSToNrmlInt(HMS_):
# * def incHMS(HMS_, hours_=0, mins_=0, secs_=0, topTime_=360000):  # 359999 for 99:59:59  86399 for 23:59:59
# * def intToHMS(intHMS_):
# * def ISO2TS(ISOStrIn):
# * def isPast(timeToChk_):
# * def isPastHMS(HMS_):
# * def mergeDicts(bigDict_, dictToAdd_, sortDict_=False):
# * def MTS():
# * def MTSclr():
# * def MTSPlus(numToAdd_):
# * def MTSS():
# * def myPp(objectToPp):
# * def mySleep(fToSleep_):
# * def mysql2LocalTime(SQLTIMEZ):
# * def now():
# * def nowIntHMS(dtObj=DT.now()):
# * def nowStr(dtObj=DT.now()):
# * def nowStrHMS(dtObj=DT.now()):
# * def nowStrSql(dtObj=DT.now()):
# * def nowTimeStr(dtObj=DT.now()):
# * def nowZ():
# * def nowZStr(dtObj=DT.utcnow()):
# * def nowZStrSql(dtObj=DT.utcnow()):
# * def nrmlIntToHMS(nrmlIntHMS_):
# * def outputHelp(argv_):
# * def outputOptionsStruct():
# * def pickleIt(fileName_, dataToPickle_):
# * def print_(*args_):
# * def readFileToStr(FILENAME_):
# * def relDateDiff(startTS, endTS):
# * def relDateDiffStripped(startTS, endTS):
# * def removeDictQuotes(dictToUnquote_):
# * def removeStrQuotes(strToStrip_):
# * def secsI():
# * def setOptions(argv_):
# * def sortADict(dictToSort_):
# * def stripCodes(strToStrip_):
# * def stripCodes(strToStrip_):
# * def stripCodesAndVersion(strToStrip_):
# * def subParms(listIn_, tupDictParms_):
# * def tabsToSpcs(strIn_, numSpcPerTab_=2):
# * def timeHoler(timeStr):
# * def today():
# * def todayStr(dtObj=DT.today()):
# * def tomorrow(dtObj=today()):
# * def tomorrowStr(dtObj=tomorrow()):
# * def toStr(TDIn):
# * def TS2ISO(TSIn):
# * def unPickleIt(fileName_):
# * def USGS2LocalTime(usgsTimeZ):
# * def USGS2MysqlTime(USGSDate):
# * def whirl():
# * def yesterday(dtObj=DT.today()):
# * def yesterdayStr(dtObj=yesterday(DT.today())):


HASH_blake2b = HL.blake2b()  # 64 byte fast hash
HASH_blake2s = HL.blake2s()  # 32 byte fast hash
HASH_md5 = HL.md5()  # 16 byte fastest hash, most likely to collide
HASH_sha1 = HL.sha1()  # 20 byte hash
HASH_sha224 = HL.sha224()  # 28 byte hash
HASH_sha256 = HL.sha256()  # 32 byte hash
HASH_sha3_224 = HL.sha3_224()  # 28 byte hash
HASH_sha3_256 = HL.sha3_256()  # 32 byte hash
HASH_sha3_384 = HL.sha3_384()  # 48 byte hash
HASH_sha3_512 = HL.sha3_512()  # 64 byte hash
HASH_sha384 = HL.sha384()  # 48 byte hash",),
HASH_sha512 = HL.sha512()  # 64 byte hash",),

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
FOLDLEN = 200
GLOBAL_CACHE_DIR = "/home/will/.cache/"
GLOBAL_CONFIG_DIR = "/home/will/.config/"
PY_CONFIG_DIR = "/rcr/0-units/python/"
TRIQT = f"""{DBLQT}{DBLQT}{DBLQT}"""


#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0002 value_ constants
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


BIN04 = lambda __X__: f"""{__X__:04b}"""
BIN08 = lambda __X__: f"""{__X__:08b}"""
BIN16 = lambda __X__: f"""{__X__:016b}"""
BIN32 = lambda __X__: f"""{__X__:032b}"""
BIN64 = lambda __X__: f"""{__X__:064b}"""
CLRALL = f"""{ESC}[2J"""
CLRDOWN = f"""{ESC}[J"""
CLREOL = f"""{ESC}[K"""
CMNTLINE = f"""# * {"#*" * (CMNTLEN // 2)}"""
DICTMODE_KEYSTR = "DICTMODE_KEYSTR"  # define dictmode 'key':val
DICTMODE_KEYVAL = "DICTMODE_KEYVAL"  # define dictmode key:val
EEOL = f"""{ESC}[K"""
EMPTY_DICT = {}
EMPTY_LIST = []
EMPTY_STR = ""
EMPTY_TUPLE = ()
EMPTYSTRLST = [None, "", DBLQT, f"""{DBLQT}{DBLQT}""", SGLQT, f"""{SGLQT}{SGLQT}""", BKQT, "None", "\r", NEWLINE, "\r\n", "\n\r", ]
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
HEX08 = lambda __X__: f"""{__X__:02H}"""  # {thisComment_}
HEX16 = lambda __X__: f"""{__X__:04H}"""  # {thisComment_}
HEX32 = lambda __X__: f"""{__X__:08H}"""  # {thisComment_}
HEX64 = lambda __X__: f"""{__X__:016H}"""  # {thisComment_}
IMPORTANTSTR = f"""# * {"!-" * (CMNTLEN // 2)}"""  # important line marker
INDENTIN = " -=> "  # display arrow RIGHT
INDENTOUT = " <=- "  # display arrow LEFT
INFOSTR = f"""# * {"%_" * (CMNTLEN // 2)}"""  # INFO _STR_ line
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
MOVELEFT = lambda __NUM__: f"""{ESC}[{__NUM__}D"""
MOVETO = lambda __LN__, __COL__: f"""{ESC}[{__LN__};{__COL__}H"""
NCR = lambda __NUM__: f"""{CRSTR * __NUM__}"""
NNL = lambda __NUM__: f"""{NEWLINE * __NUM__}"""
NSPC = lambda __NUM__: f"""{SPCSTR * __NUM__}"""  # returns a string with __NUM__ SPC
NTAB = lambda __NUM__: f"""{TABSTR * __NUM__}"""  # returns a string with __NUM__ TAB
QTSET = [DBLQT, SGLQT, BKQT]  # set of all quote characters
SERIALNUMBER = lambda __NUM__: f"""{(__NUM__ % 0XFFFFFFFF):08X}"""
USER_CACHE_URL = lambda __FILENAME__: f"""{USER_CACHE_DIR}{__FILENAME__}"""
USER_CONFIG_URL = lambda __FILENAME__: f"""{USER_CONFIG_DIR}{__FILENAME__}"""
WHIRLCOUNT = 0
WHIRLSTR = f"""-{BKSLSH}|/*"""


DAY_MS = (60 * 60 * 24 * 1000)  # 86400000
DAY_S = (60 * 60 * 24)  # 86400
HALFDAY_S = (60 * 60 * 12)  # 43200
HALFHOUR_S = (60 * 30)  # 1800
HOUR_S = (60 * 60)  # 3600
MINUTE_S = 60 # 60
QUARTERDAY_S = (60 * 60 * 6)
QUARTERHOUR_S = (60 * 15)  # 900
TIME_S_995959 = (60 * 60 * 100)  # 360000
TIME_S_DDD235959 = (60 * 60 * 24 * 1000)


NAME_GLBL_BTM_PY = lambda __NAME__: f"""{PY_CONFIG_DIR}/{__NAME__}/{__NAME__}_BTM.py"""
NAME_GLBL_IMG_PY = lambda __NAME__, __FILENAME__: f"""{PY_CONFIG_DIR}res/IMG/{__NAME__}/{__FILENAME__}"""
NAME_GLBL_IMG_ROOT_PY = lambda __FILENAME__: f"""{PY_CONFIG_DIR}res/IMG/{__FILENAME__}"""
NAME_GLBL_MD_PY = lambda __NAME__: f"""{PY_CONFIG_DIR}res/MARKDOWN/{__NAME__}.md"""
NAME_GLBL_NEW_PY = lambda __NAME__: f"""{PY_CONFIG_DIR}{__NAME__}/{__NAME__}_NEW.py"""
NAME_GLBL_RES_PY = lambda __FILENAME__: f"""{PY_CONFIG_DIR}res/{__FILENAME__}"""
NAME_GLBL_ROOT_PY = lambda __FILENAME__: f"""{PY_CONFIG_DIR}__ROOT__/{__FILENAME__}"""
NAME_GLBL_SUB_PY = lambda __NAME__, __SUB__: f"""{PY_CONFIG_DIR}{__NAME__}/{__NAME__}_{__SUB__}.py"""
NAME_GLBL_SUB_BTM_PY = lambda __NAME__, __SUB__: f"""{PY_CONFIG_DIR}{__NAME__}/{__NAME__}_{__SUB__}_BTM.py"""
NAME_GLBL_SUB_NEW_PY = lambda __NAME__, __SUB__: f"""{PY_CONFIG_DIR}{__NAME__}/{__NAME__}_{__SUB__}_NEW.py"""
NAME_GLBL_SUB_TOP_PY = lambda __NAME__, __SUB__: f"""{PY_CONFIG_DIR}{__NAME__}/{__NAME__}_{__SUB__}_TOP.py"""
NAME_GLBL_TOP_PY = lambda __NAME__: f"""{PY_CONFIG_DIR}{__NAME__}/{__NAME__}_TOP.py"""


NAME_HOME_CACHE = lambda __FILENAME__: f"""/home/will/.cache/{__FILENAME__}"""
NAME_HOME_CONFIG = lambda __FILENAME__: f"""/home/will/.config/{__FILENAME__}"""
NAME_HOME_SELF_CACHE = lambda __NAME__, __FILENAME__: f"""/home/will/.cache/{__NAME__}/{__FILENAME__}"""
NAME_HOME_SELF_CONFIG = lambda __NAME__, __FILENAME__: f"""/home/will/.config/{__NAME__}/{__FILENAME__}"""


NAME_LCL_BTM_PY = lambda __NAME__: f"""{__NAME__}/{__NAME__}_BTM.py"""
NAME_LCL_IMG_PY = lambda __FILENAME__: f"""res/IMG/{__FILENAME__}"""
NAME_LCL_MD_PY = lambda __FILENAME__: f"""res/MARKDOWN/{__FILENAME__}.md"""
NAME_LCL_NEW_PY = lambda __NAME__: f"""{__NAME__}/{__NAME__}_NEW.py"""
NAME_LCL_RES_PY = lambda __FILENAME__: f"""res/{__FILENAME__}"""
NAME_LCL_ROOT_PY = lambda __FILENAME__: f"""{__FILENAME__}"""
NAME_LCL_SUB_BTM_PY = lambda __NAME__, __SUB__: f"""{__NAME__}/{__NAME__}_{__SUB__}_BTM.py"""
NAME_LCL_SUB_NEW_PY = lambda __NAME__, __SUB__: f"""{__NAME__}/{__NAME__}_{__SUB__}_NEW.py"""
NAME_LCL_SUB_PY = lambda __NAME__, __SUB__: f"""{__NAME__}/{__NAME__}_{__SUB__}.py"""
NAME_LCL_SUB_TOP_PY = lambda __NAME__, __SUB__: f"""{__NAME__}/{__NAME__}_{__SUB__}_TOP.py"""
NAME_LCL_SUB1_BTM_PY = lambda __NAME__, __SUB__, __SUB1__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_BTM.py"""
NAME_LCL_SUB1_NEW_PY = lambda __NAME__, __SUB__, __SUB1__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_NEW.py"""
NAME_LCL_SUB1_PY = lambda __NAME__, __SUB__, __SUB1__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}.py"""
NAME_LCL_SUB1_TOP_PY = lambda __NAME__, __SUB__, __SUB1__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_TOP.py"""
NAME_LCL_SUB2_BTM_PY = lambda __NAME__, __SUB__, __SUB1__, __SUB2__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_{__SUB2__}_BTM.py"""
NAME_LCL_SUB2_NEW_PY = lambda __NAME__, __SUB__, __SUB1__, __SUB2__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_{__SUB2__}_NEW.py"""
NAME_LCL_SUB2_PY = lambda __NAME__, __SUB__, __SUB1__, __SUB2__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_{__SUB2__}.py"""
NAME_LCL_SUB2_TOP_PY = lambda __NAME__, __SUB__, __SUB1__, __SUB2__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_{__SUB2__}_TOP.py"""
NAME_LCL_TOP_PY = lambda __NAME__: f"""{__NAME__}/{__NAME__}_TOP.py"""


STR_SUBST_DICT = {
	"%CBRCE%": f"""{CBRCE}""",
	"%CBRKT%": f"""{CBRKT}""",
	"%CPAREN%": f"""{CPAREN}""",
	"%DQ%": f"""{DBLQT}""",
	"%ESCLN%": f""" {BKSLSH}{NEWLINE}""",
	"%FOLDLN1E%": f"""{FOLD1ENDHERELN}""",
	"%FOLDLN2E%": f"""{FOLD2ENDHERELN}""",
	"%FOLDLN3E%": f"""{FOLD3ENDHERELN}""",
	"%FOLDLN1S%": f"""{FOLD1STARTHERELN}""",
	"%FOLDLN2S%": f"""{FOLD2STARTHERELN}""",
	"%FOLDLN3S%": f"""{FOLD3STARTHERELN}""",
	"%FTQ%": f"""f{TRIQT}""",
	"%FTQTQ%": f"""f{TRIQT}{TRIQT}""",
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

#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0201 CF defines
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0202 options structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
OPTIONS = {
# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
}
# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

OPTIONSHELPDICT = {
# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
}
# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

OPTIONSDICT = {
}


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed sections of CF.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


# <<>>
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of not managed sections of CF.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


from datetime import datetime as DT
from datetime import timedelta as TD
from dateutil import parser as PD
from dateutil import tz as TZ
from dateutil.relativedelta import relativedelta as RD
from sys import argv
from sys import exit
from time import localtime as LT
from time import mktime as MT
from time import monotonic as TMT
from time import time as WALLSECS
from time import time_ns as TNS
import datedelta as DD
import datetime
import gc
import hashlib as HL
import inspect
import os.path as OSPATH
import pickle as PD
import pprint


ABSPATH = OSPATH.abspath
ABS_DOT = ABSPATH(".")
EXISTS = OSPATH.exists
gc.enable()
HOME = f"{OSPATH.expanduser('~')}"
PP = pprint.PrettyPrinter(indent=2)
TMTSS = DT.timestamp
GMTOFFSET = LT().tm_gmtoff


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# modules defined in CF.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * class withPickles(object):
# * def dateIntvlM(dateToUse, months):
# * def dateToStr(dateIn):
# * def displayStats(LN_, COL_, statsStr_):
# * def doAHash(HASH_, stringToHash):
# * def doError(strToOutToErr_):
# * def frameIt(name_, value_):
# * def getDebugInfo():
# * def gmdate(dtObj=DT.now()):
# * def HMSToInt(HMS_):
# * def HMSToNrmlInt(HMS_):
# * def incHMS(HMS_, hours_=0, mins_=0, secs_=0, topTime_=360000):  # 359999 for 99:59:59  86399 for 23:59:59
# * def intToHMS(intHMS_):
# * def ISO2TS(ISOStrIn):
# * def isPast(timeToChk_):
# * def isPastHMS(HMS_):
# * def mergeDicts(bigDict_, dictToAdd_, sortDict_=False):
# * def MTS():
# * def MTSclr():
# * def MTSPlus(numToAdd_):
# * def MTSS():
# * def myPp(objectToPp):
# * def mySleep(fToSleep_):
# * def mysql2LocalTime(SQLTIMEZ):
# * def now():
# * def nowIntHMS(dtObj=DT.now()):
# * def nowStr(dtObj=DT.now()):
# * def nowStrHMS(dtObj=DT.now()):
# * def nowStrSql(dtObj=DT.now()):
# * def nowTimeStr(dtObj=DT.now()):
# * def nowZ():
# * def nowZStr(dtObj=DT.utcnow()):
# * def nowZStrSql(dtObj=DT.utcnow()):
# * def nrmlIntToHMS(nrmlIntHMS_):
# * def outputHelp(argv_):
# * def outputOptionsStruct():
# * def pickleIt(fileName_, dataToPickle_):
# * def print_(*args_):
# * def readFileToStr(FILENAME_):
# * def relDateDiff(startTS, endTS):
# * def relDateDiffStripped(startTS, endTS):
# * def removeDictQuotes(dictToUnquote_):
# * def removeStrQuotes(strToStrip_):
# * def secsI():
# * def setOptions(argv_):
# * def sortADict(dictToSort_):
# * def stripCodes(strToStrip_):
# * def stripCodes(strToStrip_):
# * def stripCodesAndVersion(strToStrip_):
# * def subParms(listIn_, tupDictParms_):
# * def tabsToSpcs(strIn_, numSpcPerTab_=2):
# * def timeHoler(timeStr):
# * def today():
# * def todayStr(dtObj=DT.today()):
# * def tomorrow(dtObj=today()):
# * def tomorrowStr(dtObj=tomorrow()):
# * def toStr(TDIn):
# * def TS2ISO(TSIn):
# * def unPickleIt(fileName_):
# * def USGS2LocalTime(usgsTimeZ):
# * def USGS2MysqlTime(USGSDate):
# * def whirl():
# * def yesterday(dtObj=DT.today()):
# * def yesterdayStr(dtObj=yesterday(DT.today())):


HASH_blake2b = HL.blake2b()  # 64 byte fast hash
HASH_blake2s = HL.blake2s()  # 32 byte fast hash
HASH_md5 = HL.md5()  # 16 byte fastest hash, most likely to collide
HASH_sha1 = HL.sha1()  # 20 byte hash
HASH_sha224 = HL.sha224()  # 28 byte hash
HASH_sha256 = HL.sha256()  # 32 byte hash
HASH_sha3_224 = HL.sha3_224()  # 28 byte hash
HASH_sha3_256 = HL.sha3_256()  # 32 byte hash
HASH_sha3_384 = HL.sha3_384()  # 48 byte hash
HASH_sha3_512 = HL.sha3_512()  # 64 byte hash
HASH_sha384 = HL.sha384()  # 48 byte hash",),
HASH_sha512 = HL.sha512()  # 64 byte hash",),



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
FOLDLEN = 200
GLOBAL_CACHE_DIR = "/home/will/.cache/"
GLOBAL_CONFIG_DIR = "/home/will/.config/"
PY_CONFIG_DIR = "/rcr/0-units/python/"
TRIQT = f"""{DBLQT}{DBLQT}{DBLQT}"""


#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0002 value_ constants
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


BIN04 = lambda __X__: f"""{__X__:04b}"""
BIN08 = lambda __X__: f"""{__X__:08b}"""
BIN16 = lambda __X__: f"""{__X__:016b}"""
BIN32 = lambda __X__: f"""{__X__:032b}"""
BIN64 = lambda __X__: f"""{__X__:064b}"""
CLRALL = f"""{ESC}[2J"""
CLRDOWN = f"""{ESC}[J"""
CLREOL = f"""{ESC}[K"""
CMNTLINE = f"""# * {"#*" * (CMNTLEN // 2)}"""
DICTMODE_KEYSTR = "DICTMODE_KEYSTR"  # define dictmode 'key':val
DICTMODE_KEYVAL = "DICTMODE_KEYVAL"  # define dictmode key:val
EEOL = f"""{ESC}[K"""
EMPTY_DICT = {}
EMPTY_LIST = []
EMPTY_STR = ""
EMPTY_TUPLE = ()
EMPTYSTRLST = [None, "", DBLQT, f"""{DBLQT}{DBLQT}""", SGLQT, f"""{SGLQT}{SGLQT}""", BKQT, "None", "\r", NEWLINE, "\r\n", "\n\r", ]
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
HEX08 = lambda __X__: f"""{__X__:02H}"""  # {thisComment_}
HEX16 = lambda __X__: f"""{__X__:04H}"""  # {thisComment_}
HEX32 = lambda __X__: f"""{__X__:08H}"""  # {thisComment_}
HEX64 = lambda __X__: f"""{__X__:016H}"""  # {thisComment_}
IMPORTANTSTR = f"""# * {"!-" * (CMNTLEN // 2)}"""  # important line marker
INDENTIN = " -=> "  # display arrow RIGHT
INDENTOUT = " <=- "  # display arrow LEFT
INFOSTR = f"""# * {"%_" * (CMNTLEN // 2)}"""  # INFO _STR_ line
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
MOVELEFT = lambda __NUM__: f"""{ESC}[{__NUM__}D"""
MOVETO = lambda __LN__, __COL__: f"""{ESC}[{__LN__};{__COL__}H"""
NCR = lambda __NUM__: f"""{CRSTR * __NUM__}"""
NNL = lambda __NUM__: f"""{NEWLINE * __NUM__}"""
NSPC = lambda __NUM__: f"""{SPCSTR * __NUM__}"""  # returns a string with __NUM__ SPC
NTAB = lambda __NUM__: f"""{TABSTR * __NUM__}"""  # returns a string with __NUM__ TAB
QTSET = [DBLQT, SGLQT, BKQT]  # set of all quote characters
SERIALNUMBER = lambda __NUM__: f"""{(__NUM__ % 0XFFFFFFFF):08X}"""
USER_CACHE_URL = lambda __FILENAME__: f"""{USER_CACHE_DIR}{__FILENAME__}"""
USER_CONFIG_URL = lambda __FILENAME__: f"""{USER_CONFIG_DIR}{__FILENAME__}"""
WHIRLCOUNT = 0
WHIRLSTR = f"""-{BKSLSH}|/*"""


DAY_MS = (60 * 60 * 24 * 1000)  # 86400000
DAY_S = (60 * 60 * 24)  # 86400
HALFDAY_S = (60 * 60 * 12)  # 43200
HALFHOUR_S = (60 * 30)  # 1800
HOUR_S = (60 * 60)  # 3600
MINUTE_S = 60 # 60
QUARTERDAY_S = (60 * 60 * 6)
QUARTERHOUR_S = (60 * 15)  # 900
TIME_S_995959 = (60 * 60 * 100)  # 360000
TIME_S_DDD235959 = (60 * 60 * 24 * 1000)


NAME_GLBL_BTM_PY = lambda __NAME__: f"""{PY_CONFIG_DIR}/{__NAME__}/{__NAME__}_BTM.py"""
NAME_GLBL_IMG_PY = lambda __NAME__, __FILENAME__: f"""{PY_CONFIG_DIR}res/IMG/{__NAME__}/{__FILENAME__}"""
NAME_GLBL_IMG_ROOT_PY = lambda __FILENAME__: f"""{PY_CONFIG_DIR}res/IMG/{__FILENAME__}"""
NAME_GLBL_MD_PY = lambda __NAME__: f"""{PY_CONFIG_DIR}res/MARKDOWN/{__NAME__}.md"""
NAME_GLBL_NEW_PY = lambda __NAME__: f"""{PY_CONFIG_DIR}{__NAME__}/{__NAME__}_NEW.py"""
NAME_GLBL_RES_PY = lambda __FILENAME__: f"""{PY_CONFIG_DIR}res/{__FILENAME__}"""
NAME_GLBL_ROOT_PY = lambda __FILENAME__: f"""{PY_CONFIG_DIR}__ROOT__/{__FILENAME__}"""
NAME_GLBL_SUB_PY = lambda __NAME__, __SUB__: f"""{PY_CONFIG_DIR}{__NAME__}/{__NAME__}_{__SUB__}.py"""
NAME_GLBL_SUB_BTM_PY = lambda __NAME__, __SUB__: f"""{PY_CONFIG_DIR}{__NAME__}/{__NAME__}_{__SUB__}_BTM.py"""
NAME_GLBL_SUB_NEW_PY = lambda __NAME__, __SUB__: f"""{PY_CONFIG_DIR}{__NAME__}/{__NAME__}_{__SUB__}_NEW.py"""
NAME_GLBL_SUB_TOP_PY = lambda __NAME__, __SUB__: f"""{PY_CONFIG_DIR}{__NAME__}/{__NAME__}_{__SUB__}_TOP.py"""
NAME_GLBL_TOP_PY = lambda __NAME__: f"""{PY_CONFIG_DIR}{__NAME__}/{__NAME__}_TOP.py"""


NAME_HOME_CACHE = lambda __FILENAME__: f"""/home/will/.cache/{__FILENAME__}"""
NAME_HOME_CONFIG = lambda __FILENAME__: f"""/home/will/.config/{__FILENAME__}"""
NAME_HOME_SELF_CACHE = lambda __NAME__, __FILENAME__: f"""/home/will/.cache/{__NAME__}/{__FILENAME__}"""
NAME_HOME_SELF_CONFIG = lambda __NAME__, __FILENAME__: f"""/home/will/.config/{__NAME__}/{__FILENAME__}"""


NAME_LCL_BTM_PY = lambda __NAME__: f"""{__NAME__}/{__NAME__}_BTM.py"""
NAME_LCL_IMG_PY = lambda __FILENAME__: f"""res/IMG/{__FILENAME__}"""
NAME_LCL_MD_PY = lambda __FILENAME__: f"""res/MARKDOWN/{__FILENAME__}.md"""
NAME_LCL_NEW_PY = lambda __NAME__: f"""{__NAME__}/{__NAME__}_NEW.py"""
NAME_LCL_RES_PY = lambda __FILENAME__: f"""res/{__FILENAME__}"""
NAME_LCL_ROOT_PY = lambda __FILENAME__: f"""{__FILENAME__}"""
NAME_LCL_SUB_BTM_PY = lambda __NAME__, __SUB__: f"""{__NAME__}/{__NAME__}_{__SUB__}_BTM.py"""
NAME_LCL_SUB_NEW_PY = lambda __NAME__, __SUB__: f"""{__NAME__}/{__NAME__}_{__SUB__}_NEW.py"""
NAME_LCL_SUB_PY = lambda __NAME__, __SUB__: f"""{__NAME__}/{__NAME__}_{__SUB__}.py"""
NAME_LCL_SUB_TOP_PY = lambda __NAME__, __SUB__: f"""{__NAME__}/{__NAME__}_{__SUB__}_TOP.py"""
NAME_LCL_SUB01_BTM_PY = lambda __NAME__, __SUB__, __SUB1__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_BTM.py"""
NAME_LCL_SUB01_NEW_PY = lambda __NAME__, __SUB__, __SUB1__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_NEW.py"""
NAME_LCL_SUB01_PY = lambda __NAME__, __SUB__, __SUB1__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}.py"""
NAME_LCL_SUB01_TOP_PY = lambda __NAME__, __SUB__, __SUB1__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_TOP.py"""
NAME_LCL_SUB02_BTM_PY = lambda __NAME__, __SUB__, __SUB1__, __SUB2__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_{__SUB2__}_BTM.py"""
NAME_LCL_SUB02_NEW_PY = lambda __NAME__, __SUB__, __SUB1__, __SUB2__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_{__SUB2__}_NEW.py"""
NAME_LCL_SUB02_PY = lambda __NAME__, __SUB__, __SUB1__, __SUB2__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_{__SUB2__}.py"""
NAME_LCL_SUB02_TOP_PY = lambda __NAME__, __SUB__, __SUB1__, __SUB2__: f"""{__NAME__}/{__NAME__}_{__SUB__}_{__SUB1__}_{__SUB2__}_TOP.py"""
NAME_LCL_TOP_PY = lambda __NAME__: f"""{__NAME__}/{__NAME__}_TOP.py"""


STR_SUBST_DICT = {
	"%CBRCE%": f"""{CBRCE}""",
	"%CBRKT%": f"""{CBRKT}""",
	"%CPAREN%": f"""{CPAREN}""",
	"%DQ%": f"""{DBLQT}""",
	"%ESCLN%": f""" {BKSLSH}{NEWLINE}""",
	"%FOLDLN1E%": f"""{FOLD1ENDHERELN}""",
	"%FOLDLN2E%": f"""{FOLD2ENDHERELN}""",
	"%FOLDLN3E%": f"""{FOLD3ENDHERELN}""",
	"%FOLDLN1S%": f"""{FOLD1STARTHERELN}""",
	"%FOLDLN2S%": f"""{FOLD2STARTHERELN}""",
	"%FOLDLN3S%": f"""{FOLD3STARTHERELN}""",
	"%FTQ%": f"""f{TRIQT}""",
	"%FTQTQ%": f"""f{TRIQT}{TRIQT}""",
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

#

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0201 CF defines
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0202 options structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
OPTIONS = {
# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
}
# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

OPTIONSHELPDICT = {
# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
}
# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

OPTIONSDICT = {
}


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed sections of CF.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


# <<>>
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# start of not managed sections of CF.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# the data structure to keep the UUID:serial number pairs
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
SERIALZ = {
	"UUID": 0,
}
"""
SERIALZ = {
	"K_VERSION": SERIALNUMBER(0)
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# tabsToSpcs swap tabs for two spaces in a string for portability
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def tabsToSpcs(strIn_, numSpcPerTab_=2):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strOut_ = strIn_.replace(TABSTR, NSPC(numSpcPerTab_))
	return strOut_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * getDebugInfo
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def getDebugInfo():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	previous_frame = inspect.currentframe().f_back
	(filename, line_number, function_name, lines, index) = inspect.getframeinfo(previous_frame)
	return f"file {filename}, line {line_number}, function {function_name}"
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# doError
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doError(strToOutToErr_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	print(f"{NEWLINE}{getDebugInfo()}{NEWLINE}ERROR:{NEWLINE}{strToOutToErr_}{NEWLINE}")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# pickleIt
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def pickleIt(fileName_, dataToPickle_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	with open(fileName_, 'wb') as FD_OUT_:
		PD.dump(dataToPickle_, FD_OUT_)
		FD_OUT_.flush()
		FD_OUT_.close()
# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# unPickleIt
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def unPickleIt(filename_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if EXISTS(filename_):
		with open(filename_, "rb") as FD_IN_:
			dataToRTN_ = PD.load(FD_IN_)
		return dataToRTN_
	else:
		return None
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1



# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# class withPickles
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
class withPickles(object):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

	def __init__(self, pklFilename_, stuffToPkl_):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		self._STUFFTOPKL_ = stuffToPkl_
		self._PKLFILENAME_ = pklFilename_
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	def __enter__(self):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		_tempToPkl_ = unPickleIt(self._PKLFILENAME_)
		# print(f"""entering withPickles {self._PKLFILENAME_} {self._STUFFTOPKL_}""")

		if _tempToPkl_ is not None:

			if (self._STUFFTOPKL_["K_VERSION"] > _tempToPkl_["K_VERSION"]):
				_tempToPkl_ = self._STUFFTOPKL_

			self._STUFFTOPKL_ = _tempToPkl_

		else:
			pickleIt(self._PKLFILENAME_, self._STUFFTOPKL_)

# 		print(f"""entering pickle
# self._STUFFTOPKL_ {self._STUFFTOPKL_}
# """)
		return self
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	def __exit__(self, *args):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		# print(f"""exiting withPickles {self._PKLFILENAME_} {self._STUFFTOPKL_}""")
		pickleIt(self._PKLFILENAME_, self._STUFFTOPKL_)
# 		print(f"""exiting pickle
# self._STUFFTOPKL_ {self._STUFFTOPKL_}
# """)
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * doAHash
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doAHash(HASH_, stringToHash):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if stringToHash == "":
		return None
	HASH_.update(stringToHash.encode("utf-16", "replace"))
	hashedStr = HASH_.hexdigest()
	return hashedStr
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# readFileToStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def readFileToStr(FILENAME_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	with open(FILENAME_, "tr") as FDIN:
		strToRtn_ += FDIN.readlines()
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# myTimestamp 1612179130.285 -=> 1612179130285 if TNS used, same resolution since boot not epoch for TMT
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def MTS():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return int(TMT()*1000)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# myTimestamp 1612179130.285 -=> 1612179130285 if TNS used, same resolution since boot not epoch for TMT
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def MTSS():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return ((int(WALLSECS()) % 86400) + GMTOFFSET) % 86400 # 360000 for 99:59:59  86400 for 23:59:59
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# loseTheSecs
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def loseTheSecs(intIn_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return (intIn_ // 60) * 60
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# MTSM
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def MTSM():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return loseTheSecs(MTSS())
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# MTSMS():
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def MTSMS():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return ((int(WALLSECS() * 1000)) + (GMTOFFSET * 1000)) % (86400 * 1000) # 3600000 for 99:59:59  86400 for 23:59:59
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
"""
is_dst = time.daylight and time.localtime().tm_isdst > 0
utc_offset = - (time.altzone if is_dst else time.timezone)
"""

# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# MTSPlus
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def MTSPlus(numToAdd_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if not isinstance(numToAdd_, int):
		numToAdd_ = 0
	valToRtn_ = MTS() + numToAdd_
	# print("MTSPlus ", MTS(), numToAdd_, valToRtn_)
	return valToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# MTSclr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def MTSclr():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return f"""{CLREOL}{MTS()}{NEWLINE}{CLREOL}"""
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# isPast
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def isPast(timeToChk_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if MTS() >= timeToChk_:
		return True
	else:
		return False
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# now
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def now():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return DT.now()
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# nowZ
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def nowZ():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return DT.utcnow()
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# nowStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def nowStr(dtObj=DT.now()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj.strftime("%Y%m%d.%H%M%S")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# nowStrHMS
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def nowStrHMS(dtObj=DT.now()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj.strftime("%H:%M:%S")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# secsI
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def secsI():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return int(WALLSECS)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# HMSToInt
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def HMSToInt(HMS_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	intHMS_ = int(HMS_[0:2]) * 10000 + int(HMS_[3:5]) * 100 + int(HMS_[6:8])
	return intHMS_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# intToHMS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def intToHMS(intHMS_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	HMS_ = f"""{intHMS_:06d}"""
	HMS_ = f"""{HMS_[0:2]}:{HMS_[2:4]}:{HMS_[4:6]}"""
	return HMS_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# nowIntHMS
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def nowIntHMS(dtObj=DT.now()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	intHMS_ = int(dtObj.strftime("%H%M%S"))
	return intHMS_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# isPastHMS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def isPastHMS(HMS_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	nowStrHMS_ = nowStrHMS(DT.now())
	if nowStrHMS_ > HMS_:
		return True
	else:
		return False
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# HMSToNrmlInt
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def HMSToNrmlInt(HMS_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	intToRtn_ = (int(HMS_[0:2]) * 3600) + (int(HMS_[3:5]) * 60) + int(HMS_[6:8])
	return intToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# nrmlIntToHMS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def nrmlIntToHMS(nrmlIntHMS_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	nrmlIntHMS_ = int(nrmlIntHMS_)
	THrs_ = (nrmlIntHMS_ // 3600)
	TMins_ = (nrmlIntHMS_ - (THrs_ * 3600)) // 60
	TSecs_ = nrmlIntHMS_ % 60
	strToRtn_ = f"""{THrs_:02d}:{TMins_:02d}:{TSecs_:02d}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# addHMS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def addHMS(HMS1_, HMS2_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	TNIntHMS1_ = HMSToNrmlInt(HMS1_)
	TNIntHMS2_ = HMSToNrmlInt(HMS2_)
	TNInt_ = TNIntHMS1_ + TNIntHMS2_
	HMSToRtn_ = nrmlIntToHMS(TNInt_)
	return HMSToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# subtractHMS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def subtractHMS(HMS1_, HMS2_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	TNIntHMS1_ = HMSToNrmlInt(HMS1_)
	TNIntHMS2_ = HMSToNrmlInt(HMS2_)
	TNInt_ = TNIntHMS1_ - TNIntHMS2_
	HMSToRtn_ = nrmlIntToHMS(TNInt_)
	return HMSToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# incHMS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def incHMS(HMS_, hours_=0, mins_=0, secs_=0, topTime_=360000):  # 359999 for 99:59:59  86399 for 23:59:59
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	TNIntHMS_ = HMSToNrmlInt(HMS_) + (hours_ * 3600) + (mins_ * 60) + secs_
	TNIntHMS_ = TNIntHMS_ % topTime_
	if TNIntHMS_ < 0:
		TNIntHMS_ = topTime_
	strToRtn_ = nrmlIntToHMS(TNIntHMS_)
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# nowZStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def nowZStr(dtObj=DT.utcnow()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj.strftime("%Y%m%d.%H%M%S")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# nowZStrSql
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def nowZStrSql(dtObj=DT.utcnow()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj.strftime("%Y-%m-%d %H:%M:%S")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# nowStrSql
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def nowStrSql(dtObj=DT.now()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj.strftime("%Y-%m-%d %H:%M:%S")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# nowTimeStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def nowTimeStr(dtObj=DT.now()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj.strftime("%H%M%S")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# today
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def today():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return DT.today()
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# todayStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def todayStr(dtObj=DT.today()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj.strftime("%Y%m%d")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# todayStrFull
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def todayStrFull(dtObj=DT.today()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj.strftime("%Y.%m.%d %A %B ")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# yesterday
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def yesterday(dtObj=DT.today()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj + TD(days=-1)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# yesterdayStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def yesterdayStr(dtObj=yesterday(DT.today())):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj.strftime("%Y%m%d")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# tomorrow
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def tomorrow(dtObj=today()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj + TD(days=1)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# tomorrowStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def tomorrowStr(dtObj=tomorrow()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj.strftime("%Y%m%d")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# gmdate
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def gmdate(dtObj=DT.now()):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return dtObj.strftime('D, d M Y H:i:s GMT')
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# toStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def toStr(TDIn):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if isinstance(TDIn, str):
		return TDIn
	else:
		return TDIn.strftime("%Y-%m-%d %H:%M:%S")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# ISO2TS
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def ISO2TS(ISOStrIn):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return MT(DT.strptime(ISOStrIn, "%Y-%m-%d %H:%M:%S").timetuple())
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# TS2ISO
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def TS2ISO(TSIn):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if isinstance(TSIn, str):
		thisTime = PD.parse(TSIn).strftime("%Y-%m-%d %H:%M:%S")
	elif isinstance(TSIn, int):
		thisTime = DT.fromtimestamp(TSIn / 1000).strftime("%Y-%m-%d %H:%M:%S")
	return thisTime
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# timeHoler
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def timeHoler(timeStr):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	start = DT.strptime(PD.parse(timeStr), '%Y-%m-%d %H:%M:%S')
	parsedStr = PD.parse(ISOStrIn).strftime("%Y-%m-%d %H:%M:%S")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# USGS2MysqlTime
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def USGS2MysqlTime(USGSDate):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	tdt1 = PD.parse(USGSDate)
	return tdt1.strftime("%Y-%m-%d %H:%M:%S")
	if USGSDate[10] != "T":
		return USGSDate
	TDString = USGSDate[:-5]
	TDate = DT.strptime(TDString, "%Y-%m-%dT%H:%M:%S")
	return TDate.strftime("%Y-%m-%d %H:%M:%S")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# mysql2LocalTime
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def mysql2LocalTime(SQLTIMEZ):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if SQLTIMEZ[10] == "T":
		SQLTIMEZ = SQLTIMEZ[0:9] + " " + SQLTIMEZ[10:-5]
	if C.DEBUGME:
		print(f"timeDateStuff.42 TDString {SQLTIMEZ:s}")
	fromZone = TZ.gettz('UTC')
	toZone = TZ.gettz('MST7MDT')
	TDate = DT.strptime(SQLTIMEZ, "%Y-%m-%d %H:%M:%S")
	TDate = TDate.replace(tzinfo=fromZone)
	localTDate = TDate.astimezone(toZone)
	if C.DEBUGME:
		print(f"timeDateStuff.49 localTDate {localTDate.strftime('%Y-%m-%d %H:%M:%S'):s}")
	return f"{localTDate.strftime('%Y-%m-%d %H:%M:%S'):s}"
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# USGS2LocalTime
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def USGS2LocalTime(usgsTimeZ):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	TDString = usgsTimeZ[:-5]
	if C.DEBUGME:
		print(f"timeDateStuff.42 TDString {TDString:s}")
	fromZone = TZ.gettz('UTC')
	toZone = TZ.gettz('MST7MDT')
	TDate = DT.strptime(TDString, "%Y-%m-%dT%H:%M:%S")
	TDate = TDate.replace(tzinfo=fromZone)
	localTDate = TDate.astimezone(toZone)
	if C.DEBUGME:
		print(f"timeDateStuff.49 localTDate {localTDate.strftime('%Y-%m-%d %H:%M:%S'):s}")
	return f"{localTDate.strftime('%Y-%m-%d %H:%M:%S'):s}"
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# dateToStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def dateToStr(dateIn):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if isinstance(dateIn, str):
		return dateIn
	returnStr = dateIn.strftime('%Y-%m-%d %H:%M:%S')
	return returnStr
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# relDateDiff
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def relDateDiff(startTS, endTS):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if isinstance(startTS, str):
		start = DT.strptime(nowZStrSql(PD.parse(startTS)), '%Y-%m-%d %H:%M:%S')
	elif isinstance(startTS, int):
		start = DT.strptime(startTS, '%Y-%m-%d %H:%M:%S')
	else:
		return None
	if isinstance(endTS, str):
		ends = DT.strptime(nowZStrSql(PD.parse(endTS)), '%Y-%m-%d %H:%M:%S')
	elif isinstance(endTS, int):
		ends = DT.strptime(endTS, '%Y-%m-%d %H:%M:%S')
	else:
		return None
	diff = RD(start, ends)
	return f"{diff.years:04d}-{diff.months:02d}-{diff.days:02d} {diff.hours:02d}:{diff.minutes:02d}:{diff.seconds:02d}"
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# relDateDiff
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def relDateDiffStripped(startTS, endTS):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	startTS = DS.justTheNumbers(startTS)
	endTS = DS.justTheNumbers(endTS)
	start = DT.strptime(startTS, '%Y%m%d%H%M%S')
	ends = DT.strptime(endTS, '%Y%m%d%H%M%S')
	diff = RD(start, ends)
	return f"{diff.years:04d}{diff.months:02d}{diff.days:02d}{diff.hours:02d}{diff.minutes:02d}{diff.seconds:02d}"
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# dateIn
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def dateIntvlM(dateToUse, months):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if isinstance(dateToUse, str):
		dateToUseA = PD(dateToUse)
	elif isinstance(dateToUse, datetime.datetime):
		dateToUseA = dateToUse
	dateToRet = dateToUseA + datedelta.MONTH(months=months)
	if isinstance(dateToUse, str):
		dateToRet = DT.strftime("%Y-%m%d %H:%M:%S")
	return dateToRet
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# mySleep uses timer, not accurate to wallclock
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def mySleep(fToSleep_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	endTime_ = MTSPlus(fToSleep_)
	while MTS() < endTime_:
		pass
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# removeStrQuotes
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def removeStrQuotes(strToStrip_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = strToStrip_.replace(DBLQT, "'")
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# removeDictQuotes
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def removeDictQuotes(dictToUnquote_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	dictToRtn_ = {}
	for key_, item_ in dictToUnquote_.items():
		if isinstance(item_, str):
			strToUnquote_ = strToUnquote_.replace('"', "'")
		else:
			strToUnquote_ = item_
		dictToRtn_[key_] = strToUnquote_
	return dictToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# stripCodes
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def stripCodesAndVersion(strToStrip_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = strToStrip_
	for thisCodeToStrip_ in CODES2STRIP:
		strToRtn_ = strToRtn_.replace(thisCodeToStrip_, "")
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# stripCodes
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def stripCodes(strToStrip_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = strToStrip_
	for thisCodeToStrip_ in CODES2STRIP:
		strToRtn_ = strToRtn_.replace(thisCodeToStrip_, "")
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# print_
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def print_(*args_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	print(*args_, end="", flush=True)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# displayStats
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def displayStats(LN_, COL_, statsStr_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	print(f"""{MOVETO(LN_, COL_)}{statsStr_}""")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# setOptions
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def setOptions(argv_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	OPTIONSDICT[STARTUPDIR] = ABSPATH(argv_.pop(0))
	for thisOpt_ in argv_:
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		equalPosn_ = thisOpt_.find("=")
		if equalPosn_ > -1:
			thisParm_ = thisOpt_[equalPosn_ + 1:]
			thisOpt_ = thisOpt_[0:equalPosn_ + 1]
		else:
			thisParm_ = None

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		if thisOpt_ not in OPTIONS:
			doError(f"invalid option {thisOpt_}{NEWLINE}argv is {argv_}")
			continue

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		# if thisOptionVal_ in EMPTYSTRLST:
		# 	thisOptionVal_ = None

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		for thisParm_, thisVal_ in OPTIONS[thisOpt_].items():
			OPTIONSDICT[thisParm_] = thisVal_

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# outputHelp
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def outputHelp(argv_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	argLen = len(argv_)

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	if 0 >= argLen <= 1:
		for thisParm_ in OPTIONSHELPDICT:
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
			strToRtn_ += f"""help entry for {thisParm_}:{NEWLINE}{OPTIONSHELPDICT[thisParm_]}{NEWLINE}"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		return strToRtn_
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	argv_ = argv_[1:]
	for thisParm_ in argv_:
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		strToRtn_ += f"""help entry for {thisParm_}:{NEWLINE}{OPTIONSHELPDICT[thisParm_]}{NEWLINE}{NEWLINE}"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1
	strToRtn_ = tabsToSpcs(strToRtn_)
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# outputOptionsDict
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def outputOptionsStruct():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""OPTIONS = {OBRCE}{NEWLINE}"""

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	for key_, vals_ in OPTIONS.items():
		strToRtn_ += f"""{NSPC(2)}{DBLQT}{key_}{DBLQT}: {OBRCE}{NEWLINE}"""
		for key1_, val_ in vals_.items():

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
			strToRtn_ += f"""{NSPC(4)}{key1_}: {val_},{NEWLINE}"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
		strToRtn_ += f"""{NSPC(2)}{CBRCE},{NEWLINE}"""

	strToRtn_ += f"""{CBRCE}{NEWLINE}{NEWLINE}"""
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	strToRtn_ += f"""OPTIONSDICT = {OBRCE}{NEWLINE}"""
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	for key_, val_ in OPTIONSDICT.items():
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		strToRtn_ += f"""{NSPC(2)}{key_}: {val_},{NEWLINE}"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
	strToRtn_ += f"""{CBRCE}{NEWLINE}"""
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	strToRtn_ += f"""OPTIONSHELPDICT = {OBRCE}{NEWLINE}"""
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	for key_, val_ in OPTIONSHELPDICT.items():
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		strToRtn_ += f"""{NSPC(2)}{DBLQT}{key_}{DBLQT}: {val_},{NEWLINE}"""
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
	strToRtn_ += f"""{CBRCE}{NEWLINE}"""
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	strToRtn_ = tabsToSpcs(strToRtn_)
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


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# subParms
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def subParms(listIn_, tupDictParms_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	listToRtn_ = []
	for thisStr_ in listIn_:
		for subParm_, replaceStr_ in tupDictParms_:
			thisStr_ = thisStr_.replace(subParm_, replaceStr_)
		listToRtn_.append(thisStr_)
	return listToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# whirl
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def whirl():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	global WHIRLCOUNT
	print(WHIRLSTR[(WHIRLCOUNT % 5)])
	print(LINESUP(2))
	WHIRLCOUNT += 1

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# frameItHMS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def frameItHMS(name_, value_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = f"""{name_} |{value_}|"""
	if isinstance(value_, int):
		strToRtn_ += f"""{nrmlIntToHMS(value_)}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# frameItHMS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def frameItMS(name_, value_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = f"""{name_} |{value_}|"""
	if isinstance(value_, int):
		strToRtn_ += f"""{nrmlIntToHMS(value_ // 1000)}.{value_ % 1000}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# frameIt
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def frameIt(name_, value_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = f"""{name_} |{value_}|"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# mergeDicts
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def mergeDicts(bigDict_, dictToAdd_, sortDict_=False):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	dictToRtn_ = {}

	for key_, val_ in bigDict_.items():
		dictToRtn_[key_] = val_

	for key_, val_ in dictToAdd_.items():
		dictToRtn_[key_] = val_

	if sortDict_ is True:
		dictToRtn_ = sortADict(dictToRtn_)

	return dictToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# myPp
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def myPp(objectToPp):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return PP.pprint(objectToPp)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# IGM
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def IGM(objToInspect_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return inspect.getmembers(objToInspect_)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# IGMPP
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def IGMPP(objToIP_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	return myPp(IGM(objToIP_))
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# serializeIt
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def serializeIt(UUID_):
	global SERIALZ
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	with withPickles(f"""{NAME_HOME_CONFIG("SERIALZ.pkl")}""", SERIALZ) as _pklJar_:
		SERIALZ = _pklJar_._STUFFTOPKL_
		if UUID_ not in SERIALZ:
			SERIALZ[UUID_] = 0

		keyToRtn_ = f"""_{SERIALZ[UUID_]:08X}"""
		SERIALZ[UUID_] += 1
		SERIALZ[UUID_] = SERIALZ[UUID_] & 0XFFFFFFFF
		_pklJar_._STUFFTOPKL_ = SERIALZ

	return keyToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# incVersion
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def incVersion(versionIn_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_intIn_ = int(versionIn_, 16)
	_intIn_ += 1
	_strToRtn_ = f"""{_intIn_:08X}"""
	return _strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# quickCopyDict
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def quickCopyDict(dictIn_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	_dictToRtn_ = {}
	for _thisKey_, _thisVal_ in dictIn_.items():
		_dictToRtn_[_thisKey_] = _thisVal_

	return _dictToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# updateList
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def updateList(listIn_, itemToUpdate_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if (itemToUpdate_ in listIn_):
		return listIn_
	else:
		listIn_.append(itemToUpdate_)
		return listIn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


#
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# end of CF.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#