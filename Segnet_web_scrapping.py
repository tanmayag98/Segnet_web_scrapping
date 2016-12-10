import urllib
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException        
import sys

if len(sys.argv)<6:
	print "ERROR!!"
	print "Command line format = python Segnet_web_scrapping.py lower_limit upper_limit step input_dir_path output_dir_path" 
	sys.exit()

b = webdriver.Firefox()
ll = int(sys.argv[1])
ul = int(sys.argv[2])
step = int(sys.argv[3])
inp_b = sys.argv[4]
out_b = sys.argv[5]
n=ll

def check_exists_by_xpath(xpath):
    try:
        b.find_element_by_name(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_id(path):
    try:
        b.find_element_by_id(path)
    except NoSuchElementException:
        return False
    return True

def upload(line,out):
	ele=b.find_element_by_id("file1")
	ele.send_keys(line)
	time.sleep(20)
	print "Estimated time left :"+str((ul-n)*20/(60*step))+" min"
	while not check_exists_by_id("result_image"):
		print "loading" 
	if check_exists_by_id("result_image"):
		img = b.find_element_by_id("result_image")
		src = img.get_attribute('src')
		urllib.urlretrieve(src, out)

b.get('http://mi.eng.cam.ac.uk/projects/segnet/#demo')	
print "Website opened"
for n in range(ll,ul,step):
	inp =inp_b + str(n)+".jpeg"
	out =out_b + str(n)+".jpeg"
	if(check_exists_by_xpath("file1")):
		print "uploading "+inp
		upload(inp,out)
	elif(check_exists_by_xpath("restart")):
		b.find_element_by_name("restart").click()
		time.sleep(3)
		upload(inp,out)
