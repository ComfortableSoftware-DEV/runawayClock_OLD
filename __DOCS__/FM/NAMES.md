## NAMES

### GLOBAL

NAME                                         | SPELL IT OUT                                                                                 | EXAMPLE                                             | DESCRIPTION
---------------------------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------------------------------
============================================ | ============================================================================================ | =================================================== | ===============================================================================
NAME_GLBL_PY                                 | \_\_PYCONFIGDIR__/\_\_FILENAME__.py                                                          | /rcr/0-units/python/aModule.py                      | almost never used currently, file in the root of the python units directory
NAME_GLBL_NEW_PY_MD                          | \_\_PYCONFIGDIR__/res/MARKDOWN/\_\_FILENAME__.md                                             | /rcr/0-units/python/res/MARKDOWN/                   |
                                             |                                                                                              |                                                     |


### HOME

NAME                                         | SPELL IT OUT                                                                                 | EXAMPLE                                             | DESCRIPTION
---------------------------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------------------------------
============================================ | ============================================================================================ | =================================================== | ===============================================================================
NAME_HOME_CACHE                              | /home/will/.cache/\_\_FILENAME__.py                                                          | /home/will/.cache/web01.log                         | files in the root of ~/.cache
NAME_HOME_CONFIG                             | /home/will/.config/\_\_FILENAME__.py                                                         | /home/will/.config/serialz.pkl                      | files in the root of ~/.config
NAME_HOME_SELF_CACHE                         | /home/will/.cache/\_\_MODULE_NAME__&nbsp;\_\_FILENAME__.py                                   | /home/will/.cache/biditi/biditi.log                 | files in the \_\_MODULE_NAME__ directory of ~/.cache
NAME_HOME_SELF_CONFIG                        | /home/will/.config/\_\_MODULE_NAME__&nbsp;\_\_FILENAME__.py                                  | /home/will/.config/biditi/biditi.pkl                | files in the \_\_MODULE_NAME__ directory of ~/.config


### LOCAL

