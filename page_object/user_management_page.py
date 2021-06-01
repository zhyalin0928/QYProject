"""
@Time      ：2021/5/17 15:38
@Author    ：赵亚林
@Function  ：user_management_page
"""
from time import sleep
from selenium.webdriver.common.by import By
from base_operation.web_base_page import BasePage


class UserManagementPage(BasePage):
    """----------用户列表元素----------"""
    # 用户列表url
    user_list_url = 'https://comuhome-ty.yunzhuyang.com/memberuser/getMemberList'
    # 新建按钮
    build_btn = (By.XPATH, '//*[@id="card-body"]/div[3]/div/a')
    # 搜索框
    search_input = (By.XPATH, '//*[@id="input-search"]')
    # 搜索按钮
    search_btn = (By.XPATH, '//*[@id="card-body"]/div[3]/div/div/div')
    # 用户详情下拉箭头
    down_arrow = (By.XPATH, '//*[@id="datatable-editable1"]/tbody/tr[1]/td[9]/span/i')
    # 删除会员按钮
    del_user_btn = (By.XPATH, '//*[@id="datatable-editable1"]/tbody/tr[2]/td/button[6]')
    # 删除确定按钮
    del_sure_btn = (By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]')

    """----------新建用户页面元素----------"""
    # 会员姓名
    user_name = (By.XPATH, '//*[@id="user_name"]')
    # 手机号码
    user_phone = (By.XPATH, '//*[@id="user_phone"]')
    # 身份证号码
    user_idcard = (By.XPATH, '//*[@id="user_idcard"]')
    # 社区选择框
    user_store_selector = (By.XPATH, '//*[@id="store_id"]')
    # 第一个社区
    first_store = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]')
    # 详细地址
    user_adr = (By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[10]/div[2]/div[5]/input')
    # 保存按钮
    save_btn = (By.XPATH, '//*[@id="app"]/div[2]/div[7]/button[2]')

    """----------元素操作流----------"""
    # 新建用户
    def build_user(self, user_name, user_phone, user_idcard, user_adr):
        # 进入会员列表页面
        self.open_browser(self.user_list_url)
        sleep(1)
        # 点击新建按钮
        self.click_button(self.build_btn)
        sleep(1)
        # 输入会员姓名
        self.input_keys(self.user_name, user_name)
        # 输入手机号码
        self.input_keys(self.user_phone, user_phone)
        # 输入身份证号码:520112199003074237
        self.input_keys(self.user_idcard, user_idcard)
        # 点击社区选择框
        self.click_button(self.user_store_selector)
        sleep(1)
        # 选择第一个社区
        self.click_button(self.first_store)
        # 输入详细地址
        self.input_keys(self.user_adr, user_adr)
        # 点击保存按钮
        self.click_button(self.save_btn)

    # 搜索用户
    def search_user(self, user_phone):
        # 访问用户列表页面
        self.open_browser(self.user_list_url)
        # 在搜索框输入用户名/手机号/身份证号
        self.input_keys(self.search_input, user_phone)
        # 点击搜索按钮
        self.click_button(self.search_btn)

    # 删除用户
    def del_user(self):
        # 点击详情下拉箭头
        self.click_button(self.down_arrow)
        # 点击删除用户按钮
        self.click_button(self.del_user_btn)
        # 点击确定按钮
        self.click_button(self.del_sure_btn)