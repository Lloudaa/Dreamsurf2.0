import requests
#from googlesearch import search
import urllib
import os, sys
from os import system
from urllib.parse import urljoin, urlparse
import itertools
import re
import urllib.request
import pyfiglet
#mport time
#from pywebcopy import save_webpage
import selenium
from selenium import webdriver
from selenium.webdriver import common
from selenium.webdriver import support
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#import pyautogui
#import timeC:\Program Files (x86)\geckodriver.exe
#import urllib
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from time import sleep

#from urllib.parse import urljoin, urlparse


PATH = r"/run/media/louda/DATA/Download/geckodriver/geckodriver"
driver = webdriver.Firefox(executable_path=PATH)

a = "a","A","available","Available","AVAILABLE"
d = "d","D","download","Download","DOWNLOAD"
s = "s","S","see","See","SEE","screen","Screen","SCREEN","screenshot","Screenshot","ScreenShot","SCREENSHOT"
g = "g","G","google","Google","GOOGLE"
l = "l","L","link","LINK","Link"
a = "a","A","About","about"
t = "t", "T", "translate", "Translate", "TRANSLATE"
yes = "y","Y","yes","Yes","YES","o",'O',"oui","Oui","OUI"
no = "n","N","no","No","NO","non","Non","NON"
error = exceptions.InvalidArgumentException,exceptions.WebDriverException

def search(query=None):
    retry = True
    driver.get("https://www.google.com")
    WebDriverWait(driver, 15).until(
EC.presence_of_element_located((By.XPATH, '//input[@class="gLFyf gsfi"]')))
    query = query
    while retry:
        if len(query) == 0 or query.isspace():
            print("\nOops, looks like you typed nothing")
        else:
            bar = driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
            bar.send_keys(query)
            bar.send_keys(Keys.ENTER)
            retry = False
    WebDriverWait(driver, 15).until(
EC.presence_of_element_located((By.ID, 'res')))

    res = driver.find_element_by_id('res')
    print("\nThese are your search results:")
    print(res.text)

def screenshot():
    print("\nThis is what your webpage looks like")
    res = driver.save_screenshot('test.png')
    img = mpimg.imread('test.png')
    imgplot = plt.imshow(img)
    plt.show()

def clickable():
    clcs = driver.find_elements_by_xpath('//a[@href]')
    print("\nThese are the available links in your web page:\n")
    for clc in clcs:
        print(clc.get_attribute("href"))
    print("\nIf you'd like to go to one of these results, copy and paste them in the 'Go to a (L)ink'.\n")

def gsearch ():
    gquery = input("\nWhat would you like to know?\nType '/m' to get back to the Menu\n")

    if gquery == '/m':
        dreamsurf()
    else:
        search(gquery)
        screenshot()
        print("\nIf you'd like to go to one of these results, copy and paste them in the 'Go to a (L)ink'.\n")
        action()

def link ():
    lretry = True
    lquery = input("\nType your link as following: https://www.facebook.com/Tafitantsoa.Rakotondrafara/\nType '/m' to get back to the Menu\n")
    if lquery == "/m":
        dreamsurf()
    else:
        while lretry:
            try:
                driver.get(lquery)
                screenshot()
                lretry = False
                retry = True
                action()

            except error:
                print("\nOops, looks like your link is not valid")
                retry = True
                while retry:
                    notalink = input("\nType G if you want to make a google search with what you typed, or L to retype your link\n")
                    if notalink in g:
                        retry = False
                        search(lquery)
                        screenshot()
                        action()
                        print("If you'd like to go to one of these results, copy and paste them in the 'Go to a (L)ink' .")
                        lretry = False
                    elif notalink in l:
                        retry = False
                        lretry = False
                        link()
                    else:
                        print("I'm sorry I can't understand")
        dreamsurf()

def welcome():
    print("\nHi there :) I'm Dreamsurf, a bot created by Louda and I am here to help you surf freely on the internet")

def about():
    print("\nI am Dreamsurf and I am here to help you surf freely on the internet :) \nAt the very beginning, I was created to help students who do not have Internet connection and cannot do research for their studies. But now that I am stronk enough, you can use me to browse freely on the internet, whether it's about studies or not ;)\nI have been developped by Louda, a noice dude developping cool things for fun. If you want to talk to him, you can PM him at https://www.facebook.com/Tafitantsoa.Rakotondrafara or if you prefer emails, you can send one to the address tafitantsoa.rakotondrafara@gmail.com. Thx and don't use me for porn plz. ")
    input()
    retry = False
    dreamsurf()




def download():
    name = input("\nWhat would you like to name your page?")
    real = "%s.html" %name
    with open(real, "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("\nHere you go.")

def action():
    retry = True
    while retry:
        act = input("\nDo you want to:\n- See all the (a)vailable links in the webpage\n- (D)ownload the page as an html file\n- Get back to the (/m)enu\n")
        if act in a:
            clickable()
            retry = True
        elif act in d:
            download()
            retry = True
        elif act =="/m":
            dreamsurf()
            retry = False
        else:
            print("\nI'm sorry, I can't understand. Could you repeat?")
            retry = True

def translate():
    retry = True
    while retry:
        sl = input("\nPlease choose the language in which you'll be writing. ")
        tl = input("\nNow choose the language in which it will be translated. ")
        tobe = input("\nType your sentence.\n")
        trs = driver.get(f"https://www.deepl.com/translator#{sl}/{tl}/{tobe}")

        sleep(3)

        trslated = driver.find_element_by_xpath("//div[@id='target-dummydiv'][@class='lmt__textarea lmt__textarea_dummydiv']").get_attribute("textContent")
        print("\nTranslation: ",trslated)

        reretry = True
        while reretry:
            choice = input("\nWould you like to translate something else? ")
            if choice in yes:
                retry = True
                reretry = False
            elif choice in no:
                retry = False
                reretry = False
                dreamsurf()
            else:
                reretry = True
                print("\nI'm sorry I can't understand. Could you repeat?")


def dreamsurf():
    system('clear')
    fig = pyfiglet.Figlet(font="larry3d")
    print (fig.renderText("Dreamsurf"))
    print ("Dreamsurf - The dream browser\n".center(75))
    print ("Created by Louda\n".center(75))
    print("\nWhat would you like to do?\n- (G)oogle Search\n- Go to a (L)ink\n- (T)ranslate things\n- (A)bout me and my Senpai")
    retry = True
    while retry:
        choice = input("\nType the letter inside the paranthesis to choose your option. For example type'g' to make a google search.\n")
        if choice in g:
            retry = False
            gsearch()
        elif choice in l:
            retry = False
            link()
        elif choice in a:
            retry = False
            about()

        elif choice in t:
            retry= False
            translate()

        elif choice in a:
            retry = False
            about()

        else:
            print("\nI'm sorry, I can't understand.")

def main():
    dreamsurf()

if __name__ =="__main__":
    welcome()
    input("\nPress any key to continue")
    main()