NAME                                         | SPELL IT OUT                                                                                 | EXAMPLE                                             | DESCRIPTION
---------------------------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------------------------------
============================================ | ============================================================================================ | =================================================== | ===============================================================================
NAME_LCL_MOD_NEW_PY                          | \_\_MODULE_NAME__/\_\_MODULE_NAME__&nbsp;_NEW.py                                             | CF/CF_NEW.py                                        | raw module _NEW
NAME_LCL_MOD_PY                              | \_\_MODULE_NAME__/\_\_MODULE_NAME__.py                                                       | CF/CF.py                                            | just the raw module in it's own directory
NAME_LCL_MOD_SUB0_NEW_PY                     | \_\_MODULE_NAME__/\_\_MODULE_NAME__&nbsp;\_\_SUB0__&nbsp;.py                                 | CF/CF_DAYS_NEW.py                                   | little sub modules _NEW
NAME_LCL_MOD_SUB0_PY                         | \_\_MODULE_NAME__/\_\_MODULE_NAME__&nbsp;\_\_SUB0__.py                                       | CF/CF_DAYS.py                                       | little sub modules
NAME_LCL_MOD_SUB1_NEW_PY                     | \_\_MODULE_NAME__/\_\_MODULE_NAME__&nbsp;\_\_SUB0__&nbsp;\_\_SUB1__.py                       | CF/CF_01_DAYS_NEW.py                                | little sub modules _NEW
NAME_LCL_MOD_SUB1_PY                         | \_\_MODULE_NAME__/\_\_MODULE_NAME__&nbsp;\_\_SUB0__&nbsp;\_\_SUB1__.py                       | CF/CF_01_DAYS.py                                    | little sub modules
NAME_LCL_SELF_C_NEW_PY                       | \_\_MODULE_NAME__/\_\_CLASS__&nbsp;_NEW.py                                                   | CF/APPDS_C_NEW                                      | just a class in a module directory _NEW
NAME_LCL_SELF_C_PY                           | \_\_MODULE_NAME__/\_\_CLASS__                                                                | FM/TBGLST_C.py                                      | just a class in a module directory
NAME_LCL_SUB0_C_NEW_PY                       | \_\_MODULE_NAME__/\_\_SUB0__&nbsp;\_\_CLASS__&nbsp;.py                                       | CF/_01_APPDS_C_NEW.py                               | ordered sub classes _NEW etc.
NAME_LCL_SUB0_C_PY                           | \_\_MODULE_NAME__/\_\_SUB0__&nbsp;\_\_CLASS__.py                                             | CF/_01_APPDS_C.py                                   | ordered sub classes etc.
NAME_LCL_SUB1_C_NEW_PY                       | \_\_MODULE_NAME__/\_\_SUB0__&nbsp;\_\_SUB1__&nbsp;\_\_CLASS__\_C_NEW.py                      | CF/_03_01_PSGClasses.py                             | two deep ordered sub class
NAME_LCL_SUB1_C_PY                           | \_\_MODULE_NAME__/\_\_SUB0__&nbsp;\_\_SUB1__&nbsp;\_\_CLASS__\_C.py                          | CF/_03_01_PSGClasses.py                             | two deep ordered sub class
NAME_LCL_SUBD0_C_NEW_PY                      | \_\_MODULE_NAME__/\_\_SUBD0__/\_\_CLASS__&nbsp;_NEW.py                                       | FM/MAKE/MTBL_C_NEW.py                               | straight classes in a subdirectory
NAME_LCL_SUBD0_C_PY                          | \_\_MODULE_NAME__/\_\_SUBD0__/\_\_CLASS__.py                                                 | FM/MAKE/MTBL_C.py                                   | straight classes in a subdirectory
NAME_LCL_SUBD0_SUB1_NEW_PY                   | \_\_MODULE_NAME__&nbsp;\_\_SUBD0__&nbsp;\_\_SUB1__&nbsp;_NEW.py                              |                                                     |
NAME_LCL_SUBD0_SUB1_PY                       | \_\_MODULE_NAME__&nbsp;\_\_SUBD0__&nbsp;\_\_SUB1__.py                                        |                                                     |
NAME_LCL_SUBD0_SUB2_NEW_PY                   | \_\_MODULE_NAME__/\_\_SUBD0__/\_\_SUB1__&nbsp;\_\_SUB2__&nbsp;_NEW.py                        | FM/MAKE/\_01_CF_NEW.py                              | subordered submodules 2 deep _NEW
NAME_LCL_SUBD0_SUB2_PY                       | \_\_MODULE_NAME__/\_\_SUBD0__/\_\_SUB1__&nbsp;\_\_SUB2__                                     | FM/MAKE/\_01_CF.py                                  | subordered submodules 2 deep
NAME_LCL_SUBD0_SUB3_C_NEW_PY                 | \_\_MODULE_NAME__/\_\_SUBD0__/\_\_SUB1__&nbsp;\_\_SUB2__&nbsp;\_\_SUB3__&nbsp;\_C_NEW.py     |                                                     |
NAME_LCL_SUBD0_SUB3_C_PY                     | \_\_MODULE_NAME__/\_\_SUBD0__/\_\_SUB1__&nbsp;\_\_SUB2__&nbsp;\_\_SUB3__&nbsp;\_C.py         |                                                     |
NAME_LCL_SUBD0_SUB3_NEW_PY                   | \_\_MODULE_NAME__/\_\_SUBD0__/\_\_SUB1__&nbsp;\_\_SUB2__&nbsp;\_\_SUB3__&nbsp;\_NEW.py       | FM/MAKE/_03_00_PSG_NEW.py                           | ordered submodules 3 deep _NEW
NAME_LCL_SUBD0_SUB3_PY                       | \_\_MODULE_NAME__/\_\_SUBD0__/\_\_SUB1__&nbsp;\_\_SUB2__&nbsp;\_\_SUB3__.py                  | FM/MAKE/_03_00_PSG.py                               | ordered submodules 3 deep





***
***
***
