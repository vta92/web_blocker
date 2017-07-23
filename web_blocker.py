#uses python3
import time
from datetime import datetime as dt

#directory and IP to use
#host_path = 'C:\Windows\System32\drivers\etc\hosts'
#link host_path to your own hosts file
host_path = 'hosts'
redirected_ip = '127.0.0.1'
webs_list = ['www.facebook.com', 'facebook.com', 'www.youtube.com', 'youtube.com']

#to do, use tkinter to make an GUI for the input
start_hour = 8
end_hour = 16

#8am each day to 4pm will be blocked
def start_time():
    return dt(dt.now().year, dt.now().month, dt.now().day, start_hour)

def end_time():
    return dt(dt.now().year, dt.now().month, dt.now().day, end_hour)

def current_time():
    return dt(dt.now().year, dt.now().month, dt.now().day, dt.now().hour)


def initial_state():
    with open(host_path, 'r') as f:
        init = f.read().strip()
        for site in webs_list:
            if (redirected_ip + ' ' + site) in init:
                init = init.replace(redirected_ip + ' ' + site, '')
        return init.strip()

if __name__=='__main__':

    while True:
        if (start_time() < current_time()) and (current_time() < end_time()):
            print('Working Hours')
            with open(host_path,'r+') as f:
                data = f.read() #read the whole file

                for site in webs_list:
                    if site in data:
                        continue
                    else:
                        f.write('\n'+ redirected_ip + ' ' + site)
                #time.sleep(10)


        #if not in working hours, return to the initial state as stored earlier
        else:
            ref_file = initial_state()
            with open(host_path, 'r+') as f:
                f.truncate()
                f.write(ref_file)
                print('worked')
        time.sleep(10)

        #tester
        # if end_hour == 16:
        #     end_hour = 20
        # elif end_hour == 20:
        #     end_hour = 16

    exit()
