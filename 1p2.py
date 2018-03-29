
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
import requests
import urllib2
import re

print("Now chia-anime site will open up.Please search and enter the episode's address\n.To continue press enter or or anyother key to skip")
text=raw_input("")
if text=="":
	time.sleep(5);
	try:
		driver = webdriver.Firefox() # if you want to use chrome, replace Firefox() with Chrome()
		driver.get("http://m1.chia-anime.tv/") # load the web page
	except:
		pass
else:
	pass
raw_input("Press Enter to after copying the link...")
#driver.close()
link = raw_input("Enter the link of the stating episode\n")	
print link
n= int(input("\nEnter the ending episode no.\n"))
#save files directory
direc=raw_input("Enter the full directory where you want to save the files.\n")
#Defining main download function
def Download(link):
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
	soupeddata = BeautifulSoup(src, "html.parser")
	links=[]
	for link in soupeddata.findAll('a', attrs={'href': re.compile("^http://")}):
		links.append(link.get('href'))
	#print link[2];
	n = 2 # Specify the index of video element in the web page
	url = links[n] # get the src attribute of the video
	wget.download(url,out=direc) # download the video

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

array=[]

while (i<=n):
	try:
		x=i-1
		x=str(x)
		prev="episode-"+x
		y=i
		y=str(y)
		next="episode-"+y
		link=link.replace(prev,next)
		Download(link)
	except:
		array.append(y)
	i=i+1

if len(array)>0:
	print("The failed download episodes are:\n")
	print array
