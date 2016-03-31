import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, {0} (in {1})'.format(std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Th-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Th-B')
t1.start()
t2.start()
t1.join()
t2.join()
