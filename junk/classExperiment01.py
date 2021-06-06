#!/usr/bin/python


class testClass():

	def __init__(self):
		self._varA_ = {
			0: "hello",
			1: "there",
		}

	def __enter__(self):
		print("entered")
		self.printVarA()
		return self

	def __exit__(self, *args):
		print(f"""exiting
_varA_ {self._varA_}""")

	def printVarA(self):
		print(f"""_varA_ is {self._varA_}""")

with testClass() as _obj1_:
	_varB_ = _obj1_._varA_
	_varB_[0] = "what's upwitchew"
	_obj1_.printVarA()
	_varB_[2] = "not much you?"
	_obj1_.printVarA()
