"""公共方法"""
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from tools.get_driver import GetDriver

class Base:
    def __init__(self):
        """初始化"""
        # 定义空字典
        desired_caps = {}
        # 指定平台名称 必须写对
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        # 不能为空，可以随便写
        desired_caps['deviceName'] = 'emulator-5554'
        # 包名/
        desired_caps['appPackage'] = GetDriver.appPackage
        # 启动名
        desired_caps['appActivity'] = GetDriver.appActivity
        # 中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 声明?机驱动对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)



    def base_get_find(self, loc, timeout=30, poll=0.5):
        """查找元素方法"""
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda x: x.find_element(*loc))

    def base_click(self, loc):
        """点击方法"""
        self.base_get_find(loc).click()

    def base_input(self, loc, values):
        """输入方法"""
        # 找到元素
        el = self.base_get_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(values)
