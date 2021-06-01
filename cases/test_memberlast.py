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
    def test_addmemlast(self, drivers, memlast_name='张三'):
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


if __name__ == '__main__':
    pytest.main(['-vs'])
