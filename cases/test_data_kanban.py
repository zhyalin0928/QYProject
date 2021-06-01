"""
@Time      ：2021/5/11 20:26
@Author    ：赵亚林
@Function  ：test_data_kanban
"""
import pytest
import allure
from page_object.kanban_page import KanbanPage
from time import sleep


@allure.feature('数据看板模块')
class TestDataKanban:
    @pytest.mark.run(order=1)
    @allure.story('检查社区数量用例')
    @allure.title('数据看板社区数量')
    @allure.description('验证数据看板社区数量是否与门店管理列表中的数量一致')
    def test_comm_amount(self, drivers, login_fixture):
        with allure.step('登录并进入数据看板页面'):
            self.kp = KanbanPage(drivers)
            sleep(2)
        with allure.step('获取数据看板社区数量'):
            comm_num = self.kp.kanban_comm_num()
            print(comm_num)
        with allure.step('进入门店管理页面，筛选社区并获取社区数量'):
            store_comm_amount = self.kp.store_comm_amount()
            print(store_comm_amount)
        assert comm_num in store_comm_amount

    @pytest.mark.run(order=2)
    @allure.story('检查驿站数量用例')
    @allure.title('数据看板驿站数量')
    @allure.description('验证数据看板驿站数量是否与门店管理列表中的数量一致')
    def test_stage_amount(self, drivers):
        with allure.step('登录并进入数据看板页面'):
            self.kp = KanbanPage(drivers)
            sleep(1)
        with allure.step('获取数据看板驿站数量'):
            stage_num = self.kp.kanban_stage_num()
            print(stage_num)
        with allure.step('进入门店管理页面，筛选驿站并获取驿站数量'):
            store_stage_amount = self.kp.store_stage_amount()
            print(store_stage_amount)
        assert stage_num in store_stage_amount

    @pytest.mark.run(order=3)
    @allure.story('检查会员总量用例')
    @allure.title('数据看板会员数量')
    @allure.description('验证数据看板会员数量是否与会员列表中的数量一致')
    def test_mem_amount(self, drivers):
        with allure.step('登录并进入数据看板页面'):
            self.kp = KanbanPage(drivers)
        with allure.step('获取数据看板会员总量'):
            mem_total = self.kp.kanban_mem_total()
            print(mem_total)
        with allure.step('进入用户列表页面，获取用户总数'):
            mem_list_amount = self.kp.mem_list_amount()
            print(mem_list_amount)
        assert mem_total in mem_list_amount

    @pytest.mark.run(order=4)
    @allure.story('检查订单总量用例')
    @allure.title('数据看板订单数量')
    @allure.description('验证数据看板订单数量是否与订单管理列表中的订单数量一致')
    def test_order_amount(self, drivers):
        with allure.step('登录并进入数据看板页面'):
            self.kp = KanbanPage(drivers)
        with allure.step('获取数据看板订单总量'):
            order_total = self.kp.kanban_order_total()
            print(order_total)
        with allure.step('进入订单查询页面，获取订单总数'):
            order_search_list_amount = self.kp.order_search_list_amount()
            sleep(1)
            print(order_search_list_amount)
        assert order_total in order_search_list_amount

    @pytest.mark.run(order=5)
    @allure.story('检查工单总量用例')
    @allure.title('数据看板工单数量')
    @allure.description('验证数据看板工单数量是否与呼叫中心工单列表中的数量一致')
    def test_work_order_amount(self, drivers):
        with allure.step('登录并进入数据看板页面'):
            self.kp = KanbanPage(drivers)
        with allure.step('获取数据看板工单总量'):
            work_order_total = self.kp.kanban_work_order_total()
            print(work_order_total)
        with allure.step('进入工单管理页面，获取工单总数'):
            work_order_list_amount = self.kp.work_order_list_amount()
            print(work_order_list_amount)
        assert work_order_total in work_order_list_amount


if __name__ == '__main__':
    pytest.main(['-vs'])
