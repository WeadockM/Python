from proofPoint import proofpoint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

#O365 Authentication
directory = os.getcwd()
json_path = str(directory) + '/json.json'
username = input('Username: ')
password = input('Password: ')
options = webdriver.EdgeOptions()
options.add_argument("InPrivate")
options.add_argument("--headless")
driver = webdriver.Edge(options=options)
driver.get('https://www.office.com/login?es=Click&ru=%2F&msafed=0')
time.sleep(2)
elem = driver.find_element(By.NAME, 'loginfmt')
elem.send_keys(username)
elem.send_keys(Keys.RETURN)
time.sleep(3)
elem = driver.find_element(By.NAME, "passwd")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
time.sleep(3)
elem = driver.find_element(By.ID, 'idBtn_Back')
elem.click()
time.sleep(3)


#Function Calls

proofpoint(driver, json_path)
os.remove(json_path)