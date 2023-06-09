from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import html_to_json
import json
import csv


def proofpoint(driver, json_path):
  # Navigates to Proofpoint site using SSO link
  driver.get('https://us1.proofpointessentials.com/app/login.php?do_this=azurelogin')
  time.sleep(3)
  # Clicks the User Management dropdown
  elem = driver.find_element(By.ID, 'menu_user-management')
  elem.click()
  time.sleep(3)
  # Clicks the Users link
  elem = driver.find_element(By.ID, 'nav_users')
  elem.click()
  time.sleep(3)
  # Creates a BeatifulSoup object with all HTML data with a 'tbody' tag. Returns the innerHTML so that the relevant data is populated
  soup = BeautifulSoup(driver.find_element(By.TAG_NAME, 'tbody').get_attribute("innerHTML"))
  # Cleans up the raw HTML
  pretty = soup.prettify()
  # Converts the clean HTML to JSON
  json_conversion = html_to_json.convert(pretty)
  # Creats the JSON dump with specified parameters
  json_out = json.dumps(json_conversion, indent=4)
  # Writes the JSON to a file
  with open(json_path, 'w') as outfile:
    outfile.write(json_out)
  # Opens json file and trims extra data
  with open(json_path, 'r') as file:
      data = json.load(file)
      data = data["html"]
      data = data[0]
      data = data["body"]
      data = data[0]
      data = data["tr"]
      # Creates a dictionary and adds each users jsons code as a list
      data_out = {}
      for i in range(0, len(data)):
        data_out[i] = data[i]
      # Creates another dictionary of key values with empty lists. Loops through each list index and add the appropriate value to the key
      cleaner = {'name': [], 'Inbound': [], 'Outbound': [], 'date': []}
      for i in range(0, len(data_out)):
         cleaner['name'].append(data_out[i]["td"][1]["a"][0]["_value"])
         cleaner['Inbound'].append(int(data_out[i]["td"][4]["_value"]) + int(data_out[i]["td"][5]["_value"]) + int(data_out[i]["td"][6]["_value"]) + int(data_out[i]["td"][7]["_value"]))
         cleaner['Outbound'].append(int(data_out[i]["td"][9]["_value"]) + int(data_out[i]["td"][10]["_value"]) + int(data_out[i]["td"][11]["_value"]))
         cleaner['date'].append(data_out[i]["td"][12]["_value"])
      # Creates a list of lists that include each user's information
      final = []
      for i in range(0, len(data_out)):
         final.append([cleaner["name"][i],cleaner["Inbound"][i],cleaner["Outbound"][i],cleaner["date"][i]])
      # Writes the static headers and final list to a csv
      with open('data.csv', 'w', newline='') as csvfile:
         csvwriter = csv.writer(csvfile)
         csvwriter.writerow(['Email', 'Inbound Total', 'Outbound Total', 'Date Created'])
         csvwriter.writerows(final)