__author__ = 'sara'

import io
import os
import re
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

# web pages that contain a full list of current faculty members
# of Syracuse Maxwell
facultyURL1 = "http://www.maxwell.syr.edu/Faculty/"
facultyURL2 = "http://www.maxwell.syr.edu/faculty_az.aspx?start=G"
facultyURL3 = "http://www.maxwell.syr.edu/faculty_az.aspx?start=M"
facultyURL4 = "http://www.maxwell.syr.edu/faculty_az.aspx?start=S"


output = open("urlList.txt", "w")
# output = io.open("urlList.txt", "w", encoding='utf8')

list = [facultyURL1,facultyURL2,facultyURL3,facultyURL4]

# set up an integer to customize the html file name
i = 1
for url in list:
    # store html data to local file
    # using wget command
    os.system('wget %s -O list%d.html' % (url,i))
    html = open("list%d.html" % i).read()

    # structure the raw data with BeautifulSoup library
    soup = BeautifulSoup(html)

    for link in soup.findAll('a'):
        # write all urls into the output txt file
        output.write("%s\n" % link.get('href'))

    i = i + 1

output.close()

# before run scraping for each single url
# manually exclude all unexpected ones from the list