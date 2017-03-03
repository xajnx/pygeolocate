# pygeolocate v0.1

Pygeolocate is a python script which will retrieve geolocation information. It was
inspired while hunting for geocaches. It is my "head-first" dive into the Python 
scripting language. Future revisions will improve the help banner,  add exception 
handling, include searches for other countries (currently US only), and possibly 
a widgit-style gui in GTK+

purpose: Enter address and return lat,lng or enter lat,lng and return address.

usage: pylocate [-h] [-g GEO] [-a ADD]

examples:
pylocate.py -a "South Wacker Drive, Chicago, IL"
Approximate geotag:  41.8780797 -87.63666889999999

pylocate.py -g "41.8780797,-87.63666889999999"
Approximate address:  233 S Wacker Dr, Chicago, IL 60606, USA
