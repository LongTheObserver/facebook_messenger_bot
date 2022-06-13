import json
from datetime import datetime
import time
from Logfile import Logfile
from FAutomation import FBDebug
from FAutomation import FBNoDebug
import sched
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from Logfile import Logfile
import pyautogui
import os.path
from os.path import expanduser
import sys
from pathlib import Path


def json_data(f):
    with open(f, "r") as json_file:
        data = json.load(json_file)
        json_file.close()
        return data


def convert_datetime(da, ti):
    dt = datetime.strptime(str(da)+str(ti), "%Y%m%d%H%M")
    return dt


def find_willy():
    willy_stop = Path(".//willy.stop")
    try:
        willy_stop.resolve(strict=True)
    except FileNotFoundError:
        return "File not found"
    else:
        return "Stop the program"


js = json_data(str(input("Input file name: ")) + ".json")
if js["Debug"] != 0:
    file = Logfile(js["Logfile"])
    file.create_file()
    if convert_datetime(js["WorkUntil_Date"], js["WorkUntil_Time"]) < datetime.now():
        file.record_log("\n" + str(datetime.now()) + ": [EXIT] The WorkUntil Datetime has been reached")
    else:
        for login in js["logins"]:
            if find_willy() == "Stop the program":
                file.record_log("\n" + str(datetime.now()) + ": [EXIT] Found 'willy.stop' in the local folder")
                break
            else:
                if convert_datetime(login["Date"], login["Time"]) > convert_datetime(js["WorkUntil_Date"], js["WorkUntil_Time"]):
                    file.record_log("\n" + str(datetime.now()) + ": [FAILED] Jobs of " + login["Username"] + " has greater datetime than the WorkUntil Datetime")
                else:
                    if convert_datetime(login["Date"], login["Time"]) <= datetime.now():
                        access = FBDebug(login["Username"], login["Password"], js["Logfile"])
                        access.face_login(login["jobs"])
                    else:
                        def fb_automate():
                            acc = FBDebug(login["Username"], login["Password"], js["Logfile"])
                            acc.face_login(login["jobs"])
                        s = sched.scheduler(time.time, time.sleep)
                        t = time.strptime(str(login["Date"]) + str(login["Time"]), "%Y%m%d%H%M")
                        t = time.mktime(t)
                        s1 = s.enterabs(t, 0, fb_automate)
                        s.run()
        file.record_log("\n" + str(datetime.now()) + ": [EXIT] All jobs have been carried out")
else:
    if convert_datetime(js["WorkUntil_Date"], js["WorkUntil_Time"]) >= datetime.now():
        for login in js["logins"]:
            if find_willy() == "File not found":
                if convert_datetime(login["Date"], login["Time"]) <= datetime.now():
                    access = FBNoDebug(login["Username"], login["Password"])
                    access.face_login(login["jobs"])
                else:
                    def fb_automate():
                        acc = FBNoDebug(login["Username"], login["Password"])
                        acc.face_login(login["jobs"])
                    s = sched.scheduler(time.time, time.sleep)
                    t = time.strptime(str(login["Date"]) + str(login["Time"]), "%Y%m%d%H%M")
                    t = time.mktime(t)
                    s1 = s.enterabs(t, 0, fb_automate)
                    s.run()
