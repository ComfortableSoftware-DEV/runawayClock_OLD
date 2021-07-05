

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of CF.CONST_D._01_01_FILESYSTEM
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


import os as OS
import pathlib as PL
import re as RE
import shutil as SHU


from __KEYS__.CF import _01_01_FILESYSTEM as CFFS_K
from CF.CONST_D import _01_01_FILESYSTEM as CFFS_V


OSPATH = os.path


ABS_DOT = ABSPATH(".")
ABSPATH = OSPATH.abspath
CHMOD = os.chmod
EXISTS = OSPATH.exists
GETSIZE = OSPATH.getsize
HOME = f"{OSPATH.expanduser('~')}"
MKDIR = os.mkdir
MOVE = shutil.move
OSACCESS = os.access
RENAME = os.rename
RM = os.remove
RMDIR = os.rmdir
STAT = os.stat
SUB = re.sub


CHMODDIR = 0o755  # default mode for directories this program needs to oerate in
CHMODFILE = 0o655  # default mode for files this program needs to oerate in
CONFIGDIR = f"""{HOME}/.config/{CFFS_V.__NAME__}"""  # default mode for files this program needs to oerate in
DIRBLACKLIST = "[a-zA-Z0-9./]+"  # PCRE for directory characters to blacklist as it's result
DIRWHITELIST = "[^a-zA-Z0-9./]+"  # PCRE for directory characters to whitelist as it's result
FILEBLACKLIST = "[a-zA-Z0-9.]+"  #
FILEWHITELIST = "[^a-zA-Z0-9.]+"  #
TMPDIR = "/tmp/{CFFS_V.__NAME__}"  # default mode for files this program needs to oerate in


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0301 FO.py dictionaries
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
EQUIVEXTENSIONS = {  # an empty entry tupdict+function for each file/directory
	".jpeg": ".jpg",  # holds the blacklisted filename tail
	".jpg": ".jpeg",  # holds the blacklisted filename tail
	".mpeg": ".mpg",  # holds the blacklisted filename tail
	".mpg": ".mpeg",  # holds the blacklisted filename tail
}


