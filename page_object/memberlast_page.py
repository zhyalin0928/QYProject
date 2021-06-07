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
    # 开启/关闭开启按钮
    switch_btn = (By.XPATH, '//*[@id="datatable-editable"]/tbody/tr[1]/td[7]/span')
    # 作废原因输入框
    del_reason = (By.XPATH, '//*[@id="layui-layer2"]/div[2]/textarea')
    # 作废确定按钮
    del_save_btn = (By.XPATH, '//*[@id="layui-layer5"]/div[3]/a[1]')
    # 作废二次确认按钮
    del_confirm_btn = (By.XPATH, '//*[@id="layui-layer6"]/div[3]/a[1]')
    # 删除按钮
    del_btn = (By.XPATH, '//*[@id="datatable-editable"]/tbody/tr[1]/td[8]/a[2]')


    """-----------新建兜底老人页面元素----------"""
    # 长者搜索输入框
    memlast_input = (By.XPATH, '/html/body/span/span/span[1]/input')
    # 搜索结果第一条数据
    memlast_first = (By.XPATH, '//*[@id="select2-select-member-results"]/li[1]')

    """----------报平安管理页面元素----------"""
    # 报平安管理菜单按钮
    safety_btn = (By.XPATH, '//*[@id="sidebar-menu"]/ul/li[3]/ul/li[2]/a')
    # 报平安新建按钮
    safety_build_btn = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div/div[2]/div/div/div/div[2]/div/a')
    # 长者姓名选择框按钮
    safety_username_btn = (By.XPATH, '//*[@id="commentForm"]/div[1]/div[2]/div/div[1]/div/div/span/span[1]/span')
    # 报平安保存按钮
    safety_save_btn = (By.XPATH, '//*[@id="btn-submit-modal"]')
    # 报平安列表第一条数据
    first_data = (By.XPATH, '//*[@id="datatable-editable"]/tbody/tr[1]')
    # 报平安删除按钮
    safety_del_btn = (By.XPATH, '//*[@id="datatable-editable"]/tbody/tr[1]/td[7]/a')

    """----------主动关怀页面元素----------"""
    # 主动关怀菜单
    care_btn = (By.XPATH, '//*[@id="sidebar-menu"]/ul/li[3]/ul/li[3]/a')
    # 主动关怀新建按钮
    care_build_btn = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div/div[2]/div/div/div/div[2]/div/a')
    # 关怀方式：上门关怀按钮
    care_shangmen_btn = (By.XPATH, '//*[@id="inlineRadio2"]')
    # 关怀人员搜索框
    care_search_btn = (By.XPATH, '//*[@id="commentForm"]/div[5]/div/span/span[1]/span/ul/li/input')
    # 第一个关怀人员属性
    care_first_data = (By.XPATH, '//*[@id="select2-select_userinfo-results"]/li[1]')

    """----------页面公共元素---------"""
    # 长者姓名选择框
    mem_selector_btn = (By.XPATH, '//*[@id="commentForm"]/div[1]/div[2]/div/div[1]/div/span/span[1]/span')
    # 提交确认按钮
    confirm_btn = (By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]')
    # 搜索输入框
    username_input = (By.XPATH, '/html/body/span/span/span[1]/input')
    # 保存按钮
    save_btn = (By.XPATH, '//*[@id="btn-submit"]')

    """----------元素操作流----------"""

    # 新建兜底老人
    def build_memlast(self, memlast_name):
        # 进入老人列表页面
        self.open_browser(self.memberlast_url)
        # 点击新建按钮
        self.click_button(self.build_btn)
        sleep(1)
        # 点击长者姓名选择框
        self.click_button(self.mem_selector_btn)
        # 输入长者手机号
        self.input_keys(self.memlast_input, memlast_name)
        sleep(2)
        self.click_button(self.memlast_first)
        sleep(1)
        # 点击保存按钮
        self.click_button(self.save_btn)
        sleep(1)
        # 点击确认按钮
        self.click_button(self.confirm_btn)

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

    # 新建报平安
    def safety_build(self, username):
        # 进入老人列表页面
        self.open_browser(self.memberlast_url)
        # 判断兜底老人是否启用
        elehtml = self.locator(self.switch_btn).get_attribute('innerHTML')
        if 'small' in elehtml:
            self.click_button(self.switch_btn)
        # 点击报平安管理菜单，进入页面
        self.click_button(self.safety_btn)
        sleep(1)
        # 点击报平安新建按钮
        self.click_button(self.safety_build_btn)
        sleep(1)
        # 点击长者姓名搜索框
        self.click_button(self.safety_username_btn)
        # 输入长者姓名
        self.input_keys(self.username_input, username)
        sleep(2)
        self.click_button(self.memlast_first)
        # 点击保存按钮
        self.click_button(self.safety_save_btn)
        # 点击二次确认按钮
        self.click_button(self.confirm_btn)

    # 删除保平安记录
    def safety_del(self):
        # 点击报平安管理菜单
        self.click_button(self.safety_btn)
        sleep(1)
        # 点击删除按钮
        self.click_button(self.safety_del_btn)
        sleep(1)
        # 点击二次确认按钮
        self.click_button(self.confirm_btn)

    # 新建主动关怀
    def care_build(self, username):
        # 点击主动关怀菜单按钮
        self.click_button(self.care_btn)
        # 点击新建按钮
        self.click_button(self.care_build_btn)
        # 点击长者姓名搜索框
        self.click_button(self.mem_selector_btn)
        # 输入长者姓名搜索
        self.input_keys(self.username_input, username)
        sleep(2)
        # 点击搜索的第一个用户
        self.click_button(self.memlast_first)
        # 选择关怀方式：上门关怀
        self.click_button(self.care_shangmen_btn)
        # 点击关怀人员搜索框
        self.click_button(self.care_search_btn)
        sleep(2)
        # 选择第一个关怀人员
        self.click_button(self.care_first_data)
        # 点击保存按钮
        self.click_button(self.save_btn)
        # 点击二次确认按钮
        self.click_button(self.confirm_btn)

    # 作废兜底老人并删除
    def memlast_del(self, del_reason):
        # 进入老人列表页面
        self.open_browser(self.memberlast_url)
        # 点击是否启用按钮
        self.click_button(self.switch_btn)
        # 输入作废原因
        self.input_keys(self.del_reason, del_reason)
        # 点击确认按钮
        self.click_button(self.del_save_btn)
        # 点击作废二次确认按钮
        self.click_button(self.del_confirm_btn)
        sleep(1)
        # 点击删除按钮
        self.click_button(self.del_btn)
        # 点击删除二次确认按钮
        self.click_button(self.confirm_btn)

    # 获取列表第一条数据
    def list_first_data(self):
        ele = self.locator(self.first_data)
        return ele.text
