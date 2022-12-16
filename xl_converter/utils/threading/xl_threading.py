"""xl_threading.py

Portable multithreading utility designed to speed up repetitive file
management tasks.
"""

# maybe thread this??

## use manifes to identify multiple threads
## max threadcount from config
## if a thread is available, then the process will run in a separate thread.
## if the thread is not available, the process will be added to a queue.
## the data are processed in batches; once a batch is complete, the
## program will poll the task queue again and reestablish the threads
## close out all old threads and reassign

import logging
import queue
import subprocess
import threading
import time
