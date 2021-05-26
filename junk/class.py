class CLASS_popupDialog(object):
	global \
			MAINFRAME, \
			myPopup_, \
			poppedup_

	def __init__(self, key_):

		self.CLOCKS_TEXT_INTERVAL_COUNT_01 = {  # define the text element for CLOCKS_CLOCK_TIME
			"text": "00",  # the text to fill in
			"background_color": "#552233",  # background color for the clock elements
			"enable_events": True,  # this is clickable
			"font": ("Source Code Pro", 20),  # font+size line
			"justification": "center",  # center everything
			"key": key_,  # comment
			"pad": ((1, 1), (1, 1)),  # the text color for a clock_time element
			"size": (4, 1),  # characters, lines size line
			"text_color": "#FF3399",  # the text color for a clock_time element
		}

		self.CHECKBOX_RUNAWAY2 = {  # checkbox for runaway from mouse behavior
			"text": "RNAWY",  # text label
			"tooltip": "run away from mouse when checked",  # tooltip
			"default": False,  # leave it on by default
			"key": "KEY_CHECKBOX_RUNAWAY2",  # set the key for the checkbox
			"enable_events": True,
		}


		self.CLOCKS_LAYOUT_01 = [
			[
				SG.Text(**self.CLOCKS_TEXT_INTERVAL_COUNT_01),
				SG.Button(**BTN_QUIT20),
				SG.Checkbox(**CHECKBOX_RUNAWAY),
			]
		]

		self.CLOCKS_WINDOW_01 = {  # define the clocks window
			"auto_close": True,
			"auto_close_duration": 10,
			"background_color": "#552233",  # eliminate all not useful on the floating clocks
			"border_depth": 0,  # border depth to zero
			"element_padding": 0,  # all padding for elements ((1, 1), (1, 1)) by default
			"force_toplevel": None,  #
			"grab_anywhere": True,  # eliminate all not useful on the floating clocks
			"keep_on_top": True,  # eliminate all not useful on the floating clocks
			"layout": self.CLOCKS_LAYOUT_01,  # add the layout for CLOCKS_WINDOW
			"margins": (0, 0),  #
			"no_titlebar": False,  # no titlebar on APPMODE_CLOCKS window
			"title": "POPTEST",  #
		}

	def __enter__(self):
		global \
				MAINFRAME, \
				myPopup_, \
				poppedup_
		# MAINFRAME.hide()
		poppedup_ = True
		myPopup_ = SG.Window(**self.CLOCKS_WINDOW_01).finalize()
		myPopup_["KEY_CHECKBOX_RUNAWAY"].update(value=MAINFRAME["KEY_CHECKBOX_RUNAWAY"])

	def __exit__(self, *args_):
		global \
				MAINFRAME, \
				myPopup_, \
				poppedup_
		MAINFRAME["KEY_CHECKBOX_RUNAWAY"].update(value=myPopup_["KEY_CHECKBOX_RUNAWAY"])
		myPopup_.close()
		print(f"""{CF.frameIt("args_", args_)}""")
		myPopup_ = None
		poppedup_ = False
		# MAINFRAME.un_hide()

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# EOF class.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#
#
#
#
