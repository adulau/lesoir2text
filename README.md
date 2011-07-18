lesoir2text
===========

lesoir.be website sucks with all the advertising and
if you want to read on your Kindle, this is a disaster.

The following script fetch the most read article from lesoir.be
(from their official sitemap) and make an ascii text file of
all the articles with the junk removed.

lesoir2text uses standard Python libraries + lynx for the text conversion

The script is in the public domain.

Author: Alexandre Dulaunoy - http://www.foo.be/

You can use sendKindle to send it directly to your Kindle
https://github.com/kparal/sendKindle

Usage
-----

      python lesoir2text.py >lesoir-`date +%Y%m%M`.txt


