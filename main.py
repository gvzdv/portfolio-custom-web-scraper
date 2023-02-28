# python3
# DISCLAIMER: this script is created only for training.
# All information belongs to cryptocurrencyjobs.co and won't be distributed.

from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from time import sleep

WEBSITE = "https://cryptocurrencyjobs.co/"

# Open the website using Selenium.
# In this particular case it helps load more job listings compared to scraping it with BeautifulSoup
driver = webdriver.Chrome()

# Let the browser start up, get the website and let it load for 5 sec
sleep(5)
driver.get(WEBSITE)
sleep(5)

# Get the information from the website
soup = BeautifulSoup(driver.page_source, "html.parser")

# Get job listings using relevant class (first three items are irrelevant and are cut off)
jobs = soup.find_all(class_="grid")[3:]

# Create a header for the .csv file
header = ["Job Name", "Company", "Location", "Department", "Full-Time Or Part-Time", "Link"]

# Create/open a .csv file
with open("jobs.csv", mode="w") as file:

    # Create the writer
    writer = csv.writer(file)

    # Write the header
    writer.writerow(header)

    for job in jobs:

        # From each job listing, extract relevant information
        # Replace commas with dashes and ampersands to maintain consistency in the .csv file
        job_name = job.find("h2").getText().strip().replace(",", " -")
        company_name = job.find("h3").getText().strip().replace(",", " -")
        job_location = job.find_all(class_="leading-relaxed")[0].getText().strip().replace(",", " &")
        job_role = job.find_all(class_="leading-relaxed")[1].getText().strip().replace(",", " &")
        full_or_part_time = job.find_all(class_="leading-relaxed")[2].getText().strip().replace(",", " &")
        link = "https://cryptocurrencyjobs.co" + job.find('a').get("href")

        # Create a list with the information that should populate the current row
        data = [job_name, company_name, job_location, job_role, full_or_part_time, link]

        # Write this information to the .csv file
        writer.writerow(data)
