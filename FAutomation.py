import datetime
from datetime import datetime
import time
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


#serv = Service("C://Program Files (x86)//chromedriver.exe")
#driver = webdriver.Chrome(service=serv)


class FBDebug:

    def __init__(self, account, password, log):
        self.account = account
        self.password = password
        self.log = log

    def face_login(self, jobs):
        driver = webdriver.Chrome(executable_path='.//chromedriver.exe')
        driver.get("https://facebook.com")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(self.account)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(self.password)
        log = driver.find_element(By.XPATH, "//button[@name='login']")
        log.click()
        time.sleep(5)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@aria-current="page"]')))
            record = Logfile(self.log)
            record.record_log("\n" + str(datetime.now()) + ": [SUCCESSFUL] Login with " + self.account)
            login = "success"
        except TimeoutException:
            record = Logfile(self.log)
            record.record_log("\n" + str(datetime.now()) + ": [FAILED] Login with " + self.account)
            login = "fail"

        def send_message(url, message):
            time.sleep(3)
            pyautogui.hotkey("ESC")
            driver.get(url)
            mess_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]')))
            mess_field.send_keys(message)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o tgvbjcpo hpfvmrgz l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb n00je7tq arfg74bv qs9ysxi8 k77z8yql pq6dq46d btwxx1t3 abiwlrkh p8dawk7l lzcic4wl cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr knvmm38d kkf49tns cgat1ltu bi6gxh9e']"))).click()
            time.sleep(5)
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "{}")]'.format(message))))
                mes_record = Logfile(self.log)
                mes_record.record_log(
                    "\n" + str(datetime.now()) + ": [SUCCESSFUL] Deliver message from " + self.account)
            except TimeoutException:
                mes_record = Logfile(self.log)
                mes_record.record_log("\n" + str(datetime.now()) + ": [FAILED] Deliver message from " + self.account)

        def face_idle(idle):
            time.sleep(idle/1000)
            wait_record = Logfile(self.log)
            wait_record.record_log("\n" + str(datetime.now()) + ": [SUCCESSFUL] Finish waiting with " + self.account)

        if login == "success":
            for job in jobs:
                if job["Code"] == "176789":
                    send_message(job["Link"], job["Comment"])
                elif job["Code"] == "176791":
                    face_idle(job["Duration"])
                else:
                    record = Logfile(self.log)
                    record.record_log("\n" + str(datetime.now()) + ": [FAILED] The job code was not correct")
            driver.close()
        else:
            driver.close()


class FBNoDebug:

    def __init__(self, account, password):
        self.account = account
        self.password = password

    def face_login(self, jobs):
        driver = webdriver.Chrome(executable_path='.//chromedriver.exe')
        driver.get("https://facebook.com")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(self.account)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(self.password)
        log = driver.find_element(By.XPATH, "//button[@name='login']")
        log.click()
        time.sleep(5)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@aria-current="page"]')))
            record = Logfile(self.log)
            login = "success"
        except TimeoutException:
            record = Logfile(self.log)
            login = "fail"

        def send_message(url, message):
            time.sleep(5)
            pyautogui.hotkey("ESC")
            driver.get(url)
            mess_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]')))
            mess_field.send_keys(message)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o tgvbjcpo hpfvmrgz l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb n00je7tq arfg74bv qs9ysxi8 k77z8yql pq6dq46d btwxx1t3 abiwlrkh p8dawk7l lzcic4wl cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr knvmm38d kkf49tns cgat1ltu bi6gxh9e']"))).click()
            time.sleep(5)

        def face_idle(idle):
            time.sleep(idle/1000)

        if login == "success":
            for job in jobs:
                if job["Code"] == "176789":
                    send_message(job["Link"], job["Comment"])
                elif job["Code"] == "176791":
                    face_idle(job["Duration"])
            driver.close()
        else:
            driver.close()
