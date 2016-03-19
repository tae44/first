import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s' '%(message)s')

def worker():
    time.sleep(1)
    logging.debug('worker is started')


if __name__ == '__main__':
    t = threading.Thread(target=worker, name='worker')
    t.daemon = True
    t.start()
    t.join()
    logging.debug('main thread exiting')