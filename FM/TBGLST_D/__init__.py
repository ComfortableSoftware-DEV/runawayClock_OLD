

import os


from FM.TBGLST_D import M_01_CF

__all__ = [
		"M_01_CF",
		"M_02_FM",
		"M_03_00_PSG",
		"M_03_01_PSG_CLOCKS_C",
]

# 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥
for _module_ in os.listdir(os.path.dirname(__file__)):
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	if (
			(_module_ != "__init__.py") and
			(_module_[0:2] == "M_")
	):
		__import__(_module_[:-3], globals(), locals())
