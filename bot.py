import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
import time

class InstaBot(object):
    """Класс для создания бота в Instagramm"""
    def __init__(self,login_json='login.json',following_list='following.txt'):
        self.login_json = login_json
        self.following_list = following_list
        self.browser = webdriver.Chrome("chromedriver.exe")

    def get_json_data(self,filename):
        """Функция для получения данных логина и пароля"""
        with open(filename) as file_object:
            json_data = json.load(file_object)
        return json_data

    def log_in(self):
        """Функция входа в Instagramm через Selenium"""
        access_data = self.get_json_data(self.login_json)
        self.browser.get("https://www.instagram.com/accounts/login")
        self.browser.maximize_window()
        time.sleep(2)

        self.browser.find_element_by_xpath(
        "//section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(access_data['login'])
        self.browser.find_element_by_xpath(
        "//section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(access_data['password'])
        self.browser.find_element_by_xpath(
        "//section/main/div/article/div/div[1]/div/form/div[4]/button").click()
        time.sleep(3)

    def get_following_list(self,filename):
        """Получаем из файла список пользоватtлей для подписки"""
        with open(filename) as file_object:
            lines = file_object.readlines()
        users = ""
        for line in lines:
            line = line.replace("@",'')
            users += line
        users = users.split()
        return users

    def subscribe_to_users_list(self):
        """Подписываемся на профили из списка"""
        users_list = self.get_following_list(self.following_list)
        for user in users_list:
            self.browser.get('https://www.instagram.com/' + user)
            time.sleep(3)
            try:
                self.browser.find_element_by_xpath(
                '''//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button''').click()
            except selenium.common.exceptions.NoSuchElementException as e:
                self.browser.find_element_by_xpath(
                '''//*[@id="react-root"]/section/main/div/header/section/div[1]/button''').click()
            else:
                time.sleep(3)
                print('Блок else выполнен')


bot = InstaBot()
bot.log_in()
bot.subscribe_to_users_list()
