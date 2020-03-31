from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller

def AlphaBot():
        keyboard = Controller()
        driver = webdriver.Chrome()
        driver.get("https://www.speedtypingonline.com/games/type-the-alphabet.php")
        sleep(2)
        keyboard.type("abcdefghijklmnopqrstuvwxyz")
        sleep(5)
AlphaBot()