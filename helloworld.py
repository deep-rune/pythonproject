if __name__ == "__main__":

import tornado.ioloop
import tornado.web
import requests
from bs4 import BeautifulSoup


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is the index context route")


class HelloWorld(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World, fellow pythonistas!")


class PruneHandleHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Don't Request The Prune")

    def post(self):
        if self.request.body:
            self.json_data = tornado.escape.json_decode(self.request.body)
            self.write(self.json_data)


app = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/helloworld", HelloWorld),
    (r"/prunehandle", PruneHandleHandler)
])

URL = "https://www.bbc.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    print(job_element, end="\n"*2)

# app.listen(8080)
# tornado.ioloop.IOLoop.current().start()
