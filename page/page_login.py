import page
from base.base import Base


class PageLogin(Base):
    """登录页面"""

    def page_input_username(self, username):
        """输入帐号"""
        self.base_input(page.login_username, username)

    def page_input_pwd(self, pwd):
        """输入密码"""
        self.base_input(page.login_password, pwd)

    def page_click_login(self):
        """点击登录"""
        self.base_click(page.login_btn)

    def page_login(self, username, pwd):
        """组合业务方法"""
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login()
