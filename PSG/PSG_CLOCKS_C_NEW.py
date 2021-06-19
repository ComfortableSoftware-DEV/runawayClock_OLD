

from CF import CF
from FM import FM
from PSG import PSG
import PySimpleGUI as SG


class CLOCKS_C(object):
	global \
		DICT_ALL_THE_FORMS, \
		APPDS_MAIN
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

	def __init__(self, \
			keyBase_, \
			formName_
		):
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		self._THIS_KEY_BASE_ = keyBase_  # adopt keyBase_
		self._USE_THIS_KEY_ = lambda __KEY_TEXT__: f"""{__KEY_TEXT__}{self._THIS_KEY_BASE_}"""  # make a local key sourcer
		self._DICT_KEYS_ = {}  # 
		self._DICT_KEYS_REVERSE_ = {}  # 
		self._LIST_KEYS_TIME_ = []  # 
		self._THIS_FORM_NAME_ = formName_  # adopt formName_

		self._ALPHA_CHANNEL_ = PSG.SZ_ALPHA_HIGH  # 
		self._ALPHA_HIGH_ = PSG.SZ_ALPHA_HIGH  # 
		self._ALPHA_LOW_ = PSG.SZ_ALPHA_LOW  # 
		self._BBOX_ = PSG.EMPTY_BBOX  # 
		self._CHANGED_EVENTS_ = False  # comment
		self._CHANGED_LOCATION_ = False  # comment
		self._CHANGED_MOUSE_LOCATION_ = False  # comment
		self._CHANGED_VALUES_ = False  # comment
		self._CLOSE_BBOX_ = PSG.EMPTY_BBOX  # 
		self._CURRENTLY_DIMMED_ = False  # 
		self._CURRENT_EVENTMODE_ = None  # 
		self._CURRENT_EVENT_ = None  # 
		self._CURRENT_FLIP_INDEX_ = 0  # 
		self._CURRENT_LOCATION_ = PSG.EMPTY_XY  # 
		self._CURRENT_MOUSE_LOCATION_ = PSG.EMPTY_XY  # 
		self._CURRENT_MOUSE_STATUS_ = PSG.MOUSE_STATUS_NONE  # 
		self._CURRENT_VALUES_ = {}  # 
		self._MAINFRAME_ = None  # 
		self._MPX_ = PSG.EMPTY_XY  # comment
		self._SCREEN_DIMS_ = PSG.EMPTY_XY  # 
		self._SIZE_ = PSG.EMPTY_XY  # 
		self._TIME_MS_AT_CHECK_MOUSE_ = PSG.ZERO_CLOCK  # 
		self._TIME_MS_AT_FLIP_ = PSG.ZERO_CLOCK  # 
		self._TIME_MS_AT_MOVE_ = PSG.ZERO_CLOCK  # 
		self._TIME_MS_AT_UPDATE_ = PSG.ZERO_CLOCK  # 
		self._DICT_KEYS_[PSG.K_CHECKBOX_ALPHA_DIM] = PSG.K_CHECKBOX_ALPHA_DIM  # add foreign key for alpha dimming
		self._DICT_KEYS_REVERSE_[PSG.K_CHECKBOX_ALPHA_DIM] = PSG.K_CHECKBOX_ALPHA_DIM  # add foreign key for alpha dimming
		self._DICT_KEYS_[PSG.K_CHECKBOX_RUNAWAY] = PSG.K_CHECKBOX_RUNAWAY  # add foreign key for runningaway
		self._DICT_KEYS_REVERSE_[PSG.K_CHECKBOX_RUNAWAY] = PSG.K_CHECKBOX_RUNAWAY  # add foreign key for runningaway
		self._DICT_KEYS_[PSG.K_CURRENT_INTERVAL_COUNT] = self._USE_THIS_KEY_(PSG.K_CURRENT_INTERVAL_COUNT)  # add foreign key for CURRENT_INTERVAL_COUNT
		self._DICT_KEYS_REVERSE_[self._USE_THIS_KEY_(PSG.K_CURRENT_INTERVAL_COUNT)] = PSG.K_CURRENT_INTERVAL_COUNT  # add foreign key for CURRENT_INTERVAL_COUNT

		self._DICTIN_ = {
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		}
# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._DICTINSTR_ = {
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		}
# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._DICT_KEYS_INT_ = {  # dict of integer keys and their format
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			PSG.K_CURRENT_INTERVAL_COUNT: "04d",  # intervalCount:04d
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._DICT_KEYS_TIME_ = {  # dict of time keys and their max value int seconds
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			PSG.K_TIME_S_AT_NEXT_ALERT: CF.DAY_S,  # comment
			PSG.K_TIME_S_AT_ZEROELAPSE: CF.DAY_S,  # comment
			PSG.K_TIME_S_CLOCK: CF.DAY_S,  # 
			PSG.K_TIME_S_ELAPSED: CF.TIME_S_995959,  # 
			PSG.K_TIME_S_TOGO: CF.DAY_S,  # 
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._DPD_ = {  # define a DPD CLOCKS:/
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			PSG.F___INIT__: True,  # define a DPD at /
			PSG.F___ENTER__: False,  # define __enter__
			PSG.F___EXIT__: False,  # define __exit__ in CLOCKS
			PSG.F_CHECKMOUSE: True,  # define checkMouse
			PSG.F_DEBUGPRINT: False,  # read the frame and set self._RESULT_
			PSG.F_EASYUPDATE: False,  # load the whole thing from the file for easyUpdate
			PSG.F_EASYUPDATEPARMS: False,  # load the whole thing from the file for easyUpdate
			PSG.F_ENINT: False,  # read the frame and set self._RESULT_
			PSG.F_ENSTRING: False,  # read the frame and set self._RESULT_
			PSG.F_INTERVALCOUNTOFF: False,  # turn interval count off
			PSG.F_INTERVALCOUNTON: False,  # turn interval count on
			PSG.F_QUICKREAD: False,  # read the frame and set self._RESULT_
			PSG.F_RUNAWAY: True,  # define runaway
			PSG.F_SETCHECKBOX: True,  # define setCheckbox
			PSG.F_UPDATEFLIPPEDITEMS: False,  # read the frame and set self._RESULT_
			PSG.F_UPDATEFROMDICT: False,  # update the displayed info from a dict or the default _DICTIN_
			PSG.F_ZEROFLIPPED: False,  # update the displayed info from a dict or the default _DICTIN_
			PSG.F_UPDATE: False,  # define the required update function
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._LIST_FLIPPABLE_KEYS_ = [  # list of the items that can be str|list[str, str, ..]
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		]
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._TEXT_CURRENT_INTERVAL_COUNT_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**PSG.TEXT_CURRENT_INTERVAL_COUNT,  # interval count template
			PSG.KEY: f"""{self._USE_THIS_KEY_(K_CURRENT_INTERVAL_COUNT)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._DICT_KEYS_[K_CURRENT_INTERVAL_COUNT] = self._USE_THIS_KEY_(K_CURRENT_INTERVAL_COUNT)
		self._DICT_KEYS_REVERSE_[self._USE_THIS_KEY_(K_CURRENT_INTERVAL_COUNT)] = K_CURRENT_INTERVAL_COUNT

		self._TEXT_NAME_NEXT_EVENT_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**PSG.TEXT_NAME_NEXT_EVENT,  # interval count template
			PSG.KEY: f"""{self._USE_THIS_KEY_(K_NAME_NEXT_EVENT)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._DICT_KEYS_[K_NAME_NEXT_EVENT] = self._USE_THIS_KEY_(K_NAME_NEXT_EVENT)
		self._DICT_KEYS_REVERSE_[self._USE_THIS_KEY_(K_NAME_NEXT_EVENT)] = K_NAME_NEXT_EVENT

		self._TEXT_TIME_S_AT_ZEROELAPSE_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**PSG.TEXT_TIME_S_AT_ZEROELAPSE,  # interval count template
			PSG.KEY: f"""{self._USE_THIS_KEY_(K_TIME_S_AT_ZEROELAPSE)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._LIST_KEYS_TIME_.append(PSG.TEXT_TIME_S_AT_ZEROELAPSE)
		self._LIST_KEYS_TIME_.append(self._USE_THIS_KEY_(PSG.TEXT_TIME_S_AT_ZEROELAPSE))
		self._DICT_KEYS_[K_TIME_S_AT_ZEROELAPSE] = self._USE_THIS_KEY_(K_TIME_S_AT_ZEROELAPSE)
		self._DICT_KEYS_REVERSE_[self._USE_THIS_KEY_(K_TIME_S_AT_ZEROELAPSE)] = K_TIME_S_AT_ZEROELAPSE

		self._TEXT_TIME_S_AT_NEXT_ALERT_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**PSG.TEXT_TIME_S_AT_NEXT_ALERT,  # interval count template
			PSG.KEY: f"""{self._USE_THIS_KEY_(K_TIME_S_AT_NEXT_ALERT)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._LIST_KEYS_TIME_.append(PSG.TEXT_TIME_S_AT_NEXT_ALERT)
		self._LIST_KEYS_TIME_.append(self._USE_THIS_KEY_(PSG.TEXT_TIME_S_AT_NEXT_ALERT))
		self._DICT_KEYS_[K_TIME_S_AT_NEXT_ALERT] = self._USE_THIS_KEY_(K_TIME_S_AT_NEXT_ALERT)
		self._DICT_KEYS_REVERSE_[self._USE_THIS_KEY_(K_TIME_S_AT_NEXT_ALERT)] = K_TIME_S_AT_NEXT_ALERT

		self._TEXT_TIME_S_CLOCK_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**PSG.TEXT_TIME_S_CLOCK,  # interval count template
			PSG.KEY: f"""{self._USE_THIS_KEY_(K_TIME_S_CLOCK)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._LIST_KEYS_TIME_.append(PSG.TEXT_TIME_S_CLOCK)
		self._LIST_KEYS_TIME_.append(self._USE_THIS_KEY_(PSG.TEXT_TIME_S_CLOCK))
		self._DICT_KEYS_[K_TIME_S_CLOCK] = self._USE_THIS_KEY_(K_TIME_S_CLOCK)
		self._DICT_KEYS_REVERSE_[self._USE_THIS_KEY_(K_TIME_S_CLOCK)] = K_TIME_S_CLOCK

		self._TEXT_TIME_S_ELAPSED_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**PSG.TEXT_TIME_S_ELAPSED,  # interval count template
			PSG.KEY: f"""{self._USE_THIS_KEY_(K_TIME_S_ELAPSED)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._LIST_KEYS_TIME_.append(PSG.TEXT_TIME_S_ELAPSED)
		self._LIST_KEYS_TIME_.append(self._USE_THIS_KEY_(PSG.TEXT_TIME_S_ELAPSED))
		self._DICT_KEYS_[K_TIME_S_ELAPSED] = self._USE_THIS_KEY_(K_TIME_S_ELAPSED)
		self._DICT_KEYS_REVERSE_[self._USE_THIS_KEY_(K_TIME_S_ELAPSED)] = K_TIME_S_ELAPSED

		self._TEXT_TIME_S_TOGO_ = {  # class text for interval count
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			**PSG.TEXT_TIME_S_TOGO,  # interval count template
			PSG.KEY: f"""{self._USE_THIS_KEY_(K_TIME_S_TOGO)}""",  # interval count template
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3
		self._LIST_KEYS_TIME_.append(PSG.TEXT_TIME_S_TOGO)
		self._LIST_KEYS_TIME_.append(self._USE_THIS_KEY_(PSG.TEXT_TIME_S_TOGO))
		self._DICT_KEYS_[K_TIME_S_TOGO] = self._USE_THIS_KEY_(K_TIME_S_TOGO)
		self._DICT_KEYS_REVERSE_[self._USE_THIS_KEY_(K_TIME_S_TOGO)] = K_TIME_S_TOGO

		self._COLUMN01_ = [  # the column that puts the two smaller clocks below the main one
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			[
				SG.Text(  # add a new TEXT element to clocks column
					**self._TEXT_TIME_S_CLOCK_  # add the main clock
				),
			],
			[
				SG.Text(  # add a new row to clocks column
					**self._TEXT_TIME_S_AT_ZEROELAPSE_  # add time to go
				),
				SG.Text(  # add a new text element to row01 clocks column
					**self._TEXT_TIME_S_ELAPSED_  # add elapsed time
				),
			],
			[
				SG.Text(  # add a new text element to row01 clocks column
					**self._TEXT_TIME_S_TOGO_  # add elapsed time
				),
				SG.Text(  # add a new row to clocks column
					**self._TEXT_TIME_S_AT_NEXT_ALERT_  # add time to go
				),
			],
			[
				SG.Text(  # add a new text element to row01 clocks column
					**self._TEXT_NAME_NEXT_EVENT_  # add the main clock
				),
			],
			[
				SG.Checkbox(  # add a new text element to row01 clocks column
					**PSG.CHECKBOX_RUNAWAY01  # add elapsed time
				),
				SG.Checkbox(  # add a new text element to row01 clocks column
					**PSG.CHECKBOX_ALPHA_DIM01  # add elapsed time
				),
			],
		]
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._COLUMN02_ = [  # the column that puts the two smaller clocks below the main one
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			[
				SG.Button(  # add a button element to clocks column
					**PSG.BTN_QUIT20  # add the xpand button to clocks
				),
			],
			[
				SG.Button(  # add reset button for elapsed time
					**PSG.BTN_ZERO20  # add the zero button to clocks
				),
			],
			[
				SG.Button(  # add reset button for elapsed time
					**PSG.BTN_XPAND20  # add the zero button to clocks
				),
			],
			[
				SG.Text(  # add reset button for elapsed time
					**self._TEXT_CURRENT_INTERVAL_COUNT_  # add the zero button to clocks
				),
			],
		]
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._LAYOUT_ = [  # layout for APPMODE_CLOCKS
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			[
				SG.Column(  # add a column
					layout=self._COLUMN01_,  # comment
					pad=PSG.SZ_PAD_ALL,  # comment
				),
				SG.Column(  # add a column
					layout=self._COLUMN02_,  # comment
					pad=PSG.SZ_PAD_ALL,  # comment
				),
			],
		]
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		self._WINDOW_ = {  # define the clocks window
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			PSG.ALPHA_CHANNEL: PSG.SZ_ALPHA_HIGH,  # set the high alpha as the default
			PSG.BACKGROUND_COLOR: PSG.COLOR_BACKGROUND,  # eliminate all not useful on the floating clocks
			PSG.BORDER_DEPTH: PSG.SZ_BORDER_DEPTH,  # border depth to zero
			PSG.ELEMENT_PADDING: PSG.SZ_PAD_ALL,  # all padding for elements ((1, 1), (1, 1)) by default
			PSG.FORCE_TOPLEVEL: None,  # 
			PSG.GRAB_ANYWHERE: True,  # eliminate all not useful on the floating clocks
			PSG.KEEP_ON_TOP: True,  # eliminate all not useful on the floating clocks
			PSG.LAYOUT: self._LAYOUT_,  # add the layout for CLOCKS_WINDOW
			PSG.MARGINS: PSG.SZ_MARGINS_ALL,  # 
			PSG.NO_TITLEBAR: True,  # no titlebar on APPMODE_CLOCKS window
			PSG.TITLE: PSG.TITLE_CLOCKS,  # 
		}
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

		if (self._DPD_[PSG.F___INIT__] is True):  # see if debug printing is on
			self.debugPrint(  # debugPrint
				title_="__INIT__3",  # print _DICT_KEYS_REVERSE_
				printDictinS_=True,  # print _DICT_KEYS_
				message_=f"""self._DICT_KEYS {self._DICT_KEYS_}  # print _DICT_KEYS_
		self._DICT_KEYS_REVERSE_ {self._DICT_KEYS_REVERSE_}""")  # print _DICT_KEYS_REVERSE_

		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2


	def __enter__(self):
#		global \
#			DICT_ALL_THE_FORMS
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		self._MAINFRAME_ = SG.Window(**self._WINDOW_).finalize()
		PSG.DICT_ALL_THE_FORMS[self._THIS_FORM_NAME_] = self
		self._SIZE_ = self._MAINFRAME_.Size
		self._SCREEN_DIMS_ = self._MAINFRAME_.GetScreenDimensions()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F___ENTER__]):
			self.debugPrint(
				message_=f"""enter CLOCKS {self._THIS_FORM_NAME_}""",
			)

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# return self
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def __exit__(self, *args_):
#		global \
#			DICT_ALL_THE_FORMS, \
#			APPDS_MAIN
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		PSG.DICT_ALL_THE_FORMS[self._THIS_FORM_NAME_] = None

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F___EXIT__] is True):
			self.debugPrint(
				printDictinS_=True,
				message_=f"""exiting CLOCKS {self._THIS_FORM_NAME_}
APPDS_MAIN {PSG.APPDS_MAIN}
"""
			)

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self._MAINFRAME_.close()
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def checkMouse(self):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_CHECKMOUSE] is True):
			print(f"""checkMouse PSG.NOWMS {PSG.NOWMS} self._TIME_MS_AT_CHECK_MOUSE_ {self._TIME_MS_AT_CHECK_MOUSE_}""")
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if PSG.NOWMS < self._TIME_MS_AT_CHECK_MOUSE_:
			return
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self._TIME_MS_AT_CHECK_MOUSE_ = PSG.NOWMS + PSG.SZ_TIME_MS_BETWEEN_MOUSE_CHECKS
		_statusToRtn_ = None
		_mpxToRtn_ = (0, 0)
		_TLcn_ = self._CURRENT_LOCATION_
		_TSizeX_, _TSizeY_ = _TSize_ = self._SIZE_
		_TMouseLcnX_, _TMouseLcnY_ = _TMouseLcn_ = PSG.getMousePos()

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (_TMouseLcn_ != self._CURRENT_MOUSE_LOCATION_):
			self._CHANGED_MOUSE_LOCATION_ = True
			self._CURRENT_MOUSE_LOCATION_ = _TMouseLcn_

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		else:
			self._CHANGED_MOUSE_LOCATION_ = False

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		_TBBoxWest_, _TBBoxNorth_, _TBBoxEast_, _TBBoxSouth_ = _TBBox_ = self._BBOX_
		_TCloseBBox_ = self._CLOSE_BBOX_
		_isInCloseBBox_ = PSG.isInBBox(_TCloseBBox_, _TMouseLcn_)

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (_TBBoxWest_ < _TMouseLcnX_ < _TBBoxEast_) and (_TMouseLcnY_ < _TBBoxNorth_):
			_mpxToRtn_ = (0, 1)

				# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if _isInCloseBBox_ is True:
				_statusToRtn_ = PSG.MOUSE_STATUS_CLOSE_N

				# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			else:
				_statusToRtn_ = PSG.MOUSE_STATUS_N

			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif ( _TBBoxWest_ < _TMouseLcnX_ < _TBBoxEast_) and (_TMouseLcnY_ > _TBBoxSouth_):
			_mpxToRtn_ = (0, -1)

			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if _isInCloseBBox_ is True:
				_statusToRtn_ = PSG.MOUSE_STATUS_CLOSE_S

			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			else:
				_statusToRtn_ = PSG.MOUSE_STATUS_S

			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_TMouseLcnX_ < _TBBoxWest_) and (_TBBoxNorth_< _TMouseLcnY_ < _TBBoxSouth_):
			_mpxToRtn_ = (1, 0)

				# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if _isInCloseBBox_ is True:
				_statusToRtn_ = PSG.MOUSE_STATUS_CLOSE_W

				# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			else:
				_statusToRtn_ = PSG.MOUSE_STATUS_W

			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_TMouseLcnX_ > _TBBoxEast_) and (_TBBoxNorth_< _TMouseLcnY_ < _TBBoxSouth_):
			_mpxToRtn_ = (-1, 0)

			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if _isInCloseBBox_ is True:
				_statusToRtn_ = PSG.MOUSE_STATUS_CLOSE_E

			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			else:
				_statusToRtn_ = PSG.MOUSE_STATUS_E

			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_TMouseLcnY_ > _TBBoxSouth_) and (_TMouseLcnX_ < _TBBoxWest_):
			_mpxToRtn_ = (1, -1)

			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if _isInCloseBBox_ is True:
				_statusToRtn_ = PSG.MOUSE_STATUS_CLOSE_SW

			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			else:
				_statusToRtn_ = PSG.MOUSE_STATUS_SW

			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_TMouseLcnY_ > _TBBoxSouth_) and (_TMouseLcnX_ > _TBBoxEast_):
			_mpxToRtn_ = (-1, -1)

			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if _isInCloseBBox_ is True:
				_statusToRtn_ = PSG.MOUSE_STATUS_CLOSE_SE

			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			else:
				_statusToRtn_ = PSG.MOUSE_STATUS_SE

			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_TMouseLcnY_ < _TBBoxNorth_) and (_TMouseLcnX_ < _TBBoxWest_):
			_mpxToRtn_ = (1, 1)

			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if _isInCloseBBox_ is True:
				_statusToRtn_ = PSG.MOUSE_STATUS_CLOSE_NW

			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			else:
				_statusToRtn_ = PSG.MOUSE_STATUS_NW

			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_TMouseLcnY_ < _TBBoxNorth_) and (_TMouseLcnX_ > _TBBoxEast_):
			_mpxToRtn_ = (-1, 1)

			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if _isInCloseBBox_ is True:
				_statusToRtn_ = PSG.MOUSE_STATUS_CLOSE_NE

			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			else:
				_statusToRtn_ = PSG.MOUSE_STATUS_NE

			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif PSG.isInBBox(_TBBox_, _TMouseLcn_) is True:
			_mpxToRtn_ = (0, 0)
			_statusToRtn_ = PSG.MOUSE_STATUS_OVER
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_CHECKMOUSE] is True):
			self.debugPrint(
				title_="checkMouse",
				printDictinS_=True,
				message_=f"""returning:
_CURRENT_MOUSE_STATUS_ {self._CURRENT_MOUSE_STATUS_} = {_statusToRtn_}
_MPX_ {self._MPX_} = {_mpxToRtn_}{CF.NEWLINE}"""
			)
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_CHECKMOUSE] is True):
			print(f"""_statusToRtn_ {_statusToRtn_} _CURRENT_MOUSE_STATUS_ {self._CURRENT_MOUSE_STATUS_} _DICTIN_[PSG.K_CHECKBOX_ALPHA_DIM] {self._DICTIN_[PSG.K_CHECKBOX_ALPHA_DIM]}""")
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# deal with alpha checkbox and settings
		# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (
			(_statusToRtn_ == PSG.MOUSE_STATUS_OVER) and
			(self._CURRENT_MOUSE_STATUS_ != PSG.MOUSE_STATUS_OVER) and
			(self._DICTIN_[PSG.K_CHECKBOX_ALPHA_DIM] is True)
		):
			self._MAINFRAME_.AlphaChannel = self._ALPHA_LOW_

		# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (
			(_statusToRtn_ != PSG.MOUSE_STATUS_OVER) and
			(self._CURRENT_MOUSE_STATUS_ == PSG.MOUSE_STATUS_OVER)
			) or (
			(self._CURRENT_MOUSE_STATUS_ == PSG.MOUSE_STATUS_OVER) and
			(self._DICTIN_[PSG.K_CHECKBOX_ALPHA_DIM] is False)
		):
			self._MAINFRAME_.AlphaChannel = self._ALPHA_HIGH_

			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if (self._DPD_[PSG.F_CHECKMOUSE] is True):
				print(f"""mouseOver alpha **NOT** dimming""")

			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DICTIN_[PSG.K_CHECKBOX_RUNAWAY] is True) and (self._CURRENT_MOUSE_STATUS_ in PSG.LIST_CLOSE):
			print("running away")
			self.runaway()

		self._CURRENT_MOUSE_STATUS_ = _statusToRtn_
		self._MPX_ = _mpxToRtn_

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	def debugPrint(self,
			cfDebugInfo_=None,
			message_=None,
			printDictinS_=None,
			title_=None,
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		_strToPrint_ = ""
		_strToPrint_ += f"""{CF.INDENTIN}{CF.NEWLINE}"""

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (title_ is not None):
			_strToPrint_ += f"""{CF.NEWLINE}{title_}{CF.NEWLINE}"""

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (cfDebugInfo_ is True):
			_strToPrint_ += f"""debuginfo: {CF.getDebugInfo()}{CF.NEWLINE}"""

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (message_ is not None):
			_strToPrint_ += f"""message: {message_}{CF.NEWLINE}"""

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (printDictinS_ is True):
#			_strToPrint_ += f"""_DICTIN_: {self.enstring(self._DICTIN_)}{CF.NEWLINE}"""
#			_strToPrint_ += f"""_DICTINSTR_: {self.enstring(self._DICTINSTR_)}{CF.NEWLINE}"""
			_strToPrint_ += f"""_DICTIN_: {self._DICTIN_}{CF.NEWLINE}"""
			_strToPrint_ += f"""_DICTINSTR_: {self._DICTINSTR_}{CF.NEWLINE}"""

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		_strToPrint_ += f"""{CF.NEWLINE}"""
		print(_strToPrint_)

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_DEBUGPRINT] is True):
			print("debugPrinting myself feels weird, redundant, and recursive enough to crash")

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def easyUpdate(self,
			checkboxAlphaDim_=None,
			checkboxRunaway_=None,
			currentFlipInfo_=None,
			eventMode_=None,
			timeAtNextAlert_=None,
			timeAtZeroelapse_=None,
			timeClock_=None,
			timeElapsed_=None,
			timeTogo_=None,
		):
		global \
			APPMODE_MAIN
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (checkboxAlphaDim_ is not None):
			self.setCheckbox(PSG.K_CHECKBOX_ALPHA_DIM, checkboxAlphaDim_)
			__dummy__ = self.quickRead()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (checkboxRunaway_ is not None):
			self.setCheckbox(PSG.K_CHECKBOX_RUNAWAY, checkboxRunaway_)
			__dummy__ = self.quickRead()

			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
		if (currentFlipInfo_ is not None):
			self._DICTIN_[PSG.K_LIST_FLIP_INFO] = currentFlipInfo_.copy()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (eventMode_ is not None):
			self.CURRENT_EVENTMODE = eventMode_

			# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
		if (eventMode_ == PSG.EVENTMODE_INTERVAL):
			self.intervalCountOn()

			# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
		else:
			self.intervalCountOff()

			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

