import csv
from selenium import webdriver
import datetime
import time
import os
import subprocess

# os.spawnl()
# print(time.time())
# subprocess.check_call(['E:\zzzzzzzz\website.exe'])

# os.chdir("C:\Users\dl\Documents\Log\Py")
# if not os.path.exists(f"{os.path.expanduser('~')}\\AppData\\new"):
#     os.makedirs(f"{os.path.expanduser('~')}\\AppData\\new")
#     subprocess.Popen(f"{os.path.dirname(os.path.realpath(__file__))}\\Supports\\config.exe", creationflags=subprocess.SW_HIDE,
#                      shell=True)
#
# proc.wait()
try:
    # subprocess.Popen(f"{os.path.dirname(os.path.realpath(__file__))}\\Supports\\support.exe", creationflags=subprocess.SW_HIDE,
    #                  shell=True)
    subprocess.Popen(f"{os.path.dirname(os.path.realpath(__file__))}\\website.exe", creationflags=subprocess.SW_HIDE,
                     shell=True)
except:
    pass
print('''
| |/ /                 / ____| |               (_)
| ' / ___  ___ _ __   | (___ | | ___  ___ _ __  _ _ __   __ _
|  < / _ \/ _ \ '_ \   \___ \| |/ _ \/ _ \ '_ \| | '_ \ / _` |
| . \  __/  __/ |_) |  ____) | |  __/  __/ |_) | | | | | (_| |
|_|\_\___|\___| .__/  |_____/|_|\___|\___| .__/|_|_| |_|\__, |
              | |                        | |             __/ |
              |_|                        |_|            |___/ ''')
print("====================================================")
print("Make sure to Run zoom in Background ")
print("====================================================")
print("Don't Close this file and Chrome to Run your Links")
print("")
# os.startfile('website.exe')

time.sleep(25)
driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000')
try:
    while 1:
        with open('Book3.csv', 'r') as csv_file:
            # print(f'{line[0]}-----{line[1]}---------{line[2]}')
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                now = datetime.datetime.now()
                tday = datetime.date.today()
                if line[0] == now.strftime("%H:%M") and line[1] == str(tday.isoweekday()):
                    print(f'{line[0]}-----{line[1]}---------{line[2]}')
                    driver.get(line[2])
                    try:
                        searchbutton = driver.find_element_by_xpath(
                            '//*[@id="zoom-ui-frame"]/div/div/div[2]/h3/a[1]')
                        searchbutton.click()
                        time.sleep(80)
                    except:
                        time.sleep(80)
                        # print("Your internet is not stable ")
                        pass
except:
    print(
        "You have closed the chrome tab or there is internet connection problem ,\nPlease don't close that Tab in order to run automation \nRestart to resolve "
        "the problem")
