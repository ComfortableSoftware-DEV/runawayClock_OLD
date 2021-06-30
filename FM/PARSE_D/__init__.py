

import imp
import os


__SCTNS__ = {}
# 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱
for _module_ in sorted(os.listdir(os.path.dirname(__file__))):
	# 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
	if (
			(_module_[0:2] != "__") and
			(_module_[-7:] != "_NEW.py") and
			(_module_[0] == "_")
	):
		_moduleToImport_ = f"""FM/PARSE_D/{_module_}"""
		_thisModule_ = imp.load_source("module", _moduleToImport_)
		__SCTNS__.update(_thisModule_._SCTNS_)
	# ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1
# ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0
_TBGLST_.sort()
print(f"""swallowed {len(_TBGLST_)} lines of potentially useful data""")


#
