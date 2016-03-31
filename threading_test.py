import time, threading, multiprocessing

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop)
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


# def loop():
#     print('process {} is running...'.format(multiprocessing.current_process().name))
#     n = 0
#     while n < 5:
#         n += 1
#         print('process {0} >>> {1}'.format(multiprocessing.current_process().name, n))
#         time.sleep(1)
#     print('process {} ended.'.format(multiprocessing.current_process().name))
#
#
# print('process {} is running...'.format(multiprocessing.current_process().name))
# p = multiprocessing.Process(target=loop)
# p.start()
# p.join()
# print('process {} ended.'.format(multiprocessing.current_process().name))
