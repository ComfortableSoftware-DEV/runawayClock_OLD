#!/usr/bin/python


class one(object):

	def __init__(self,
			val1_,
			val2_,
	):
		self._DICT_ = {
				"one": 1,
				"two": 2,
				"val1": val1_,
				"val2": val2_,
		}

	def __enter__(self):
		print(f"""_DICT_ {self._DICT_}""")
		return self

	def __exit__(self,
			*args_,
			**KWArgs_):
		print(f"""_DICT_ {self._DICT_}
args_ {args_}
KWArgs_ {KWArgs_}
""")


	def doSomething(self,
			somethingToDo_=None
	):
		self._DICT_[somethingToDo_[0]] = somethingToDo_[1]


with one("hello", "there") as ONE:
	_myDict_ = ONE._DICT_
	_myDict_["new1"] = "another"
	_myDict_["new2"] = "one bites it"
	ONE.doSomething(("add1", "the dust I mean"))
	print(f"""_myDict_ {_myDict_}
ONE._DICT_ {ONE._DICT_}
""")
