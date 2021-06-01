"""
@Time      ：2021/5/11 20:24
@Author    ：赵亚林
@Function  ：login_page
"""
from time import sleep

from selenium.webdriver.common.by import By
from base_operation.web_base_page import *


class LoginPage(BasePage):
    # 登录页url
    url = 'https://comuhome-ty.yunzhuyang.com/ulogin'
    # 页面元素
    # 手机号
    user_num = (By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[1]/div/div[1]/input')
    # 验证码
    user_pwd = (By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[2]/div/div[1]/input')
    # 登录按钮
    login_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/form/button')
    # # 手机号格式错误提示
    # user_num_error = (By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[1]/div/div[2]')
    # # 验证码错误提示
    # user_pwd_error = (By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[2]/div/div[3]')
    # 智慧养老运营中心
    cho_btn = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div/div[2]/div[1]/div/div[3]/img')

    # 元素操作流
    def login(self, user_num, user_pwd):
        # 访问url
        self.open_browser(self.url)
        # 输入登录手机号
        self.input_keys(self.user_num, user_num)
        # 输入登录验证码
        self.input_keys(self.user_pwd, user_pwd)
        # 点击登录按钮
        self.click_button(self.login_btn)
        # 强制等待1秒，加载出需要点击的元素
        sleep(1)
        # 点击智慧养老运营中心模块
        self.click_button(self.cho_btn)