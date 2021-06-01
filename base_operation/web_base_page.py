"""
@Time      ：2021/5/11 20:22
@Author    ：赵亚林
@Function  ：web_base_page
"""


class BasePage:
    """构造函数"""

    def __init__(self, driver):
        self.driver = driver

    # 访问url
    def open_browser(self, url):
        self.driver.get(url)

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_keys(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click_button(self, loc):
        self.locator(loc).click()

    # 获取文本
    def get_text(self, loc):
        text = self.locator(loc).text
        return text

    # 强制等待
    # def wait_time(self, time_):
    #     sleep(time_)

    # 隐式等待
    # def imp_wait(self, time_):
    #     self.driver.implicity_wait(time_)

    # 关闭浏览器
    def quit_browser(self):
        self.driver.quit()
