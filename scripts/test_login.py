"""
测试用例
"""
import sys
import os
sys.path.append(os.getcwd())

import pytest
from page.page_login import PageLogin
from tools.get_driver import GetDriver
def get_data():
    # with open("../data/data_login.txt", "r", encoding="utf-8") as f:
    #     r = f.readlines()
    #     arr = []
    #     read_data = r
    #     read_data = read_data[1:]
    #     for data in read_data:
    #         arr.append(tuple(data.strip().split(",")))
    #     print(arr)
    return [("13100011111","123")]


class TestLogin:
    """测试类"""

    def setup_class(self):
        """初始化"""
        # 获取PageLogin()对象
        self.login = PageLogin()

    def teardown_class(self):
        """结束"""
        GetDriver.close_driver()

    @pytest.mark.parametrize("username,pwd", get_data())
    def test_login(self, username, pwd):
        """测试方法"""
        self.login.page_login(username, pwd)
