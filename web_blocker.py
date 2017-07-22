#uses python3
import time
from datetime import datetime as dt

#directory and IP to use
host_path = 'C:\Windows\System32\drivers\etc\hosts'
redirected_ip = '127.0.0.1'
webs_list = ['www.facebook.com', 'facebook.com', 'www.youtube.com', 'youtube.com']

#8am each day to 4pm will be blocked
def start_time():
    return dt(dt.now().year, dt.now().month, dt.now().day, 8)

def end_time():
    return dt(dt.now().year, dt.now().month, dt.now().day, 16)

def current_time():
    return dt(dt.now().year, dt.now().month, dt.now().day, dt.now().hour)

if __name__=='__main__':
    while 1:
        if (start_time() < current_time()) and (current_time() < end_time()):
            print('Working Hours')
        else:
            print('Break Hours')
            break
        time.sleep(5)

    exit()
