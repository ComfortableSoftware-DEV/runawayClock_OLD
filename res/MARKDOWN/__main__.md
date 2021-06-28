# RUNAWAY CLOCK

  * ## CF

    * ### APPDS_C.py

    * ### CF_DAYS.py
      * days of the week flags 
      * ##### DAYS_mtwtfss = 0b00000000 
      * ##### DAYS_MTWTFSS = 0b01111111
        * ###### Monday Tuesday Wednesday Thursday Friday Saturday Sunday
        CAPITALIZED for included in the flag, not capitalized for not included in the flag</span>

    * ### \_00_PKL_C.py
      * ### PKL_C(object):

        * #### \_\_init__
          * ##### self
          * ##### pklFilename_
          the filename for the pkl file, with full path
          * ##### stuffToPkl_
          the dictionary to pickle, "K_VERSION: 0" will be added if not present
          * ##### RETURNS None

        * #### \_\_exit__
          * ##### self

        * #### incVersion
          * ##### self
          * ##### versionIn_
          int or 8 digit hex string to be incremented<br>
          CF.SRI_C.py also allows a key in the \_SERIALZ_ dict to be used and will default to \_\_KEY__ if no other info is added
          * ##### RETURNS incremented value

        * #### pickleIt
          * ##### self
          * ##### filename_
          full path to the pkl file
          * ##### dataToPickle_
          the dict to pickle, will have "K_VERSION: 0," added if not present
          * ##### RETURNS None

        * #### unPickleIt
          * ##### self
          * ##### filename_
          filename to be read<br>
          

          



  * ## FM
  * ## PSG
