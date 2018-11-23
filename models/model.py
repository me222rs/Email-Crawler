from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import time
import re
import random
from itertools import repeat


class Model:
    def __init__(self):
        print("Inne i model")

    def process_website(self, url, resume):
        # Sätt tidsintervall mellan varje crawl
        min_crawl_time = 7
        max_crawl_time = 10

        # If you choose to resume
        if resume:
            print("Återupptar")

            start_url = url

            new_urls = deque([start_url])

            processed_urls = set()
            external_urls = set()

            emails = set()
        else:
            start_url = url

            new_urls = deque([start_url])

            processed_urls = set()
            external_urls = set()

            emails = set()

        while len(new_urls):
            # Save after each crawl
            self.save(emails, processed_urls, new_urls, external_urls, emails)

            time.sleep(random.randint(min_crawl_time, max_crawl_time))
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

                print(new_emails)

                soup = BeautifulSoup(response.text, "html.parser")

                for anchor in soup.find_all("a"):
                    link = anchor.attrs["href"] if "href" in anchor.attrs else ''
                    if link.startswith('/'):
                        link = base_url + link
                    elif not link.startswith('http'):
                        link = path + link
                    if not link in new_urls and not link in processed_urls:
                        new_urls.append(link)
            else:
                print("Extern url hittad: "+url)
                external_urls.add(url)

    def result(self, emails):
        print("----- Klar -----")
        print("Epost-adresser: " + str(len(emails)))
        # print("Urler skannade: " + str(len(processed_urls)))
        # print("Totalt antal urler: " + str(len(processed_urls) + len(emails)))
        print("Tid: ")
        self.save(emails)

    # Saves everything
    def save(self, emails, processedURLs, newURLs, externalURLs, emailAdresses):
        print("Saving")
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
