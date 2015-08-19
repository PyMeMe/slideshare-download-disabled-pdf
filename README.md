

Installing dependency
=====================
$sudo pip install img2pdf

$sudo pip install PyPDF2

$sudo apt-get install libxml2-dev libxslt-dev

$sudo pip install lxml

Usage
=====================

    $python slideshare.py -h
    

Usage: 
 slideshare.py -u url -f output
	
    optional arguments:
    -h, --help  show this help message and exit
    -u ,--url   Type the URL of slideshare report
    -f ,--flile output report name

Example
=======
	 
    root@boox:~# python slideshare.py -u http://www.slideshare.net/sandeepsaini001/complete-guide-to-become-an-ethical-hacker -f ethical-hacker.pdf


	parsing http://www.slideshare.net/sandeepsaini001/complete-guide-to-become-an-ethical-hacker
	84 slides found
	Begin download slides : Please wait ...
	End Download
	Begin convert slides to pdf file
	End  convert to pdf
	File saved at /root/Desktop/slideshare download disabled pdf/ethical-hacker.pdf

    
