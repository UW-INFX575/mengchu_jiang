import re
import os

txt = open("filename")
file = txt.read()

title = re.search('<title>(.*)</title>', file)

>>> title = re.search('<title>(.*)</title>', file)
>>> title
<_sre.SRE_Match object; span=(346, 419), match='<title>Jevin West | Information School | Universi>

title = re.search(r'(?<=<title>).*?(?=\s)',file)
title = re.search(r'(?<=<title>).*?(?=</title>)',file)

# title = re.search('<title>(.*)</title>', file, re.IGNORECASE).group(1)

>>> title = re.search(r'(?<=<h1>).*?(?=</h1>)',file)
>>> title
<_sre.SRE_Match object; span=(10082, 10097), match='Kristi Andersen'>
<_sre.SRE_Match object; span=(9509, 9527), match='Elizabeth F. Cohen'>
