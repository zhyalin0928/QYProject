"""
@Time      ：2021/5/11 20:21
@Author    ：赵亚林
@Function  ：conftest.py
"""
import os
from time import sleep
import allure
import pytest
from selenium import webdriver
from page_object.login_page import LoginPage

driver = None


@pytest.fixture(scope='session')
def drivers():
    global driver
    if driver is None:
        driver = webdriver.Chrome()  # GUI界面运行
        driver.maximize_window()
        driver.implicitly_wait(10)
    yield driver  # 返回驱动
    sleep(2)
    driver.quit()


@pytest.fixture(scope='session')
def login_fixture(drivers):
    lp = LoginPage(driver)
    lp.login('18166784094', '9879')
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    """
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                sleep(1)
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
