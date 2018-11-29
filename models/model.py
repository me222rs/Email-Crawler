from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import time
import re
import random
import os


class Model:

    def __init__(self):
        print("Startar")

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def process_website(self, url, resume):
        # Set a time interval between crawls
        min_crawl_time = 7
        max_crawl_time = 10
        start_url = url
        new_urls = deque()
        processed_urls = set()
        external_urls = set()
        emails = set()

        # If you choose to resume
        if resume:
            with open('data/new_urls.txt') as file:
                for line in file:
                    new_urls.append(line.strip())

            with open('data/processed_urls.txt') as file:
                for line in file:
                    processed_urls.add(line.strip())

            with open('data/external_urls.txt') as file:
                for line in file:
                    external_urls.add(line.strip())

            with open('data/emails.txt') as file:
                for line in file:
                    emails.add(line.strip())
        else:
            new_urls = deque([start_url])
            processed_urls = set()
            external_urls = set()
            emails = set()

        while len(new_urls):
            # Save after each crawl
            self.save(emails, processed_urls, new_urls, external_urls, emails)

            self.cls()

            url = new_urls.popleft()

            if start_url in url:
                processed_urls.add(url)
                parts = urlsplit(url)
                base_url = "{0.scheme}://{0.netloc}".format(parts)
                path = url[:url.rfind('/') + 1] if '/' in parts.path else url
                print("Processing %s" % url)

                try:
                    response = requests.get(url)
                except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                    print("Connection error. Trying again in 60 minutes")
                    time.sleep(3600)
                    new_urls.append(url)
                    continue

                new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
                emails.update(new_emails)

                print("Hittade: "+str(len(new_emails))+" epostadresser")

                soup = BeautifulSoup(response.text, "html.parser")

                for anchor in soup.find_all("a"):
                    link = anchor.attrs["href"] if "href" in anchor.attrs else ''
                    if link.startswith('/'):
                        link = base_url + link
                    elif not link.startswith('http'):
                        link = path + link
                    if not link in new_urls and not link in processed_urls:
                        new_urls.append(link)
                time.sleep(random.randint(min_crawl_time, max_crawl_time))
            else:
                print("Extern url hittad: "+url)
                external_urls.add(url)

    # Saves everything
    def save(self, emails, processedURLs, newURLs, externalURLs, emailAdresses):
        print("Sparar...")
        if emailAdresses:
            emails = emailAdresses

        with open("Output.txt", "w") as text_file:
            for item in emails:
                text_file.write(item+"\n")

        with open("data/processed_urls.txt", "w") as text_file:
            for item in processedURLs:
                text_file.write(item+"\n")

        with open("data/external_urls.txt", "w") as text_file:
            for item in externalURLs:
                text_file.write(item+"\n")

        with open("data/new_urls.txt", "w") as text_file:
            for item in newURLs:
                text_file.write(item+"\n")

        with open("data/emails.txt", "w") as text_file:
            for item in emailAdresses:
                text_file.write(item+"\n")