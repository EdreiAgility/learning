import tornado.ioloop
import tornado.web
import json
import zmq

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        response = "Hello World...with added text"
        self.write(response)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),

    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(5008)
    tornado.ioloop.IOLoop.current().start()

