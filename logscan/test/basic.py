# -*- coding: utf-8 -*-
import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')


def worker(message):
    time.sleep(2)
    logging.debug("worker is started, {0}".format(message))


if __name__ == '__main__':
    t = threading.Thread(target=worker, name='worker', kwargs={'message': 'ha ha ha'})
    t.daemon = True
    t.start()
    t.join() # 主线程会等待所有子线程执行完毕后一起返回,可以设置超时时间
    logging.debug('main thread exiting')