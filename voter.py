'''
_____________________
Author: Krishaay Jois
Date:   02 April 2020
'''
from selenium import webdriver
from time import sleep
from secrets import emailID , password

class Voter:
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('https://top.gg/bot/pokecord/vote')

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

# If you want to use this file as a standalone program , uncomment the code below . Only remove the ''' '''
'''
voterBot = Voter() Creates a Voter object
#You can run this in 2 ways
#1:
voterBot.login()
voterBot.vote()
#
#2:
voterBot.run
'''
