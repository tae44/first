from japen_buy import buy2
from japen_buy import tornado_test

if __name__ == '__main__':
    # tornado_test.application.listen(8888)
    # tornado_test.tornado.ioloop.IOLoop.instance().start()
    # tornado_test.tornado.ioloop.IOLoop.instance().stop()
    j = buy2.Japen()
    while True:
        j.enter_data()
