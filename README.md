This code takes your well made C code and makes it unmaintainable. 
This is based on Droogan's How To Write Unmaintainable Code. https://github.com/Droogans/unmaintainable-code/blob/master/README.md

Watch your code become garbage!

Dependencies:
	Python 3.7.X
	pip modules: pycparser, click, pymysql

Run python3 beautify.py yourfile.c (only works on singular files and will break if there are mutiple .c files with headers and stuff)

Use flags such as --probability X from 0 to 100 to specify probability of garbage
				  --optimize X from 0 to 100 to optimize your code more!!11!!

This code uses a MySql database to grab variable and function replacements as well as comments.  We didn't include the login so make ur own in
'dev_settings.py'


Email none of us for problems thanks


S/o to vthacks for the boneless bizza and monster
