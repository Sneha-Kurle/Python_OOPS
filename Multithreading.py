#multithreadin- Used to perform multiple task parelell
#mostly used in i/o operations
#to fetch the data from API
import threading
import time
def walk(frst):
    time.sleep(6)
    print(f'you take the {frst} for walk')

def out_trash():
    time.sleep(4)
    print('You take the trash out')

def mail():
    time.sleep(2)
    print('You received the mail')


chore1=threading.Thread(target=walk,args=('doggi',))
chore1.start()
chore2=threading.Thread(target=out_trash)
chore2.start()
chore3=threading.Thread(target=mail)
chore3.start()
chore1.join()
chore2.join()
chore3.join()
print('all chore are complete')