from threading import Thread
import random


array = []

for i in range(200):
    array.append(i)

def maker():
	while True:
			array.append(random.randint(1, 100))
			
def consumer():
	while True:
			del (array[-1])
			print(array)

if len(array) >= 100:
	consumer1 = Thread(target=consumer).start()
	consumer2 = Thread(target=consumer).start()
if len(array) <= 80:
	maker1 = Thread(target=maker).start()
	maker2 = Thread(target=maker).start()
	maker3 = Thread(target=maker).start()








