#!/usr/bin/python
import lxml.etree
import urllib2
import sys

# Type './news.py' to show latest news
# Type './news.py boston bombing' to show latest news on Boston bombings or use any keywords as arguments
# I like to copy this to /usr/bin/ to make usage easier

query = '%20'.join(sys.argv[1:])
url = 'https://news.google.com/news/feeds?output=rss&num=10&q='+query
content = urllib2.urlopen(url)
parsed = lxml.etree.parse(content)
for item in parsed.xpath('.//item'):
  if len(query) > 0:
    print item[3].text + ' | ' + item[0].text.encode('ascii','replace') + '\n' + item[1].text.split('&url=')[1] + '\n'
  else:
    print item[4].text + ' | ' + item[0].text.encode('ascii','replace') + '\n' + item[1].text.split('&url=')[1] + '\n'
