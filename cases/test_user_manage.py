"""
@Time      ：2021/5/24 15:30
@Author    ：赵亚林
@Function  ：test_user_manage
"""
from time import sleep
import allure
import pytest
from page_object.user_management_page import UserManagementPage


@allure.feature('用户管理模块')
class TestUserManage:
    @pytest.mark.run(order=6)
    @allure.story('用户列表用例')
    @allure.title('新增用户')
    @allure.description('验证新建用户功能是否正常')
    def test_adduser(self, drivers, login_fixture):
        with allure.step('新建手机号为18199999999的用户张三'):
            self.ump = UserManagementPage(drivers)
            sleep(1)
            self.ump.build_user('张三', '18199999999', '520112199003074237', '云岭中路天水花园四单元202')
        with allure.step('等待提示信息弹出'):
            sleep(1)
        with allure.step('获取提交数据后的提示信息'):
            text = drivers.find_element_by_css_selector('body>div.el-message.el-message--success>p').text
            print(text)
        assert '保存成功' in text

    @pytest.mark.run(order=7)
    @allure.story('用户列表用例')
    @allure.title('搜索用户')
    @allure.description('验证搜索用户功能是否正常')
    def test_searchuser(self, drivers):
        with allure.step('搜索框中输入手机号18199999999，并点击搜索按钮'):
            self.ump = UserManagementPage(drivers)
            sleep(1)
            self.ump.search_user('18199999999')
        with allure.step('获取搜索结果手机号信息'):
            text = drivers.find_element_by_xpath('//*[@id="datatable-editable1"]/tbody/tr/td[4]').text
            print(text)
        assert '18199999999' in text

    @pytest.mark.run(order=8)
    @allure.story('用户列表用例')
    @allure.title('删除用户')
    @allure.description('验证删除用户功能是否正常')
    def test_deluser(self, drivers):
        with allure.step('搜索用户手机号'):
            self.ump = UserManagementPage(drivers)
            sleep(1)
            self.ump.search_user('18199999999')
        with allure.step('删除用户'):
            self.ump.del_user()
            sleep(1)
        with allure.step('获取删除提示'):
            text = drivers.find_element_by_css_selector('#layui-layer3 > div').text
            print(text)
        assert '操作成功' in text


if __name__ == '__main__':
    pytest.main(['-vs'])
