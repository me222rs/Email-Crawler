from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import time
import re


class Model:
    def __init__(self):
        print("Inne i model")

    def process_website(self):
        start_url = ""

        new_urls = deque([start_url])

        processed_urls = set()
        external_urls = set()

        emails = set()

        while len(new_urls):
            self.save(emails, False)
            time.sleep(5)
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
            if not new_urls:
                self.result(emails, processed_urls, True)

    def result(self, emails):
        print("----- Klar -----")
        print("Epost-adresser: " + str(len(emails)))
        # print("Urler skannade: " + str(len(processed_urls)))
        # print("Totalt antal urler: " + str(len(processed_urls) + len(emails)))
        print("Tid: ")
        self.save(emails)

    def save(self, emails, test):
        print(emails)
        print(test)