import sys
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

download_dir = r"/Users/VPDiddy/Desktop/Ecra"
# r”C:\Users\pathtodir” where C is the harddrive name for windows
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : download_dir}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://hydrology.cee.duke.edu/POLARIS/PROPERTIES/v1.0/bd/mean/0_5/")

# Rest of your code...


#error message if url not specified in command line
#if len(sys.argv) < 2:
 #   print("Please provide a URL as a command line argument in form python3 script.py url.")
#    sys.exit(1)

#url = sys.argv[1] #uncomment for command line arguments

# Navigate to the ftp server url
#driver.get("http://hydrology.cee.duke.edu/POLARIS/PROPERTIES/v1.0/bd/mean/0_5/")
#driver.get(url) #uncomment for command line arguments

#in the event that ftp server requires password and username
#username and password elements and enter the credentials, not tested
#username = driver.find_elements(By.ID, "username")
#password = driver.find_elements(By.ID, "password")
#username.send_keys("mylogin")
#password.send_keys("mypass")

#login button
#login = driver.find_elements(By.ID, "login")
#login.click()

#function to traverse the file structure iteratively
def traverse_iterative():
    #create an empty stack and push the root url
    stack = ["http://hydrology.cee.duke.edu/POLARIS/PROPERTIES/v1.0/bd/mean/0_5/"]
    #stack = [url]
    #repeat until the stack is empty
    while stack:
        #pop a url from the stack
        url = stack.pop()
        # Navigate to the url
        driver.get(url)
        #find all the links in the current directory
        links = driver.find_elements(By.TAG_NAME, "a")
        count = 0
        #loop through each link
        for link in links:
            #get the text and href attributes of the link
            text = link.text
            href = link.get_attribute("href")
            #if the link is a file, download it by clicking on it
            if text.endswith(".nc"): #or text.endswith(".pdf") or text.endswith(".zip"):
                link.click()
                print("downloaded")
                print(text)
        
                
            #if the link is a directory, push it onto the stack
            elif text.endswith("/"):
                stack.append(href)
                print(text," was added to stack ")
            #ignore the link
            else:
                pass

#call the function
traverse_iterative()

#driver.close() terminates program earlier
#program terminates when stack is empty