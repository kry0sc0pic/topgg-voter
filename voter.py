'''
_____________________
Author: Krishaay Jois
Date:   02 April 2020
'''
from selenium import webdriver
from time import sleep
from config import emailID , password , bot_link

class Voter:
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get(bot_link)

    def login(self):

        votebtn = self.driver.find_element_by_xpath("/html/body/section/article/div[2]/div[2]/div/div/div[2]/span")
        votebtn.click()
        login = self.driver.find_element_by_xpath("/html/body/section/article/div[1]/div[2]/p/a/strong")
        login.click()
        sleep(5)
        emailbox = self.driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/div[1]/div/input")
        emailbox.send_keys(emailID)
        paswdbox = self.driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/div[2]/div/input")
        paswdbox.send_keys(password)
        dlogin = self.driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/button[2]")
        dlogin.click()
        sleep(5)
        authorize = self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/div/div[2]/button[2]')
        authorize.click()

    def vote(self):
        votebtn = self.driver.find_element_by_xpath("/html/body/section/article/div[2]/div[2]/div/div/div[2]/span")
        votebtn.click()
        sleep(1)
        self.driver.close()

    def run(self):
        sleep(1)
        self.login()
        sleep(2)
        self.vote()
 
bot = Voter()
bot.run()
