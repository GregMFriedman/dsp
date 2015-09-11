# Hint:  use Google to find python function

from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_format = "%m-%d-%Y"
a = datetime.strptime(date_start, date_format)
b = datetime.strptime(date_stop, date_format)
delta = b - a
print "a) " + str(delta.days)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_format = "%m%d%Y"
a = datetime.strptime(date_start, date_format)
b = datetime.strptime(date_stop, date_format)
delta = b - a
print "b) " + str(delta.days)


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_format = "%d-%b-%Y"
a = datetime.strptime(date_start, date_format)
b = datetime.strptime(date_stop, date_format)
delta = b - a
print "c) " + str(delta.days)