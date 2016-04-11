import json
import time
from tornado.web import RequestHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.log import app_log


class ArgumentHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello {}'.format(self.get_argument('name')))


class Argumentshandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello {}'.format(','.join(self.get_arguments('name'))))


class BodyHandler(RequestHandler):
    def post(self, *args, **kwargs):
        body = json.loads(self.request.body.decode())
        app_log.warning(self.request.body.decode())
        self.write('hello {}'.format(body['name']))


class PathArgsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello {}'.format(args[0]))


class PathKwargsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello {}'.format(kwargs['name']))


class RemoteIpHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello {}'.format(self.request.remote_ip))


class FobiddenHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(403)
        self.write('forbidden')


class CustomStatusHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(498, reason='custom error')


class HeaderHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.add_header('X-Header', 'xxxxx')
        self.add_header('x-header', 'yyyyy')
        self.write('hello')


class MultiWriteHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('start\n')
        self.flush()
        for i in range(10):
            self.write('{}\n'.format(i))
            self.flush()
            time.sleep(0.1)
        self.finish('complete')


if __name__ == '__main__':
    app = Application(
        [
            (r'/', ArgumentHandler),
            (r'/args', Argumentshandler),
            (r'/body', BodyHandler),
            (r'/path/args/(.*)', PathArgsHandler),
            (r'/path/kwargs/(?P<name>.*)', PathKwargsHandler),
            (r'/ip', RemoteIpHandler),
            (r'/403', FobiddenHandler),
            (r'/498', CustomStatusHandler),
            (r'/head', HeaderHandler),
            (r'/multi', MultiWriteHandler)
        ]
    )
    app.listen(port=8000, address='0.0.0.0')
    IOLoop.current().start()
