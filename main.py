# importing Dependencies 
import cloudscraper
import requests
from bs4 import BeautifulSoup
import csv
# creating scraper from cloudscraper
url = 'https://in.indeed.com/jobs?q=python+developer&l=Mumbai%2C+Maharashtra&from=searchOnHP'
scraper = cloudscraper.create_scraper()
response = scraper.get(url)
# # working with BeautifulSoup
soup = BeautifulSoup(response.text,'html.parser')

# Finding All Joblists
job_list = soup.find_all('li',class_="css-5lfssm eu4oa1w0")


for job in job_list:
    job = soup
    title = job.find('a',class_='jcs-JobTitle css-jspxzf eu4oa1w0').text.strip()
    company_name = job.find('span',class_='heading6 company_location tapItem-gutter companyInfo').text.strip()
    company_location = job.find('div',class_='heading6 company_location tapItem-gutter companyInfo').text.strip()
    summary = job.find('div',class_='job-snippet').text.strip()
    try:
        salary = job.find('div',class_='attribute_snippet').text.strip()
    except AttributeError:
        salary = 'Not disclosed'

    print("Title:",title)
    print("CompanyName:",company_name)
    print('CompanyLocation:',company_location)
    print('Salary:',salary)
    print('Summary:',summary)
    print("=" * 30)
