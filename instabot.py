from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format('owenshade_')).click()
        

mybot = InstaBot('owenshade_', 'Celtic1967')
mybot.get_unfollowers()