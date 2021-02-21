import random
import sys
import sqlite3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from getpass import getpass
import os
import datetime

# Shell Settings

clear = lambda: os.system('cls')
title = lambda: os.system('title MAIA: Console')
color = lambda: os.system('color a')
colorOff = lambda: os.system('color ')
exit = lambda: os.system('exit')
clear()
title()
color()

#SQLite3 Connector

mydb = sqlite3.connect('_data.db')

#Timer 

def timecount(seconds):
    while seconds:
        min, sec = divmod(seconds, 60)
        count = 'Timer: {:d}min:{:d}sec'.format(min, sec)
        print(count, end='\r')
        sleep(1)
        seconds -= 1

# Instagram Engagement Function

def doengagement(username, password, hashtag, limit):
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    driver.set_window_position(800, 0)
    driver.set_window_size(200, 800)
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    print("Opening instagram.com")
    timecount(2)
    print("Handling Cookies.")
    driver.find_element_by_xpath("//html/body/div[2]/div/div/div/div[2]/button[1]").click()
    timecount(2)
    userLogin = driver.find_element_by_name('username')
    userHashtag = str(hashtag)
    userLogin.send_keys(username)
    print("Handling Username.")
    passLogin = driver.find_element_by_name('password')
    passLogin.send_keys(password)
    print("Handling Password.")
    submit = driver.find_element_by_tag_name('form')
    submit.submit()
    print("Accessing Instagram.")
    timecount(5) 
    driver.get("https://instagram.com/explore/tags/" + userHashtag)
    print("Opening Hashtag #" + userHashtag + ".")
    print("https://instagram.com/explore/tags/" + userHashtag)
    sleep(10)
    driver.find_element_by_xpath("//a[contains(@href, '/p/')]").click()
    print("Starting Engagement.\n")
    timecount(3)
    print("---------------------------------------------------------")
    engagements = 0
    engLimit = int(limit)
    while engagements != engLimit:
        if engagements < engLimit:
            try:
                try:
                    profile = driver.find_element_by_xpath("//html/body/div/div/div/article/header/div/div/div/span/a").text
                    profile_url = driver.current_url
                    date_time = datetime.datetime.now()
                    driver.find_element_by_xpath('//*[name()="svg"][@aria-label="Like"]').click()
                    
                    NULL_ = None
                    _dateTime = str(date_time.date())
                    _dateTime2 = str(date_time.strftime("%X"))

                    sql_insert = "INSERT INTO instagram_engagement (Id, username, hashtag, date, time, profile, post_url) VALUES (?, ?, ?, ?, ?, ?, ?)"
                    sql_values = (NULL_, username, hashtag, _dateTime, _dateTime2, profile, profile_url)
                    maiacursor = mydb.cursor()
                    maiacursor.execute(sql_insert,sql_values)

                    engDisplay = engagements + 1
                    print("Starting Engagement: " + str(engDisplay) + "/" + limit)
                    timecount(1)
                    print("#########################################################")
                    print("Profile: " + profile)
                    print("URL: " + profile_url)
                    print("Date: " + str(date_time.date()))
                    print("Time: " + str(date_time.strftime("%X")))
                    mydb.commit()
                    print("Engagement Recorded.")
                    print("#########################################################")
                    try:
                        try:
                            driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a[2]").click()
                        except:
                            driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a").click()
                    except ElementClickInterceptedException:
                        print("WARNING: Interaction intercepted by Instagram.")
                        status_label.config(text="WARNING: Interaction intercepted by Instagram.")
                        print("Closing Application, please try again later.")
                        timecount(10)
                        print("Disconnecting Driver")
                        status_label.config(text="Disconnecting Chrome Driver")
                        driver.close()
                        timecount(3)
                        print("Disconnecting Database")
                        status_label.config(text="Disconnecting Database")
                        mydb.close()
                        timecount(3)
                        print("Closing MAIA User Interface")
                        status_label.config(text="Closing MAIA Interface")
                        timecount(5)
                        root.destroy()
                        timecount(3)
                        print("EXECUTING KILL COMMAND")
                        timecount(3)
                        exit()
                        timecount(100)
                    print("Completing Engagement.")
                    maia_rand_int_7 = random.randint(3,7)
                    timecount(maia_rand_int_7)
                    print("Engagement Complete.")
                    print("---------------------------------------------------------")
                    engagements += 1
                except ElementNotInteractableException:
                    try:
                        driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a[2]").click()
                    except:
                        driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a").click()
                    print("Post already liked: Moving to the next.")
                    timecount(3)
                    print("Complete.")
                    print("---------------------------------------------------------")
            except NoSuchElementException:
                try:
                    driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a[2]").click()
                except:
                    driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a").click()
                print("Post already liked: Moving to the next. -- NSElement")
                timecount(3)
                print("Complete.")
                print("---------------------------------------------------------")
    else:
        print("\nEngagement Function Complete.")
        timecount(1)
        print("Disconnecting from MAIA Database")
        mydb.close()
        timecount(1)
        print("Closing Browser.")
        colorOff()
        driver.close()

# Welcome Screen

print("#########################################################")
print("#               MAIA Blocks - FBI 1.0.1                 #")
print("#########################################################")
insta_username = input("Username: ")
insta_password = getpass("Password: ")
insta_hashtag = input("Hashtagh: ")
insta_limit = input("Limit: ")

doengagement(insta_username, insta_password, insta_hashtag, insta_limit)
