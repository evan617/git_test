#!/usr/bin/env python

import threading, time
import Queue
import random

q = Queue.Queue()

def Producer(name):
	for i in range(20):
		q.put(i)
		print '\033[32;1mProducer %s has made %s baozi..\033[0m' % (name, i)
		time.sleep(random.randrange(2))

def Consumer(name):
	count = 0
	while count < 20:
		data = q.get()
		print '\033[31;1mConsumer %s has eaten %s baozi...\033[0m' % (name, data)
		count +=1
		time.sleep(random.randrange(4))

p = threading.Thread(target=Producer, args=('evan',))
c = threading.Thread(target=Consumer, args=('lin', ))

p.start()
c.start()
