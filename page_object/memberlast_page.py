"""
@Time      ：2021/5/25 19:59
@Author    ：赵亚林
@Function  ：memberlast_page
"""
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_operation.web_base_page import BasePage


class MemberLastPage(BasePage):
    """----------兜底老人页面元素----------"""
    # 老人列表url
    memberlast_url = 'https://comuhome-ty.yunzhuyang.com/memberlast/list'
    # 新建按钮
    build_btn = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div/div[2]/div/div/div/div[2]/div/a[2]')
    # 搜索框
    search_input = (By.XPATH, '//*[@id="input-search"]')
    # 搜索按钮
    search_btn = (By.XPATH, '//*[@id="btn-iptSearch"]')
    # 搜索结果的老人姓名
    memlast_name = (By.XPATH, '//*[@id="datatable-editable"]/tbody/tr/td[1]')

    """-----------新建兜底老人页面元素----------"""
    # 长者姓名选择框
    mem_selector = (By.XPATH, '//*[@id="commentForm"]/div[1]/div[2]/div/div[1]/div/span/span[1]/span')
    # 长者搜索输入框
    memlast_input = (By.XPATH, '/html/body/span/span/span[1]/input')
    # 搜索结果第一条数据
    memlast_first = (By.XPATH, '//*[@id="select2-select-member-results"]/li[1]')
    # 保存按钮
    save_btn = (By.XPATH, '//*[@id="btn-submit"]')
    # 提交确认按钮
    put_sure_btn = (By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]')

    """----------元素操作流----------"""
    # 新建兜底老人
    def build_memlast(self, memlast_name):
        # 进入老人列表页面
        self.open_browser(self.memberlast_url)
        # 点击新建按钮
        self.click_button(self.build_btn)
        sleep(1)
        # 点击长者姓名选择框
        self.click_button(self.mem_selector)
        # 输入长者手机号
        self.input_keys(self.memlast_input, memlast_name)
        sleep(2)
        self.click_button(self.memlast_first)
        sleep(1)
        # 点击保存按钮
        self.click_button(self.save_btn)
        sleep(1)
        # 点击确认按钮
        self.click_button(self.put_sure_btn)

    # 搜索兜底老人
    def search_memlast(self, memlast_name):
        # 进入老人列表页面
        self.open_browser(self.memberlast_url)
        # 点击搜索输入框,并输入搜索条件
        self.input_keys(self.search_input, memlast_name)
        # 点击搜索按钮
        self.click_button(self.search_btn)
        # 获取搜索结果的手机号数据
        text = self.locator(self.memlast_name).text
        return text
