# script to fetch the emails of iucaa people 
# from the webpage

import requests
from bs4 import BeautifulSoup

# url = "https://www.iucaa.in/en/people/people-project-students"
# url = "https://www.iucaa.in/en/people/people-post-doctoral-fellows"
# url = "https://www.iucaa.in/en/people/people-research-scholars"
def fetch_emails(url):

    r = requests.get(url)
    # print(r.content)

    soup = BeautifulSoup(r.content, 'html.parser')

    emails = []

    for span_tag in soup.find_all('span', class_="position-italic")[1:]:
        email_id = span_tag.text
        emails.append(email_id.strip())
    
    return emails

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="enter url of iucaa webpage from which emails to be fetched")
    args = parser.parse_args()
    url = args.url
    emails = fetch_emails(url)
    print(emails)

