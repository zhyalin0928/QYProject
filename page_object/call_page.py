"""
@Time      ：2021/6/16 13:57
@Author    ：赵亚林
@Function  ：call_page
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

from base_operation.web_base_page import BasePage


class CallPage(BasePage):
    """----------呼叫面板页面元素----------"""
    # 呼叫面板页面url
    call_panel_url = 'https://comuhome-ty.yunzhuyang.com/workorder/call_panel'
    # 外呼输入框
    call_input = (By.ID, 'phoneNum')
    # 外呼按钮
    call_btn = (By.XPATH, '//*[@id="seat-ctrl-app"]/div/form/div[2]/div')
    #
