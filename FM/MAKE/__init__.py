

import os


__all__ = [
		"00_00_MTBL_C"
		"01_makeCF",
		"02_makeFM",
		"03_00_makePSG",
		"03_01_makePSGClasses",
		"04_00_makeMD_C",
		"04_01_makeMD_SCTNS"
]


_moduleList_ = []
# 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥ 0⥥
for _module_ in os.listdir(os.path.dirname(__file__)):
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	if (
			(_module_ != "__init__.py") and
			(_module_[0] == "_")
	):
		__import__(module[:-3], locals(), globals())
