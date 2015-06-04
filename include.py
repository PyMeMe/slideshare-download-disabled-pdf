import requests 
import os
from os import path
from lxml import html
def listoffiles(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        subindent = ' ' * 4 * (level + 1)
        return files
def parser( str ):
	print "parsing "+ str
	response = requests.get(str)
	parsed_body = html.fromstring(response.text)
	urls= parsed_body.xpath('//img[@class="slide_image"]/@data-full') #
	allurls=[]
	for index, item in enumerate(urls):
		(base, opt) = item.split('?',1)
		allurls.append(base)
        i=index
   	return allurls,(i+1)