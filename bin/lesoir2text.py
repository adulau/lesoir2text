
# lesoir.be website sucks with all the advertising and
# if you want to read in your Kindle, this is a disaster.
#
# The following script fetch the most read article from lesoir.be
# and make an ascii text-file to read with some comfort the news on your Kindle.
#

from lxml import etree
import urllib2
import os.path
from urlparse import urlparse
import re
#import BeautifulSoup
# Non core modules
# 'easy_install stripogram'
#from stripogram import html2text
#import html2text

import TextFormat

max = 3
toplesoir = "http://www.lesoir.be/sitemap-mostread.xml"

sock = urllib2.urlopen(toplesoir)

etree.set_default_parser(etree.XMLParser(dtd_validation=False, load_dtd=False, no_network=False))
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
                print "Fetching... "+child.text
                x=urlparse(child.text)
                path = os.path.split(x[2])
                article=FetchPage(child.text)
                x = TextFormat.TextFormatter()
                txtarticle = x.html2text( article )
                print RemoveJunk(txtarticle[0])

sock.close()