#			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
#		if (nameNextEvent_ is not None):
#			(self._DICTIN_[PSG.K_NAME_NEXT_EVENT].update(nameNextEvent_)

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (timeAtNextAlert_ is not None):
			self._DICTIN_[PSG.K_TIME_S_AT_NEXT_ALERT] = timeAtNextAlert_

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (timeAtZeroelapse_ is not None):
			self._DICTIN_[PSG.K_TIME_S_AT_ZEROELAPSE] = timeAtZeroelapse_

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (timeClock_ is not None):
			self._DICTIN_[PSG.K_TIME_S_CLOCK] = timeClock_

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (timeElapsed_ is not None):
			self._DICTIN_[PSG.K_TIME_S_ELAPSED] = timeElapsed_

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (timeTogo_ is not None):
			self._DICTIN_[PSG.K_TIME_S_TOGO] = timeTogo_

		self.enint()
		self.updateFromDict()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_EASYUPDATE]):
			self.debugPrint(
				printDictinS_=True,
				title_="easyUpdate",
				message_=f"""input:
checkboxAlphaDim_ {checkboxAlphaDim_}
checkboxRunaway_ {checkboxRunaway_}
currentIntervalCount_ {currentIntervalCount_}
eventMode_ {eventMode_}
nameNextEvent_ {nameNextEvent_}
timeAtNextAlert_ {timeAtNextAlert_}
timeAtZeroelapse_ {timeAtZeroelapse_}
timeClock_ {timeClock_}
timeElapsed_ {timeElapsed_}
timeTogo_ {timeTogo_}
"""
			)
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def easyUpdateParms(self,
			tooltip_=None,  # (key_, val_)
			alphaChannel_=None,  # float
		):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (alphaChannel_ is not None):
			self._MAINFRAME_.Update(alpha_channel=alphaChannel_)

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (tooltip_ is not None):
			self._MAINFRAME_[self._USE_THIS_KEY_(tooltip_[0])].Update(tooltip=tooltip_[1])

		self.enint()
		self.updateFromDict()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_EASYUPDATEPARMS]):
			self.debugPrint(
				printDictinS_=True,
				title_="easyUpdateParms",

				message_=f"""input:
tooltip_ {tooltip_}
alphaChannel_ {alphaChannel_}
"""
			)
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def enint(self):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		_thisDictin_ = CF.quickCopyDict(self._DICTIN_)
		_dictToRtn_ = {}
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisKey_, _thisVal_ in _thisDictin_.items():
			_isInstanceOfStr_ = isinstance(_thisDictin_[_thisKey_], str)
			_isInstanceOfList_ = isinstance(_thisDictin_[_thisKey_], list)

				# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if (_isInstanceOfStr_ is True):

					# 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥
				if (_thisKey_ in self._DICT_KEYS_TIME_):
					_dictToRtn_[_thisKey_] = CF.HMSToNrmlInt(_thisVal_)

					# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
				elif (_thisKey_ in self._DICT_KEYS_INT_):
					_dictToRtn_[_thisKey_] = int(_thisVal_)

					# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
				else:
					_dictToRtn_[_thisKey_] = _thisVal_

					# ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4

				# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			elif (_isInstanceOfList_ is True):
				_dictToRtn_[_thisKey_] = []

					# 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥
				if (_thisKey_ in self._DICT_KEYS_TIME_):

					# 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥
					for _thisItem_ in _thisVal_:

							# 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥
						if (isinstance(_thisItem_, str) is True):
							_dictToRtn_[_thisKey_].append(CF.HMSToNrmlInt(_thisItem_))

							# ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥
						else:
							_dictToRtn_[_thisKey_].append(_thisItem_)

						# ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6

					# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
				elif (_thisKey_ in self._DICT_KEYS_INT_):

						# 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥
						for _thisItem_ in _thisVal_:
							_dictToRtn_[_thisKey_].append(int(_thisItem_))

					# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
				else:
					_dictToRtn_[_thisKey_] = _thisVal_

				# ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4

				# ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥ ⥣3⥥
			else:
				_dictToRtn_[_thisKey_] = _thisVal_

			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_ENINT]):
			self.debugPrint(
				printDictinS_=True,
				title_="enint",
			)
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def enstring(self, dictToUse_=None):
		 # fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (dictToUse_ is None):
			dictToUse_ = CF.quickCopyDict(self._DICTIN_)
			_returnMode_ = False
		else:
			_returnMode_ = True

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_ENSTRING]):
			self.debugPrint(
				printDictinS_=True,
				title_="start of enstring",
				message_= f"""dictToUse_ {dictToUse_}
{CF.frameIt("_returnMode_", _returnMode_)}"""
			)

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		_dictToRtn_ = {}
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisKey_, _thisVal_ in dictToUse_.items():

				# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if (isinstance(_thisVal_, list) is True):
				# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
				_dictToRtn_[_thisKey_] = []

					# 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥
				if (self._DPD_[PSG.F_ENSTRING] is True):
					print(f"""*********** list {_thisKey_}: {_thisVal_}""")

				# ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4

				# 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥
				for _thisItem_ in _thisVal_:

						# 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥
					if (_thisKey_ in self._DICT_KEYS_TIME_):
						_dictToRtn_[self._DICT_KEYS_[_thisKey_]].append(CF.nrmlIntToHMS(_thisItem_))

						# 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥
					elif (_thisKey_ in self._DICT_KEYS_INT_):

							# 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥
						if (self._DICT_KEYS_INT_[_thisKey_] == "04d"):
							_dictToRtn_[_thisKey_].append(f"""{_thisItem_:04d}""")

							# ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥ ⥣6⥥
						else:
							_dictToRtn_[_thisKey_].append(f"""{_thisItem_}""")

						# ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6

						# ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥
					else:
						_dictToRtn_[_thisKey_].append(f"""{_thisItem_}""")

					# ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5

				# ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

				# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
				# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
			else:
				# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2

					# 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥ 4⥥
				if (_thisKey_ in self._DICT_KEYS_TIME_):
					_dictToRtn_[self._DICT_KEYS_[_thisKey_]] = CF.nrmlIntToHMS(_thisVal_)

						# 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥
					if (self._DPD_[PSG.F_ENSTRING] is True):
						print(f"""time element in enstrging {_thisKey_}: {_thisVal_}""")
					# ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5

					# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
				elif (_thisKey_ in self._DICT_KEYS_INT_):

						# 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥
					if (self._DICT_KEYS_INT_[_thisKey_] == "04d"):
						_dictToRtn_[self._DICT_KEYS_[_thisKey_]] = f"""{_thisVal_:04d}"""

							# 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥
						if (self._DPD_[PSG.F_ENSTRING] is True):
							print(f"""int04d element in enstrging {_thisKey_}: {_thisVal_}""")

						# ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6

						# ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥
					else:
						_dictToRtn_[self._DICT_KEYS_[_thisKey_]] = f"""{_thisVal_}"""

							# 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥ 6⥥
						if (self._DPD_[PSG.F_ENSTRING] is True):
							print(f"""time element in enstrging {_thisKey_}: {_thisVal_}""")

					# ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥ ⥣5⥥

					# ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥ ⥣4⥥
				else:
					_dictToRtn_[_thisKey_] = (f"""{_thisVal_}""")

						# 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥ 5⥥
					if (self._DPD_[PSG.F_ENSTRING] is True):
						print(f"""normal key {_thisKey_}: {_thisVal_}""")

				# ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (_returnMode_ is True):
			return _dictToRtn_
		else:
			self._DICTINSTR_ = CF.quickCopyDict(_dictToRtn_)

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_ENSTRING]):
			print(f"""end of enstring
dictToUse_ {dictToUse_}
_dictToRtn_ {_dictToRtn_}
""")

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def intervalCountOff(self):
		# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
		self._MAINFRAME_[self._DICT_KEYS_[PSG.K_CURRENT_INTERVAL_COUNT]].update(text_color=PSG.COLOR_TEXT_CURRENT_INTERVAL_COUNT_INACTIVE)
		self.updateFlippedItems()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_INTERVALCOUNTOFF]):
			self.debugPrint(
				title_="intervalCountOff",
			)

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


	def intervalCountOn(self,
			intervalCount_=None):
		# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

		self._MAINFRAME_[self._DICT_KEYS_[PSG.K_CURRENT_INTERVAL_COUNT]].update(text_color=PSG.COLOR_TIME_TOGO)
		self.updateFromDict()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_INTERVALCOUNTON]):
			self.debugPrint(
				title_="intervalCountOn",
			)

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


	def quickRead(self,
			timeout_=1):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		_event_, _values_ = self._MAINFRAME_.Read(timeout=timeout_)

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (_event_ != self._CURRENT_EVENT_):
			self._CHANGED_EVENT_ = True
			self._CURRENT_EVENT_ = _event_
			# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		else:
			self._CHANGED_EVENT_ = False
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (_values_ != self._CURRENT_VALUES_):
			self._CHANGED_VALUES_ = True
			self._CURRENT_VALUES_ = _values_
			# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		else:
			self._CHANGED_VALUES_ = False
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		if (self._DPD_[PSG.F_QUICKREAD]):
			self.debugPrint(
				title_="quickRead",
				message_=f"""set:
_CURRENT_EVENT_ {self._CURRENT_EVENT_}
_CURRENT_VALUES_ {self._CURRENT_VALUES_}"""
			)

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def runaway(self):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (PSG.NOWMS < self._TIME_MS_AT_MOVE_):
			return  # only move at minimum  PSG.SZ_TIME_BETWEEN_MOVES apart

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self._TIME_MS_AT_MOVE_ = PSG.NOWMS + PSG.SZ_TIME_MS_BETWEEN_MOVES
		_screenSZX_, _screenSZY_ = self._SCREEN_DIMS_
		_sizeX_, _sizeY_ = self._SIZE_
		_lcnX_, _lcnY_ = self._CURRENT_LOCATION_
		_moveToX_ = _lcnX_ + (self._MPX_[PSG.INDEX_X] * PSG.SZ_MOVE_DIST)
		_moveToY_ = _lcnY_ + (self._MPX_[PSG.INDEX_Y] * PSG.SZ_MOVE_DIST)

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_RUNAWAY] is True):
			print(f"""{CF.getDebugInfo()}
{CF.frameItMS("_TIME_MS_AT_MOVE_", self._TIME_MS_AT_MOVE_)} = {CF.frameItMS("PSG.NOWMS", PSG.NOWMS)} + {CF.frameItMS("PSG.SZ_TIME_MS_BETWEEN_MOVES", PSG.SZ_TIME_MS_BETWEEN_MOVES)}
{CF.frameIt("_screenSZX_", _screenSZX_)}, {CF.frameIt("_screenSZY_", _screenSZY_)} = {CF.frameIt("self._SCREEN_DIMS_", self._SCREEN_DIMS_)}
{CF.frameIt("_sizeX_", _sizeX_)}, {CF.frameIt("_sizeY_", _sizeY_)} = {CF.frameIt("self._SIZE_", self._SIZE_)}
{CF.frameIt("_lcnX_", _lcnX_)}, {CF.frameIt("_lcnY_", _lcnY_)} = {CF.frameIt("_CURRENT_LOCATION_", self._CURRENT_LOCATION_)}
{CF.frameIt("_moveToX_", _moveToX_)} = {CF.frameIt("_lcnX_", _lcnX_)} + ({CF.frameIt("_MPX_[PSG.INDEX_X]", self._MPX_[PSG.INDEX_X])} * {CF.frameIt("PSG.SZ_MOVE_DIST", PSG.SZ_MOVE_DIST)})
{CF.frameIt("_moveToY_", _moveToY_)} = {CF.frameIt("_lcnY_", _lcnY_)} + ({CF.frameIt("_MPX_[PSG.INDEX_Y]", self._MPX_[PSG.INDEX_Y])} * {CF.frameIt("PSG.SZ_MOVE_DIST", PSG.SZ_MOVE_DIST)})
""")

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (_moveToX_ < 0):
			_moveToX_ = 0

			# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_moveToX_ > (_screenSZX_ - _sizeX_)):
			_moveToX_ = (_screenSZX_ - _sizeX_)

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (_moveToY_ < 0):
			_moveToY_ = 0

			# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		elif (_moveToY_ > (_screenSZY_ - _sizeY_)):
			_moveToY_ = (_screenSZY_ - _sizeY_)

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_RUNAWAY] is True):
			print(f"""runaway: ready to move to {CF.OPAREN}{_moveToX_}, {_moveToY_}{CF.CPAREN}""")

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

