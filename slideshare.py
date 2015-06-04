import sys, getopt
import os
import signal
from os import path
import shutil
import urllib2, urllib 
import img2pdf
import time
from PyPDF2 import PdfFileMerger, PdfFileReader
from include import parser, listoffiles
class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    YELLOW = '\033[33m'

    def disable(self):
        self.OKGREEN = ''
        self.FAIL = ''
        self.ENDC = ''
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)


def run():
	directoryimg="/tmp/img"
	directorypdf="/tmp/pdf"
	directoryworking= os.getcwd()

	(listurl,lenlisturl)=parser(url)
	print str(lenlisturl)+" slides found"
	if not os.path.exists(directoryimg):
		os.makedirs(directoryimg)
	else :
		shutil.rmtree(directoryimg)
		os.makedirs(directoryimg)
	if not os.path.exists(directorypdf):
		os.makedirs(directorypdf)
	else :
		shutil.rmtree(directorypdf)
		os.makedirs(directorypdf)

	print "Begin download slides : Please wait ..."

	for index, item in enumerate(listurl):
	       os.system('wget -q -P /tmp/img %s 2>&1 >/dev/null'%item)

	print "End Download"
	print "Begin convert slides to pdf file"
	files = listoffiles(directoryimg)

	for index, item in enumerate(files):
		pdf_bytes = img2pdf.convert([directoryimg+"/"+item])
		(base, ext) = item.split('.',1)
		itempdf=directorypdf+"/"+base+".pdf"
		file = open(itempdf,"a")
		file.write(pdf_bytes)
		file.close()
	merger = PdfFileMerger()
	files = [x for x in os.listdir(directorypdf) if x.endswith('.pdf')]
	for fname in sorted(files):
	    merger.append(PdfFileReader(open(os.path.join(directorypdf, fname), 'rb')))

	merger.write(filename)
	print "End  convert to pdf"
	print "File saved at "+directoryworking+"/"+filename

def logo():
    hello = """
   ___ _                 _____ _ _     _ 
  / __\ |__   ___  _   _|___ /(_) |__ / |
 / /  | '_ \ / _ \| | | | |_ \| | '_ \| |
/ /___| | | | (_) | |_| |___) | | |_) | |
\____/|_| |_|\___/ \__,_|____/|_|_.__/|_|
"""
    print(bcolors.YELLOW + hello + bcolors.ENDC)
    now = time.strftime("%c")
def main(argv):
   global url
   url=""
   global filename
   filename=""
   try:
      opts, args = getopt.getopt(argv,"hu:f:",["url=","file="])
   except getopt.GetoptError:
      print 'Usage: \n slideshare.py -u <url> -f <output pdf  name>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'Usage: \n slideshare.py -u <url> -f <output pdf  name>'
         sys.exit(2)
      elif opt in ("-u", "--url"):
         url = arg
      elif opt in ("-f", "--file"): 
         filename = arg
if __name__ == "__main__":
	logo()
	url = ""
	filename = ""
   	main(sys.argv[1:])
   	signal.signal(signal.SIGINT, signal_handler)
   	run()
	