
#Sources(Main)
#https://dvenkatsagar.github.io/tutorials/python/2015/10/26/ddlv/
#https://stackoverflow.com/questions/46753393/how-to-make-firefox-headless-programatically-in-selenium-with-python

# The standard library modules
import os
import sys
import re
import time
# The wget module
import wget

# The BeautifulSoup module
from bs4 import BeautifulSoup

# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

print("Now chia-anime site will open up.Please search and enter the episode's address\n")
time.sleep(10);

driver = webdriver.Firefox() # if you want to use chrome, replace Firefox() with Chrome()
driver.get("http://m1.chia-anime.tv/") # load the web page
raw_input("Press Enter to after copying the link...")
driver.close()

link = raw_input("Enter the link of the stating episode\n")
n= int(input("\nEnter the ending episode no.\n"))

#Defining main download function
def Download(link):
	#Invoking headless Firefox
	options = Options()
	options.add_argument("--headless")
	driver = webdriver.Firefox(firefox_options=options)
	print("Firefox Headless Browser Invoked")
	driver.get(link)

	# for websites that need you to login to access the information
	#elem = driver.find_element_by_id("email") # Find the email input field of the login form
	#elem.send_keys("user@example.com") # Send the users email
	#elem = driver.find_element_by_id("pwd") # Find the password field of the login form
	#elem.send_keys("userpwd") # send the users password
	#elem.send_keys(Keys.RETURN) # press the enter key

	#driver.get("http://www.example.com/path/of/video/page.html") # load the page that has the video

	WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "video"))) # waits till the element with the specific id appears
	src = driver.page_source # gets the html source of the page

	parser = BeautifulSoup(src,"lxml") # initialize the parser and parse the source "src"
	#list_of_attributes = {"name" : ".mp4"} # A list of attributes that you want to check in a tag
	tag = parser.findAll('a', attrs={'href': re.compile("^http://luffy.chia-anime.tv")}) # Get the video tag from the source
	print tag[0];
	n = 0 # Specify the index of video element in the web page
	url = tag[n]['href'] # get the src attribute of the video
	wget.download(url,out="/home/sudipta/Downloads") # download the video

	driver.close() # closes the driver
#Finding out te episode no. of the inserted link
def FirstEpi(link):
	pos=link.find("episode")
	res=link[pos:]
	pos1=res.find("-")
	#print res[pos1+3]
	if(res[pos1+2]=="/"):
		res1=res[pos1+1:pos1+2]
	elif(res[pos1+3]=="/"):
		res1=res[pos1+1:pos1+3]
	elif(res[pos1+4]=="/"):
		res1=res[pos1+1:pos1+4]
	a=int(res1)					#converting string to int
	return a

Download(link)
i=FirstEpi(link)
i=i+1

while (i<=n):
	x=i-1
	x=str(x)
	prev="episode-"+x
	y=i
	y=str(y)
	next="episode-"+y
	link=link.replace(prev,next)
	Download(link)
	i=i+1
