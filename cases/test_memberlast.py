"""
@Time      ：2021/5/25 20:38
@Author    ：赵亚林
@Function  ：test_memberlast
"""
from time import sleep
import allure
import pytest
from page_object.memberlast_page import MemberLastPage
from page_object.user_management_page import UserManagementPage


@allure.feature('兜底老人模块')
class TestMemLast:
    @allure.story('老人列表用例')
    @allure.title('新建兜底老人')
    @allure.description('验证兜底老人新建功能是否正常')
    def test_addmemlast(self, drivers, login_fixture, memlast_name='张三'):
        with allure.step('新建手机号为18199999999的用户'):
            self.ump = UserManagementPage(drivers)
            sleep(1)
            self.ump.build_user(memlast_name, '18199999999', '520112199003074237', '云岭中路天水花园四单元202')
        with allure.step('新建手机号为18199999999的兜底老人'):
            self.mlp = MemberLastPage(drivers)
            sleep(1)
            self.mlp.build_memlast(memlast_name)
        with allure.step('在老人列表搜索手机号为18199999999的兜底老人'):
            memlast_name = self.mlp.search_memlast(memlast_name)
            print(memlast_name)
        assert '张三' == memlast_name

    @allure.story('报平安用例')
    @allure.title('新建报平安')
    @allure.description('验证报平安新建功能是否正常')
    def test_safety_add(self, drivers, memlast_name='张三'):
        with allure.step("开启兜底老人显示，进入新建页面新建张三的报平安记录"):
            self.mlp = MemberLastPage(drivers)
            sleep(1)
            self.mlp.safety_build(memlast_name)
        with allure.step('获取报平安列表第一条数据'):
            memlast_phone = self.mlp.list_first_data()
            sleep(1)
            print(memlast_phone)
        assert '18199999999' in memlast_phone

    @allure.story('报平安用例')
    @allure.title('删除报平安记录')
    @allure.description('验证报平安删除功能是否正常')
    def test_safety_del(self, drivers):
        with allure.step('点击删除按钮并确认'):
            self.mlp = MemberLastPage(drivers)
            sleep(1)
            self.mlp.safety_del()

    @allure.story('主动关怀用例')
    @allure.title('新建主动关怀')
    @allure.description('验证主动关怀新建功能是否正常')
    def test_care_add(self, drivers, username='张三'):
        with allure.step('进入新建页面新建张三的上门关怀记录'):
            self.mlp = MemberLastPage(drivers)
            sleep(1)
            self.mlp.care_build(username)
        with allure.step('获取主动关怀列表第一条数据'):
            memlast_phone = self.mlp.list_first_data()
            sleep(1)
            print(memlast_phone)
        assert '18199999999' in memlast_phone

    @allure.story('主动关怀用例')
    @allure.title('删除主动关怀')
    @allure.description('验证主动关怀删除功能是否正常')
    def test_care_del(self, drivers):
        with allure.step('点击删除按钮并确认'):
            self.mlp = MemberLastPage(drivers)
            sleep(1)
            self.mlp.care_del()

    @allure.story('老人列表用例')
    @allure.title('作废并删除兜底老人')
    @allure.description('验证兜底老人删除功能是否正常')
    def test_memlast_del(self, drivers):
        with allure.step('点击删除按钮，输入作废原因并确认'):
            self.mlp = MemberLastPage(drivers)
            sleep(1)
            self.mlp.memlast_del(del_reason='已作废')
        with allure.step('获取列表第一条数据'):
            memlast_phone = self.mlp.list_first_data()
            sleep(1)
            print(memlast_phone)
        assert '18199999999' not in memlast_phone


if __name__ == '__main__':
    pytest.main(['-vs'])
