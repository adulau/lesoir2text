#!/usr/bin/python
#
# lesoir.be website sucks with all the advertising and
# if you want to read on your Kindle, this is a disaster.
#
# The following script fetch the most read article from lesoir.be
# (from their official sitemap) and make an ascii text file of
# all the articles with the junk removed.
#
# lesoir2text uses standard Python libraries + lynx for the text conversion
#
# The script is in the public domain.
#
# Author: Alexandre Dulaunoy - http://www.foo.be/
#
# You can use sendKindle to send it directly to your Kindle
# https://github.com/kparal/sendKindle
#
# To use it : python lesoir2text.py >lesoir-`date +%Y%m%M`.txt

try:
  from lxml import etree
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
        except ImportError:
          print("Failed to import ElementTree from any known place")

import urllib2
import os.path
from urlparse import urlparse
import re
import sys

# require lynx
import TextFormat

max = 15
toplesoir = "http://www.lesoir.be/sitemap-mostread.xml"

sock = urllib2.urlopen(toplesoir)

#etree.set_default_parser(etree.XMLParser(dtd_validation=False, load_dtd=False, no_network=False))
tree = etree.parse(sock)

def FetchPage (url=None):
    sock = urllib2.urlopen(url)
    lpage = sock.read()
    sock.close()
    return lpage


def RemoveJunk (page=None):
    toggleview = False
    toprint = []
    for line in page.split('\n'):
        if re.search (" Tweet", line):
             toggleview = not toggleview
        if toggleview is True:
             toprint.append(line)
    return "\n".join(toprint)

i = 0

for parent in tree.getiterator():
        for child in parent:
            if i==max:
                break
            if child.tag == '{http://www.google.com/schemas/sitemap/0.84}loc':
                i=i+1
                sys.stderr.write("Fetching... "+child.text)
                x=urlparse(child.text)
                path = os.path.split(x[2])
                article=FetchPage(child.text)
                x = TextFormat.TextFormatter()
                txtarticle = x.html2text( article )
                print "----\n"
                print RemoveJunk(txtarticle[0])
sock.close()
