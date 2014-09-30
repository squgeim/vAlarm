vAlarm
===

timer.py
--
Basically, this script lets you run any command or script at a given date and time.

Usage:
./timer.py yyyy:mm:dd hh:mm:ss command


vAlarm.py
--
This script uses timer.py and VLC to play a given file, playlist or folder at a given time. You can use this as a musical alarm.

Usage:
./vAlarm.py yyyy:mm:dd hh:mm:ss /path/to/file

Dependency
--
Obviously, you'll need VLC; and of course python and a shell.
Tested and developed with Bash and Python 2.7.5, on Fedora 20.
