import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

search = input("What kind of job are you looking for?\n")

# Search h2 tag for the search keyword. Lambda function is for case sensitivity
python_jobs = results.find_all("h2", string=lambda text: search in text.lower())

# List comprehension the returns the third parent element information. This includes all needed data
python_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Iterate through search results list and formats
for job_element in python_jobs_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    links = job_element.find_all("a")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        if link_url != "https://www.realpython.com":
          print(f"Apply here: {link_url}\n")
    print()