#			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
#		if (abs(_moveToX_ - _lcnX_) > PSG.SZ_MAX_DELTA) or (abs(_moveToY_ - _lcnY_) > PSG.SZ_MAX_DELTA):
#			return

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self._MAINFRAME_.Move(_moveToX_, _moveToY_)
		__dummy__ = self.quickRead()

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def setCheckbox(self, checkboxKey_, checkboxValue_=None):
		global \
			APPDS_MAIN
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3

		if (checkboxValue_ is None):
			checkboxValue_ = not self._DICTIN_[checkboxKey_]

		self._MAINFRAME_[self._DICT_KEYS_[checkboxKey_]].update(
			value=checkboxValue_,
		)
		# self._VALUES_[checkboxKey_] = checkboxValue_
		PSG.APPDS_MAIN[checkboxKey_] = checkboxValue_
		self._DICTIN_[checkboxKey_] = checkboxValue_

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_SETCHECKBOX] is True):
			self.debugPrint(
				printDictinS_=True,
				message_=f"""setCheckbox
checkboxKey_ {checkboxKey_}
checkboxValue_ {checkboxValue_}
"""
			)
		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def updateFlippedItems(self):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_UPDATEFLIPPEDITEMS] is True):
			print(f"""updateFlippedItems
{CF.frameIt("self._CURRENT_FLIP_INDEX_", self._CURRENT_FLIP_INDEX_)}
{CF.frameItMS("PSG.NOWMS", PSG.NOWMS)}
{CF.frameIt("_TIME_MS_AT_FLIP_", self._TIME_MS_AT_FLIP_)}
""")

		if (PSG.NOWMS < self._TIME_MS_AT_FLIP_):  # or (self._CURRENT_FLIP_INDEX_ == -1):
			return  # wait until the timer has expired between doing anything

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self._TIME_MS_AT_FLIP_ = PSG.NOWMS + PSG.SZ_TIME_MS_BETWEEN_FLIPS

		self.enstring()

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		try:
			_thisInfo_ = self._DICTIN_[PSG.K_LIST_FLIP_INFO].pop()
		except IndexError:
			_thisInfo_ = PSG.EMPTY_TUPDICT_FLIP_INFODICT()

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self._DICTIN_[PSG.K_LIST_FLIP_INFO].append(_thisInfo_)

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisKey_, _thisVal_ in _thisInfo_.items():
			self._MAINFRAME_[self._DICT_KEYS_[_thisKey_]].Update(value=_thisVal_)

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		__dummy__ = self.quickRead()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_UPDATEFLIPPEDITEMS]):
			self.debugPrint(
				title_="updateFlippedItems",
				printDictinS_=True,
				message_=f"""
_thisInfo_ {_thisInfo_}
__dummy__ {__dummy__}{CF.NEWLINE}""")
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2


		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def updateFromDict(self,
			dictToUpdateFrom_=None):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if dictToUpdateFrom_ is None:
			dictToUpdateFrom_ = CF.quickCopyDict(self._DICTIN_)

			# ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥ ⥣2⥥
		else:
			self._DICTIN_.update(dictToUpdateFrom_)

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_UPDATEFROMDICT] is True):
			print(f"""not default updateFromDict before
dictToUpdateFrom_ {self.enstring(dictToUpdateFrom_)}
_DICTIN_ {self.enstring(self._DICTIN_)}
""")

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self.enint()
		self.enstring()
		dictToUpdateFrom_ = CF.quickCopyDict(self._DICTINSTR_)

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_UPDATEFROMDICT] is True):
			print(f"""not default updateFromDict after CF.quickCopyDict(self._DICTINSTR_)
dictToUpdateFrom_ {self.enstring(dictToUpdateFrom_)}
_DICTINSTR_ {self.enstring()}
""")

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisKey_, _thisVal_ in dictToUpdateFrom_.items():

				# 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥ 3⥥
			if (_thisKey_ not in PSG.LIST_DNUPDATE):
				self._MAINFRAME_[_thisKey_].Update(value=_thisVal_)
			# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self.updateFlippedItems()
		__dummy__ = self.quickRead()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_UPDATEFROMDICT]):
			self.debugPrint(
				title_="updateFromDict",
				printDictinS_=True,
				message_=f"""
dictToUpdateFrom_ {dictToUpdateFrom_}
__dummy__ {__dummy__}{CF.NEWLINE}""")
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def zeroFlipped(self):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		for _thisKey_ in self._LIST_FLIPPABLE_KEYS_:
			self._DICTIN_[_thisKey_] = []

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self._CURRENT_FLIP_INDEX_ = -1

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3


	def update(self):
		# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
		if (PSG.NOWMS < self._TIME_MS_AT_UPDATE_):
			return

		self._TIME_MS_AT_UPDATE_ = PSG.NOWMS + PSG.SZ_TIME_MS_BETWEEN_UPDATES
		_TLcn_ = self._MAINFRAME_.CurrentLocation()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (_TLcn_ != self._CURRENT_LOCATION_):
			self._CHANGED_LOCATION_ = True
			self._CURRENT_LOCATION_ = _TLcn_
			self._BBOX_ = PSG.getBBox(self._CURRENT_LOCATION_, self._SIZE_)
			self._CLOSE_BBOX_ = PSG.getCloseBBox(self._CURRENT_LOCATION_, self._SIZE_)
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		self._DICTIN_[PSG.K_TIME_S_CLOCK] = PSG.NOWS
		self._DICTIN_[PSG.K_TIME_S_TOGO] = (self._DICTIN_[PSG.K_TIME_S_AT_NEXT_ALERT] - PSG.NOWS)
		self._DICTIN_[PSG.K_TIME_S_ELAPSED] = (PSG.NOWS - self._DICTIN_[PSG.K_TIME_S_AT_ZEROELAPSE])
		self.checkMouse()
		self.quickRead()
		self.updateFromDict()
		self.updateFlippedItems()

			# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥
		if (self._DPD_[PSG.F_UPDATE] is True):
			self.debugPrint(
				title_="update",
				printDictinS_=False,
				message_=f"""
self._TIME_MS_AT_UPDATE_ {CF.frameItMS("_TIME_MS_AT_UPDATE_", self._TIME_MS_AT_UPDATE_)} = {CF.frameItMS("PSG.NOWMS", PSG.NOWMS)} + PSG.SZ_TIME_MS_BETWEEN_UPDATES {PSG.SZ_TIME_MS_BETWEEN_UPDATES / 1000}
self._CURRENT_LOCATION_ {self._CURRENT_LOCATION_} = self._MAINFRAME_.CurrentLocation()
self._BBOX_ {self._BBOX_} = getBBox(self._CURRENT_LOCATION_, self._SIZE_ {self._SIZE_})
self._CLOSE_BBOX_ {self._CLOSE_BBOX_} = getCloseBBox(self._CURRENT_LOCATION_, self._SIZE_)
self._DICTIN_[PSG.K_TIME_S_CLOCK] {CF.frameItHMS("K_TIME_S_CLOCK", self._DICTIN_[PSG.K_TIME_S_CLOCK])} = {CF.frameItHMS("PSG.NOWS", PSG.NOWS)}
self._DICTIN_[PSG.K_TIME_S_TOGO] {CF.frameItHMS("K_TIME_S_TOGO", self._DICTIN_[PSG.K_TIME_S_TOGO])} = (self._DICTIN_[PSG.K_TIME_S_AT_NEXT_ALERT] {CF.frameItHMS("K_TIME_S_AT_NEXT_ALERT", self._DICTIN_[PSG.K_TIME_S_AT_NEXT_ALERT])} - PSG.NOWS  {CF.frameItHMS("PSG.NOWS", PSG.NOWS)})
self._DICTIN_[PSG.K_TIME_S_ELAPSED] {CF.frameItHMS("K_TIME_S_ELAPSED", self._DICTIN_[PSG.K_TIME_S_ELAPSED])} = (PSG.NOWS - self._DICTIN_[PSG.K_TIME_S_AT_ZEROELAPSE] {CF.frameItHMS("K_TIME_S_AT_ZEROELAPSE", self._DICTIN_[PSG.K_TIME_S_AT_ZEROELAPSE])})
self._CURRENT_MOUSE_LOCATION_ {self._CURRENT_MOUSE_LOCATION_}, self._CURRENT_MOUSE_STATUS_ {self._CURRENT_MOUSE_STATUS_} = self.checkMouse()
""",
			)
		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


