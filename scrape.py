if __name__ == "__main__":

import requests
from bs4 import BeautifulSoup


class WebScraperService():
    def __init__(self, URL, htclass, keyword):
        self.URL = URL
        self.htclass = htclass
        self.keyword = keyword
        self.page = requests.get(URL)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def testresults(self):
        results = self.soup.find_all(self.htclass, class_=self.keyword)
        print(len(results))


new = WebScraperService("http://www.thonk.co.uk", "li", "product")
new.testresults()
