# music_sanitizer
Cleanse media filename and correct metadata

usage: RN.py [-h] [-d _DELETE] [-r REPLACE] dir

Mp3 and FLAC filename fixer

positional arguments:
  dir                   File directory, full path

optional arguments:
  -h, --help            show this help message and exit
  -d _DELETE, --delete _DELETE
                        Strings to delete, separated by comma. E.g.:
                        Frank,Sinatra,delete,this,message
  -r REPLACE, --replace REPLACE
                        Strings to replace, separated by comma, match:replace
                        separated by colon. E.g.:
                        change:to,ALBUM:album,replace:Replace
