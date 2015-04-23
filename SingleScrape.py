__author__ = 'sara'

import os
import re
import csv
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

# expend this url for each faculty
BASE_URL = "http://www.maxwell.syr.edu"

def make_url(str):
    return BASE_URL + str

# use BeautifulSoup library to acquire raw html data from website
def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html)

# extract faculty first name and last name
def get_name(soup):

    fullName = soup.find("h1").string

    result = re.split("\s",fullName)
    countNames = len(result)
    lastName = result[countNames - 1]
    if countNames == 2:
        firstName = result[0]
    else:
        firstName = " ".join(result[:countNames-2])

    # try:
    #     result = re.split("\s",name)
    #     countNames = len(result)
    #     lastName = result[countNames - 1]
    #     if countNames == 2:
    #         firstName = result[0]
    #     else:
    #         firstName = " ".join(result[:countNames-2])
    # except:
    #     firstName = ""
    #     lastName = fullName

    return firstName, lastName

# extract faculty title and department info
def get_title_department(soup):

    match = soup.find("h2").string
    try:
        result = re.split(",\s",match)
        facultyTitle = result[0]
        facultyDept = result[1]
    except:
        print "Unable to detect title or department from: %s" % match
        facultyTitle = ""
        facultyDept = ""

    return facultyTitle, facultyDept

# extract faculty education info
def get_degree(url):
    html = urlopen(url).read()
    degree = re.search(r'(?<=</h3>\n<p>).*?(?=</p>)',html)
    if degree:
        result = re.split(", ", degree.group())
        gradSchool = result[1]

    return gradSchool


# main code
if __name__ == '__main__':

    # get expend url list from earlier cleaned file
    links = open("urlList.txt").readlines()
    count = len(links)

    facultySchool = "Syracuse"

    file = open('syracuseFaculty.csv','w')
    # file = open('syracuseFaculty.csv', 'a')
    writer = csv.writer(file)
    # write header
    writer.writerow(['First Name', 'Last Name', 'Grad School', 'Title', 'Department', 'School'])

    for i in range(145,count):
        url = make_url(links[i])
        soup = make_soup(url)

        firstName, lastName = get_name(soup)
        title, dept = get_title_department(soup)
        gradSchool = get_degree(url)

        data = [firstName,lastName,gradSchool,title,dept,facultySchool]

        # write data to csv file
        writer.writerow([data[0], data[1], data[2], data[3], data[4], data[5]])