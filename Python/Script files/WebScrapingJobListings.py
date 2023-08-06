import requests
from bs4 import BeautifulSoup
import csv

'''Build a web scraper that extracts job listings from a job 
search website, such as Indeed or LinkedIn. The program can use 
libraries like BeautifulSoup and requests to parse the HTML 
content and collect job information, such as job title, company, 
location, and application link. It can save the data in a CSV 
file for further analysis.'''

def scrape_job_listings(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    job_listings = soup.find_all("div", class_="job-listing")

    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["Title", "Company", "Location", "Link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for job in job_listings:
            title = job.find("h2").text.strip()
            company = job.find("p", class_="company").text.strip()
            location = job.find("p", class_="location").text.strip()
            link = job.find("a")["href"]
            writer.writerow({"Title": title, "Company": company, "Location": location, "Link": link})

# Usage example
url = "https://example.com/jobs"
output_file = "job_listings.csv"
scrape_job_listings(url, output_file)
