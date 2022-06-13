import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is the index context route")

class HelloWorld(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World, fellow pythonistas!")

class PruneHandleHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Don't Request The Prune")

app = tornado.web.Application([
    (r"/",IndexHandler),
    (r"/helloworld",HelloWorld),
    (r"/prunehandle",PruneHandleHandler)
])
app.listen(8080)
tornado.ioloop.IOLoop.current().start()