EXTENSIONBOOLS = {  # dict holding the process or not bools pulled from CF.OPTIONSDICT, not built by FM.py
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0302 FO.py lists
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
ILLEGALPATHS = [  # list of absolute paths to be completely ignored if used
	"/",  # do not operate on / ever
]


ILLEGALWILDCARDS = [  # list all of the portions of a filename which will result in an error [0:] based
	"/bin/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/boot/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/dev/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/efi/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/etc/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/home/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/lib/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/lib64/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/media/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/opt/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/proc/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/root/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/run/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/sbin/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/srv/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/sys/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/tmp/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/usr/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/var/",  # illegal wildcards, these are most often /path/ and will be [0:] based
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0303 FO.py tupdicts
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTYENTRY structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTYENTRYTUP = (
	(CFFS_K.BLACKTAIL, ""),  # holds the blacklisted filename tail
	(CFFS_K.EXTENSIONGUESSED, ""),  # whole extension
	(CFFS_K.EXTHEAD, ""),  # whole FILENAME
	(CFFS_K.EXTTAIL, ""),  # whole FILENAME
	(CFFS_K.FILETYPEEXT, UNKNOWN),  # filetype group flag
	(CFFS_K.FILETYPEFILE, UNKNOWN),  # filetype group flag
	(CFFS_K.FILETYPEID, UNKNOWN),  # filetype group flag
	(CFFS_K.GID, ""),  # path tail
	(CFFS_K.ICANEXECUTE, ""),  # path tail
	(CFFS_K.ICANREAD, ""),  # path tail
	(CFFS_K.ICANWRITE, ""),  # path tail
	(CFFS_K.ISADIR, False),  # entry is a directory
	(CFFS_K.ISAFILE, False),  # entry is a file
	(CFFS_K.ISAKNOWNFILETYPE, False),  # in an unknown filetype
	(CFFS_K.ISASYMLINK, False),  # is a synlink
	(CFFS_K.MODE, 0),  # mode bits
	(CFFS_K.PATH, ""),  # whole path
	(CFFS_K.PATHHEAD, ""),  # path head
	(CFFS_K.PATHTAIL, ""),  # path tail
	(CFFS_K.RAWENTRY, ""),  # path tail
	(CFFS_K.SIZE, 0),  # size of file, 0/1 for a directory if empty/not-empty
	(CFFS_K.UID, ""),  # path tail
	(CFFS_K.WHITEEXTHEAD, ""),  #
	(CFFS_K.WHITEEXTTAIL, ""),  #
	(CFFS_K.WHITEFILENAME, ""),  # white filename
	(CFFS_K.WHITEFULLNAME, ""),  # white path+filename
	(CFFS_K.WHITEFULLPATH, ""),  # white full path
)

def EMPTYENTRYDICT():
	return dict((x, y) for x, y in EMPTYENTRYTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN0304 FO.py extension management structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


EXTENSIONSTYPES = {
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	CFFS_K.CODE:  [# filetype code
	# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
		".c",  # c code file
		".C",  # c code file
		".php",  # php code file
		".PHP",  # php code file
		".py",  # python code file
		".PY",  # python code file
	],
	# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2

	CFFS_K.DOCS:  [# filetype docs
	# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
	],
	# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2

	CFFS_K.KNOWN:  [# filetype known
	# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
	],
	# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2

	CFFS_K.MEDIA:  [# filetype media
	# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
	],
	# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2

	CFFS_K.PICS:  [# filetype pics
	# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
		".bmp",  # bmp image file
		".BMP",  # bmp image file
		".gif",  # gif image file
		".GIF",  # gif image file
		".jpeg",  # jpeg image file
		".JPEG",  # jpeg image file
		".jpg",  # jpg image file
		".JPG",  # jpg image file
		".png",  # png image file
		".PNG",  # png image file
		".webp",  # webp image file
		".WEBP",  # webp image file
	],
	# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2

	CFFS_K.TEXT:  [# filetype text
	# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
		".lst",  # text file
		".LST",  # text file
		".lst.txt",  # text file
		".LST.TXT",  # text file
	],
	# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2

	CFFS_K.UNKNOWN:  [# filetype unknown
	# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
	],
	# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2

	CFFS_K.VIDS:  [# filetype video
	# fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
		".asx",  # asx/wmv video file
		".ASX",  # asx/wmv video file
		".avi",  # avi video file
		".AVI",  # avi video file
		".divx",  # divx video file
		".DIVX",  # divx video file
		".flv",  # flv video file
		".FLV",  # flv video file
		".gifv",  # gifv video file
		".GIFV",  # gifv video file
		".m2ts",  # m2ts video file
		".M2TS",  # m2ts video file
		".m4a",  # m4a video file
		".M4A",  # m4a video file
		".m4v",  # m4v video file
		".M4V",  # m4v video file
		".mkv",  # mkv video file
		".MKV",  # mkv video file
		".mov",  # mov video file
		".MOV",  # mov video file
		".mp4",  # mp4 video file
		".MP4",  # mp4 video file
		".mpeg",  # mpeg video file
		".MPEG",  # mpeg video file
		".mpg",  # mpg video file
		".MPG",  # mpg video file
		".webm",  # webm video file
		".WEBM",  # webm video file
		".wmv",  # wmv video file
		".WMV",  # wmv video file
		".mpeg",
		"mp1v",
		"mpg1",
		'vcr2',
		'hdv1',
		'hdv2',
		'hdv3',
	],
	# fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2

}
# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


EXTENSIONLOOKUP = {
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	".asx": CFFS_K.VIDS,  # asx/wmv video file
	".ASX": CFFS_K.VIDS,  # asx/wmv video file
	".avi": CFFS_K.VIDS,  # avi video file
	".AVI": CFFS_K.VIDS,  # avi video file
	".bmp": CFFS_K.PICS,  # bmp image file
	".BMP": CFFS_K.PICS,  # bmp image file
	".c": CFFS_K.CODE,  # c code file
	".C": CFFS_K.CODE,  # c code file
	".divx": CFFS_K.VIDS,  # divx video file
	".DIVX": CFFS_K.VIDS,  # divx video file
	".flv": CFFS_K.VIDS,  # flv video file
	".FLV": CFFS_K.VIDS,  # flv video file
	".gif": CFFS_K.PICS,  # gif image file
	".GIF": CFFS_K.PICS,  # gif image file
	".gifv": CFFS_K.VIDS,  # gifv video file
	".GIFV": CFFS_K.VIDS,  # gifv video file
	".jpeg": CFFS_K.PICS,  # jpeg image file
	".JPEG": CFFS_K.PICS,  # jpeg image file
	".jpg": CFFS_K.PICS,  # jpg image file
	".JPG": CFFS_K.PICS,  # jpg image file
	".lst": CFFS_K.TEXT,  # text file
	".LST": CFFS_K.TEXT,  # text file
	".lst.txt": CFFS_K.TEXT,  # text file
	".LST.TXT": CFFS_K.TEXT,  # text file
	".m2ts": CFFS_K.VIDS,  # m2ts video file
	".M2TS": CFFS_K.VIDS,  # m2ts video file
	".m4a": CFFS_K.VIDS,  # m4a video file
	".M4A": CFFS_K.VIDS,  # m4a video file
	".m4v": CFFS_K.VIDS,  # m4v video file
	".M4V": CFFS_K.VIDS,  # m4v video file
	".mkv": CFFS_K.VIDS,  # mkv video file
	".MKV": CFFS_K.VIDS,  # mkv video file
	".mov": CFFS_K.VIDS,  # mov video file
	".MOV": CFFS_K.VIDS,  # mov video file
	".mp4": CFFS_K.VIDS,  # mp4 video file
	".MP4": CFFS_K.VIDS,  # mp4 video file
	".mpeg": CFFS_K.VIDS,  # mpeg video file
	".MPEG": CFFS_K.VIDS,  # mpeg video file
	".mpg": CFFS_K.VIDS,  # mpg video file
	".MPG": CFFS_K.VIDS,  # mpg video file
	".php": CFFS_K.CODE,  # php code file
	".PHP": CFFS_K.CODE,  # php code file
	".png": CFFS_K.PICS,  # png image file
	".PNG": CFFS_K.PICS,  # png image file
	".py": CFFS_K.CODE,  # python code file
	".PY": CFFS_K.CODE,  # python code file
	".webm": CFFS_K.VIDS,  # webm video file
	".WEBM": CFFS_K.VIDS,  # webm video file
	".webp": CFFS_K.PICS,  # webp image file
	".WEBP": CFFS_K.PICS,  # webp image file
	".wmv": CFFS_K.VIDS,  # wmv video file
	".WMV": CFFS_K.VIDS,  # wmv video file
}
# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


EXTENSIONGROUPS = {
	CFFS_K.CODE: CFFS_K.GTEXT,  # filetype code
	CFFS_K.DOCS: CFFS_K.GNONE,  # filetype docs
	CFFS_K.KNOWN: CFFS_K.GKNOWN,  # filetype known
	CFFS_K.MEDIA: CFFS_K.GMEDIA,  # filetype media
	CFFS_K.PICS: CFFS_K.GMEDIA,  # filetype pics
	CFFS_K.TEXT: CFFS_K.GTEXT,  # filetype text
	CFFS_K.UNKNOWN: CFFS_K.GNONE,  # filetype unknown
	CFFS_K.VIDS: CFFS_K.GMEDIA,  # filetype video
}


INDEXES = {
	CFFS_K.CODE: 0,  # filetype code
	CFFS_K.DOCS: 0,  # filetype docs
	CFFS_K.KNOWN: 0,  # filetype known
	CFFS_K.MEDIA: 0,  # filetype media
	CFFS_K.PICS: 0,  # filetype pics
	CFFS_K.TEXT: 0,  # filetype text
	CFFS_K.UNKNOWN: 0,  # filetype unknown
	CFFS_K.VIDS: 0,  # filetype video
}


SPREADS = {
	CFFS_K.SPREADCODE: False,  # zfiletype code
	CFFS_K.SPREADDOCS: False,  # filetype docs
	CFFS_K.SPREADKNOWN: False,  # filetype known
	CFFS_K.SPREADMEDIA: True,  # filetype media
	CFFS_K.SPREADPICS: True,  # filetype pics
	CFFS_K.SPREADTEXT: False,  # filetype text
	CFFS_K.SPREADUNKNOWN: False,  # filetype unknown
	CFFS_K.SPREADVIDS: True,  # filetype video
}


WHATTODO = {
	CFFS_K.DOCODE: False,  # zfiletype code
	CFFS_K.DODOCS: False,  # filetype docs
	CFFS_K.DOKNOWN: False,  # filetype known
	CFFS_K.DOMEDIA: True,  # filetype media
	CFFS_K.DOPICS: True,  # filetype pics
	CFFS_K.DOTEXT: False,  # filetype text
	CFFS_K.DOUNKNOWN: False,  # filetype unknown
	CFFS_K.DOVIDS: True,  # filetype video
}


EXTENSIONTYPETRANS = {
	CFFS_K.DOCODE: CFFS_K.CODE,
	CFFS_K.DODOCS: CFFS_K.DOCS,
	CFFS_K.DOKNOWN: CFFS_K.KNOWN,
	CFFS_K.DOMEDIA: CFFS_K.MEDIA,
	CFFS_K.DOPICS: CFFS_K.PICS,
	CFFS_K.DOTEXT: CFFS_K.TEXT,
	CFFS_K.DOUNKNOWN: CFFS_K.UNKNOWN,
	CFFS_K.DOVIDS: CFFS_K.VIDS,
	CFFS_K.SPREADCODE: CFFS_K.CODE,
	CFFS_K.SPREADDOCS: CFFS_K.DOCS,
	CFFS_K.SPREADKNOWN: CFFS_K.KNOWN,
	CFFS_K.SPREADMEDIA: CFFS_K.MEDIA,
	CFFS_K.SPREADPICS: CFFS_K.PICS,
	CFFS_K.SPREADTEXT: CFFS_K.TEXT,
	CFFS_K.SPREADUNKNOWN: CFFS_K.UNKNOWN,
	CFFS_K.SPREADVIDS: CFFS_K.VIDS,
}
