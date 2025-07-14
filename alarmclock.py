import datetime
import time
import pygame
def set_alarm(alarm):
    print(f'The alrm is set at {alarm}')
    running=True
    mp_file='alarm.mp3'
    while running:
        current=datetime.datetime.now().strftime('%H:%M:%S')
        print(current)
        if current==alarm:
            print('Wake upp....')
            pygame.mixer.init()
            pygame.mixer.music.load(mp_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                cmd = input("Type 'Stop' if you are awake now: ").lower()
                if cmd == 'Stop' :
                    pygame.mixer.music.stop()
                    break
                time.sleep(1)


            running=False
        time.sleep(1)
if  __name__=="__main__":
    alarm=input('enter an time to set alarm HH:MM:SS :')
    set_alarm(alarm)
    