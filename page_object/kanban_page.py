"""
@Time      ：2021/5/11 20:25
@Author    ：赵亚林
@Function  ：kanban_page
"""
from time import sleep
from selenium.webdriver.common.by import By
from base_operation.web_base_page import BasePage


class KanbanPage(BasePage):
    # 数据看板url
    kanban_url = 'https://comuhome-ty.yunzhuyang.com/main/index'

    '''--------------------页面元素--------------------'''
    '''数据看板页面元素'''
    # 数据看板导航
    kanban_btn = (By.XPATH, '//*[@id="sidebar-menu"]/ul/li/a')
    # 社区数量
    comm_num = (By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div[2]/div[1]')
    # 驿站数量
    stage_num = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[1]')
    # 会员总量
    mem_total = (By.XPATH, '//*[@id="app"]/div/div[1]/div[3]/div[2]/div[1]')
    # 订单总量
    order_total = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div[2]/div[1]')
    # 工单总量
    work_order_total = (By.XPATH, '//*[@id="app"]/div/div[1]/div[5]/div[2]/div[1]')
    # 设备总量
    equipment_total = (By.XPATH, '//*[@id="app"]/div/div[1]/div[6]/div[2]/div[1]')
    # 报警总量
    warn_total = (By.XPATH, '//*[@id="app"]/div/div[1]/div[7]/div[2]/div[1]')
    # 今日动态
    # 新增会员
    new_mem = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]')
    # 新增订单
    new_order = (By.XPATH, '//*[@id="app"]/div/div[2]/div[4]')
    # 新增工单
    new_work_order = (By.XPATH, '//*[@id="app"]/div/div[2]/div[5]')
    # 新增呼入
    new_call_in = (By.XPATH, '//*[@id="app"]/div/div[2]/div[6]')
    # 新增订单金额
    new_order_money = (By.XPATH, '//*[@id="app"]/div/div[2]/div[7]')
    # 新增预警
    new_warn = (By.XPATH, '//*[@id="app"]/div/div[2]/div[8]')

    '''--------------------关联页面元素--------------------'''
    '''组织机构-门店管理页面元素'''
    # 关联门店管理url
    stage_url = 'https://comuhome-ty.yunzhuyang.com/org/store'
    # 类型选择框
    type_choose_btn = (By.XPATH, '//*[@id="select-cat"]')
    # 选择社区
    comm_type_btn = (By.XPATH, '//*[@id="select-cat"]/option[2]')
    # 选择驿站
    stage_type_btn = (By.XPATH, '//*[@id="select-cat"]/option[3]')
    # 获取筛选条数
    amount = (By.XPATH, '//*[@id="datatable-editable-pagination"]/div/span')

    '''用户管理-用户列表页面元素'''
    # 用户列表url
    mem_list_url = 'https://comuhome-ty.yunzhuyang.com/memberuser/getMemberList'
    # 用户总数
    mem_list_total = (By.XPATH, '//*[@id="layui-laypage-1"]/span[1]')

    '''订单管理-订单查询页面元素'''
    # 订单查询url
    order_search_url = 'https://comuhome-ty.yunzhuyang.com/order/search'
    # 订单总数
    order_list_total = (By.XPATH, '//*[@id="layui-laypage-1"]/span[1]')

    '''呼叫中心-工单管理页面元素'''
    # 工单管理url
    work_order_url = 'https://comuhome-ty.yunzhuyang.com/workorder/call-order-management'
    work_order_list_total = (By.XPATH, '//*[@id="content-page"]/div[2]/div[3]/div/span[1]')

    '''-------------------------------元素操作流-----------------------------------------'''
    '''获取数据看板数据'''
    # 获取数据看板社区数量
    def kanban_comm_num(self):
        self.open_browser(self.kanban_url)
        sleep(1)
        ele = self.locator(self.comm_num)
        comm_num = ele.text
        return comm_num

    # 获取数据看板驿站数量
    def kanban_stage_num(self):
        self.open_browser(self.kanban_url)
        sleep(1)
        ele = self.locator(self.stage_num)
        stage_num = ele.text
        return stage_num

    # 获取数据看板会员总量
    def kanban_mem_total(self):
        self.open_browser(self.kanban_url)
        sleep(1)
        ele = self.locator(self.mem_total)
        mem_total = ele.text
        return mem_total

    # 获取数据看板订单总量
    def kanban_order_total(self):
        self.open_browser(self.kanban_url)
        sleep(1)
        ele = self.locator(self.order_total)
        order_total = ele.text
        return order_total

    # 获取数据看板工单总量
    def kanban_work_order_total(self):
        self.open_browser(self.kanban_url)
        sleep(1)
        ele = self.locator(self.work_order_total)
        work_order_total = ele.text
        return work_order_total

    '''获取门店管理页面数据'''
    # 获取社区数量
    def store_comm_amount(self):
        self.open_browser(self.stage_url)
        sleep(1)
        self.click_button(self.type_choose_btn)
        sleep(1)
        self.click_button(self.comm_type_btn)
        sleep(1)
        ele = self.locator(self.amount)
        amount = ele.text
        return amount

    # 获取驿站数量
    def store_stage_amount(self):
        self.open_browser(self.stage_url)
        sleep(1)
        self.click_button(self.type_choose_btn)
        sleep(1)
        self.click_button(self.stage_type_btn)
        sleep(1)
        ele = self.locator(self.amount)
        amount = ele.text
        return amount

    '''获取用户管理页面数据'''
    # 获取用户列表用户总数
    def mem_list_amount(self):
        self.open_browser(self.mem_list_url)
        sleep(1)
        # 操作鼠标，滑动到底部
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        sleep(2)
        ele = self.locator(self.mem_list_total)
        mem_list_total = ele.text
        return mem_list_total

    # 获取工单管理工单总数
    def work_order_list_amount(self):
        self.open_browser(self.work_order_url)
        sleep(1)
        # 操作鼠标，滑动到底部
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        sleep(2)
        ele = self.locator(self.work_order_list_total)
        work_order_list_total = ele.text
        return work_order_list_total

    # 获取订单查询列表订单总数
    def order_search_list_amount(self):
        self.open_browser(self.order_search_url)
        sleep(1)
        # 操作鼠标，滑动到底部
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        sleep(2)
        ele = self.locator(self.order_list_total)
        order_list_total = ele.text
        return order_list_total


