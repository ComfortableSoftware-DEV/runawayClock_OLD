

import imp
import os


__all__ = []
_TBGLST_ = []
# 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥
for _module_ in sorted(os.listdir(os.path.dirname(__file__))):
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	if (
			(_module_[0:2] != "__") and
			(_module_[-7:] != "_NEW.py") and
			(_module_[0] == "_")
	):
		_moduleToImport_ = f"""FM/MAKE_D/{_module_}"""
		__all__.append(_module_)
		print(f"""making {_module_}""")
		_thisModule_ = imp.load_source("module", _moduleToImport_)
		_TBGLST_.extend(_thisModule_.TBGLST)
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1
# ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0 ⥣0
_TBGLST_.sort()
print(f"""swallowed {len(_TBGLST_)} lines of potentially useful data""")


#
