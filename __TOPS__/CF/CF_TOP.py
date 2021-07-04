

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
