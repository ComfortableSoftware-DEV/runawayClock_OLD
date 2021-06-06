# \_THIS_KEY_BASE\_

  * the text submitted from outside which is used to make sure that PySimpleGUI has ample keys available for often reused text elements
- K_STANDARD_KEY is the key everywhere except PySimpleGUI (K_STANDARD_KEY is an example, any defined key (FMAXPSG_SCTN0900_KEY_DEF, "__key__") works)
- _USE_THIS_KEY_(K_STANDARD_KEY) returns (K_STANDARD_KEY + keybase_/_THIS_KEY_BASE_) as the PySimpleGUI safe key for those elements which require such
- this is set in TBGLST when elements are defined which require them, the far left bool just before the comment
- ### code line in TBGLST setting up a foreign key, this is the whole line broken down and commented<p><p>
  * ("PSGVAL__CLOCKS_FUNC_00_INIT03_KEY01",
  *  * [useless] name given in TBGLST to keep things smooth there
  * FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY,
  *  * the FM action used to add a foreign key
"CLOCKS", "K_CHECKBOX_ALPHA_DIM", "K_CHECKBOX_ALPHA_DIM", "False", "add foreign key for alpha dimming",),
- ("PSGVAL__CLOCKS_FUNC_00_INIT03_KEY01",
-  * [useless] name used to keep everything straight in TBGLST
-  * FMAXPSG_SCTN09FF_CLASS_INIT_ADD2_FOREIGN_KEY,
-  * "CLOCKS",
-  * "K_CHECKBOX_ALPHA_DIM",
-  * "K_CHECKBOX_ALPHA_DIM",
-  * "bool is reverse entry capable using _USE_THIS_KEY_",
-  * "add foreign key for alpha dimming",),
-   *  * [useless] name used internally
-   *  *
