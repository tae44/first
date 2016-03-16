import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class Myhandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == '/Users/a123/Desktop/456.txt':
            print('file {} is changed!'.format(event.src_path))

if __name__ == '__main__':
    event_handler = Myhandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
