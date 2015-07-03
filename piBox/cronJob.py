import os
import sys
import time  
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler
from connect import *


path = ''

class MyHandler(PatternMatchingEventHandler):
    ignore_patterns = [".DS_Store", "*swp", "*~"]


    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there

        f = open('count.txt', 'r+')
        now = [name for name in os.listdir(path) \
            if os.path.isfile(os.path.join(path, name))]
        if event.event_type is 'created':
            connect(event.src_path.split('/')[-1])
        prev = [each for each in f.readlines()]
        if len(prev) > len(now):
            for each in list(set(prev) - set(now)):
                connect(each.strip('\n'), remove=True)

        string = ''
        for each in now:
            string += each+'\n'
        f.seek(0)
        f.write(string)
        f.close()



    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

if __name__ == '__main__':
    observer = Observer()
    path = os.getcwd().split('/')
    path = '/'.join(path[:-1])+'/Box/'
    observer.schedule(MyHandler(), path)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
