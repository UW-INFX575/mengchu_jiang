__author__ = 'sara'

import os
import re
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

if (os.path.isfile("AAllport.html") != True):
    URL = "https://www.maxwell.syr.edu/hist/Maxwell_School__Alan_Allport,_Assistant_Professor,_History/"
    os.system('wget %s -O AAllport.html' % URL)
html = open("AAllport.html").read()
soup = BeautifulSoup(html)

fullName = soup.find("h1").string
try:
    result = re.split("\s",fullName)
    countNames = len(result)
    lastName = result[countNames - 1]
    if countNames == 2:
        firstName = result[0]
    else:
        firstName = " ".join(result[:countNames-2])
except:
    firstName = ""
    lastName = fullName

match = soup.find("h2").string
try:
    result = re.split(",\s",match)
    facultyTitle = result[0]
    facultyDept = result[1]
except:
    print "Unable to detect title or department from: %s" % match
    facultyTitle = ""
    facultyDept = ""

degree = re.search(r'(?<=</h3>\n<p>).*?(?=</p>)',html)
if degree:
    result = re.split(", ", degree.group())
    gradSchool = result[1]

facultySchool = "Syracuse"
data = [firstName,lastName,gradSchool,facultyTitle,facultyDept,facultySchool]

print data
#
# output :
# [u'Alan', u'Allport', 'University of Pennsylvania', u'Assistant Professor', u'History', 'Syracuse']
#